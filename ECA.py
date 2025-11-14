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
            "VERSION": "9.1.SYNTAX_FIX", # Nova Versió amb correcció de sintaxi
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
        /* 1. Definició del Color Primari (Neó Cyan) */
        :root {
            --primary-color: #00FFFF; /* Vibrant Cyan */
            --primary-color-800: #00CCCC;
            --background-dark: #0A0A0A; /* Fons molt fosc */
            --background-medium: #1A1A1A; /* Fons de contenidors */
            --text-color: #E0E0E0;
            --highlight-color: #00FF7F; /* Green Terminal Text for important items */
            --warning-color: #FFD700; /* Gold for warnings */
        }

        /* 2. Configuració de la Pàgina i el Cos */
        .stApp {
            background-color: var(--background-dark);
            color: var(--text-color);
            font-family: 'Consolas', 'Courier New', monospace; /* Fuente más técnica */
        }
        
        /* 3. Títols amb efecte "Glow" */
        h1 {
            color: var(--primary-color); 
            text-shadow: 0 0 7px rgba(0, 255, 255, 0.7); 
            font-family: 'Consolas', 'Courier New', monospace; 
            border-bottom: 3px solid var(--primary-color-800);
            padding-bottom: 10px;
            margin-top: 0px;
            animation: glow 1.5s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 0 0 5px rgba(0, 255, 255, 0.5); }
            to { text-shadow: 0 0 10px rgba(0, 255, 255, 1), 0 0 15px rgba(0, 255, 255, 0.8); }
        }
        
        /* 4. Subtítols (Headers de Secció amb barra de càrrega) */
        h2, h3 {
            color: var(--text-color); 
            border-left: 6px solid var(--primary-color); 
            padding-left: 15px;
            margin-top: 30px;
            background-color: var(--background-medium);
            padding: 10px 15px 10px 15px;
            font-family: 'Consolas', monospace;
            box-shadow: 0 0 5px rgba(0, 255, 255, 0.2);
            border-radius: 5px;
        }

        /* 5. Contenidors (Panells d'Informació - Més estètica) */
        .st-emotion-cache-1c7v0s, .st-emotion-cache-1ftrz5p, .st-emotion-cache-qn80jo, .st-emotion-cache-f1g04y { /* Afegits selectors per expanders i altres contenidors */
             background-color: var(--background-medium);
             padding: 15px;
             border-radius: 8px;
             border: 1px solid var(--primary-color-800);
             box-shadow: 0 0 5px rgba(0, 255, 255, 0.2);
             margin-bottom: 15px; /* Espai entre contenidors */
        }
        
        /* 6. Barra Lateral (Sidebar) */
        .st-emotion-cache-vk3ypz { /* Contenidor principal de la sidebar */
            background-color: #050505; 
            border-right: 2px solid var(--primary-color);
            box-shadow: 2px 0 10px rgba(0, 255, 255, 0.3);
        }
        .st-emotion-cache-vk3ypz .st-emotion-cache-1pxeayr { /* Títols i elements dins de la sidebar */
            color: var(--primary-color) !important;
            font-family: 'Consolas', monospace;
        }
        
        /* 7. Altres elements UI (Code blocks, info, success, error) */
        .stCode {
            background-color: #000000;
            border: 1px solid var(--primary-color-800);
            color: var(--highlight-color); /* Green Terminal Text */
            font-size: 0.9em;
            padding: 10px;
            border-radius: 5px;
        }

        .stAlert {
            border-left: 5px solid;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 10px;
        }
        .stAlert.st-emotion-cache-1a6x41r.st-emotion-cache-1r4qj8m { /* Info */
            background-color: rgba(0, 191, 255, 0.1);
            border-color: #00BFFF;
            color: #00BFFF;
        }
        .stAlert.st-emotion-cache-1a6x41r.st-emotion-cache-mk01mr { /* Success */
            background-color: rgba(0, 255, 127, 0.1);
            border-color: #00FF7F;
            color: #00FF7F;
        }
        .stAlert.st-emotion-cache-1a6x41r.st-emotion-cache-h5gxh1 { /* Warning */
            background-color: rgba(255, 215, 0, 0.1);
            border-color: var(--warning-color);
            color: var(--warning-color);
        }
        .stAlert.st-emotion-cache-1a6x41r.st-emotion-cache-1e5xgrb { /* Error */
            background-color: rgba(255, 69, 0, 0.1);
            border-color: #FF4500;
            color: #FF4500;
        }

        /* Estil per al botó de ràdio seleccionat */
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
        
        /* Subratllat per destacar text */
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
            background-color: var(--primary-color-800);
            color: var(--background-dark);
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
            transition: all 0.2s ease-in-out;
            box-shadow: 0 0 5px rgba(0, 255, 255, 0.5);
        }
        .stButton button:hover {
            background-color: var(--primary-color);
            color: var(--background-dark);
            box-shadow: 0 0 10px rgba(0, 255, 255, 0.8);
            transform: translateY(-2px);
        }

        /* Expander styling */
        .streamlit-expanderHeader {
            background-color: var(--primary-color-800);
            color: var(--background-dark);
            border-radius: 5px;
            padding: 10px;
            font-weight: bold;
            box-shadow: 0 0 5px rgba(0, 255, 255, 0.3);
        }
        .streamlit-expanderContent {
            background-color: var(--background-medium);
            border-left: 3px solid var(--primary-color-800);
            padding: 10px;
            border-bottom-left-radius: 5px;
            border-bottom-right-radius: 5px;
        }
        
        </style>
        """,
        unsafe_allow_html=True
    )

# Funció per subratllar text
def highlight(text, color="highlight"):
    return f'<span class="{color}">{text}</span>'

# Funció per subratllar text amb color d'advertència
def warning_highlight(text, color="warning-highlight"):
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
    # Aquesta línia només s'executarà un cop si la sessió no està iniciada
    if st.session_state.system_status == "INITIALIZING":
        run_boot_sequence()


# --- FUNCIÓ PRINCIPAL DEL QUIZ ---
def run_quiz():
    st.header(f"❓ Posa't a Prova! ({highlight('Terminal de Test - NF 1.1, 1.2, 1.3')})")
    st.markdown("---")
    st.info("🟢 **EXECUTANT TEST DE VALIDACIÓ DE CONEIXEMENTS...** Aquesta prova cobreix totes les unitats formatives.")
    
    # 12 Preguntes extretes directament dels PDFs
    preguntes = {
        "Q1: Climograma (Sequera)": {
            "pregunta": f"En un climograma, la condició de {highlight('Sequera/Aridesa')} es dóna quan (Regla de Gaussen):",
            "opcions": ["La P supera $2 \\times T$", "La Tº supera la P ($T > P$)", "$T \\times 2 > P$"],
            "correcta": "La Tº supera la P ($T > P$)" # _NF1.1. Climogrames.pptx.pdf (p. 6)
        },
        "Q2: Bosc Mediterrani (Flora)": {
            "pregunta": f"Quin estrat vegetal, a més de l'arbre dominant (Alzina), pren gran rellevància en el {highlight('Bosc Mediterrani Escleròfil')}?",
            "opcions": ["L'estrat arbori secundari", "Només l'estrat herbaci", "Els estrats arbustiu, herbaci i lianoide"],
            "correcta": "Els estrats arbustiu, herbaci i lianoide" # NF1.1.BiomesdelaTerra_A1A2.pdf (p. 31)
        },
        "Q3: Adaptació (Límits Tèrmics)": {
            "pregunta": f"Per sota de quina Tº la planta {highlight('paralitza l\'activitat')} d'absorció i processament d'aigua?",
            "opcions": ["$10^{\\circ}C$", "$0^{\\circ}C$", "$-5^{\\circ}C$", "$45^{\\circ}C$"],
            "correcta": "$0^{\\circ}C$" # ADAPTACIONS_FLORA.pdf (p. 3)
        },
        "Q4: Biodiversitat (Endemisme)": {
            "pregunta": f"Quina de les següents espècies és un exemple d'{highlight('endemisme montàno')} als Pirineus?",
            "opcions": ["Linx Ibèric", "Desman dels Pirineus (*Galemys pyrenaicus*)", "Faig (*Fagus sylvatica*)"],
            "correcta": "Desman dels Pirineus (*Galemys pyrenaicus*)" # NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf (p. 13)
        },
        "Q5: Classificació (NF 1.3)": {
            "pregunta": f"Quin sistema de classificació {highlight('jeràrquica')} s'utilitza a la UE per catalogar tots els hàbitats (naturals, seminaturals i artificialitzats)?",
            "opcions": ["Ramsar", "CORINE Biotopes", "ZEPA", "Whittaker"],
            "correcta": "CORINE Biotopes" # NF1.1. Habitats. Classificació Corinne.pptx.pdf (p. 4)
        },
        "Q6: Regió Biogeogràfica": {
            "pregunta": f"La Regió Eurosiberiana es caracteritza per la dominància de:",
            "opcions": ["Boscos Perennifolis Escleròfils", f"{highlight('Boscos Caducifolis')} (Roures, Faigs)", "Vegetació estenoterma"],
            "correcta": "Boscos Caducifolis (Roures, Faigs)" # NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 9)
        },
        "Q7: Hàbitats Catalunya (Fageda)": {
            "pregunta": f"La Fageda es troba típicament en climes Medioeuropeus subatlàntics i sobre quin tipus de sòl/substrat?",
            "opcions": ["Terrenys calcaris", f"{highlight('Terrenys àcids')} (o sòls acidificats)", "Terrenys salins"],
            "correcta": "Terrenys àcids (o sòls acidificats)" # NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 54)
        },
        "Q8: Adaptació (Foc - Serotinia)": {
            "pregunta": f"Quin arbre utilitza el mecanisme de {highlight('Serotinia')} (obertura de pinyes amb la calor) com a adaptació al foc?",
            "opcions": ["Faig (*Fagus sylvatica*)", "Alzina (*Quercus ilex*)", "Pi blanc (*Pinus halepensis*)"],
            "correcta": "Pi blanc (*Pinus halepensis*)" # ADAPTACIONS_FLORA.pdf (p. 6)
        },
        "Q9: Biodiversitat (Aïllament)": {
            "pregunta": f"Quin factor pot causar la formació d'endemismes a part de l'aïllament geogràfic?",
            "opcions": ["Un augment de la pluja anual", f"{highlight('Un canvi brusc de les condicions del medi')} (aridesa, glaciacions)", "Una disminució de la Tº a l'estiu"],
            "correcta": "Un canvi brusc de les condicions del medi (aridesa, glaciacions)" # NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf (p. 11)
        },
        "Q10: Xarxa Natura 2000": {
            "pregunta": f"La Xarxa Natura 2000 està formada per les ZEC (Zones Especials de Conservació) i per quins altres espais de protecció?",
            "opcions": ["ZAD (Zones d'Alt Valor)", f"{highlight('ZEPA')} (Zones d'Especial Protecció per a les Aus)", "ZER (Zones d'Exclusió Ràpida)"],
            "correcta": "ZEPA (Zones d'Especial Protecció per a les Aus)" # NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 16)
        },
        "Q11: Bosc de Pi Negre (Catalunya)": {
            "pregunta": f"El Bosc de Pi Negre és típic de quin ambient a Catalunya?",
            "opcions": ["Litoral (dunes)", f"{highlight('Alta Muntanya')} (Alpí / Subalpí)", "Zona Prelitoral"],
            "correcta": "Alta Muntanya (Alpí / Subalpí)" # NF1.2.HabitatsCatalunya.pptx (1).pdf (p. 3)
        },
        "Q12: Classificació Tèrmica": {
            "pregunta": f"Les plantes que només poden viure en un rang de temperatures molt concret s'anomenen:",
            "opcions": ["Euritermes", "Xeròfiles", f"{highlight('Estenotermes')}"],
            "correcta": "Estenotermes" # ADAPTACIONS_FLORA.pdf (p. 3)
        }
    }

    respostes_usuari = {}

    with st.form(key="quiz_form_ampliat"):
        for i, (key, value) in enumerate(preguntes.items()):
            st.markdown(f"#### {key.split(':')[0].strip()}")
            st.markdown(value["pregunta"], unsafe_allow_html=True)
            respostes_usuari[key] = st.radio(
                "Selecciona la teva resposta:",
                options=value["opcions"],
                key=f"q_amp{i}",
                label_visibility="collapsed"
            )
            st.markdown("---")
            
        submitted = st.form_submit_button("⏩ INICIAR ESCANEIG DE RESULTATS (ENVIAR) 🚀")

    if submitted:
        score = 0
        total_preguntes = len(preguntes)
        
        st.header("✅ INFORME DE VALIDACIÓ FINAL:")
        
        # Mòdul d'avaluació amb detall
        for key, value in preguntes.items():
            resposta_correcta = value["correcta"]
            resposta_usuari = respostes_usuari[key]
            
            status_col, res_col = st.columns([1, 4])
            
            if resposta_usuari == resposta_correcta:
                score += 1
                with status_col:
                    st.success("STATUS: OK")
                with res_col:
                    st.markdown(f"**{key}**: Resposta: `{highlight(resposta_usuari)}`", unsafe_allow_html=True)
            else:
                with status_col:
                    st.error("STATUS: ERROR")
                with res_col:
                    st.markdown(f"**{key}**: La teva resposta: `{warning_highlight(resposta_usuari)}`. **Correcta**: `{highlight(resposta_correcta)}`", unsafe_allow_html=True)

        st.markdown("---")
        st.subheader(f"Puntuació Final del Sistema: **{score}/{total_preguntes}**")
        
        percentatge = (score / total_preguntes)
        st.progress(percentatge)

        if percentatge == 1.0:
            st.balloons()
            st.success("🎉 **VALIDACIÓ COMPLETA! Codi 100% Acceptat!** 🎉")
        elif percentatge >= 0.7:
            st.warning("VALIDACIÓ PARCIALMENT OK. Repassa els punts febles.")
        else:
            st.error("ERROR CRÍTIC. Repassa la UF1 abans de tornar a executar el test.")
            
# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("🧬 Mòdul Bio-Explorador 9.1")
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
    st.markdown(
        """
        Aquesta aplicació cobreix els coneixements mínims requerits per la Unitat Formativa 1: "Caracterització d'hàbitats".
        """
    )

    col_nf1, col_nf2 = st.columns(2)
    
    with col_nf1:
        st.subheader(f">> {highlight('NF 1.1 (Biomes, Climogrames, Biodiversitat)')}")
        st.markdown(
            f"""
            * **A1, A2 (Biomes):** El {highlight('Bioma')} és un conjunt de comunitats amb vegetació climàtica uniforme i clima característic (NF1.1.BiomesdelaTerra_A1A2.pdf, p. 3).
            * **A3 (Climogrames):** Anàlisi de la relació Tº/P. La {highlight('Sequera')} es dóna quan $P < 2 \\times T$ o $T > P$.
            * **Biodiversitat:** {highlight('Varietat d\'éssers vius')} resultat de l'evolució i l'acció humana (NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf, p. 3).
            """
        , unsafe_allow_html=True)
        
        st.subheader(f">> {highlight('NF 1.2/1.3 (Hàbitats, Biotops, Protecció)')}")
        st.markdown(
            f"""
            * **Definició Clau:** {highlight('Biotop')} (territori amb condicions ambientals) vs. {highlight('Hàbitat')} (conjunt de biòtops, espai físic amb aliment, refugi i aigua) (NF1.2.HabitatsaEspanya.pptx (2).pdf, p. 4-5).
            * **CORINE Biotopes (NF 1.3):** Classificació {highlight('jeràrquica')} europea per a hàbitats naturals, seminaturals i artificialitzats (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 4).
            """
        , unsafe_allow_html=True)
    
    with col_nf2:
        st.subheader(f">> {highlight('NF 1.2 (Hàbitats Peninsulars i Catalunya)')}")
        st.markdown(
            f"""
            * **Regions Biogeogràfiques:** {highlight('Eurosiberiana')} (Caducifolis), {highlight('Mediterrània')} (Escleròfils), {highlight('Macaronèsica')} (Endemisme), {highlight('Alpina')} (Fred intens).
            * **Fageda (Catalunya):** Clima Medioeuropeu subatlàntic, sobre {highlight('terrenys àcids')} (NF1.2.HabitatsaEspanya.pptx (2).pdf, p. 54).
            * **Alzinar:** Bosc {highlight('perennifoli escleròfil')} adaptat a la sequera estival (NF1.1.BiomesdelaTerra_A1A2.pdf, p. 31).
            * **Xarxa Natura 2000 (NF 1.3):** Xarxa d'àrees de conservació amb {highlight('ZEC')} (Hàbitats/Espècies) i {highlight('ZEPA')} (Aus).
            """
        , unsafe_allow_html=True)
        st.info(f"EXECUCIÓ OK. Concentració de dades a l'àrea d'informació. Versió {st.session_state.config.get('VERSION', 'N/A')}")

elif pagina == "🌍 Biomes de la Terra (NF 1.1)":
    st.title(f"🌍 Cartografia Global: {highlight('Biomes de la Terra (NF 1.1: A1, A2)')}")
    st.markdown("Unitats de gran extensió amb una vegetació climàtica uniforme i clima característic (NF1.1.BiomesdelaTerra_A1A2.pdf, p. 3).")

    st.subheader(f"Definicions de Biomes Clau ({highlight('Més Enllà del Mediterrani')})")
    st.info("Aquesta secció inclou referències als biomes de Pastures i Sabana, esmentats en la classificació global (NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf, p. 2).")

    bio_col1, bio_col2 = st.columns(2)
    
    with bio_col1:
        st.markdown("#### **Pastures (Grasslands)**")
        st.markdown(f"* **Clima:** Zones temperades amb estius càlids i hiverns freds. Pluges moderades que no permeten el desenvolupament d'arbres alts.")
        st.markdown(f"* **Vegetació:** Domini de {highlight('gramínies')} i herbes. Exemples: Praderies Nord-americanes, Estepes d'Euràsia.")
    
    with bio_col2:
        st.markdown("#### **Sabana (Tropical Grasslands)**")
        st.markdown(f"* **Clima:** Tropical amb una estació {highlight('seca molt marcada')} i una estació humida. Clima amb temperatura constantment alta.")
        st.markdown(f"* **Vegetació:** Gramínies altes amb arbres aïllats o petits grups d'arbres (ex: acàcies). Adaptada als incendis i a la pastura d'herbívors.")

    with st.expander(f"Fitxa Tècnica: {highlight('Bosc Escleròfil Mediterrani')} (Densitat Màxima)", expanded=True):
        
        tab_flora, tab_fauna, tab_estrategia = st.tabs(["[1] Detall Flora i Estructura", "[2] Detall Fauna", "[3] Clima i Sòl Crític"])
        
        with tab_flora:
            st.subheader(f"Estratègia {highlight('Escleròfil·la')} i Estructura Vegetal (NF1.1, p. 31)")
            st.markdown(f"* La vegetació és principalment {highlight('escleròfil·la')} (fulla dura) i {highlight('perenne')} per a resistir la sequera estival.")
            st.markdown(f"* **Arbres Perennes Clau:** Alzines (*Quercus ilex*), Sureres, Garrofers, Oliveres, Arboç.")
            st.markdown(f"* **Estrats Inferiors:** Els estrats {highlight('Arbustiu')}, {highlight('Herbaci')} i {highlight('Lianoide')} prenen gran rellevància (gran abundància d'espècies).")
            
        with tab_fauna:
            st.subheader(f"Fauna Clau per Nínxol Ecològic (NF1.1, p. 32)")
            
            st.markdown(
                f"""
                * **Herbívors Clau:** Cabirols, Esquirols, Llebres, Cabres salvatges.
                * **Carnívors Representatius:** Guineus, geneta, {highlight('Linx Ibèric')} (el carnívor més representatiu i amenaçat).
                * **Omnívors Destacats:** Porc senglar, rata de camp, Teixó.
                """
            , unsafe_allow_html=True)

        with tab_estrategia:
            st.subheader(f"Clima i Sòl ({highlight('Determinants del Bioma')})")
            st.markdown(
                f"""
                * **Clima:** Mediterrani (estius secs i calorosos, hiverns suaus).
                * **Factor Determinant:** La {highlight('sequera estival')} (període d'aridesa) i les altes temperatures.
                * **Sòl:** Tendeix a ser {highlight('pobre en matèria orgànica')} i amb capacitat per absorbir ràpidament l'aigua.
                """
            , unsafe_allow_html=True)

elif pagina == "🌲 Classificació dels Biomes Principals":
    st.title(f"🌲 Classificació dels {highlight('Biomes Principals (NF 1.1: A2)')}")
    st.markdown("Anàlisi comparativa dels biomes de latituds extremes i humits.")

    with st.expander(f"Fitxa Tècnica: {highlight('Biomes de Latituds Altes i Grans Humitats')}", expanded=True):
        
        bio_col1, bio_col2 = st.columns(2)
        
        with bio_col1:
            st.subheader("1. Tundra (Bioma Frèd Extrem)")
            st.markdown(
                f"""
                * **Clima:** Tº mitjanes baixíssimes (gran part de l'any sota $0^{\\circ}C$). Poca precipitació (neu).
                * **Vegetació:** Prats i landes. Predomini de molses, líquens i arbusts nans. {highlight('Sense arbres')}.
                * **Sòl Clau:** {highlight('Permafrost')} (sòl permanentment congelat).
                """
            , unsafe_allow_html=True)
            st.subheader("3. Bosc de Coníferes o Taiga (Bioma Boreal)")
            st.markdown(
                f"""
                * **Clima:** Fred extrem amb estius curts i suaus. Precipitació moderada.
                * **Vegetació:** Boscos d'arbres de {highlight('fulla perenne acicular')} (en forma d'agulla) i resistents al fred (Pins, Avets).
                * **Adaptació:** Forma {highlight('cònica')} per evitar l'acumulació d'acumulació de neu.
                """
            , unsafe_allow_html=True)
            
        with bio_col2:
            st.subheader("2. Desert (Bioma Amb Dèficit Hídric Extrem)")
            st.markdown(
                f"""
                * **Clima:** Molt poca precipitació (sovint {highlight('$< 250$ mm/any')}). Gran oscil·lació tèrmica diària.
                * **Vegetació:** Escassa i molt adaptada ({highlight('xeròfites')}, suculentes com els cactus). Fulles transformades en espines.
                * **Sòl Clau:** Pobre, amb poques substàncies orgàniques.
                """
            , unsafe_allow_html=True)
            st.subheader("4. Selva Tropical (Bioma Humit Càlid)")
            st.markdown(
                f"""
                * **Clima:** Tº mitjanes altes i constants. Precipitació molt alta i constant. {highlight('Sense estació seca')}.
                * **Vegetació:** Boscos densos, amb molts estrats i gran diversitat d'espècies ({highlight('alta biodiversitat')}).
                * **Sòl Clau:** Freqüentment {highlight('pobre')} per l'alt rentat de nutrients ({highlight('lixiviació')}).
                """
            , unsafe_allow_html=True)


elif pagina == "📊 Climogrames i Distribució":
    st.title(f"📊 Anàlisi Gràfica Climàtica ({highlight('NF 1.1: A3')})")
    st.markdown("Eina essencial per caracteritzar un bioma mitjançant la combinació de Tº i P (NF1.1. Climogrames.pptx.pdf, p. 2).")

    with st.expander(f"Detall Tècnic: {highlight('Interpretació Visual i Regles Crítiques')} (Ampliat)", expanded=True):
        st.header("Mòdul: Interpretació Visual i Regla de Gaussen")
        
        # Inserció de la imatge demanada pel client
        st.image("https://www.meteorologiaenred.com/wp-content/uploads/2018/06/Climograma.jpg", caption="Exemple de Climograma de Walter i Lieth")
        
        st.subheader(f"1. ⚙️ Guia de Lectura i Escales ({highlight('Regla de Gaussen')})")
        
        col_lectura, col_regla = st.columns(2)
        
        with col_lectura:
            st.markdown(
                f"""
                * {highlight('Línia Vermella (Tº)')}: Representa la {highlight('Temperatura mitjana mensual')} (Eix vertical esquerre).
                * {highlight('Barres Blaves (P)')}: Representen la {highlight('Precipitació mitjana mensual')} (Eix vertical dret).
                * **Relació Clau:** L'escala utilitza la relació {highlight('$10^{\\circ}C$ s\'alinea amb $20$ mm')}. Aquesta escala doble (P:T, 2:1) és la que permet llegir ràpidament la sequera.
                """
            , unsafe_allow_html=True)
        with col_regla:
            st.markdown("#### **Interpretació de la Vida Vegetal:**")
            st.markdown(
                f"""
                * {highlight('HUMITAT')}: La línia **Blava (P)** es troba {highlight('per sobre')} de la línia **Vermella (T)**. L'aigua no és limitant.
                * {highlight('SEQUERA (ARIDESA)')}: La línia **Vermella (T)** es troba {highlight('per sobre')} de la línia **Blava (P)**. L'aigua és el factor limitant.
                * {highlight('GELADA/FRED')}: La línia **Vermella (T)** cau {highlight('per sota dels $0^{\circ}C$')}. Paralització de l'activitat de la planta.
                """
            , unsafe_allow_html=True)

        st.markdown("---")
        st.subheader(f"2. 🌍 Escenaris Climàtics Clàssics ({highlight('Tipus de Clima')})")
        
        tab_med, tab_oce, tab_pol = st.tabs(["[A] Mediterrani (Escleròfil)", "[B] Oceànic (Caducifoli)", "[C] Polar / Alta Muntanya"])
        
        with tab_med:
            st.markdown(f"#### **Escenari {highlight('Mediterrani Típic')} (Bioma Escleròfil)**")
            st.code(">>> ZONA DE VEGETACIÓ: Alzinar, Pinar (Xeròfil·la)")
            st.markdown(
                f"""
                * **Factor Clau:** Forta i clara {highlight('sequera estival')}.
                * **Visualització:** La línia vermella (T) puja bruscament i {highlight('supera')} clarament la línia blava (P) durant els mesos d'estiu (J, L, A).
                * **Hivern:** Temperat, amb temperatures mitjanes superiors als $5^{\\circ}C$ ({highlight('sense gelades significatives')}).
                """
            , unsafe_allow_html=True)
        
        with tab_oce:
            st.markdown(f"#### **Escenari {highlight('Temperat Oceànic')} (Regió Eurosiberiana)**")
            st.code(">>> ZONA DE VEGETACIÓ: Bosc Caducifoli (Faig, Roure)")
            st.markdown(
                f"""
                * **Factor Clau:** {highlight('Absència total de sequera estival.')}
                * **Visualització:** La línia blava (P) es manté {highlight('sempre')} per sobre de la línia vermella (T).
                * **Hivern:** Fred, però amb precipitació abundant i ben distribuïda.
                """
            , unsafe_allow_html=True)

        with tab_pol:
            st.markdown(f"#### **Escenari {highlight('Polar / Alta Muntanya')} (Clima Alpí)**")
            st.code(">>> ZONA DE VEGETACIÓ: Tundra, Prats Alpins")
            st.markdown(
                f"""
                * **Factor Clau:** {highlight('Fred extrem')} i limitant.
                * **Visualització:** La línia vermella (T) es troba {highlight('per sota o molt a prop dels $0^{\circ}C$')} durant diversos mesos.
                * **Implicació:** La baixa Tº {highlight('paralitza')} l'activitat de la planta (aigua no disponible) i impedeix el desenvolupament arbori.
                """
            , unsafe_allow_html=True)
    
    st.markdown("---")


elif pagina == "🇪🇸 Hàbitats Peninsulars i Protecció (NF 1.2/1.3)":
    st.title(f"🇪🇸 Regions Biogeogràfiques i Classificació ({highlight('NF 1.2 & NF 1.3')})")
    st.markdown("La península es divideix en 4 regions principals (NF1.2.HabitatsaEspanya.pptx).")

    st.subheader(f"Mòdul {highlight('NF 1.2: Anàlisi Densa de Regions Biogeogràfiques (A2)')}")
    
    reg_tab1, reg_tab2, reg_tab3, reg_tab4 = st.tabs(["[1] Eurosiberiana", "[2] Mediterrània", "[3] Macaronèsica", "[4] Alpina"])

    with reg_tab1:
        st.markdown(f"* **Clima:** Temperat, humit, {highlight('sense aridesa estival')} (clima Oceànic).")
        st.markdown(f"* **Vegetació Clau:** Dominància de {highlight('Boscos Caducifolis')} (Roures, Faigs).")

    with reg_tab2:
        st.markdown(f"* **Clima:** Estius secs i calorosos. {highlight('Sequera estival present')}.")
        st.markdown(f"* **Vegetació Clau:** {highlight('Boscos Perennifolis Escleròfils')} (Alzinar, Surera, Pi).")
    
    with reg_tab3:
        st.markdown(f"* **Particularitat:** Aïllament insular, que genera un {highlight('altíssim nivell d\'endemisme')}.")
        st.markdown(f"* **Flora Única:** Laurissilva, Pi canari.")

    with reg_tab4:
        st.markdown(f"* **Condicions:** {highlight('Fred intens')}, vent, baixa Tº (per sobre de la zona subalpina).")
        st.markdown(f"* **Vegetació Clau:** Bosc Subalpí (Pi Negre) i Prats Alpins.")

    st.markdown("---")
    st.subheader(f"Mòdul {highlight('NF 1.3: Classificació i Protecció (Detall Extens)')}")
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.header(f"Classificació ({highlight('CORINE Biotopes')})")
        st.code(">>> NF1.1. Habitats. Classificació Corinne.pptx.pdf (p. 4)")
        st.markdown(
            f"""
            * **Base Legal:** Sistema {highlight('jeràrquic')} estandarditzat per la Unió Europea.
            * **Abast:** Classifica la totalitat dels hàbitats de la UE: {highlight('naturals')}, {highlight('seminaturals')} i {highlight('artificialitzats')}.
            * **Objectiu:** Ordenar, cartografiar i comparar la diversitat d'hàbitats.
            """
        , unsafe_allow_html=True)

    with col_p2:
        st.header(f"Xarxa {highlight('Natura 2000')} (ZEC i ZEPA)")
        st.code(">>> NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 16)")
        st.markdown(
            f"""
            Xarxa d'àrees de conservació (Directiva Hàbitats / Directiva Ocells).
            * {highlight('ZEC (Zones Especials de Conservació)')}: Protegeix {highlight('hàbitats i espècies d\'interès comunitari')}.
            * {highlight('ZEPA (Zones d\'Especial Protecció per a les Aus)')}: Espais designats per a la protecció dels ocells.
            """
        , unsafe_allow_html=True)


elif pagina == "🏞️ Hàbitats de Catalunya (Detall Exhaustiu)":
    st.title(f"🏞️ Fitxer d'Hàbitats Nacionals ({highlight('NF 1.2: A3')})")
    st.markdown("La gran varietat geogràfica de Catalunya resulta en una elevada diversitat d'hàbitats.")
    
    hab_tab1, hab_tab2, hab_tab3 = st.tabs(["[1] Boscos de Fulla Caduca i Perenne", "[2] Boscos de Pi i Formacions Arbustives", "[3] Formacions Herbàcies (Detall)"])

    with hab_tab1:
        st.header(f"🌳 La {highlight('Fageda (*Fagus sylvatica*)')} - Bosc Tancat")
        fag_col1, fag_col2 = st.columns(2)
        
        with fag_col1:
            st.subheader(f"Ecologia del Faig ({highlight('Medioeuropeu Subatlàntic')})")
            st.markdown(
                f"""
                * **Clima:** {highlight('Medioeuropeu subatlàntic')} (molta humitat).
                * **Substrat:** Terrenys {highlight('àcids')} o sòls acidificats (NF1.2.HabitatsaEspanya.pptx (2).pdf, p. 54).
                * **Ubicació:** Muntanya mitjana, típicament en vessants obacs i inclinats.
                """
            , unsafe_allow_html=True)
        with fag_col2:
            st.subheader(f"Sotabosc Pobre ({highlight('Plantes Acidòfiles')}) - NF1.2, p. 56")
            st.markdown(
                f"""
                El sotabosc és pobre per manca de llum. Està compost per:
                * **Arbustiu Clau:** Boix (*Buxus sempervirens*), Grèvol (*Ilex aquifolium*).
                * **Herbaci Específic:** Bruguerola (*Calluna vulgaris*), Falguera comuna (*Pteridium aquilinum*), Te de muntanya (*Veronica officinalis*).
                """
            , unsafe_allow_html=True)

        st.header(f"🌲 L'{highlight('Alzinar (*Quercus ilex*)')} - Bosc Escleròfil")
        al_col1, al_col2 = st.columns(2)
        
        with al_col1:
            st.subheader(f"Tipus Escleròfil·le i Rols")
            st.markdown(
                f"""
                * **Tipus:** Bosc perennifoli {highlight('escleròfil mediterrani')}.
                * **Funció de la Fulla:** La duresa redueix la {highlight('transpiració')}, essencial per a sobreviure a la sequera estival.
                * **Observació:** És el {highlight('clímax')} potencial del clima mediterrani.
                """
            , unsafe_allow_html=True)

        with al_col2:
            st.subheader(f"Flora de Sotabosc Mediterrani")
            st.markdown(
                f"""
                * **Arbusts Específics:** Marfull, Arboç, Llentiscle.
                * **Lianes Comunes:** Arítjol.
                """
            , unsafe_allow_html=True)

    with hab_tab2:
        st.header(f"🌳 Boscos de Pi ({highlight('Diversitat Ecològica')})")
        st.markdown("Varien segons l'altitud i la resistència:")
        
        pi_col1, pi_col2 = st.columns(2)
        
        with pi_col1:
            st.markdown("#### **Alta Muntanya/Interior:**")
            st.markdown(f"* {highlight('Pi Negre (*Pinus uncinata*)')}: Alta Muntanya (Estrat Subalpí/Alpí). Resistent al fred extrem i als vents (NF1.2.HabitatsCatalunya.pptx (1).pdf, p. 3).")
            st.markdown(f"* {highlight('Pi Roig (*Pinus sylvestris*)')}: Muntanya mitjana/interior. S'adapta a sòls més pobres.")

        with pi_col2:
            st.markdown("#### **Litoral i Baixa Muntanya (Piròfites):**")
            st.markdown(f"* {highlight('Pi Blanc (*Pinus halepensis*)')}: Litoral/prelitoral. Fortament {highlight('piròfita')} (mecanisme de {highlight('Serotinia')}) (ADAPTACIONS_FLORA.pdf, p. 6).")
            st.markdown(f"* **Arbustives:** {highlight('Màquia')} (densa, degradació de l'alzinar) i {highlight('Brolla')} (oberta, brucs, romaní).")
            
    with hab_tab3:
        st.header(f"🌱 Formacions Herbàcies ({highlight('Classificació Tècnica')})")
        st.markdown("NF1.2.HabitatsCatalunya.pptx (1).pdf, p. 54-55")
        
        herb_col1, herb_col2 = st.columns(2)
        with herb_col1:
             st.subheader(f"Definicions d'Estructura")
             st.markdown(f"- {highlight('Prat')}: Comunitat dominada per gramínies. Aspecte {highlight('compacte i homogeni')}.")
             st.markdown(f"- {highlight('Pradell')}: Prat de {highlight('reduïda extensió')} o recobriment escàs.")
             st.markdown(f"- {highlight('Gramenet/Gespa')}: Prats en què predominen les gramínies o plantes graminoides; la gespa és molt atapeïda.")
        with herb_col2:
             st.subheader(f"Tipus de Prats Clau")
             st.markdown(f"- {highlight('Prats Alpins')}: Típics de la zona pirinenca, sobre el límit del bosc (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 10).")
             st.markdown(f"- {highlight('Prats Halòfils')}: Associats a zones litorals o salines.")
             st.markdown(f"- {highlight('Aiguamolls')}: Zones d'alta biodiversitat que combinen aigua dolça/salada i vegetació herbàcia/arbustiva.")


elif pagina == "🌱 Adaptacions i Biodiversitat (NF 1.1)":
    st.title(f"🌱 Adaptacions i Biodiversitat ({highlight('NF 1.1')})")
    st.markdown("Respostes dels éssers vius als factors ambientals extrems.")

    with st.expander(f"Mòdul [1]: {highlight('Adaptacions Tèrmiques, Hídriques i Lumíniques')} (Detall Exhaustiu)", expanded=True):
        
        adapt_tab1, adapt_tab2, adapt_tab3 = st.tabs(["[A] Límits Tèrmics Crítics", "[B] Sequera/Xeròfiles", "[C] Fred, Llum i Foc"])

        with adapt_tab1:
            st.subheader(f"Límits de Supervivència (NF1.1, p. 3)")
            st.code(">>> RANG VITAL: 0°C a 45°C")
            st.markdown(
                f"""
                * {highlight('$0^{\\circ}C$')}: La planta {highlight('paralitza')} l'activitat d'absorció d'aigua.
                * {highlight('$45^{\\circ}C$')}: L'activitat vegetativa es paralitza.
                * **Classificació Tèrmica:** {highlight('Euritermes')} (ample rang de Tº) vs. {highlight('Estenotermes')} (Tº més concretes).
                """
            , unsafe_allow_html=True)
        
        with adapt_tab2:
            st.subheader(f"Mecanismes {highlight('Xeròfils')} (Evitar Pèrdua d'Aigua) - NF1.1, p. 5")
            
            xerofila_col1, xerofila_col2 = st.columns(2)
            
            with xerofila_col1:
                 st.markdown("#### Tàctiques de Reducció de Transpiració:")
                 st.markdown(f"* {highlight('Fulles petites')} o transformades en {highlight('espines')} (per reduir la superfície).")
                 st.markdown(f"* **Protecció:** Presència de {highlight('pèls i ceres')} (redueixen la Tº foliar i l'efecte del vent).")
            
            with xerofila_col2:
                 st.markdown("#### Tàctiques de Reserva/Captació:")
                 st.markdown(f"* {highlight('Acumulació d\'aigua')} en teixits (plantes {highlight('suculentes')}).")
                 st.markdown(f"* {highlight('Arrels profundes i llargues')} (captació d'aigua profunda).")

        with adapt_tab3:
            st.subheader(f"Fred, Llum i Foc")
            col_ad1, col_ad2 = st.columns(2)
            with col_ad1:
                st.markdown("#### Adaptacions al Fred i la Llum:")
                st.markdown(f"* **Fred:** Plantes petites prop del terra, {highlight('saba més espessa')} (ralentir congelació), fulles enfosquides (augmentar insolació) (ADAPTACIONS_FLORA.pdf, p. 4).")
                st.markdown(f"* **Llum:** Augment de la superfície foliar, augment de la {highlight('concentració de clorofil·la')} (ADAPTACIONS_FLORA.pdf, p. 2).")
            with col_ad2:
                st.markdown("#### Adaptacions al Foc (Piròfites):")
                st.markdown(f"* **Resistència Passiva:** Abundància d'aigua a les fulles.")
                st.markdown(f"* {highlight('Rebrotat Ràpid')}: Capacitat de tornar a créixer (ADAPTACIONS_FLORA.pdf, p. 6).")
                st.markdown(f"* {highlight('Serotinia')}: Alliberament de llavors activat per l'alta Tº (ex: Pi blanc).")
            

    with st.expander(f"Mòdul [2]: {highlight('Biodiversitat i Endemisme')} (Detall Exhaustiu)", expanded=True):
        st.header(f"🧬 Endemisme: Factors d'Aïllament ({highlight('NF 1.1')})")
        st.markdown(f"L'endemisme és una espècie amb una {highlight('àrea de distribució molt limitada')}.")
        
        col_end1, col_end2 = st.columns(2)
        
        with col_end1:
            st.subheader(f"Causes d'Aïllament (NF1.1, p. 11):")
            st.markdown(
                f"""
                1.  {highlight('Aïllament Geogràfic (Més comú)')}: Montàno (muntanya), Insular (illes), Edàfic (sòl), Desèrtic.
                2.  {highlight('Aïllament Genètic')}: Interrupció de la comunicació amb comunitats veïnes.
                """
            , unsafe_allow_html=True)

        with col_end2:
            st.subheader(f"Altres Factors i Exemples:")
            st.markdown(
                f"""
                * {highlight('Canvi Brusc del Medi')}: Augment de l'aridesa, glaciacions, variacions extremes de Tº i humitat.
                * **Exemples Clau:** Endemismes montanos ({highlight('Desman dels Pirineus')}, Lagartija aranesa) (NF1.1, p. 13).
                * **Contrast:** {highlight('Cosmopolita')} (espècie distribuïda per tot el món, ex: *Circaetus gallicus* - Au migradora) (NF1.1, p. 14).
                """
            , unsafe_allow_html=True)

elif pagina == "❓ Posa't a Prova! (Quiz)":
    run_quiz()
