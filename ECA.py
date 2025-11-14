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
            "VERSION": "8.3.CLIMOGRAM_IMAGES", # Nova Versió amb imatges
            "AUTHORS": "IMR_Bio-Lab"
        }

def run_boot_sequence():
    initialize_system()
    
    # 1. Crear un contenidor placeholder per a la seqüència de boot
    boot_placeholder = st.empty()

    with boot_placeholder.container():
        st.title(">> 💻 Terminal de Caracterització: Boot Sequence")
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
        }

        /* 2. Configuració de la Pàgina i el Cos */
        .stApp {
            background-color: var(--background-dark);
            color: var(--text-color);
        }
        
        /* 3. Títols amb efecte "Glow" */
        h1 {
            color: var(--primary-color); 
            text-shadow: 0 0 7px rgba(0, 255, 255, 0.7); 
            font-family: 'Consolas', 'Courier New', monospace; 
            border-bottom: 3px solid var(--primary-color-800);
            padding-bottom: 10px;
            margin-top: 0px;
        }
        
        /* 4. Subtítols (Headers de Secció amb barra de càrrega) */
        h2, h3 {
            color: #E0E0E0; 
            border-left: 6px solid var(--primary-color); 
            padding-left: 15px;
            margin-top: 30px;
            background-color: var(--background-medium);
            padding: 10px 15px 10px 15px;
            font-family: 'Consolas', monospace;
        }
        
        /* 5. Contenidors (Panells d'Informació - Més estètica) */
        .st-emotion-cache-1c7v0s, .st-emotion-cache-1ftrz5p { 
             background-color: var(--background-medium);
             padding: 15px;
             border-radius: 8px;
             border: 1px solid var(--primary-color-800);
             box-shadow: 0 0 5px rgba(0, 255, 255, 0.2);
        }
        
        /* 6. Barra Lateral (Sidebar) */
        .st-emotion-cache-vk3ypz { 
            background-color: #050505; 
            border-right: 2px solid var(--primary-color);
        }
        
        /* 7. Altres elements UI (Code blocks) */
        .stCode {
            background-color: #000000;
            border: 1px solid var(--primary-color-800);
            color: #00FF7F; /* Green Terminal Text */
            font-size: 0.9em;
        }
        
        /* Estil per al botó de ràdio seleccionat */
        div[role=radiogroup] label:has(input:checked) {
            background-color: var(--primary-color-800);
            color: var(--background-dark) !important;
            border-radius: 5px;
            padding: 5px 10px;
        }


        </style>
        """,
        unsafe_allow_html=True
    )

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


# --- FUNCIÓ PRINCIPAL DEL QUIZ (Mantenim el Quiz per a densitat i funcionalitat) ---
def run_quiz():
    st.header("❓ Posa't a Prova! (Terminal de Test - NF 1.1, 1.2, 1.3)")
    st.markdown("---")
    st.info("🟢 **EXECUTANT TEST DE VALIDACIÓ DE CONEIXEMENTS...** Aquesta prova cobreix totes les unitats formatives.")
    
    # 12 Preguntes extretes directament dels PDFs
    preguntes = {
        "Q1: Climograma (Sequera)": {
            "pregunta": "En un climograma, la condició de **Sequera/Aridesa** es dóna quan (Regla de Gaussen):",
            "opcions": ["La P supera $2 \times T$", "La Tº supera la P ($T > P$)", "$T \times 2 > P$"],
            "correcta": "La Tº supera la P ($T > P$)" # _NF1.1. Climogrames.pptx.pdf (p. 6)
        },
        "Q2: Bosc Mediterrani (Flora)": {
            "pregunta": "Quin estrat vegetal, a més de l'arbre dominant (Alzina), pren gran rellevància en el Bosc Mediterrani Escleròfil?",
            "opcions": ["L'estrat arbori secundari", "Només l'estrat herbaci", "Els estrats arbustiu, herbaci i lianoide"],
            "correcta": "Els estrats arbustiu, herbaci i lianoide" # NF1.1.BiomesdelaTerra_A1A2.pdf (p. 31)
        },
        "Q3: Adaptació (Límits Tèrmics)": {
            "pregunta": "Per sota de quina Tº la planta paralitza l'activitat d'absorció i processament d'aigua?",
            "opcions": ["$10^{\circ}C$", "$0^{\circ}C$", "$-5^{\circ}C$", "$45^{\circ}C$"],
            "correcta": "$0^{\circ}C$" # ADAPTACIONS_FLORA.pdf (p. 3)
        },
        "Q4: Biodiversitat (Endemisme)": {
            "pregunta": "Quina de les següents espècies és un exemple d'endemisme montàno als Pirineus?",
            "opcions": ["Linx Ibèric", "Desman dels Pirineus (*Galemys pyrenaicus*)", "Faig (*Fagus sylvatica*)"],
            "correcta": "Desman dels Pirineus (*Galemys pyrenaicus*)" # NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf (p. 13)
        },
        "Q5: Classificació (NF 1.3)": {
            "pregunta": "Quin sistema de classificació jeràrquica s'utilitza a la UE per catalogar tots els hàbitats (naturals, seminaturals i artificialitzats)?",
            "opcions": ["Ramsar", "CORINE Biotopes", "ZEPA", "Whittaker"],
            "correcta": "CORINE Biotopes" # NF1.1. Habitats. Classificació Corinne.pptx.pdf (p. 4)
        },
        "Q6: Regió Biogeogràfica": {
            "pregunta": "La Regió Eurosiberiana es caracteritza per la dominància de:",
            "opcions": ["Boscos Perennifolis Escleròfils", "Boscos Caducifolis (Roures, Faigs)", "Vegetació estenoterma"],
            "correcta": "Boscos Caducifolis (Roures, Faigs)" # NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 9)
        },
        "Q7: Hàbitats Catalunya (Fageda)": {
            "pregunta": "La Fageda es troba típicament en climes Medioeuropeus subatlàntics i sobre quin tipus de sòl/substrat?",
            "opcions": ["Terrenys calcaris", "Terrenys àcids (o sòls acidificats)", "Terrenys salins"],
            "correcta": "Terrenys àcids (o sòls acidificats)" # NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 54)
        },
        "Q8: Adaptació (Foc - Serotinia)": {
            "pregunta": "Quin arbre utilitza el mecanisme de **Serotinia** (obertura de pinyes amb la calor) com a adaptació al foc?",
            "opcions": ["Faig (*Fagus sylvatica*)", "Alzina (*Quercus ilex*)", "Pi blanc (*Pinus halepensis*)"],
            "correcta": "Pi blanc (*Pinus halepensis*)" # ADAPTACIONS_FLORA.pdf (p. 6)
        },
        "Q9: Biodiversitat (Aïllament)": {
            "pregunta": "Quin factor pot causar la formació d'endemismes a part de l'aïllament geogràfic?",
            "opcions": ["Un augment de la pluja anual", "Un canvi brusc de les condicions del medi (aridesa, glaciacions)", "Una disminució de la Tº a l'estiu"],
            "correcta": "Un canvi brusc de les condicions del medi (aridesa, glaciacions)" # NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf (p. 11)
        },
        "Q10: Xarxa Natura 2000": {
            "pregunta": "La Xarxa Natura 2000 està formada per les ZEC (Zones Especials de Conservació) i per quins altres espais de protecció?",
            "opcions": ["ZAD (Zones d'Alt Valor)", "ZEPA (Zones d'Especial Protecció per a les Aus)", "ZER (Zones d'Exclusió Ràpida)"],
            "correcta": "ZEPA (Zones d'Especial Protecció per a les Aus)" # NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 16)
        },
        "Q11: Bosc de Pi Negre (Catalunya)": {
            "pregunta": "El Bosc de Pi Negre és típic de quin ambient a Catalunya?",
            "opcions": ["Litoral (dunes)", "Alta Muntanya (Alpí / Subalpí)", "Zona Prelitoral"],
            "correcta": "Alta Muntanya (Alpí / Subalpí)" # NF1.2.HabitatsCatalunya.pptx (1).pdf (p. 3)
        },
        "Q12: Classificació Tèrmica": {
            "pregunta": "Les plantes que només poden viure en un rang de temperatures molt concret s'anomenen:",
            "opcions": ["Euritermes", "Xeròfiles", "Estenotermes"],
            "correcta": "Estenotermes" # ADAPTACIONS_FLORA.pdf (p. 3)
        }
    }

    respostes_usuari = {}

    with st.form(key="quiz_form_ampliat"):
        for i, (key, value) in enumerate(preguntes.items()):
            # Utilitzem un layout més complex per al quiz
            q_col1, q_col2 = st.columns([1, 4])
            with q_col1:
                 st.markdown(f"**{key.split(':')[0].strip()}**")
            with q_col2:
                 st.markdown(f"**{value['pregunta']}**")
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
                    st.markdown(f"**{key}**: Resposta: `{resposta_usuari}`")
            else:
                with status_col:
                    st.error("STATUS: ERROR")
                with res_col:
                    st.markdown(f"**{key}**: La teva resposta: `{resposta_usuari}`. **Correcta**: `{resposta_correcta}`")

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
st.sidebar.title("🧬 Mòdul Bio-Explorador 8.3")
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
    
    st.header("🎯 Matriu d'Objectius (NF 1.1, 1.2, 1.3)")
    st.markdown(
        """
        Aquesta aplicació cobreix els coneixements mínims requerits per la Unitat Formativa 1.
        """
    )
    # Imatge per a l'Estat del Sistema
    st.image("", caption="Estat del Sistema: Mòduls Operatius")

    col_nf1, col_nf2 = st.columns(2)
    
    with col_nf1:
        st.subheader(">> NF 1.1 (Biomes, Climogrames, Biodiversitat)")
        st.markdown(
            """
            * **A1, A2 (Biomes):** El **Bioma** és un conjunt de comunitats amb vegetació climàtica uniforme i clima característic (NF1.1.BiomesdelaTerra_A1A2.pdf, p. 3).
            * **A3 (Climogrames):** Anàlisi de la relació Tº/P. La **Sequera** es dóna quan $P < 2 \times T$ o $T > P$.
            * **Biodiversitat:** Varietat d'éssers vius resultat de l'evolució i l'acció humana (NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf, p. 3).
            """
        )
        st.subheader(">> NF 1.2/1.3 (Hàbitats, Biotops, Protecció)")
        st.markdown(
            """
            * **Definició Clau:** **Biotop** (territori amb condicions ambientals) vs. **Hàbitat** (conjunt de biòtops, espai físic amb aliment, refugi i aigua) (NF1.2.HabitatsaEspanya.pptx (2).pdf, p. 4-5).
            * **CORINE Biotopes (NF 1.3):** Classificació **jeràrquica** europea per a hàbitats naturals, seminaturals i artificialitzats (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 4).
            """
        )
    
    with col_nf2:
        st.subheader(">> NF 1.2 (Hàbitats Peninsulars i Catalunya)")
        st.markdown(
            """
            * **Regions Biogeogràfiques:** Eurosiberiana (Caducifolis), Mediterrània (Escleròfils), Macaronèsica (Endemisme), Alpina (Fred intens).
            * **Fageda (Catalunya):** Clima Medioeuropeu subatlàntic, sobre **terrenys àcids** (NF1.2.HabitatsaEspanya.pptx (2).pdf, p. 54).
            * **Alzinar:** Bosc perennifoli escleròfil adaptat a la sequera estival (NF1.1.BiomesdelaTerra_A1A2.pdf, p. 31).
            * **Xarxa Natura 2000 (NF 1.3):** Xarxa d'àrees de conservació amb **ZEC** (Hàbitats/Espècies) i **ZEPA** (Aus).
            """
        )
        st.info(f"EXECUCIÓ OK. Concentració de dades a l'àrea d'informació. Versió {st.session_state.config.get('VERSION', 'N/A')}")

elif pagina == "🌍 Biomes de la Terra (NF 1.1)":
    st.title("🌍 Cartografia Global: Biomes de la Terra (NF 1.1: A1, A2)")
    st.markdown("Unitats de gran extensió amb una vegetació climàtica uniforme i clima característic (NF1.1.BiomesdelaTerra_A1A2.pdf, p. 3).")

    # Imatge per als Biomes de la Terra (Mapa)
    st.image("

[Image of World Biomes Map]
", caption="Distribució Global dels Principals Biomes Terrestres")

    st.subheader("Definicions de Biomes Clau (Més Enllà del Mediterrani)")
    st.info("Aquesta secció inclou referències als biomes de Pastures i Sabana, esmentats en la classificació global (NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf, p. 2).")

    bio_col1, bio_col2 = st.columns(2)
    
    with bio_col1:
        st.markdown("#### **Pastures (Grasslands)**")
        st.markdown("* **Clima:** Zones temperades amb estius càlids i hiverns freds. Pluges moderades que no permeten el desenvolupament d'arbres alts.")
        st.markdown("* **Vegetació:** Domini de gramínies i herbes. Exemples: Praderies Nord-americanes, Estepes d'Euràsia.")
    
    with bio_col2:
        st.markdown("#### **Sabana (Tropical Grasslands)**")
        st.markdown("* **Clima:** Tropical amb una estació seca molt marcada i una estació humida. Clima amb temperatura constantment alta.")
        st.markdown("* **Vegetació:** Gramínies altes amb arbres aïllats o petits grups d'arbres (ex: acàcies). Adaptada als incendis i a la pastura d'herbívors.")

    with st.expander("Fitxa Tècnica: Bosc Escleròfil Mediterrani (Densitat Màxima)", expanded=True):
        
        tab_flora, tab_fauna, tab_estrategia = st.tabs(["[1] Detall Flora i Estructura", "[2] Detall Fauna", "[3] Clima i Sòl Crític"])
        
        with tab_flora:
            st.subheader("Estratègia Escleròfil·la i Estructura Vegetal (NF1.1, p. 31)")
            st.markdown("* La vegetació és principalment **escleròfil·la** (fulla dura) i **perenne** per a resistir la sequera estival.")
            st.markdown("* **Arbres Perennes Clau:** Alzines (*Quercus ilex*), Sureres, Garrofers, Oliveres, Arboç.")
            st.markdown("* **Estrats Inferiors:** Els estrats **Arbustiu**, **Herbaci** i **Lianoide** prenen gran rellevància (gran abundància d'espècies).")
            
        with tab_fauna:
            st.subheader("Fauna Clau per Nínxol Ecològic (NF1.1, p. 32)")
            
            st.markdown(
                """
                * **Herbívors Clau:** Cabirols, Esquirols, Llebres, Cabres salvatges.
                * **Carnívors Representatius:** Guineus, geneta, **Linx Ibèric** (el carnívor més representatiu i amenaçat).
                * **Omnívors Destacats:** Porc senglar, rata de camp, Teixó.
                """
            )
            st.image("", caption="Linx ibèric, un carnívor clau del bioma mediterrani")


        with tab_estrategia:
            st.subheader("Clima i Sòl (Determinants del Bioma)")
            st.markdown(
                """
                * **Clima:** Mediterrani (estius secs i calorosos, hiverns suaus).
                * **Factor Determinant:** La **sequera estival** (període d'aridesa) i les altes temperatures.
                * **Sòl:** Tendeix a ser **pobre en matèria orgànica** i amb capacitat per absorbir ràpidament l'aigua.
                """
            )

elif pagina == "🌲 Classificació dels Biomes Principals":
    st.title("🌲 Classificació dels Biomes Principals (NF 1.1: A2)")
    st.markdown("Anàlisi comparativa dels biomes de latituds extremes i humits.")

    # Imatge per a la Classificació dels Biomes
    st.image("", caption="Bosc de Coníferes (Taiga): Bosc Boreal")

    with st.expander("Fitxa Tècnica: Biomes de Latituds Altes i Grans Humitats", expanded=True):
        
        bio_col1, bio_col2 = st.columns(2)
        
        with bio_col1:
            st.subheader("1. Tundra (Bioma Frèd Extrem)")
            st.markdown(
                """
                * **Clima:** Tº mitjanes baixíssimes (gran part de l'any sota $0^{\circ}C$). Poca precipitació (neu).
                * **Vegetació:** Prats i landes. Predomini de molses, líquens i arbusts nans. **Sense arbres**.
                * **Sòl Clau:** **Permafrost** (sòl permanentment congelat).
                """
            )
            st.subheader("3. Bosc de Coníferes o Taiga (Bioma Boreal)")
            st.markdown(
                """
                * **Clima:** Fred extrem amb estius curts i suaus. Precipitació moderada.
                * **Vegetació:** Boscos d'arbres de **fulla perenne acicular** (en forma d'agulla) i resistents al fred (Pins, Avets).
                * **Adaptació:** Forma cònica per evitar l'acumulació d'acumulació de neu.
                """
            )
            
        with bio_col2:
            st.subheader("2. Desert (Bioma Amb Dèficit Hídric Extrem)")
            st.markdown(
                """
                * **Clima:** Molt poca precipitació (sovint $< 250$ mm/any). Gran oscil·lació tèrmica diària.
                * **Vegetació:** Escassa i molt adaptada (**xeròfites**, suculentes com els cactus). Fulles transformades en espines.
                * **Sòl Clau:** Pobre, amb poques substàncies orgàniques.
                """
            )
            st.subheader("4. Selva Tropical (Bioma Humit Càlid)")
            st.markdown(
                """
                * **Clima:** Tº mitjanes altes i constants. Precipitació molt alta i constant. **Sense estació seca**.
                * **Vegetació:** Boscos densos, amb molts estrats i gran diversitat d'espècies (**alta biodiversitat**).
                * **Sòl Clau:** Freqüentment pobre per l'alt rentat de nutrients (**lixiviació**).
                """
            )


elif pagina == "📊 Climogrames i Distribució":
    st.title("📊 Anàlisi Gràfica Climàtica (NF 1.1: A3)")
    st.markdown("Eina essencial per caracteritzar un bioma mitjançant la combinació de Tº i P (NF1.1. Climogrames.pptx.pdf, p. 2).")

    with st.expander("Detall Tècnic: Interpretació Visual i Regles Crítiques (Ampliat)", expanded=True):
        st.header("Mòdul: Interpretació Visual i Regla de Gaussen")
        
        # Imatge per al Climograma (la que has pujat, si és possible, o una genèrica)
        st.image("", caption="Exemple de Climograma de Walter i Lieth")
        
        st.subheader("1. ⚙️ Guia de Lectura i Escales (Regla de Gaussen)")
        
        col_lectura, col_regla = st.columns(2)
        
        with col_lectura:
            st.markdown(
                """
                * **Línia Vermella (Tº):** Representa la **Temperatura mitjana mensual** (Eix vertical esquerre).
                * **Barres Blaves (P):** Representen la **Precipitació mitjana mensual** (Eix vertical dret).
                * **Relació Clau:** L'escala utilitza la relació $10^{\circ}C$ s'alinea amb $20$ mm. Aquesta escala doble (P:T, 2:1) és la que permet llegir ràpidament la sequera.
                """
            )
        with col_regla:
            st.markdown("#### **Interpretació de la Vida Vegetal:**")
            st.markdown(
                """
                * **HUMITAT:** La línia **Blava (P)** es troba **per sobre** de la línia **Vermella (T)**. L'aigua no és limitant.
                * **SEQUERA (ARIDESA):** La línia **Vermella (T)** es troba **per sobre** de la línia **Blava (P)**. L'aigua és el factor limitant.
                * **GELADA/FRED:** La línia **Vermella (T)** cau **per sota dels $0^{\circ}C$**. Paralització de l'activitat de la planta.
                """
            )

        st.markdown("---")
        st.subheader("2. 🌍 Escenaris Climàtics Clàssics (Tipus de Clima)")
        
        tab_med, tab_oce, tab_pol = st.tabs(["[A] Mediterrani (Escleròfil)", "[B] Oceànic (Caducifoli)", "[C] Polar / Alta Muntanya"])
        
        with tab_med:
            st.markdown("#### **Escenari Mediterrani Típic (Bioma Escleròfil)**")
            st.code(">>> ZONA DE VEGETACIÓ: Alzinar, Pinar (Xeròfil·la)")
            st.markdown(
                """
                * **Factor Clau:** Forta i clara **sequera estival**.
                * **Visualització:** La línia vermella (T) puja bruscament i **supera** clarament la línia blava (P) durant els mesos d'estiu (J, L, A).
                * **Hivern:** Temperat, amb temperatures mitjanes superiors als $5^{\circ}C$ (sense gelades significatives).
                """
            )
        
        with tab_oce:
            st.markdown("#### **Escenari Temperat Oceànic (Regió Eurosiberiana)**")
            st.code(">>> ZONA DE VEGETACIÓ: Bosc Caducifoli (Faig, Roure)")
            st.markdown(
                """
                * **Factor Clau:** **Absència total de sequera estival.**
                * **Visualització:** La línia blava (P) es manté **sempre** per sobre de la línia vermella (T).
                * **Hivern:** Fred, però amb precipitació abundant i ben distribuïda.
                """
            )

        with tab_pol:
            st.markdown("#### **Escenari Polar / Alta Muntanya (Clima Alpí)**")
            st.code(">>> ZONA DE VEGETACIÓ: Tundra, Prats Alpins")
            st.markdown(
                """
                * **Factor Clau:** **Fred extrem** i limitant.
                * **Visualització:** La línia vermella (T) es troba **per sota o molt a prop dels $0^{\circ}C$** durant diversos mesos.
                * **Implicació:** La baixa Tº **paralitza** l'activitat de la planta (aigua no disponible) i impedeix el desenvolupament arbori.
                """
            )
    
    st.markdown("---")


elif pagina == "🇪🇸 Hàbitats Peninsulars i Protecció (NF 1.2/1.3)":
    st.title("🇪🇸 Regions Biogeogràfiques i Classificació (NF 1.2 & NF 1.3)")
    st.markdown("La península es divideix en 4 regions principals (NF1.2.HabitatsaEspanya.pptx).")

    # Imatge per a les Regions Biogeogràfiques
    st.image("", caption="Mapa de les Regions Biogeogràfiques de la Península Ibèrica")


    st.subheader("Mòdul NF 1.2: Anàlisi Densa de Regions Biogeogràfiques (A2)")
    
    reg_tab1, reg_tab2, reg_tab3, reg_tab4 = st.tabs(["[1] Eurosiberiana", "[2] Mediterrània", "[3] Macaronèsica", "[4] Alpina"])

    with reg_tab1:
        st.markdown("* **Clima:** Temperat, humit, **sense aridesa estival** (clima Oceànic).")
        st.markdown("* **Vegetació Clau:** Dominància de **Boscos Caducifolis** (Roures, Faigs).")

    with reg_tab2:
        st.markdown("* **Clima:** Estius secs i calorosos. Sequera estival present.")
        st.markdown("* **Vegetació Clau:** **Boscos Perennifolis Escleròfils** (Alzinar, Surera, Pi).")
    
    with reg_tab3:
        st.markdown("* **Particularitat:** Aïllament insular, que genera un **altíssim nivell d'endemisme**.")
        st.markdown("* **Flora Única:** Laurissilva, Pi canari.")

    with reg_tab4:
        st.markdown("* **Condicions:** Fred intens, vent, baixa Tº (per sobre de la zona subalpina).")
        st.markdown("* **Vegetació Clau:** Bosc Subalpí (Pi Negre) i Prats Alpins.")

    st.markdown("---")
    st.subheader("Mòdul NF 1.3: Classificació i Protecció (Detall Extens)")
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.header("Classificació (CORINE Biotopes)")
        st.code(">>> NF1.1. Habitats. Classificació Corinne.pptx.pdf (p. 4)")
        st.markdown(
            """
            * **Base Legal:** Sistema **jeràrquic** estandarditzat per la Unió Europea.
            * **Abast:** Classifica la totalitat dels hàbitats de la UE: **naturals**, **seminaturals** i **artificialitzats**.
            * **Objectiu:** Ordenar, cartografiar i comparar la diversitat d'hàbitats.
            """
        )

    with col_p2:
        st.header("Xarxa Natura 2000 (ZEC i ZEPA)")
        st.code(">>> NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 16)")
        st.markdown(
            """
            Xarxa d'àrees de conservació (Directiva Hàbitats / Directiva Ocells).
            * **ZEC (Zones Especials de Conservació):** Protegeix **hàbitats i espècies d'interès comunitari**.
            * **ZEPA (Zones d'Especial Protecció per a les Aus):** Espais designats per a la protecció dels ocells.
            """
        )


elif pagina == "🏞️ Hàbitats de Catalunya (Detall Exhaustiu)":
    st.title("🏞️ Fitxer d'Hàbitats Nacionals (NF 1.2: A3)")
    st.markdown("La gran varietat geogràfica de Catalunya resulta en una elevada diversitat d'hàbitats.")

    # Imatge per als Hàbitats de Catalunya
    st.image("", caption="La Fageda d'en Jordà, exemple d'hàbitat medioeuropeu")
    
    hab_tab1, hab_tab2, hab_tab3 = st.tabs(["[1] Boscos de Fulla Caduca i Perenne", "[2] Boscos de Pi i Formacions Arbustives", "[3] Formacions Herbàcies (Detall)"])

    with hab_tab1:
        st.header("🌳 La Fageda (*Fagus sylvatica*) - Bosc Tancat")
        fag_col1, fag_col2 = st.columns(2)
        
        with fag_col1:
            st.subheader("Ecologia del Faig (Medioeuropeu Subatlàntic)")
            st.markdown(
                """
                * **Clima:** **Medioeuropeu subatlàntic** (molta humitat).
                * **Substrat:** Terrenys **àcids** o sòls acidificats (NF1.2.HabitatsaEspanya.pptx (2).pdf, p. 54).
                * **Ubicació:** Muntanya mitjana, típicament en vessants obacs i inclinats.
                """
            )
        with fag_col2:
            st.subheader("Sotabosc Pobre (Plantes Acidòfiles) - NF1.2, p. 56")
            st.markdown(
                """
                El sotabosc és pobre per manca de llum. Està compost per:
                * **Arbustiu Clau:** Boix (*Buxus sempervirens*), Grèvol (*Ilex aquifolium*).
                * **Herbaci Específic:** Bruguerola (*Calluna vulgaris*), Falguera comuna (*Pteridium aquilinum*), Te de muntanya (*Veronica officinalis*).
                """
            )

        st.header("🌲 L'Alzinar (*Quercus ilex*) - Bosc Escleròfil")
        al_col1, al_col2 = st.columns(2)
        
        with al_col1:
            st.subheader("Tipus Escleròfil·le i Rols")
            st.markdown(
                """
                * **Tipus:** Bosc perennifoli **escleròfil** mediterrani.
                * **Funció de la Fulla:** La duresa redueix la **transpiració**, essencial per a sobreviure a la sequera estival.
                * **Observació:** És el **clímax** potencial del clima mediterrani.
                """
            )

        with al_col2:
            st.subheader("Flora de Sotabosc Mediterrani")
            st.markdown(
                """
                * **Arbusts Específics:** Marfull, Arboç, Llentiscle.
                * **Lianes Comunes:** Arítjol.
                """
            )

    with hab_tab2:
        st.header("🌳 Boscos de Pi (Diversitat Ecològica)")
        st.markdown("Varien segons l'altitud i la resistència:")
        
        pi_col1, pi_col2 = st.columns(2)
        
        with pi_col1:
            st.markdown("#### **Alta Muntanya/Interior:**")
            st.markdown("* **Pi Negre (*Pinus uncinata*):** Alta Muntanya (Estrat Subalpí/Alpí). Resistent al fred extrem i als vents (NF1.2.HabitatsCatalunya.pptx (1).pdf, p. 3).")
            st.markdown("* **Pi Roig (*Pinus sylvestris*):** Muntanya mitjana/interior. S'adapta a sòls més pobres.")

        with pi_col2:
            st.markdown("#### **Litoral i Baixa Muntanya (Piròfites):**")
            st.markdown("* **Pi Blanc (*Pinus halepensis*):** Litoral/prelitoral. Fortament **piròfita** (mecanisme de **Serotinia**) (ADAPTACIONS_FLORA.pdf, p. 6).")
            st.markdown("* **Arbustives:** **Màquia** (densa, degradació de l'alzinar) i **Brolla** (oberta, brucs, romaní).")
            
    with hab_tab3:
        st.header("🌱 Formacions Herbàcies (Classificació Tècnica)")
        st.markdown("NF1.2.HabitatsCatalunya.pptx (1).pdf, p. 54-55")
        
        herb_col1, herb_col2 = st.columns(2)
        with herb_col1:
             st.subheader("Definicions d'Estructura")
             st.markdown("- **Prat:** Comunitat dominada per gramínies. Aspecte **compacte i homogeni**.")
             st.markdown("- **Pradell:** Prat de **reduïda extensió** o recobriment escàs.")
             st.markdown("- **Gramenet/Gespa:** Prats en què predominen les gramínies o plantes graminoides; la gespa és molt atapeïda.")
        with herb_col2:
             st.subheader("Tipus de Prats Clau")
             st.markdown("- **Prats Alpins:** Típics de la zona pirinenca, sobre el límit del bosc (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 10).")
             st.markdown("- **Prats Halòfils:** Associats a zones litorals o salines.")
             st.markdown("- **Aiguamolls:** Zones d'alta biodiversitat que combinen aigua dolça/salada i vegetació herbàcia/arbustiva.")


elif pagina == "🌱 Adaptacions i Biodiversitat (NF 1.1)":
    st.title("🌱 Adaptacions i Biodiversitat (NF 1.1)")
    st.markdown("Respostes dels éssers vius als factors ambientals extrems.")

    # Imatge per a les Adaptacions
    st.image("", caption="Exemple de planta xeròfila (suculenta) adaptada a la sequera")

    with st.expander("Mòdul [1]: Adaptacions Tèrmiques, Hídriques i Lumíniques (Detall Exhaustiu)", expanded=True):
        
        adapt_tab1, adapt_tab2, adapt_tab3 = st.tabs(["[A] Límits Tèrmics Crítics", "[B] Sequera/Xeròfiles", "[C] Fred, Llum i Foc"])

        with adapt_tab1:
            st.subheader("Límits de Supervivència (NF1.1, p. 3)")
            st.code(">>> RANG VITAL: 0°C a 45°C")
            st.markdown(
                """
                * **$0^{\circ}C$:** La planta **paralitza** l'activitat d'absorció d'aigua.
                * **$45^{\circ}C$:** L'activitat vegetativa es paralitza.
                * **Classificació Tèrmica:** **Euritermes** (ample rang de Tº) vs. **Estenotermes** (Tº més concretes).
                """
            )
        
        with adapt_tab2:
            st.subheader("Mecanismes Xeròfils (Evitar Pèrdua d'Aigua) - NF1.1, p. 5")
            
            xerofila_col1, xerofila_col2 = st.columns(2)
            
            with xerofila_col1:
                 st.markdown("#### Tàctiques de Reducció de Transpiració:")
                 st.markdown("* **Fulles petites** o transformades en **espines** (per reduir la superfície).")
                 st.markdown("* **Protecció:** Presència de **pèls i ceres** (redueixen la Tº foliar i l'efecte del vent).")
            
            with xerofila_col2:
                 st.markdown("#### Tàctiques de Reserva/Captació:")
                 st.markdown("* **Acumulació d'aigua** en teixits (plantes **suculentes**).")
                 st.markdown("* **Arrels profundes i llargues** (captació d'aigua profunda).")

        with adapt_tab3:
            st.subheader("Fred, Llum i Foc")
            col_ad1, col_ad2 = st.columns(2)
            with col_ad1:
                st.markdown("#### Adaptacions al Fred i la Llum:")
                st.markdown("* **Fred:** Plantes petites prop del terra, **saba més espessa** (ralentir congelació), fulles enfosquides (augmentar insolació) (ADAPTACIONS_FLORA.pdf, p. 4).")
                st.markdown("* **Llum:** Augment de la superfície foliar, augment de la **concentració de clorofil·la** (ADAPTACIONS_FLORA.pdf, p. 2).")
            with col_ad2:
                st.markdown("#### Adaptacions al Foc (Piròfites):")
                st.markdown("* **Resistència Passiva:** Abundància d'aigua a les fulles.")
                st.markdown("* **Rebrotat Ràpid:** Capacitat de tornar a créixer (ADAPTACIONS_FLORA.pdf, p. 6).")
                st.markdown("* **Serotinia:** Alliberament de llavors activat per l'alta Tº (ex: Pi blanc).")
            

    with st.expander("Mòdul [2]: Biodiversitat i Endemisme (Detall Exhaustiu)", expanded=True):
        st.header("🧬 Endemisme: Factors d'Aïllament (NF 1.1)")
        st.markdown("L'endemisme és una espècie amb una **àrea de distribució molt limitada**.")
        
        col_end1, col_end2 = st.columns(2)
        
        with col_end1:
            st.subheader("Causes d'Aïllament (NF1.1, p. 11):")
            st.markdown(
                """
                1.  **Aïllament Geogràfic (Més comú):** Montàno (muntanya), Insular (illes), Edàfic (sòl), Desèrtic.
                2.  **Aïllament Genètic:** Interrupció de la comunicació amb comunitats veïnes.
                """
            )

        with col_end2:
            st.subheader("Altres Factors i Exemples:")
            st.markdown(
                """
                * **Canvi Brusc del Medi:** Augment de l'aridesa, glaciacions, variacions extremes de Tº i humitat.
                * **Exemples Clau:** Endemismes montanos (Desman dels Pirineus, Lagartija aranesa) (NF1.1, p. 13).
                * **Contrast:** **Cosmopolita** (espècie distribuïda per tot el món, ex: *Circaetus gallicus* - Au migradora) (NF1.1, p. 14).
                """
            )


elif pagina == "❓ Posa't a Prova! (Quiz)":
    run_quiz()
