# -*- coding: utf-8 -*-
import streamlit as st
import openmeteo_requests
import requests_cache
from retry_requests import retry
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
from matplotlib.colors import ListedColormap, BoundaryNorm
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from scipy.interpolate import griddata
from datetime import datetime, timedelta
import pytz
import metpy.calc as mpcalc
from metpy.units import units
from metpy.plots import SkewT, Hodograph

# --- 0. CONFIGURACIÓ INICIAL DE LA PÀGINA I APIs ---
st.set_page_config(
    layout="wide", 
    page_title="Visor de Mapes i Sondejos", 
    initial_sidebar_state="expanded", # Sidebar visible per defecte
    menu_items={'About': "Visor Meteorològic avançat amb dades Open-Meteo (model AROME Seamless) i Streamlit/MetPy."}
)
cache_session = requests_cache.CachedSession('.cache', expire_after=1800) # Cache de 30 minuts
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# --- 1. CONSTANTS I DICCIONARIS ---
API_URL = "https://api.open-meteo.com/v1/forecast"
TIMEZONE = pytz.timezone('Europe/Madrid')
MAP_EXTENT_CAT = [0, 3.5, 40.4, 43] # Extensió sobre Catalunya
PRESS_LEVELS = sorted([1000, 950, 925, 900, 850, 800, 700, 600, 500, 400, 300, 250, 200], reverse=True)

CIUTATS_CATALUNYA = {
    'Barcelona': {'lat': 41.3851, 'lon': 2.1734}, 'Girona': {'lat': 41.9831, 'lon': 2.8249},
    'Lleida': {'lat': 41.6177, 'lon': 0.6200}, 'Tarragona': {'lat': 41.1189, 'lon': 1.2445},
    'Manresa': {'lat': 41.7230, 'lon': 1.8268}, 'Vic': {'lat': 41.9301, 'lon': 2.2545},
    'Figueres': {'lat': 42.2662, 'lon': 2.9622}, 'Tortosa': {'lat': 40.8126, 'lon': 0.5211},
    'La Seu d\'Urgell': {'lat': 42.3582, 'lon': 1.4593}, 'Sort': {'lat': 42.4131, 'lon': 1.1278},
    'Puigcerdà': {'lat': 42.4333, 'lon': 1.9333}, 'Reus': {'lat': 41.1500, 'lon': 1.1000}
}

# --- 2. FUNCIONS DE CÀRREGA I PROCESSAMENT DE DADES ---

@st.cache_data(ttl=1800, show_spinner=False)
def carregar_dades_mapa_base(variables, hourly_index):
    """Funció base per carregar dades de la API per a la creació de mapes."""
    try:
        # Punts de la graella de Catalunya. Més punts = millor resolució, però més lenta
        lats, lons = np.linspace(MAP_EXTENT_CAT[2], MAP_EXTENT_CAT[3], 15), np.linspace(MAP_EXTENT_CAT[0], MAP_EXTENT_CAT[1], 15)
        lon_grid, lat_grid = np.meshgrid(lons, lats)
        params = {"latitude": lat_grid.flatten().tolist(), "longitude": lon_grid.flatten().tolist(), "hourly": variables, "models": "arome_seamless", "forecast_days": 2}
        responses = openmeteo.weather_api(API_URL, params=params)
        output = {"lats": [], "lons": [], **{var: [] for var in variables}}
        for r in responses:
            try:
                vals = [r.Hourly().Variables(i).ValuesAsNumpy()[hourly_index] for i in range(len(variables))]
                # Assegurar que totes les variables tenen valors no-NaN
                if not any(np.isnan(v) for v in vals):
                    output["lats"].append(r.Latitude()); output["lons"].append(r.Longitude())
                    for i, var in enumerate(variables): output[var].append(vals[i])
            except IndexError: continue # No hi ha dades per a aquest punt i hora
        return (output, None) if output["lats"] else (None, "No s'han rebut dades vàlides per al mapa.")
    except Exception as e: return None, f"Error en la petició a la API: {e}"

@st.cache_data(ttl=1800)
def carregar_dades_mapa_complet(nivell, hourly_index):
    """Carrega CAPE i vent per a mapes combinats."""
    variables = ["cape", f"wind_speed_{nivell}hPa", f"wind_direction_{nivell}hPa"]
    map_data_raw, error = carregar_dades_mapa_base(variables, hourly_index)
    if error: return None, error
    map_data_raw['cape_data'] = map_data_raw.pop('cape')
    map_data_raw['speed_data'] = map_data_raw.pop(f"wind_speed_{nivell}hPa")
    map_data_raw['dir_data'] = map_data_raw.pop(f"wind_direction_{nivell}hPa")
    return map_data_raw, None

@st.cache_data(ttl=1800)
def carregar_dades_mapa_cisalladura(hourly_index, top_level_hpa):
    """Carrega vent de 10m i del nivell superior per a calcular la cisalladura."""
    variables = ["wind_speed_10m", "wind_direction_10m", f"wind_speed_{top_level_hpa}hPa", f"wind_direction_{top_level_hpa}hPa"]
    map_data_raw, error = carregar_dades_mapa_base(variables, hourly_index)
    if error: return None, error
    
    # Utilitzem MetPy per calcular components U/V i manejar les unitats
    u_low, v_low = mpcalc.wind_components(np.array(map_data_raw.pop('wind_speed_10m')) * units('km/h'), np.array(map_data_raw.pop('wind_direction_10m')) * units.degrees)
    u_high, v_high = mpcalc.wind_components(np.array(map_data_raw.pop(f'wind_speed_{top_level_hpa}hPa')) * units('km/h'), np.array(map_data_raw.pop(f'wind_direction_{top_level_hpa}hPa')) * units.degrees)
    
    map_data_raw['u_low'], map_data_raw['v_low'] = u_low.to('m/s').m, v_low.to('m/s').m
    map_data_raw['u_high'], map_data_raw['v_high'] = u_high.to('m/s').m, v_high.to('m/s').m
    return map_data_raw, None

@st.cache_data(ttl=1800)
def carregar_dades_mapa_rosada(hourly_index):
    map_data_raw, error = carregar_dades_mapa_base(["dew_point_2m"], hourly_index)
    if error: return None, error
    map_data_raw['dewpoint_data'] = map_data_raw.pop('dew_point_2m')
    return map_data_raw, None

@st.cache_data(ttl=1800)
def carregar_dades_mapa_vents(nivell, hourly_index):
    variables = [f"wind_speed_{nivell}hPa", f"wind_direction_{nivell}hPa"]
    map_data_raw, error = carregar_dades_mapa_base(variables, hourly_index)
    if error: return None, error
    map_data_raw['speed_data'] = map_data_raw.pop(variables[0])
    map_data_raw['dir_data'] = map_data_raw.pop(variables[1])
    return map_data_raw, None

@st.cache_data(ttl=1800)
def carregar_dades_mapa_temperatura_500hpa(hourly_index):
    map_data_raw, error = carregar_dades_mapa_base(["temperature_500hPa"], hourly_index)
    if error: return None, error
    map_data_raw['temp_data'] = map_data_raw.pop('temperature_500hPa')
    return map_data_raw, None

def processar_dades_sondeig(p_profile, T_profile, Td_profile, u_profile, v_profile, h_profile):
    """Processa les dades en brut i calcula paràmetres com CAPE, CIN, LI i SRH."""
    if len(p_profile) < 4: return None, "Perfil atmosfèric massa curt."
    
    # Conversió a unitats MetPy
    p = np.array(p_profile) * units.hPa; T = np.array(T_profile) * units.degC; Td = np.array(Td_profile) * units.degC
    u = np.array(u_profile) * units('m/s'); v = np.array(v_profile) * units('m/s'); heights = np.array(h_profile) * units.meter
    
    # Neteja de dades NaN i ordenació
    valid_indices = ~np.isnan(p.m) & ~np.isnan(T.m) & ~np.isnan(Td.m) & ~np.isnan(u.m) & ~np.isnan(v.m)
    p, T, Td, u, v, heights = p[valid_indices], T[valid_indices], Td[valid_indices], u[valid_indices], v[valid_indices], heights[valid_indices]
    if len(p) < 4: return None, "No hi ha prou nivells amb dades vàlides."
    sort_idx = np.argsort(p.m)[::-1]
    p, T, Td, u, v, heights = p[sort_idx], T[sort_idx], Td[sort_idx], u[sort_idx], v[sort_idx], heights[sort_idx]
    
    params_calc = {}
    
    # 1. Perfil de Parcel·la Basada en Superfície (SBCAPE/SBCIN)
    try: 
        # Perfil per una parcel·la que puja des de la superfície
        main_prof = mpcalc.parcel_profile(p, T[0], Td[0]).to('degC')
        sbcape, sbcin = mpcalc.cape_cin(p, T, Td, main_prof); 
        params_calc['SBCAPE'], params_calc['SBCIN'] = float(sbcape.m), float(sbcin.m)
    except Exception as e: 
        main_prof = None
        params_calc['SBCAPE'], params_calc['SBCIN'] = 0.0, 0.0
        # Permetre continuar tot i l'error crític, però retornar el missatge a la consola si fos necessari
        # st.warning(f"Error en càlcul termodinàmic: {e}") 

    # 2. Càlcul d'altres paràmetres termodinàmics
    try: params_calc['LI'] = float(mpcalc.lifted_index(p, T, main_prof)[0].m) if main_prof is not None else np.nan
    except Exception: params_calc['LI'] = np.nan
    try: lcl_p, _ = mpcalc.lcl(p[0], T[0], Td[0]); params_calc['LCL_p'] = float(lcl_p.m)
    except Exception: params_calc['LCL_p'] = np.nan
    try: lfc_p, _ = mpcalc.lfc(p, T, Td, main_prof); params_calc['LFC_p'] = float(lfc_p.m)
    except Exception: params_calc['LFC_p'] = np.nan
    try: el_p, _ = mpcalc.el(p, T, Td, main_prof); params_calc['EL_p'] = float(el_p.m)
    except Exception: params_calc['EL_p'] = np.nan
    
    # 3. Càlcul de la cinemàtica (SRH - Helicitat Relativa a la Tempesta)
    try:
        # Estimar el moviment de la tempesta (Storm Motion) usant el vent mitjà 0-6km (proxy simple)
        idx_6km = np.argmin(np.abs(heights.m - 6000))
        u_6km = u[:idx_6km+1]; v_6km = v[:idx_6km+1]; p_6km = p[:idx_6km+1]
        
        # Calcular vent mitjà 0-6km (integració sobre l'alçada per pressió)
        u_mean_6km, v_mean_6km = mpcalc.mean_pressure_level_winds(p_6km, u_6km, v_6km)
        storm_motion_simple = units.Quantity([u_mean_6km.m, v_mean_6km.m]) * units('m/s')

        # Helicitat 0-1 km (clau per a tornados)
        idx_1km = np.argmin(np.abs(heights.m - 1000))
        srh_0_1 = mpcalc.storm_relative_helicity(u[:idx_1km+1], v[:idx_1km+1], heights[:idx_1km+1], storm_motion_simple, bottom=0 * units.meter, depth=1000 * units.meter)
        params_calc['SRH_0_1'] = float(srh_0_1.m)

        # Helicitat 0-3 km (clau per a supercèl·lules)
        idx_3km = np.argmin(np.abs(heights.m - 3000))
        srh_0_3 = mpcalc.storm_relative_helicity(u[:idx_3km+1], v[:idx_3km+1], heights[:idx_3km+1], storm_motion_simple, bottom=0 * units.meter, depth=3000 * units.meter)
        params_calc['SRH_0_3'] = float(srh_0_3.m)
        
        # Guardar la velocitat de la tempesta
        sm_speed = mpcalc.wind_speed(storm_motion_simple[0], storm_motion_simple[1]).to('knots').m
        params_calc['SM_SPEED'] = sm_speed

    except Exception:
        params_calc['SRH_0_1'], params_calc['SRH_0_3'], params_calc['SM_SPEED'] = 0.0, 0.0, 0.0
        
    processed_tuple = (p, T, Td, u, v, heights, main_prof, None)
    return (processed_tuple, params_calc), None


@st.cache_data(ttl=1800, show_spinner=False)
def carregar_dades_sondeig(lat, lon, hourly_index):
    """Carrega totes les dades necessàries de pressió per al sondeig en un sol API call."""
    try:
        h_base = ["temperature_2m", "dew_point_2m", "surface_pressure", "wind_speed_10m", "wind_direction_10m"]
        h_press = [f"{v}_{p}hPa" for v in ["temperature", "relative_humidity", "wind_speed", "wind_direction", "geopotential_height"] for p in PRESS_LEVELS]
        params = {"latitude": lat, "longitude": lon, "hourly": h_base + h_press, "models": "arome_seamless", "forecast_days": 2}
        
        # Ús de Open-Meteo per obtenir les dades
        response = openmeteo.weather_api(API_URL, params=params)[0]; hourly = response.Hourly()
        
        sfc_data = {v: hourly.Variables(i).ValuesAsNumpy()[hourly_index] for i, v in enumerate(h_base)}
        p_data = {var: [hourly.Variables(len(h_base) + i * len(PRESS_LEVELS) + j).ValuesAsNumpy()[hourly_index] for j in range(len(PRESS_LEVELS))] for i, var in enumerate(["T", "RH", "WS", "WD", "H"])}
        
        # Dades de superfície
        sfc_u, sfc_v = mpcalc.wind_components(sfc_data["wind_speed_10m"] * units('km/h'), sfc_data["wind_direction_10m"] * units.degrees)
        p, T, Td, u, v, h = ([sfc_data["surface_pressure"]], [sfc_data["temperature_2m"]], [sfc_data["dew_point_2m"]], [sfc_u.to('m/s').m], [sfc_v.to('m/s').m], [0.0])
        
        # Dades per nivells de pressió
        for i, p_val in enumerate(PRESS_LEVELS):
            if p_val < p[-1] and all(not np.isnan(p_data[var][i]) for var in ["T", "RH", "WS", "WD", "H"]):
                p.append(p_val); T.append(p_data["T"][i])
                # Càlcul del punt de rosada a partir de la temperatura i la humitat relativa
                Td.append(mpcalc.dewpoint_from_relative_humidity(p_data["T"][i] * units.degC, p_data["RH"][i] * units.percent).m)
                u_i, v_i = mpcalc.wind_components(p_data["WS"][i] * units('km/h'), p_data["WD"][i] * units.degrees)
                u.append(u_i.to('m/s').m); v.append(v_i.to('m/s').m); h.append(p_data["H"][i])
        
        processed_data, error = processar_dades_sondeig(p, T, Td, u, v, h)
        return (processed_data, error) if not error else (None, error)
    except Exception as e: return None, f"Error carregant dades del sondeig: {e}"

# --- 3. FUNCIONS DE DIBUIX (Mantenen l'estructura original amb petites millores) ---

def crear_mapa_base(map_extent):
    """Crea una figura i eixos amb la projecció base i els elements geogràfics."""
    fig, ax = plt.subplots(figsize=(10, 10), dpi=130, subplot_kw={'projection': ccrs.PlateCarree()})
    ax.set_extent(map_extent, crs=ccrs.PlateCarree())
    ax.add_feature(cfeature.LAND, facecolor="#D4E6B5", zorder=0)
    ax.add_feature(cfeature.OCEAN, facecolor='#4682B4', zorder=0)
    ax.add_feature(cfeature.COASTLINE, edgecolor='black', linewidth=1.2, zorder=5)
    ax.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='black', zorder=5)
    return fig, ax

def crear_mapa_cape_streamlines(lons, lats, cape_data, speed_data, dir_data, nivell, timestamp_str, map_extent):
    """Dibuixa CAPE i línies de corrent."""
    fig, ax = crear_mapa_base(map_extent)
    grid_lon, grid_lat = np.meshgrid(np.linspace(map_extent[0], map_extent[1], 200), np.linspace(map_extent[2], map_extent[3], 200))
    grid_cape = griddata((lons, lats), cape_data, (grid_lon, grid_lat), 'cubic')
    u_comp, v_comp = mpcalc.wind_components(np.array(speed_data) * units('km/h'), np.array(dir_data) * units.degrees)
    grid_u = griddata((lons, lats), u_comp.to('m/s').m, (grid_lon, grid_lat), 'cubic')
    grid_v = griddata((lons, lats), v_comp.to('m/s').m, (grid_lon, grid_lat), 'cubic')
    
    # Només pintar CAPE significativa
    grid_cape[grid_cape < 50] = np.nan 
    
    cape_colors = ['#90EE90', '#32CD32', '#FFFF00', '#FFA500', '#FF4500', '#FF0000', '#C71585', '#9932CC']
    cape_levels = [100, 250, 500, 1000, 1500, 2000, 2500, 3000, 4000]
    cmap_cape = ListedColormap(cape_colors); norm_cape = BoundaryNorm(cape_levels, ncolors=cmap_cape.N)
    im_cape = ax.contourf(grid_lon, grid_lat, grid_cape, levels=cape_levels, cmap=cmap_cape, norm=norm_cape, extend='max', alpha=0.7, zorder=2, transform=ccrs.PlateCarree())
    
    cbar_cape = fig.colorbar(im_cape, ax=ax, shrink=0.7, pad=0.02, orientation='horizontal'); cbar_cape.set_label("CAPE (J/kg)")
    ax.streamplot(grid_lon, grid_lat, grid_u, grid_v, color='black', linewidth=0.8, density=3, arrowsize=0.8, zorder=4, transform=ccrs.PlateCarree())
    
    ax.set_title(f"CAPE i Línies de Corrent a {nivell}hPa\n{timestamp_str}", weight='bold', fontsize=16)
    return fig

def crear_mapa_cisalladura(lons, lats, u_low, v_low, u_high, v_high, layer_name, timestamp_str, map_extent):
    """Dibuixa un mapa de cisalladura del vent entre dos nivells."""
    fig, ax = crear_mapa_base(map_extent)
    grid_lon, grid_lat = np.meshgrid(np.linspace(map_extent[0], map_extent[1], 150), np.linspace(map_extent[2], map_extent[3], 150))
    grid_u_low = griddata((lons, lats), u_low, (grid_lon, grid_lat), 'cubic')
    grid_v_low = griddata((lons, lats), v_low, (grid_lon, grid_lat), 'cubic')
    grid_u_high = griddata((lons, lats), u_high, (grid_lon, grid_lat), 'cubic')
    grid_v_high = griddata((lons, lats), v_high, (grid_lon, grid_lat), 'cubic')
    
    shear_u, shear_v = (grid_u_high - grid_u_low) * units('m/s'), (grid_v_high - grid_v_low) * units('m/s')
    shear_magnitude = mpcalc.wind_speed(shear_u, shear_v).to('knots').m
    
    if layer_name == "0-6km":
        colors = ['#ADD8E6', '#87CEEB', '#90EE90', '#FFFF00', '#FFA500', '#FF4500', '#FF0000', '#C71585']
        levels = [15, 25, 35, 45, 55, 65, 75, 85]
        cbar_label = "Cisalladura 0–6 km (nusos) - Organització"
        title = f"Cisalladura per a l'Organització de Tempestes\n{timestamp_str}"
        cbar_shrink = 0.7
    else:  # 0–1 km
        colors = ['#ADD8E6', '#90EE90', '#FFFF00', '#FFA500', '#FF4500', '#FF0000', '#DC143C', '#C71585']
        levels = [5, 15, 25, 35, 45, 55, 65, 75, 85]
        cbar_label = "Cisalladura 0–1 km (nusos) - Potencial de Tornados"
        title = f"Cisalladura a Baixos Nivells (Potencial de Tornados)\n{timestamp_str}"
        cbar_shrink = 0.9

    cmap = ListedColormap(colors)
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    
    im = ax.contourf(grid_lon, grid_lat, shear_magnitude, levels=levels, cmap=cmap, norm=norm, extend='max', alpha=0.7, zorder=2, transform=ccrs.PlateCarree())
    
    cbar = fig.colorbar(im, ax=ax, shrink=cbar_shrink, pad=0.03, orientation='horizontal', ticks=levels); 
    cbar.set_label(cbar_label, fontsize=12, weight='bold')
    cbar.ax.tick_params(labelsize=10)
    ax.set_title(title, weight='bold', fontsize=16)
    
    return fig

def crear_mapa_punt_rosada(lons, lats, dewpoint_data, timestamp_str, map_extent):
    """Dibuixa el Punt de Rosada (humitat a 2m)."""
    fig, ax = crear_mapa_base(map_extent); 
    dewpoint_colors = ['#FFFFFF', '#E6E6FA', '#D8BFD8', '#ADD8E6', '#B0C4DE', "#ECEC63", '#FFD700', '#FFA500', '#FF8C00', '#FF4500', '#DC143C', '#B22222']
    dewpoint_levels = [-25, 0, 5, 8, 12, 15, 16, 17, 18, 19, 20, 22, 25]; 
    custom_cmap = ListedColormap(dewpoint_colors); norm_dewpoint = BoundaryNorm(dewpoint_levels, ncolors=custom_cmap.N, clip=True)
    
    grid_lon, grid_lat = np.meshgrid(np.linspace(map_extent[0], map_extent[1], 200), np.linspace(map_extent[2], map_extent[3], 200))
    grid_dewpoint = griddata((lons, lats), dewpoint_data, (grid_lon, grid_lat), 'cubic')
    
    im = ax.contourf(grid_lon, grid_lat, grid_dewpoint, levels=dewpoint_levels, cmap=custom_cmap, norm=norm_dewpoint, extend='both', zorder=2, transform=ccrs.PlateCarree())
    
    # Línia de contorn clau a 15°C (llindar per a inestabilitat)
    ax.contour(grid_lon, grid_lat, grid_dewpoint, levels=[15], colors='black', linewidths=2.5, linestyles='-', zorder=4, transform=ccrs.PlateCarree())
    
    cbar = fig.colorbar(im, ax=ax, shrink=0.7, pad=0.02, ticks=dewpoint_levels[::2]); cbar.set_label("Punt de Rosada a 2m (°C)")
    ax.set_title(f"Humitat a Superfície (Punt de Rosada - Td)\n{timestamp_str}", weight='bold', fontsize=16); 
    return fig

def crear_mapa_vents(lons, lats, speed_data, dir_data, nivell, timestamp_str, map_extent):
    """Dibuixa la velocitat i direcció del vent amb bàrbules."""
    fig, ax = crear_mapa_base(map_extent); 
    grid_lon, grid_lat = np.meshgrid(np.linspace(map_extent[0], map_extent[1], 200), np.linspace(map_extent[2], map_extent[3], 200))
    grid_speed = griddata((lons, lats), speed_data, (grid_lon, grid_lat), 'cubic'); 
    u_comp, v_comp = mpcalc.wind_components(np.array(speed_data) * units('km/h'), np.array(dir_data) * units.degrees)
    
    colors = ['#FFFFFF', '#B0E0E6', '#87CEEB', '#90EE90', '#FFFF00', '#FFD700', '#FFA500', '#FF4500', '#FF0000', '#DC143C', '#FF00FF', '#9932CC']; 
    levels = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 240, 280]
    cmap = ListedColormap(colors); norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    
    im = ax.contourf(grid_lon, grid_lat, grid_speed, levels=levels, cmap=cmap, norm=norm, extend='max', zorder=2, transform=ccrs.PlateCarree())
    
    # Barbs (Bàrbules de vent)
    u_knots, v_knots = u_comp.to('knots'), v_comp.to('knots'); 
    lon_b, lat_b = np.meshgrid(np.linspace(map_extent[0], map_extent[1], 20), np.linspace(map_extent[2], map_extent[3], 20)) # Graella més dispersa per a les bàrbules
    u_b = griddata((lons, lats), u_knots, (lon_b, lat_b), 'linear'); v_b = griddata((lons, lats), v_knots, (lon_b, lat_b), 'linear')
    ax.barbs(lon_b, lat_b, u_b, v_b, length=7, color='black', zorder=10, transform=ccrs.PlateCarree())
    
    cbar = fig.colorbar(im, ax=ax, shrink=0.7, ticks=levels[::2]); cbar.set_label("Velocitat del Vent (km/h)")
    ax.set_title(f"Vent a {nivell} hPa\n{timestamp_str}", weight='bold', fontsize=16); 
    return fig

def crear_mapa_temperatura_500hpa(lons, lats, temp_data, timestamp_str, map_extent):
    """Dibuixa la temperatura a 500 hPa (índex de fred en altura)."""
    fig, ax = crear_mapa_base(map_extent); 
    grid_lon, grid_lat = np.meshgrid(np.linspace(map_extent[0], map_extent[1], 200), np.linspace(map_extent[2], map_extent[3], 200))
    grid_temp = griddata((lons, lats), temp_data, (grid_lon, grid_lat), 'cubic'); 
    cmap = plt.get_cmap('coolwarm'); 
    levels = np.arange(-30, 0, 1); norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    
    im = ax.contourf(grid_lon, grid_lat, grid_temp, levels=levels, cmap=cmap, norm=norm, extend='both', zorder=2, transform=ccrs.PlateCarree())
    
    # Contorns de temperatura i etiquetes
    contours = ax.contour(grid_lon, grid_lat, grid_temp, levels=np.arange(-30, 0, 2), colors='black', linestyles='solid', linewidths=1.2, zorder=4, transform=ccrs.PlateCarree())
    labels = ax.clabel(contours, inline=True, fontsize=9, fmt='%1.0f°C'); 
    [label.set_path_effects([path_effects.withStroke(linewidth=2.5, foreground='white')]) for label in labels]
    
    cbar = fig.colorbar(im, ax=ax, shrink=0.7, ticks=np.arange(-30, 1, 5)); cbar.set_label("Temperatura a 500hPa (°C)")
    ax.set_title(f"Masses d'Aire en Altura (Temperatura a 500 hPa)\n{timestamp_str}", weight='bold', fontsize=16); 
    return fig

def crear_skewt(p, T, Td, u, v, prof, params_calc, titol, timestamp_str):
    """Crea el diagrama Skew-T Log-P amb paràmetres clau."""
    fig = plt.figure(figsize=(8, 9), dpi=150); skew = SkewT(fig, rotation=45); skew.ax.grid(True, linestyle='-', alpha=0.5, color='grey')
    skew.ax.set_ylim(1000, 100); skew.ax.set_xlim(-30, 40)
    
    # Línies termodinàmiques
    skew.plot_dry_adiabats(color='#b57a7a', linestyle='--', alpha=0.5, linewidth=1); 
    skew.plot_moist_adiabats(color='#6a5acd', linestyle='--', alpha=0.5, linewidth=1)
    skew.plot_mixing_lines(color='#4682b4', linestyle='--', alpha=0.5, linewidth=1)
    
    # Perfil de la parcel·la i ombres (CAPE/CIN)
    if prof is not None:
        skew.shade_cape(p, T, prof, color='red', alpha=0.3); 
        skew.shade_cin(p, T, prof, color='#E0E0E0', alpha=0.5)
        skew.plot(p, prof, 'k', linewidth=2, label='Parcel·la Superfície')
        
    # Perfils de Temperatura i Punt de Rosada
    skew.plot(p, T, 'red', lw=2.5, label='Temperatura'); 
    skew.plot(p, Td, 'green', lw=2.5, label='Punt de Rosada'); 
    skew.plot_barbs(p.to('hPa'), u.to('knots'), v.to('knots'), y_clip_radius=0.03)
    
    skew.ax.set_title(f"{titol}\n{timestamp_str}", weight='bold', fontsize=14, pad=20)
    skew.ax.set_xlabel("Temperatura (°C)"); skew.ax.set_ylabel("Pressió (hPa)")
    
    # Text amb paràmetres (Actualitzat amb SBCAPE i SRH)
    text = (
        f"SBCAPE = {params_calc.get('SBCAPE', 0):.1f} J/kg\n" 
        f"SBCIN = {params_calc.get('SBCIN', 0):.1f} J/kg\n" 
        f"SRH 0-1km = {params_calc.get('SRH_0_1', 0):.1f} m²/s²\n"
        f"SRH 0-3km = {params_calc.get('SRH_0_3', 0):.1f} m²/s²\n"
        f"LI = {params_calc.get('LI', 0):.1f} K\n" 
        f"EL = {params_calc.get('EL_p', 0):.1f} hPa\n" 
        f"LCL = {params_calc.get('LCL_p', 0):.1f} hPa\n" 
        f"LFC = {params_calc.get('LFC_p', 0):.1f} hPa"
    )
    props = dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.85, edgecolor='black')
    skew.ax.text(0.03, 0.97, text, transform=skew.ax.transAxes, fontsize=10, verticalalignment='top', bbox=props); 
    
    return fig

def crear_hodograf_avancat(p, u, v, heights, params_calc, titol, timestamp_str):
    """Crea l'Hodògraf amb la codificació per colors segons l'alçada."""
    fig = plt.figure(dpi=150, figsize=(8, 8)); gs = fig.add_gridspec(nrows=1, ncols=1); ax_hodo = fig.add_subplot(gs[0, 0])
    
    # Afegir el vector de moviment de la tempesta (Storm Motion)
    sm_u, sm_v = params_calc.get('SM_U', 0), params_calc.get('SM_V', 0)
    if sm_u != 0 or sm_v != 0:
        ax_hodo.arrow(0, 0, sm_u, sm_v, color='red', linewidth=3, head_width=2, head_length=2, label=f"Storm Motion (0-6km) {params_calc.get('SM_SPEED', 0):.1f} kt", zorder=10)
        ax_hodo.legend(loc='lower left', framealpha=0.7)

    fig.suptitle(f"{titol}\n{timestamp_str}", weight='bold', fontsize=16)
    
    # Hodògraf i graella
    h = Hodograph(ax_hodo, component_range=80.) # Augmentar el rang per visualitzar millor
    h.add_grid(increment=20, color='gray', linestyle='--')
    
    # Intervals de colors per alçada
    intervals = np.array([0, 1, 3, 6, 9, 12]) * units.km; 
    colors_hodo = ['red', 'blue', 'green', 'purple', 'gold']
    
    # Plot amb codificació per alçada
    h.plot_colormapped(u.to('kt'), v.to('kt'), heights, intervals=intervals, colors=colors_hodo, linewidth=2)
    
    # Afegir punts de referència (1km, 3km)
    h.plot(u.to('kt')[np.argmin(np.abs(heights.m - 1000))], v.to('kt')[np.argmin(np.abs(heights.m - 1000))], 'o', color='blue', markeredgecolor='black', markersize=8, label='1 km')
    h.plot(u.to('kt')[np.argmin(np.abs(heights.m - 3000))], v.to('kt')[np.argmin(np.abs(heights.m - 3000))], 'o', color='green', markeredgecolor='black', markersize=8, label='3 km')
    
    ax_hodo.set_xlabel('Component U (nusos)'); 
    ax_hodo.set_ylabel('Component V (nusos)'); 
    
    return fig

# --- 4. FUNCIÓ PRINCIPAL DE L'APLICACIÓ (MELLORADA) ---
def main():
    st.title("⛈️ Visor de Mapes i Sondejos Meteorològics (Model AROME)")
    st.markdown("---")
    
    now_local = datetime.now(TIMEZONE)
    
    # --- BARRA LATERAL (UX Millorada) ---
    with st.sidebar:
        st.header("⚙️ Configuració de la Previsió")
        
        # Selector de Dia i Hora
        dia_sel_str = st.selectbox("📅 Dia:", 
            [(now_local + timedelta(days=i)).strftime('%d/%m/%Y') for i in range(2)], 
            format_func=lambda d: f"Avui ({d})" if d == now_local.strftime('%d/%m/%Y') else f"Demà ({d})")
        
        hora_sel_num = st.slider("🕰️ Hora (HLC):", 0, 23, now_local.hour, format="%d:00h", step=1)
        
        target_date = datetime.strptime(dia_sel_str, '%d/%m/%Y').date()
        target_dt = TIMEZONE.localize(datetime.combine(target_date, datetime.min.time())).replace(hour=hora_sel_num)
        
        # Càlcul de l'índex horari per a l'API
        start_of_today_utc = datetime.now(pytz.utc).replace(hour=0, minute=0, second=0, microsecond=0)
        hourly_index = int((target_dt.astimezone(pytz.utc) - start_of_today_utc).total_seconds() / 3600)
        timestamp_str = f"{target_dt.strftime('%d/%m/%Y')} a les {target_dt.strftime('%H:%Mh')}"
        
        st.info(f"**Previsió per:**\n\n**{timestamp_str}**")
        
        st.markdown("---")
        
        # Selector de Localitat
        poble_seleccionat = st.selectbox("📍 Localitat per al Sondeig:", options=sorted(CIUTATS_CATALUNYA.keys()))
        
        st.markdown("---")
        
        # Selector de Mapa
        mapa_seleccionat = st.selectbox("🗺️ Selecciona el tipus de mapa:",
            ["CAPE i Línies de Corrent", "Humitat (Punt de Rosada)", "Cisalladura 0-6km (Organització)", 
             "Cisalladura 0-1km (Tornados)", "Vent a 850 hPa", "Vent a 700 hPa", "Vent a 500 hPa", 
             "Fred en Altura (500 hPa)"])
        
    # --- CONTINGUT PRINCIPAL ---
    
    col_mapa, col_sondeig = st.columns([0.6, 0.4], gap="large")

    # --- COLUMNA DE MAPES ---
    with col_mapa:
        st.subheader("Mapes de Paràmetres Sinòptics (Catalunya)")
        
        if mapa_seleccionat == "Humitat (Punt de Rosada)":
            with st.spinner("Carregant mapa d'humitat..."):
                map_data, error = carregar_dades_mapa_rosada(hourly_index)
                if error: st.error(f"Error: {error}")
                else: fig = crear_mapa_punt_rosada(map_data['lons'], map_data['lats'], map_data['dewpoint_data'], timestamp_str, MAP_EXTENT_CAT); st.pyplot(fig, use_container_width=True); plt.close(fig)
        
        elif mapa_seleccionat == "CAPE i Línies de Corrent":
            # Selectbox específic per a aquest mapa (es queda a la columna de mapa)
            nivell_vent = st.selectbox("Nivell per a les línies de corrent:", [1000, 925], format_func=lambda x: f"{x} hPa")
            with st.spinner(f"Carregant mapa de CAPE i línies de corrent a {nivell_vent} hPa..."):
                map_data, error = carregar_dades_mapa_complet(nivell_vent, hourly_index)
                if error: st.error(f"Error: {error}")
                else:
                    fig = crear_mapa_cape_streamlines(map_data['lons'], map_data['lats'], map_data['cape_data'], map_data['speed_data'], map_data['dir_data'], nivell_vent, timestamp_str, MAP_EXTENT_CAT)
                    st.pyplot(fig, use_container_width=True); plt.close(fig)
                    
        elif "Cisalladura" in mapa_seleccionat:
            layer_name, top_level = ("0-6km", 500) if "0-6km" in mapa_seleccionat else ("0-1km", 925)
            with st.spinner(f"Carregant mapa de cisalladura {layer_name}..."):
                map_data, error = carregar_dades_mapa_cisalladura(hourly_index, top_level)
                if error: st.error(f"Error: {error}")
                else:
                    fig = crear_mapa_cisalladura(map_data['lons'], map_data['lats'], map_data['u_low'], map_data['v_low'], map_data['u_high'], map_data['v_high'], layer_name, timestamp_str, MAP_EXTENT_CAT)
                    st.pyplot(fig, use_container_width=True); plt.close(fig)
        
        elif "Vent a" in mapa_seleccionat:
            nivell_hpa = int(mapa_seleccionat.split(' ')[2])
            with st.spinner(f"Carregant mapa de vent a {nivell_hpa} hPa..."):
                map_data, error = carregar_dades_mapa_vents(nivell_hpa, hourly_index)
                if error: st.error(f"Error: {error}")
                else:
                    fig = crear_mapa_vents(map_data['lons'], map_data['lats'], map_data['speed_data'], map_data['dir_data'], nivell_hpa, timestamp_str, MAP_EXTENT_CAT)
                    st.pyplot(fig, use_container_width=True); plt.close(fig)

        elif mapa_seleccionat == "Fred en Altura (500 hPa)":
            with st.spinner("Carregant mapa de temperatura a 500 hPa..."):
                map_data, error = carregar_dades_mapa_temperatura_500hpa(hourly_index)
                if error: st.error(f"Error: {error}")
                else:
                    fig = crear_mapa_temperatura_500hpa(map_data['lons'], map_data['lats'], map_data['temp_data'], timestamp_str, MAP_EXTENT_CAT)
                    st.pyplot(fig, use_container_width=True); plt.close(fig)

    # --- COLUMNA DE SONDEIG ---
    with col_sondeig:
        st.subheader(f"Perfil Atmosfèric - {poble_seleccionat}")
        coords = CIUTATS_CATALUNYA[poble_seleccionat]
        
        with st.spinner(f"Processant dades del sondeig per a {poble_seleccionat}..."):
            data_tuple, error = carregar_dades_sondeig(coords['lat'], coords['lon'], hourly_index)
        
        if error: 
            st.error(f"❌ Error al carregar o processar el sondeig: {error}")
        else:
            sounding_data, params_calculats = data_tuple
            p, T, Td, u, v, heights, prof, _ = sounding_data
            
            # Mètriques clau (UX molt millorada)
            st.markdown("##### 📈 Paràmetres Clau per a Tempestes")
            col_met_1, col_met_2 = st.columns(2)
            
            with col_met_1:
                st.metric(label="SBCAPE (J/kg)", value=f"{params_calculats.get('SBCAPE', 0):.1f}")
                st.metric(label="SRH 0-3km (m²/s²)", value=f"{params_calculats.get('SRH_0_3', 0):.1f}", delta="Supercèl·lula")
            with col_met_2:
                st.metric(label="SBCIN (J/kg)", value=f"{params_calculats.get('SBCIN', 0):.1f}", delta_color="inverse")
                st.metric(label="SRH 0-1km (m²/s²)", value=f"{params_calculats.get('SRH_0_1', 0):.1f}", delta="Tornado")
            
            st.markdown("---")
            
            # Pestanyes per Skew-T i Hodògraf
            tab1, tab2 = st.tabs(["📊 Skew-T Log-P", "🔄 Hodògraf (Cinemàtica)"])
            
            with tab1:
                fig_skewt = crear_skewt(p, T, Td, u, v, prof, params_calculats, f"Sondeig - {poble_seleccionat}", timestamp_str)
                st.pyplot(fig_skewt, use_container_width=True); plt.close(fig_skewt)
            
            with tab2:
                fig_hodo = crear_hodograf_avancat(p, u, v, heights, params_calculats, f"Hodògraf - {poble_seleccionat}", timestamp_str)
                st.pyplot(fig_hodo, use_container_width=True); plt.close(fig_hodo)

if __name__ == "__main__":
    main()
