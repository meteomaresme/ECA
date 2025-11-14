import streamlit as st
import pandas as pd
import numpy as np
import base64

# Configuració de la pàgina
st.set_page_config(
    page_title="ECA - Caracterització d'Hàbitats",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ----------------------------------------------------------------------
# FUNCIONS AUXILIARS
# ----------------------------------------------------------------------

def display_pdf(file_path):
    """Funció per mostrar PDF incrustat (requereix Streamlit Cloud/entorn amb accés al fitxer)."""
    try:
        with open(file_path, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="600" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Error: El fitxer '{file_path}' no s'ha trobat. Assegura't que és accessible.")
    except Exception as e:
        st.error(f"Error en carregar el PDF: {e}")

# ----------------------------------------------------------------------
# PÀGINES DE L'APLICACIÓ
# ----------------------------------------------------------------------

def intro_page():
    st.title("🌱 UF 1: Caracterització d'Hàbitats")
    st.markdown("""
        Benvingut/da a l'aplicació interactiva per a l'estudi dels biomes, hàbitats peninsulars i les adaptacions de la flora i la fauna.
        
        Aquesta aplicació explora els continguts de les unitats formatives **NF 1.1** (Biomes de la Terra) i **NF 1.2** (Hàbitats Peninsulars) del Mòdul Professional de Medi Natural.
    """)
    # Imatge conceptual general (Línia corregida per evitar l'error de sintaxi)
    st.image("https://images.unsplash.com/photo-1620247656209-4b2a3a5f4f4f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80", caption="Interfície conceptual Biociència i Tecnologia", use_column_width=True)

    st.subheader("Contingut dels Mòduls")
    st.info("""
        * **Biomes de la Terra (NF 1.1):** Definició, tipus i factors climàtics (climogrames).
        * **Hàbitats Peninsulars (NF 1.2):** Classificació CORINE, exemples d'hàbitats a Catalunya i adaptacions.
    """)
    
    st.write("---")
    
    st.subheader("Material de Referència")
    st.markdown("Aquesta app es basa en els documents *NF 1.1 Biomes de la Terra* i *NF 1.2 Hàbitats Peninsulars*.")
    # Si vols incloure el PDF, descomenta la línia següent (assegura't que el PDF està a la mateixa carpeta):
    # st.subheader("NF 1.1 Biomes de la Terra (A1-A2)")
    # display_pdf("NF1.1.BiomesdelaTerra_A1A2.pdf")

def biomes_page():
    st.title("🌍 1. Biomes de la Terra i Distribució")
    st.subheader("Què és un Bioma?")
    st.markdown("""
        Un **bioma** és el conjunt de comunitats que ocupen una mateixa àrea geogràfica,
        caracteritzat per una vegetació climàtica uniforme i un clima característic (NF 1.1, pàg. 3).
    """)

    st.subheader("Mapa Global dels Biomes")
    # Imatge de mapa de Biomes
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e0/World_biomes_map.svg", caption="Mapa Global de la Distribució dels Biomes Terrestres", use_column_width=True)
    
    st.write("---")

    st.subheader("Exemples de Biomes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Bosc Mediterrani (Escleròfil)**")
        st.markdown("Clima temperat, estius secs i càlids. Vegetació de fulla dura (alzines, pins) (NF 1.1, pàg. 31).")
        st.markdown(f"Fauna com el Linx Ibèric (NF 1.1, pàg. 32).")
        # Imatge: Linx Ibèric
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Lynx_pardinus_Andujar_7.jpg/1280px-Lynx_pardinus_Andujar_7.jpg", caption="Linx ibèric al matoll mediterrani", use_column_width=True)

    with col2:
        st.markdown("**Taiga / Bosc Boreal**")
        st.markdown("Clima fred, hiverns llargs. Boscos de coníferes (pins, avets).")
        # Imatge: Bosc Boreal
        st.image("https://images.unsplash.com/photo-1555546194-e3a5a73099b2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80", caption="Bosc Boreal (Taiga) a l'hivern", use_column_width=True)


def climograms_page():
    st.title("📊 2. Climogrames i Condicions Climàtiques")
    st.markdown("""
        Els **climogrames** ens permeten entendre les condicions climàtiques d'una zona,
        mostrant la relació entre la temperatura mitjana mensual i la precipitació (NF 1.1 A3 / _NF1.1. Climogrames.pptx.pdf, pàg. 2).
    """)

    st.subheader("Diagrama de Walter-Lieth")
    # Imatge: Climograma Walter-Lieth
    st.image("https://www.geo.fu-berlin.de/en/v/soga-r/Introduction-to-R/Plotting-Data/Walter_Lieth/image_03.png", caption="Exemple de Climograma de Walter-Lieth", use_column_width=True)

    st.write("---")

    st.subheader("Interpretació Clau")
    st.markdown("""
        * **Línia Vermella/Taronja:** Temperatura $(^{\circ}C)$.
        * **Barres Blaves:** Precipitació (mm).
        * **Aridesa:** Es produeix quan la línia de Temperatura és **per sobre** de la línia de Precipitació (utilitzant la relació $T \times 2 = P$).
    """)
    
    st.subheader("Exemples de Climes (Segons els teus materials)")
    
    # Taula simple per il·lustrar tipus (basada en _NF1.1. Climogrames.pptx.pdf)
    data = {
        "Tipus de Clima": ["Tropical", "Polar", "Mediterrani"],
        "Característica Climograma": ["T alt, P molt alt", "T molt baix ($< 0^{\circ}C$), P baix", "T alt a l'estiu, Aridesa estival (T > P)"],
        "Bioma Típic": ["Selva Tropical", "Tundra/Glaç", "Bosc Escleròfil"],
    }
    st.table(pd.DataFrame(data))

def habitats_page():
    st.title("🇪🇸 3. Hàbitats Peninsulars i de Catalunya")
    st.markdown("""
        La Península Ibèrica es caracteritza per una gran diversitat biogeogràfica, influenciada per la seva posició i relleu (NF 1.2). El sistema de classificació d'hàbitats més utilitzat a la UE és el **CORINE Biotopes** (NF1.2.HabitatsCatalunya.pptx, pàg. 4).
    """)
    
    st.subheader("Regions Biogeogràfiques")
    # Imatge: Mapa Biogeogràfic Peninsular
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/Iberian_Peninsula_biogeographic_regions_map.svg/1024px-Iberian_Peninsula_biogeographic_regions_map.svg.png", caption="Mapa de les Regions Biogeogràfiques de la Península Ibèrica", use_column_width=True)

    st.write("---")

    st.subheader("Hàbitats Clau a Catalunya (NF 1.2)")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Bosc de Pi Negre** *(Pinus uncinata)*")
        st.markdown("Típic de l'estatge Subalpí (1800-2400 m), resistent al fred i la neu. És un hàbitat de muntanya (NF1.2.HabitatsCatalunya.pptx, pàg. 3).")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Pinus_uncinata_pirineus.jpg/1280px-Pinus_uncinata_pirineus.jpg", caption="Pi Negre als Pirineus", use_column_width=True)
        
    with col2:
        st.markdown("**La Fageda** *(Fagus sylvatica)*")
        st.markdown("Bosc caducifoli, típic de muntanya mitjana (Medioeuropeu subatlàntic), vessants obacs i sòls àcids (NF1.2.HabitatsaEspanya.pptx, pàg. 54).")
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/La_Fageda_d%27en_Jord%C3%A0_-_2015-11-04_-_2.jpg/1280px-La_Fageda_d%27en_Jord%C3%A0_-_2015-11-04_-_2.jpg", caption="Fageda d'en Jordà (La Garrotxa)", use_column_width=True)

    with col3:
        st.markdown("**Alzinar** *(Quercus ilex)*")
        st.markdown("Bosc perennifoli, típic mediterrani escleròfil (fulla dura). Domina zones seques i càlides (NF 1.1, pàg. 31 / NF1.2.HabitatsCatalunya.pptx, pàg. 3).")
        # Imatge: Alzinar
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Quercus_ilex_forest.jpg/1024px-Quercus_ilex_forest.jpg", caption="Alzinar mediterrani", use_column_width=True)

def adaptations_page():
    st.title("🔬 4. Adaptacions de Flora i Fauna")
    st.markdown("Els organismes desenvolupen adaptacions per sobreviure a les condicions extremes del seu hàbitat (ADAPTACIONS_FLORA.pdf).")

    st.subheader("Adaptacions de la Flora")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**Adaptació a la Sequera (Xeròfiles)**")
        st.markdown("""
            * **Fulles petites/espines:** Redueixen la superfície de transpiració.
            * **Acumulació d'aigua:** Teixits suculents (cactus, crasses).
            * **Arrels profundes:** Per buscar aigua freàtica.
            *(ADAPTACIONS_FLORA.pdf, pàg. 5)*
        """)
        # Imatge: Planta Suculenta
        st.image("https://images.unsplash.com/photo-1549410148-28c949c9f69b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80", caption="Planta Suculenta (adaptació xeròfila)", use_column_width=True)

    with col2:
        st.markdown("**Adaptació al Fred Intens**")
        st.markdown("""
            * **Plantes petites i prop del terra:** Millor aprofitament de la calor (Tundra/Alta Muntanya).
            * **Saba espessa:** Ralentir la congelació.
            * **Pèrdua de fulla:** Evitar congelació (caducifolis).
            *(ADAPTACIONS_FLORA.pdf, pàg. 4)*
        """)
        # Imatge: Adaptació al fred (Bedoll - Betula Pendula)
        st.image("https://images.unsplash.com/photo-1542603837-f8e65e6d0752?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80", caption="Betula Pendula (bedoll) en hivern", use_column_width=True)

    st.subheader("Adaptacions de la Fauna (Exemple)")
    st.markdown("""
        El Linx Ibèric, que habita el bosc escleròfil mediterrani (NF 1.1), té adaptacions per a la caça, com:
        * **Orelles amb pinzells de pèl:** Milloren la percepció auditiva.
        * **Potes amples i peludes:** Actuen com a 'raquetes' per caminar per la neu (encara que al clima mediterrani és menys freqüent, ajuden també en sòls tous).
    """)

# ----------------------------------------------------------------------
# ESTRUCTURA PRINCIPAL DE STREAMLIT
# ----------------------------------------------------------------------

# Creació de la barra lateral (Sidebar)
st.sidebar.title("Menú d'ECA")
selection = st.sidebar.radio("Navegació", [
    "Introducció",
    "1. Biomes de la Terra",
    "2. Climogrames",
    "3. Hàbitats Peninsulars",
    "4. Adaptacions"
])

# Crida a la funció de la pàgina seleccionada
if selection == "Introducció":
    intro_page()
elif selection == "1. Biomes de la Terra":
    biomes_page()
elif selection == "2. Climogrames":
    climograms_page()
elif selection == "3. Hàbitats Peninsulars":
    habitats_page()
elif selection == "4. Adaptacions":
    adaptations_page()
    
st.sidebar.markdown("---")
st.sidebar.markdown("*(MP2 - Medi Natural, IMR)*")
