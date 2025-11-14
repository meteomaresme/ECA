import streamlit as st
import time

# --- MÒDUL D'INICIALITZACIÓ (Sistema de Càrrega Única) ---
def initialize_system():
    # Inicialització de variables de sessió
    if 'system_status' not in st.session_state:
        st.session_state.system_status = "INITIALIZING"
        st.session_state.progress = 0
        st.session_state.config = {
            "PROJECT_NAME": "TERMINAL_UF1_HABITATS",
            "VERSION": "9.5.VISUAL_OVERHAUL", # Nova Versió amb millores visuals completes
            "AUTHORS": "IMR_Bio-Lab"
        }

def run_boot_sequence():
    initialize_system()
    
    # 1. Crear un contenidor placeholder per a la seqüència de boot
    boot_placeholder = st.empty()

    with boot_placeholder.container():
        st.title(">> 💻 Terminal de Caracterització: Seqüència de Boot")
        st.code("SYSTEM: CHECKING MODULE INTEGRITY AND CONFIGURATION...")
        
        progress_bar = st.progress(0)
        
        # Simula la càrrega de dades amb granularitat
        components = {
            "INIT_CORE_CORE (05%)": 0.05,
            "NF1.1_BIOMES_A1_A2 (15%)": 0.20,
            "NF1.1_CLIMOGRAM_ENGINE_A3 (15%)": 0.35,
            "NF1.2_HABITAT_PENINSULAR_A2 (15%)": 0.50,
            "NF1.2_HABITAT_CAT_A3_PART1 (15%)": 0.65,
            "NF1.3_PROTECTION_PROTOCOLS (15%)": 0.80,
            "NF1.1_BIODIVERSITY_ADAPTATIONS (19%)": 0.99
        }
        
        current_progress = 0
        
        # Bucle de càrrega visual
        for module, target in components.items():
            st.code(f"LOADING MODULE: {module}...")
            time.sleep(0.05) 
            while current_progress < target:
                current_progress += 0.01
                progress_bar.progress(min(current_progress, target))
                
        progress_bar.progress(1.0)
        st.success(f"✅ BOOT SEQUENCE COMPLETE. SYSTEM ONLINE. V.{st.session_state.config.get('VERSION', 'N/A')}")
        time.sleep(1) 

    # 2. ELIMINAR EL CONTENIDOR DE BOOT
    boot_placeholder.empty()
    st.session_state.system_status = "ONLINE"


# --- Configuració del Tema Futurista (CSS Fix i Més Detalls) ---
def inject_futuristic_style():
    st.markdown(
        """
        <style>
        /* 1. Definició de la Paleta de Colors */
        :root {
            --primary-color: #00FFFF; /* Vibrant Cyan */
            --primary-color-800: #00CCCC;
            --background-dark: #0A0A0A; 
            --background-medium: #1A1A1A; 
            --text-color: #E0E0E0;
            --highlight-color: #00FF7F; /* Green Terminal Text */
            --warning-color: #FFD700; /* Gold for warnings */
        }

        /* 2. Configuració General de la Pàgina */
        .stApp {
            background-color: var(--background-dark);
            color: var(--text-color);
            font-family: 'Consolas', 'Courier New', monospace;
        }
        
        /* 3. Títols amb Efecte "Glow" Animado */
        h1 {
            color: var(--primary-color); 
            text-shadow: 0 0 7px rgba(0, 255, 255, 0.7); 
            border-bottom: 3px solid var(--primary-color-800);
            padding-bottom: 10px;
            margin-top: 0px;
            animation: glow 1.5s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 0 0 5px rgba(0, 255, 255, 0.5); }
            to { text-shadow: 0 0 10px rgba(0, 255, 255, 1), 0 0 15px rgba(0, 255, 255, 0.8); }
        }
        
        /* 4. Subtítols (Headers de Secció) */
        h2, h3 {
            color: var(--text-color); 
            border-left: 6px solid var(--primary-color); 
            padding-left: 15px;
            margin-top: 30px;
            background-color: var(--background-medium);
            padding: 10px 15px;
            box-shadow: 0 0 5px rgba(0, 255, 255, 0.2);
            border-radius: 5px;
        }

        /* 5. Contenidors (Panells d'Informació) */
        .st-emotion-cache-1c7v0s, .st-emotion-cache-1ftrz5p, .st-emotion-cache-qn80jo, .st-emotion-cache-f1g04y {
             background-color: var(--background-medium);
             padding: 15px;
             border-radius: 8px;
             border: 1px solid var(--primary-color-800);
             box-shadow: 0 0 8px rgba(0, 255, 255, 0.2);
             margin-bottom: 15px;
        }
        
        /* 6. Barra Lateral (Sidebar) */
        [data-testid="stSidebar"] {
            background-color: #050505; 
            border-right: 2px solid var(--primary-color);
            box-shadow: 2px 0 10px rgba(0, 255, 255, 0.3);
        }
        
        /* 7. Altres elements UI (Code, Alerts) */
        .stCode {
            background-color: #000000;
            border: 1px solid var(--primary-color-800);
            color: var(--highlight-color);
            font-size: 0.9em;
            padding: 10px;
            border-radius: 5px;
        }

        .stAlert {
            border-left: 5px solid;
            border-radius: 5px;
        }
        
        /* Estils personalitzats per a Radio Buttons */
        div[role=radiogroup] label:has(input:checked) {
            background-color: var(--primary-color-800);
            color: var(--background-dark) !important;
            border-radius: 5px;
            padding: 5px 10px;
            font-weight: bold;
        }
        div[role=radiogroup] label {
            background-color: var(--background-dark);
            color: var(--text-color);
            border: 1px solid var(--primary-color-800);
            border-radius: 5px;
            padding: 5px 10px;
            margin: 2px;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
        }
        div[role=radiogroup] label:hover {
            background-color: var(--primary-color-800);
            color: var(--background-dark) !important;
        }
        
        /* Classes per ressaltar text */
        .highlight {
            color: var(--highlight-color);
            font-weight: bold;
            text-shadow: 0 0 3px rgba(0, 255, 127, 0.5);
        }
        .warning-highlight {
            color: var(--warning-color);
            font-weight: bold;
            text-shadow: 0 0 3px rgba(255, 215, 0, 0.5);
        }
        
        /* Botons futuristes */
        .stButton button {
            background: linear-gradient(45deg, var(--primary-color-800), var(--primary-color));
            color: var(--background-dark);
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
            transition: all 0.3s ease-in-out;
            box-shadow: 0 0 10px rgba(0, 255, 255, 0.5);
        }
        .stButton button:hover {
            box-shadow: 0 0 15px rgba(0, 255, 255, 0.8);
            transform: translateY(-2px);
        }

        /* Estil per a Expanders */
        .streamlit-expanderHeader {
            background-color: var(--background-medium);
            color: var(--primary-color);
            border-left: 5px solid var(--primary-color);
            border-radius: 5px;
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Funcions Auxiliars ---
def highlight(text, color="highlight"):
    """Funció per aplicar estils CSS al text dins de st.markdown."""
    return f'<span class="{color}">{text}</span>'

# --- Configuració de la Pàgina ---
st.set_page_config(
    page_title="Terminal UF1: Caracterització d'Hàbitats",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Injectar l'estil personalitzat
inject_futuristic_style()

# **CORRECCIÓ CLAU:** Executar la seqüència de boot una sola vegada a l'inici
if 'system_status' not in st.session_state or st.session_state.system_status == "INITIALIZING":
    initialize_system()
    if st.session_state.system_status == "INITIALIZING":
        run_boot_sequence()

# --- FUNCIÓ PRINCIPAL DEL QUIZ ---
def run_quiz():
    st.header(f"❓ Posa't a Prova! ({highlight('Terminal de Test - NF 1.1, 1.2, 1.3')})")
    st.markdown("---")
    st.info("🟢 **EXECUTANT TEST DE VALIDACIÓ DE CONEIXEMENTS...** Aquesta prova cobreix totes les unitats formatives.")
    
    preguntes = {
        "Q1: Climograma (Sequera)": {
            "pregunta": f"En un climograma, la condició de {highlight('Sequera/Aridesa')} es dóna quan (Regla de Gaussen):",
            "opcions": ["La P supera $2 \\times T$", "La Tº supera la P ($T > P$)", "$T \\times 2 > P$"],
            "correcta": "La Tº supera la P ($T > P$)"
        },
        "Q2: Bosc Mediterrani (Flora)": {
            "pregunta": f"Quin estrat vegetal, a més de l'arbre dominant (Alzina), pren gran rellevància en el {highlight('Bosc Mediterrani Escleròfil')}?",
            "opcions": ["L'estrat arbori secundari", "Només l'estrat herbaci", "Els estrats arbustiu, herbaci i lianoide"],
            "correcta": "Els estrats arbustiu, herbaci i lianoide"
        },
        "Q3: Adaptació (Límits Tèrmics)": {
            "pregunta": f"Per sota de quina Tº la planta {highlight('paralitza l\'activitat')} d'absorció i processament d'aigua?",
            "opcions": ["$10^{\\circ}C$", "$0^{\\circ}C$", "$-5^{\\circ}C$", "$45^{\\circ}C$"],
            "correcta": "$0^{\\circ}C$"
        },
        "Q4: Biodiversitat (Endemisme)": {
            "pregunta": f"Quina de les següents espècies és un exemple d'{highlight('endemisme montà')} als Pirineus?",
            "opcions": ["Linx Ibèric", "Desman dels Pirineus (*Galemys pyrenaicus*)", "Faig (*Fagus sylvatica*)"],
            "correcta": "Desman dels Pirineus (*Galemys pyrenaicus*)"
        },
        "Q5: Classificació (NF 1.3)": {
            "pregunta": f"Quin sistema de classificació {highlight('jeràrquica')} s'utilitza a la UE per catalogar tots els hàbitats?",
            "opcions": ["Ramsar", "CORINE Biotopes", "ZEPA", "Whittaker"],
            "correcta": "CORINE Biotopes"
        },
        "Q6: Regió Biogeogràfica": {
            "pregunta": f"La Regió Eurosiberiana es caracteritza per la dominància de:",
            "opcions": ["Boscos Perennifolis Escleròfils", f"{highlight('Boscos Caducifolis')} (Roures, Faigs)", "Vegetació estenoterma"],
            "correcta": "Boscos Caducifolis (Roures, Faigs)"
        },
        "Q7: Hàbitats Catalunya (Fageda)": {
            "pregunta": f"La Fageda es troba típicament en climes Medioeuropeus subatlàntics i sobre quin tipus de sòl/substrat?",
            "opcions": ["Terrenys calcaris", f"{highlight('Terrenys àcids')} (o sòls acidificats)", "Terrenys salins"],
            "correcta": "Terrenys àcids (o sòls acidificats)"
        },
        "Q8: Adaptació (Foc - Serotinia)": {
            "pregunta": f"Quin arbre utilitza el mecanisme de {highlight('Serotinia')} (obertura de pinyes amb la calor) com a adaptació al foc?",
            "opcions": ["Faig (*Fagus sylvatica*)", "Alzina (*Quercus ilex*)", "Pi blanc (*Pinus halepensis*)"],
            "correcta": "Pi blanc (*Pinus halepensis*)"
        },
        "Q9: Biodiversitat (Aïllament)": {
            "pregunta": f"Quin factor pot causar la formació d'endemismes a part de l'aïllament geogràfic?",
            "opcions": ["Un augment de la pluja anual", f"{highlight('Un canvi brusc de les condicions del medi')}", "Una disminució de la Tº a l'estiu"],
            "correcta": "Un canvi brusc de les condicions del medi (aridesa, glaciacions)"
        },
        "Q10: Xarxa Natura 2000": {
            "pregunta": f"La Xarxa Natura 2000 està formada per les ZEC i per quins altres espais de protecció?",
            "opcions": ["ZAD (Zones d'Alt Valor)", f"{highlight('ZEPA')} (Zones d'Especial Protecció per a les Aus)", "ZER (Zones d'Exclusió Ràpida)"],
            "correcta": "ZEPA (Zones d'Especial Protecció per a les Aus)"
        },
        "Q11: Bosc de Pi Negre (Catalunya)": {
            "pregunta": f"El Bosc de Pi Negre és típic de quin ambient a Catalunya?",
            "opcions": ["Litoral (dunes)", f"{highlight('Alta Muntanya')} (Alpí / Subalpí)", "Zona Prelitoral"],
            "correcta": "Alta Muntanya (Alpí / Subalpí)"
        },
        "Q12: Classificació Tèrmica": {
            "pregunta": f"Les plantes que només poden viure en un rang de temperatures molt concret s'anomenen:",
            "opcions": ["Euritermes", "Xeròfiles", f"{highlight('Estenotermes')}"],
            "correcta": "Estenotermes"
        }
    }

    respostes_usuari = {}
    with st.form(key="quiz_form_ampliat"):
        for i, (key, value) in enumerate(preguntes.items()):
            st.markdown(f"#### {key}")
            st.markdown(value["pregunta"], unsafe_allow_html=True)
            respostes_usuari[key] = st.radio(
                "Selecciona la teva resposta:", options=value["opcions"], key=f"q_amp{i}", label_visibility="collapsed"
            )
            st.markdown("---")
        submitted = st.form_submit_button("⏩ INICIAR ESCANEIG DE RESULTATS (ENVIAR) 🚀")

    if submitted:
        score = 0
        total_preguntes = len(preguntes)
        st.header("✅ INFORME DE VALIDACIÓ FINAL:")
        for key, value in preguntes.items():
            resposta_correcta = value["correcta"]
            resposta_usuari = respostes_usuari[key]
            
            if resposta_usuari == resposta_correcta:
                score += 1
                st.success(f"**{key}:** Resposta Correcta! -> `{resposta_usuari}`")
            else:
                st.error(f"**{key}:** Resposta Incorrecta. La teva resposta: `{resposta_usuari}`. La correcta era: `{resposta_correcta}`")

        st.markdown("---")
        st.subheader(f"Puntuació Final del Sistema: **{score}/{total_preguntes}**")
        percentatge = score / total_preguntes
        st.progress(percentatge)

        if percentatge == 1.0:
            st.balloons()
            st.success("🎉 **VALIDACIÓ COMPLETA! Codi 100% Acceptat!** 🎉")
        elif percentatge >= 0.7:
            st.warning("VALIDACIÓ PARCIALMENT OK. Repassa els punts febles.")
        else:
            st.error("ERROR CRÍTIC. Repassa la UF1 abans de tornar a executar el test.")

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("🧬 Mòdul Bio-Explorador 9.5")
st.sidebar.markdown("Un recorregut digital per la vida a la Terra. (**MP 02: Medi Natural**)")
pagina = st.sidebar.radio(
    "🖥️ SELECCIÓ DE MÒDUL (UF 1):",
    [
        "🏠 Inici & Estat del Sistema",
        "🌍 Biomes de la Terra (NF 1.1)",
        "🌲 Classificació dels Biomes Principals",
        "📊 Climogrames i Distribució",
        "🇪🇸 Hàbitats Peninsulars i Protecció (NF 1.2/1.3)",
        "🏞️ Hàbitats de Catalunya (Detall Exhaustiu)",
        "🌱 Adaptacions i Biodiversitat (NF 1.1)",
        "❓ Posa't a Prova! (Quiz)"
    ],
    index=0
)
st.sidebar.markdown("---")
st.sidebar.info(f"Codi Generat | Versió: {st.session_state.config.get('VERSION', 'N/A')}\n\n© IMR Bio-Lab")

# --- Contingut de les Pàgines ---
if pagina == "🏠 Inici & Estat del Sistema":
    st.title("🤖 Terminal de Caracterització d'Hàbitats (UF1)")
    st.markdown("---")
    st.header(f"🎯 Matriu d'Objectius ({highlight('NF 1.1, 1.2, 1.3')})")
    st.markdown("Aquesta aplicació cobreix els coneixements mínims requerits per la Unitat Formativa 1.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f">> {highlight('NF 1.1 (Biomes, Climogrames, Biodiversitat)')}")
        st.markdown(f"""
        - **A1, A2 (Biomes):** El {highlight('Bioma')} és un conjunt de comunitats amb vegetació climàtica uniforme.
        - **A3 (Climogrames):** Anàlisi Tº/P. La {highlight('Sequera')} es dóna quan $P < 2 \\times T$ o $T > P$.
        - **Biodiversitat:** {highlight("Varietat d'éssers vius")} resultant de l'evolució i l'acció humana.
        """, unsafe_allow_html=True)
        
        st.subheader(f">> {highlight('NF 1.2/1.3 (Hàbitats, Biotops, Protecció)')}")
        st.markdown(f"""
        - **Definició Clau:** {highlight('Biotop')} (territori) vs. {highlight('Hàbitat')} (espai físic amb recursos).
        - **CORINE Biotopes (NF 1.3):** Classificació {highlight('jeràrquica')} europea per a tots els hàbitats.
        """, unsafe_allow_html=True)
    
    with col2:
        st.subheader(f">> {highlight('NF 1.2 (Hàbitats Peninsulars i Catalunya)')}")
        st.markdown(f"""
        - **Regions Biogeogràfiques:** Eurosiberiana (Caducifolis), Mediterrània (Escleròfils), Macaronèsica (Endemisme), Alpina (Fred intens).
        - **Fageda (Catalunya):** Clima Medioeuropeu subatlàntic, sobre {highlight('terrenys àcids')}.
        - **Alzinar:** Bosc {highlight('perennifoli escleròfil')} adaptat a la sequera estival.
        - **Xarxa Natura 2000 (NF 1.3):** Xarxa d'àrees de conservació amb {highlight('ZEC')} i {highlight('ZEPA')}.
        """, unsafe_allow_html=True)
        st.info(f"EXECUCIÓ OK. Concentració de dades a l'àrea d'informació. Versió {st.session_state.config.get('VERSION', 'N/A')}")

elif pagina == "🌍 Biomes de la Terra (NF 1.1)":
    st.title(f"🌍 Cartografia Global: {highlight('Biomes de la Terra (NF 1.1: A1, A2)')}")
    st.markdown("Unitats de gran extensió amb una vegetació climàtica uniforme i clima característic.")

    st.subheader(f"Definicions de Biomes Clau ({highlight('Més Enllà del Mediterrani')})")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### **Pastures (Grasslands)**")
        st.markdown(f"- **Clima:** Temperat amb pluges moderades.")
        st.markdown(f"- **Vegetació:** Domini de {highlight('gramínies')} i herbes.")
    with col2:
        st.markdown("#### **Sabana (Tropical Grasslands)**")
        st.markdown(f"- **Clima:** Tropical amb {highlight('estació seca marcada')}.")
        st.markdown(f"- **Vegetació:** Gramínies altes amb arbres aïllats.")

    with st.expander(f"Fitxa Tècnica: {highlight('Bosc Escleròfil Mediterrani')}", expanded=True):
        tab_flora, tab_fauna, tab_estrategia = st.tabs(["[1] Flora i Estructura", "[2] Fauna", "[3] Clima i Sòl"])
        with tab_flora:
            st.subheader(f"Estratègia {highlight('Escleròfil·la')} i Estructura Vegetal")
            st.markdown(f"- Vegetació {highlight('escleròfil·la')} (fulla dura) i {highlight('perenne')} per resistir la sequera.")
            st.markdown(f"- **Arbres Clau:** Alzines, Sureres, Oliveres.")
            st.markdown(f"- **Estrats Inferiors:** Gran rellevància dels estrats {highlight('Arbustiu, Herbaci i Lianoide')}.")
        with tab_fauna:
            st.subheader("Fauna Clau per Nínxol Ecològic")
            st.markdown(f"""
            - **Herbívors:** Cabirols, Esquirols, Llebres.
            - **Carnívors:** Guineus, geneta, {highlight('Linx Ibèric')} (el més amenaçat).
            - **Omnívors:** Porc senglar, Teixó.
            """, unsafe_allow_html=True)
        with tab_estrategia:
            st.subheader("Clima i Sòl (Factors Determinants)")
            st.markdown(f"""
            - **Factor Clau:** La {highlight('sequera estival')}.
            - **Sòl:** Tendeix a ser {highlight('pobre en matèria orgànica')}.
            """, unsafe_allow_html=True)

elif pagina == "🌲 Classificació dels Biomes Principals":
    st.title(f"🌲 Classificació dels {highlight('Biomes Principals (NF 1.1: A2)')}")
    st.markdown("Anàlisi comparativa dels biomes de latituds extremes i humits.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. Tundra (Fred Extrem)")
        st.markdown(f"""
        - **Clima:** Tº mitjanes sota $0^{\\circ}C$ gran part de l'any.
        - **Vegetació:** {highlight('Sense arbres')}. Molses i líquens.
        - **Sòl Clau:** {highlight('Permafrost')} (permanentment congelat).
        """, unsafe_allow_html=True)
        st.subheader("3. Bosc de Coníferes o Taiga")
        st.markdown(f"""
        - **Vegetació:** Arbres de {highlight('fulla perenne acicular')} (pins, avets).
        - **Adaptació:** Forma {highlight('cònica')} per evitar acumulació de neu.
        """, unsafe_allow_html=True)
    with col2:
        st.subheader("2. Desert (Dèficit Hídric Extrem)")
        st.markdown(f"""
        - **Clima:** Precipitació molt baixa ($< 250$ mm/any).
        - **Vegetació:** Adaptada a la sequera ({highlight('xeròfites')}, cactus).
        """, unsafe_allow_html=True)
        st.subheader("4. Selva Tropical (Humitat Extrema)")
        st.markdown(f"""
        - **Clima:** Càlid i plujós tot l'any ({highlight('sense estació seca')}).
        - **Vegetació:** {highlight('Alta biodiversitat')} amb molts estrats.
        - **Sòl:** Pobre a causa del rentat de nutrients ({highlight('lixiviació')}).
        """, unsafe_allow_html=True)

elif pagina == "📊 Climogrames i Distribució":
    st.title(f"📊 Anàlisi Gràfica Climàtica ({highlight('NF 1.1: A3')})")
    st.markdown("Eina essencial per caracteritzar un bioma mitjançant Tº i Precipitació (P).")

    with st.expander(f"Detall Tècnic: {highlight('Interpretació Visual i Regles Crítiques')}", expanded=True):
        st.image("https://www.meteorologiaenred.com/wp-content/uploads/2018/06/Climograma.jpg", caption="Exemple de Climograma de Walter i Lieth")
        
        st.subheader(f"1. ⚙️ Guia de Lectura ({highlight('Regla de Gaussen')})")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            - **Línia Vermella (Tº):** Temperatura mitjana mensual.
            - **Barres Blaves (P):** Precipitació mitjana mensual.
            - **Relació Clau:** L'escala $10^{\\circ}C = 20$ mm permet la detecció visual de la sequera.
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            - {highlight('HUMITAT')}: **P** > **T**.
            - {highlight('SEQUERA (ARIDESA)')}: **T** > **P**.
            - {highlight('GELADA/FRED')}: **T** < $0^{\\circ}C$.
            """, unsafe_allow_html=True)

        st.subheader(f"2. 🌍 Escenaris Climàtics Clàssics")
        tab_med, tab_oce, tab_pol = st.tabs(["[A] Mediterrani", "[B] Oceànic", "[C] Polar / Alta Muntanya"])
        with tab_med:
            st.markdown(f"#### **Escenari {highlight('Mediterrani Típic')}**")
            st.markdown(f"- **Factor Clau:** Forta {highlight('sequera estival')}.")
            st.markdown(f"- **Visualització:** La línia de Tº supera la de P a l'estiu.")
        with tab_oce:
            st.markdown(f"#### **Escenari {highlight('Temperat Oceànic')}**")
            st.markdown(f"- **Factor Clau:** {highlight('Absència de sequera')}.")
            st.markdown(f"- **Visualització:** La línia de P sempre està per sobre de la de Tº.")
        with tab_pol:
            st.markdown(f"#### **Escenari {highlight('Polar / Alta Muntanya')}**")
            st.markdown(f"- **Factor Clau:** {highlight('Fred extrem')} limitant.")
            st.markdown(f"- **Visualització:** La Tº cau per sota de $0^{\\circ}C$ durant diversos mesos.")

elif pagina == "🇪🇸 Hàbitats Peninsulars i Protecció (NF 1.2/1.3)":
    st.title(f"🇪🇸 Regions Biogeogràfiques i Protecció ({highlight('NF 1.2 & 1.3')})")
    
    st.subheader(f"Mòdul {highlight('NF 1.2: Regions Biogeogràfiques')}")
    t1, t2, t3, t4 = st.tabs(["[1] Eurosiberiana", "[2] Mediterrània", "[3] Macaronèsica", "[4] Alpina"])
    with t1: st.markdown(f"**Clima:** Temperat i humit, {highlight('sense aridesa estival')}. **Vegetació:** {highlight('Boscos Caducifolis')}.")
    with t2: st.markdown(f"**Clima:** Estius secs i calorosos. **Vegetació:** {highlight('Boscos Perennifolis Escleròfils')}.")
    with t3: st.markdown(f"**Particularitat:** Aïllament insular, {highlight('altíssim nivell d\'endemisme')}. **Flora:** Laurissilva.")
    with t4: st.markdown(f"**Condicions:** {highlight('Fred intens')}. **Vegetació:** Bosc Subalpí (Pi Negre) i Prats Alpins.")

    st.subheader(f"Mòdul {highlight('NF 1.3: Classificació i Protecció')}")
    col1, col2 = st.columns(2)
    with col1:
        st.header(f"Classificació ({highlight('CORINE Biotopes')})")
        st.markdown(f"""
        - **Base:** Sistema {highlight('jeràrquic')} estandarditzat per la UE.
        - **Abast:** Classifica hàbitats {highlight('naturals, seminaturals i artificialitzats')}.
        """, unsafe_allow_html=True)
    with col2:
        st.header(f"Xarxa {highlight('Natura 2000')}")
        st.markdown(f"""
        - {highlight('ZEC:')} Protegeix hàbitats i espècies.
        - {highlight('ZEPA:')} Protegeix aus.
        """, unsafe_allow_html=True)

elif pagina == "🏞️ Hàbitats de Catalunya (Detall Exhaustiu)":
    st.title(f"🏞️ Fitxer d'Hàbitats Nacionals ({highlight('NF 1.2: A3')})")
    
    tabs = st.tabs(["[1] Boscos de Fulla Caduca i Perenne", "[2] Boscos de Pi i Arbusts", "[3] Formacions Herbàcies"])
    with tabs[0]:
        st.header(f"🌳 La {highlight('Fageda (*Fagus sylvatica*)')}")
        col1, col2 = st.columns(2)
        with col1: st.markdown(f"**Clima:** {highlight('Medioeuropeu subatlàntic')}. **Substrat:** {highlight('Terrenys àcids')}.")
        with col2: st.markdown(f"**Sotabosc:** Pobre per manca de llum, amb plantes acidòfiles com el grèvol.")
        
        st.header(f"🌲 L'{highlight('Alzinar (*Quercus ilex*)')}")
        col1, col2 = st.columns(2)
        with col1: st.markdown(f"**Tipus:** Bosc {highlight('escleròfil mediterrani')}. **Funció:** Redueix la {highlight('transpiració')} per sobreviure a la sequera.")
        with col2: st.markdown(f"**Sotabosc:** Ric i divers, amb marfull, arboç i lianes.")
        
    with tabs[1]:
        st.header(f"🌳 Boscos de Pi ({highlight('Diversitat Ecològica')})")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"#### **Alta Muntanya/Interior:**")
            st.markdown(f"- {highlight('Pi Negre (*P. uncinata*)')}: Resistent al fred extrem.")
            st.markdown(f"- {highlight('Pi Roig (*P. sylvestris*)')}: Muntanya mitjana, sòls pobres.")
        with col2:
            st.markdown(f"#### **Litoral (Piròfites):**")
            st.markdown(f"- {highlight('Pi Blanc (*P. halepensis*)')}: Adaptat al foc ({highlight('Serotinia')}).")
            st.markdown(f"- **Arbustives:** {highlight('Màquia')} (densa) i {highlight('Brolla')} (oberta).")
    with tabs[2]:
        st.header(f"🌱 Formacions Herbàcies ({highlight('Classificació Tècnica')})")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Definicions d'Estructura")
            st.markdown(f"- **Prat:** Comunitat dominada per gramínies, aspecte {highlight('compacte')}.")
            st.markdown(f"- **Pradell:** Prat de {highlight('reduïda extensió')}.")
        with col2:
            st.subheader("Tipus de Prats Clau")
            st.markdown(f"- **Prats Alpins:** Sobre el límit del bosc.")
            st.markdown(f"- **Prats Halòfils:** Zones litorals o salines.")
            st.markdown(f"- **Aiguamolls:** Alta biodiversitat.")

elif pagina == "🌱 Adaptacions i Biodiversitat (NF 1.1)":
    st.title(f"🌱 Adaptacions i Biodiversitat ({highlight('NF 1.1')})")

    with st.expander(f"Mòdul [1]: {highlight('Adaptacions Fisiològiques')}", expanded=True):
        tabs = st.tabs(["[A] Límits Tèrmics", "[B] Sequera (Xeròfiles)", "[C] Fred, Llum i Foc"])
        with tabs[0]:
            st.subheader("Límits de Supervivència")
            st.code(">>> RANG VITAL: 0°C a 45°C")
            st.markdown(f"- $0^{\\circ}C$: Es {highlight('paralitza')} l'absorció d'aigua.")
            st.markdown(f"- **Classificació:** {highlight('Euritermes')} (rang ample) vs. {highlight('Estenotermes')} (rang estret).")
        with tabs[1]:
            st.subheader(f"Mecanismes {highlight('Xeròfils')}")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### Reducció de Transpiració:")
                st.markdown(f"- {highlight('Fulles petites')} o espines.")
                st.markdown(f"- Presència de {highlight('pèls i ceres')}.")
            with col2:
                st.markdown("#### Reserva/Captació:")
                st.markdown(f"- Acumulació d'aigua ({highlight('suculentes')}).")
                st.markdown(f"- {highlight('Arrels profundes')}.")
        with tabs[2]:
            st.subheader("Fred, Llum i Foc")
            st.markdown(f"**Fred:** {highlight('Saba més espessa')} per alentir la congelació.")
            st.markdown(f"**Llum:** Augment de la {highlight('concentració de clorofil·la')}.")
            st.markdown(f"**Foc (Piròfites):** Capacitat de {highlight('rebrotar ràpidament')} i mecanisme de {highlight('Serotinia')}.")

    with st.expander(f"Mòdul [2]: {highlight('Biodiversitat i Endemisme')}", expanded=True):
        st.header(f"🧬 Endemisme: Factors d'Aïllament")
        st.markdown(f"Un endemisme és una espècie amb una {highlight('àrea de distribució molt limitada')}.")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Causes d'Aïllament:")
            st.markdown(f"""
            1.  {highlight('Aïllament Geogràfic (Més comú)')}: Illes, muntanyes.
            2.  {highlight('Aïllament Genètic')}.
            3.  {highlight('Canvi Brusc del Medi')}: Glaciacions, aridesa.
            """, unsafe_allow_html=True)
        with col2:
            st.subheader("Exemples i Contrastos:")
            st.markdown(f"- **Endemisme Montà:** {highlight('Desman dels Pirineus')}.")
            st.markdown(f"- **Contrast (Cosmopolita):** Espècie distribuïda per tot el món.")

elif pagina == "❓ Posa't a Prova! (Quiz)":
    run_quiz()
