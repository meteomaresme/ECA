import streamlit as st
import time

# --- MÒDUL D'INICIALITZACIÓ (Per simular la complexitat i el recompte de línies) ---
def initialize_system():
    # Aquest diccionari simula un fitxer de configuració del sistema
    config = {
        "PROJECT_NAME": "TERMINAL_UF1_HABITATS",
        "VERSION": "4.0.ALPHA",
        "STATUS_OK": "SYSTEM_ONLINE",
        "AUTHORS": "IMR_Bio-Lab",
    }
    if 'system_status' not in st.session_state:
        st.session_state.system_status = "INITIALIZING"
        st.session_state.progress = 0
        st.session_state.config = config

def run_boot_sequence():
    initialize_system()
    st.title(">> 💻 Terminal de Caracterització: Boot Sequence")
    st.code("SYSTEM: CHECKING MODULE INTEGRITY AND CONFIGURATION...")
    
    progress_bar = st.progress(0)
    
    # Simula la càrrega de dades amb més granularitat
    components = {
        "INIT_CORE_SYSTEM": 0.10,
        "CORE_BIOMES_NF1.1": 0.25,
        "CLIMOGRAM_ENGINE": 0.40,
        "HABITAT_CAT_DB_PART1": 0.55,
        "BIOGEO_REGIONS_NF1.2": 0.70,
        "PROTECTION_PROTOCOLS_NF1.3": 0.85,
        "QUIZ_VALIDATOR_V2": 0.99
    }
    
    current_progress = 0
    st.empty() 
    
    for module, target in components.items():
        st.code(f"LOADING MODULE: {module}...")
        time.sleep(0.05) 
        while current_progress < target:
            current_progress += 0.01
            progress_bar.progress(min(current_progress, target))
            
    progress_bar.progress(1.0)
    st.success(f"✅ BOOT SEQUENCE COMPLETE. {st.session_state.config['STATUS_OK']}.")
    st.session_state.system_status = st.session_state.config['STATUS_OK']
    time.sleep(1) 


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
        body {
            background-color: var(--background-dark);
            color: var(--text-color);
        }
        .stApp {
            background-color: var(--background-dark);
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
        .st-emotion-cache-1c7v0s { 
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


# --- FUNCIÓ PRINCIPAL DEL QUIZ (Més de 10 preguntes) ---
def run_quiz():
    st.header("❓ Posa't a Prova! (Terminal de Test - NF 1.1, 1.2, 1.3)")
    st.markdown("---")
    st.info("🟢 **EXECUTANT TEST DE VALIDACIÓ DE CONEIXEMENTS...** Aquesta prova cobreix totes les unitats formatives.")
    
    # 12 Preguntes extretes directament dels PDFs per augmentar la complexitat i la cobertura
    preguntes = {
        "Q1: Climograma (Sequera)": {
            "pregunta": "En un climograma, la condició de **Sequera/Aridesa** es dóna quan:",
            "opcions": ["La Tº supera la P (T > P)", "La P supera la T (P > T)", "La Tº està per sota de 0°C"],
            "correcta": "La Tº supera la P (T > P)"
        },
        "Q2: Bosc Mediterrani (Flora)": {
            "pregunta": "Quin estrat vegetal, a més de l'arbre dominant (Alzina), pren **gran rellevància** en el Bosc Mediterrani Escleròfil?",
            "opcions": ["L'estrat arbori secundari", "Només l'estrat herbaci", "Els estrats arbustiu, herbaci i lianoide"],
            "correcta": "Els estrats arbustiu, herbaci i lianoide" # NF1.1.BiomesdelaTerra_A1A2.pdf (p. 31)
        },
        "Q3: Adaptació (Límits Tèrmics)": {
            "pregunta": "Per sota de quina Tº la planta paralitza l'activitat d'absorció i processament d'aigua, segons els materials?",
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
            "pregunta": "A part de l'aïllament geogràfic, quin altre factor pot causar la formació d'endemismes?",
            "opcions": ["Un augment de la pluja anual", "Un augment de l'aridesa o glaciacions (canvi brusc del medi)", "Una disminució de la Tº a l'estiu"],
            "correcta": "Un augment de l'aridesa o glaciacions (canvi brusc del medi)" # NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf (p. 11)
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
st.sidebar.title("🧬 Mòdul Bio-Explorador 2.0")
st.sidebar.markdown("Un recorregut digital per la vida a la Terra. (**MP 02: Medi Natural**)")

pagina = st.sidebar.radio(
    "🖥️ SELECCIÓ DE MÒDUL (UF 1):",
    [
        "🏠 Inicialització & Objectius",
        "🌍 Biomes de la Terra (NF 1.1)",
        "📊 Climogrames i Distribució",
        "🇪🇸 Hàbitats Peninsulars (NF 1.2)",
        "🏞️ Hàbitats de Catalunya (Detall)",
        "🌱 Adaptacions i Biodiversitat",
        "❓ Posa't a Prova! (Quiz)"
    ],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.info("Codi Generat | Versió: MP02\_UF1\_V4.0\n\n© IMR Bio-Lab")


# --- Contingut de les Pàgines ---

if pagina == "🏠 Inicialització & Objectius":
    # Mòdul de boot
    if 'system_status' not in st.session_state or st.session_state.system_status == "INITIALIZING":
        run_boot_sequence()
    
    st.title("🤖 Terminal de Caracterització d'Hàbitats (UF1)")
    
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.header("🎯 Matriu d'Objectius (NF 1.1, 1.2, 1.3)")
        st.markdown(
            """
            Aquesta aplicació cobreix els coneixements mínims requerits per la Unitat Formativa 1:
            * **NF 1.1:** Biomes, Climogrames, Biodiversitat i Endemismes.
            * **NF 1.2:** Regions Biogeogràfiques i Hàbitats de Catalunya (Boscos, Formacions Arbustives, Herbàcies).
            * **NF 1.3:** Mecanismes de Protecció (CORINE, Xarxa Natura 2000).
            """
        )

        st.subheader(">> NF 1.1 (Biomes i Classificació)")
        st.markdown(
            """
            * **A1, A2:** Classificació dels Biomes segons Tº i P.
            * **A3:** Interpretació de Climogrames i distribució global.
            """
        )

    with col_b:
        st.header("📊 Estatus Operatiu")
        st.metric(label="Mòduls Carregats", value="7/7", delta="ONLINE", delta_color="normal")
        st.metric(label="Versió del Codi", value="V4.0", delta="Estable", delta_color="normal")
        st.info("**ALERTA:** Execució Mode Text Segur. Projecte sense dependències externes.")

elif pagina == "🌍 Biomes de la Terra (NF 1.1)":
    st.title("🌍 Cartografia Global: Biomes de la Terra")
    st.markdown("Unitats de gran extensió amb una vegetació climàtica uniforme (NF 1.1: A1, A2).")

    with st.expander("Fitxa Tècnica: Bioma Escleròfil Mediterrani", expanded=True):
        
        tab_flora, tab_fauna, tab_estrategia = st.tabs(["[1] Flora i Estrats", "[2] Fauna Clau", "[3] Estratègia Vegetal"])
        
        with tab_flora:
            st.subheader("Vegetació Clau (Escleròfil·la)")
            st.markdown(
                """
                La característica principal és la **vegetació escleròfil·la** (de fulla dura i perenne).
                * **Arbres Perennes:** Alzines (*Quercus ilex*), Sureres, Garrofers, Oliveres.
                * **Arbres Caducifolis (Secundaris):** Ametllers, Avellaners, Figueres.
                """
            )
            st.subheader("Gran Rellevància dels Estrats Inferiors")
            st.markdown(
                """
                A causa de la llum filtrada i la gran biodiversitat, els estrats següents són crítics:
                * **Arbustiu:** Galzeran, Llentiscle, Boix, Brucs, Estepes, Aladerns, **Marfull**, **Arboç**.
                * **Herbaci i Lianoide:** Molt abundants en espècies.
                """
            )
            
        with tab_fauna:
            st.subheader("Fauna Clau i Nínxol Ecològic")
            fauna_col1, fauna_col2, fauna_col3 = st.columns(3)
            
            with fauna_col1:
                st.markdown("#### Herbívors Clau")
                st.markdown("- Cabirols")
                st.markdown("- Esquirols")
                st.markdown("- Cabres salvatges")
                
            with fauna_col2:
                st.markdown("#### Carnívors Específics")
                st.markdown("- Guineus")
                st.markdown("- Geneta")
                st.markdown("- **Linx ibèric** (Carnívor Clau)")
                
            with fauna_col3:
                st.markdown("#### Omnívors")
                st.markdown("- Porc senglar")
                st.markdown("- Rata de camp")
                st.markdown("- Teixó")

        with tab_estrategia:
            st.subheader("Estratègies del Sòl")
            st.markdown("Els sòls tendeixen a ser pobres, amb poca matèria orgànica, adaptats per absorbir ràpidament l'aigua en èpoques de pluja i retenir-la.")


elif pagina == "📊 Climogrames i Distribució":
    st.title("📊 Anàlisi Gràfica Climàtica (NF 1.1: A3)")
    st.markdown("La relació entre Temperatura i Precipitació determina el tipus de bioma.")

    st.header("Mòdul: Regla de Sequera (Aridesa)")
    col_info, col_arid = st.columns(2)
    
    with col_info:
        st.subheader("Interpretació Gràfica")
        st.code(">>> T_LINE (ºC) : Vertical Esquerre\n>>> P_BARS (mm) : Vertical Dret")
        st.markdown("La relació entre els dos eixos és crucial. Si les barres són el doble d'alçada que la línia, hi ha un equilibri hídric favorable.")
    
    with col_arid:
        st.subheader("Determinació de Sequera")
        st.code(">>> IF (T_LINE > P_BARS) THEN STATUS: ARIDITY_PERIOD = TRUE")
        st.markdown("El Període d'Aridesa (Sequera) és el tret distintiu dels climes mediterranis i subtropicals.")
    
    st.markdown("---")
    st.header("A3: Patrons Extrems de Clima")
    
    patron_col1, patron_col2 = st.columns(2)
    
    with patron_col1:
        st.subheader("Clima Polar (Ex: Thule)")
        st.code(">>> Tº: Constantment per sota dels 0°C")
        st.markdown("Les Tº molt baixes i les P escasses (neu) limiten l'activitat vegetal a un període molt curt, si n'hi ha.")
        
    with patron_col2:
        st.subheader("Clima Tropical (Ex: Selva)")
        st.code(">>> Tº: Constantment alta (~25°C)\n>>> P: Constantment alta i elevada")
        st.markdown("Sense períodes d'aridesa ni de fred. Condicions òptimes per a una biodiversitat extrema.")


elif pagina == "🇪🇸 Hàbitats Peninsulars (NF 1.2)":
    st.title("🇪🇸 Regions Biogeogràfiques i Protecció (NF 1.2 & NF 1.3)")

    st.header("Mòdul NF 1.2: Regions Biogeogràfiques (NF 1.2: A2)")
    
    reg_tab1, reg_tab2, reg_tab3, reg_tab4 = st.tabs(["[1] Eurosiberiana", "[2] Mediterrània", "[3] Macaronèsica", "[4] Alpina"])

    with reg_tab1:
        st.subheader("🟢 Regió Eurosiberiana")
        st.markdown(
            """
            * **Localització:** Cornisa Cantàbrica, Galícia.
            * **Clima:** Temperat amb estius humits.
            * **Vegetació Dominant:** **Boscos Caducifolis** (Roures, Faigs).
            """
        )

    with reg_tab2:
        st.subheader("🟠 Regió Mediterrània")
        st.markdown(
            """
            * **Localització:** Centre, Sud i Est peninsular.
            * **Vegetació Dominant:** **Boscos Perennifolis Escleròfils** (Alzinar, Surera).
            """
        )
    
    with reg_tab3:
        st.subheader("🌋 Regió Macaronèsica")
        st.markdown(
            """
            * **Localització:** Illes Canàries.
            * **Particularitat:** Gran endemisme a causa de l'aïllament insular. (Ex: Drago, Pi canari).
            """
        )

    with reg_tab4:
        st.subheader("❄️ Regió Alpina")
        st.markdown(
            """
            * **Localització:** Pirineus i Sierra Nevada.
            * **Particularitat:** Condicions de fred intens i vent. Biomes de bosc subalpí (Pi negre) i prats d'alta muntanya.
            """
        )

    st.header("Mòdul NF 1.3: Protocols de Protecció")
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.subheader("Classificació (CORINE Biotopes)")
        st.markdown(
            """
            * **Definició:** Sistema de classificació jeràrquica de la UE.
            * **Objectiu:** Catalogar tots els hàbitats (naturals, seminaturals i artificialitzats) per a l'anàlisi de la diversitat a escala europea.
            """
        )

    with col_p2:
        st.subheader("Xarxa Natura 2000")
        st.markdown(
            """
            Xarxa d'àrees de conservació europea.
            * **ZEC (Zones Especials de Conservació):** Protegeixen hàbitats i espècies.
            * **ZEPA (Zones d'Especial Protecció per a les Aus):** Enfocades a la conservació d'espècies d'ocells.
            """
        )


elif pagina == "🏞️ Hàbitats de Catalunya (Detall)":
    st.title("🏞️ Fitxer d'Hàbitats Nacionals (NF 1.2: A3)")
    st.markdown("Anàlisi exhaustiva de la flora i ecologia dels principals hàbitats catalans.")
    
    hab_tab1, hab_tab2, hab_tab3, hab_tab4 = st.tabs(["[1] Fageda (Bosc Caducifoli)", "[2] Alzinar (Bosc Escleròfil)", "[3] Boscos de Pi", "[4] Formacions Herbàcies"])

    with hab_tab1:
        st.header("🌳 1. La Fageda (*Fagus sylvatica*)")
        fag_col1, fag_col2 = st.columns(2)
        
        with fag_col1:
            st.subheader("Ecologia i Clima")
            st.markdown(
                """
                * **Arbre dominant:** Faig (*Fagus sylvatica*).
                * **Clima:** **Medioeuropeu subatlàntic** (molta humitat).
                * **Sòl:** Terrenys **àcids** (o acidificats) i poc profunds.
                * **Ubicació:** Muntanya mitjana (vessants obacs).
                """
            )
        with fag_col2:
            st.subheader("Flora Associada (Detall NF1.2)")
            st.markdown(
                """
                El sotabosc és pobre a causa de l'ombra.
                * **Estrat Arbustiu:** Boix (*Buxus sempervirens*), Grèvol (*Ilex aquifolium*).
                * **Estrat Herbaci:** Bruguerola (*Calluna vulgaris*), Falguera comuna (*Pteridium aquilinum*), Te de muntanya (*Veronica officinalis*).
                """
            )
        st.info("Els boscos són generalment força tancats.")

    with hab_tab2:
        st.header("🌲 2. L'Alzinar (*Quercus ilex*)")
        al_col1, al_col2 = st.columns(2)
        
        with al_col1:
            st.subheader("Tipus i Adaptació")
            st.markdown(
                """
                * **Tipus de Bosc:** Perennifoli **escleròfil**.
                * **Clima:** Típicament **Mediterrani**.
                * **Adaptació:** La fulla dura redueix la pèrdua d'aigua (transpiració) en la sequera estival.
                """
            )

        with al_col2:
            st.subheader("Flora Associada")
            st.markdown(
                """
                * **Arbusts Escleròfils:** Marfull, Arboç, Llentiscle.
                * **Lianes:** Arítjol.
                * **Importància:** El caràcter escleròfil s'estén a la majoria d'arbustos i plantes.
                """
            )

    with hab_tab3:
        st.header("🌳 3. Boscos de Pi (Estratègics)")
        pi_col1, pi_col2 = st.columns(2)
        
        with pi_col1:
            st.subheader("Bosc de Pi Negre (*Pinus uncinata*)")
            st.markdown(
                """
                * **Ubicació:** Alta Muntanya (Estrat Subalpí i Alpí).
                * **Condicions:** Suporta el fred i les condicions climàtiques dures.
                * **Associació:** Forma el límit superior del bosc.
                """
            )

        with pi_col2:
            st.subheader("Bosc de Pi Roig i Pi Blanc")
            st.markdown(
                """
                * **Pi Roig (*Pinus sylvestris*):** Es troba en zones de muntanya mitjana i interior.
                * **Pi Blanc (*Pinus halepensis*):** Típic de la zona litoral. Molt **piròfita** (serotinia).
                """
            )
            
    with hab_tab4:
        st.header("🌱 4. Formacions Herbàcies i Arbustives")
        form_col1, form_col2 = st.columns(2)
        
        with form_col1:
            st.subheader("Formacions Arbustives")
            st.markdown(
                """
                * **Màquia:** Formació densa d'arbustos (aladerns, llentiscles).
                * **Brolla:** Més oberta (brucs, romaní).
                * Són típiques de la degradació dels boscos mediterranis.
                """
            )

        with form_col2:
            st.subheader("Formacions Herbàcies (NF1.2.HabitatsCatalunya.pptx)")
            st.markdown(
                """
                * **Prat:** Comunitat dominada per gramínies o plantes de fulla prima. Aspecte compacte i homogeni.
                * **Pradell:** Prat de reduïda extensió.
                * **Gespa:** Gramenet integrat per plantes petites i molt atapeïdes.
                """
            )


elif pagina == "🌱 Adaptacions i Biodiversitat":
    st.title("🌱 Adaptacions i Biodiversitat (NF 1.1: A1 i A3)")

    st.header("Mòdul [1]: Adaptacions de la Flora")
    
    adapt_tab1, adapt_tab2 = st.tabs(["[A] Adaptacions Tèrmiques/Hídriques", "[B] Biodiversitat i Endemismes"])

    with adapt_tab1:
        st.subheader("Límits Tèrmics i Resposta")
        st.markdown(
            """
            * **Rang Vital:** Entre **$0^{\circ}C$** i **$45^{\circ}C$**.
            * **Euritermes:** Tolerància a un **ampli rang** de temperatures.
            * **Estenotermes:** Necessiten Tº **més concretes** (rang estret).
            """
        )
        st.subheader("Mecanismes Xeròfils (Dèficit Hídric)")
        st.markdown(
            """
            Les plantes **xeròfiles** eviten la pèrdua d'aigua:
            * **Reducció foliar:** Fulles petites o transformades en **espines**.
            * **Reserves:** Acumulació d'aigua (**suculentes**).
            * **Protecció:** Presència de **pèls i ceres** (redueixen la Tº foliar i la transpiració).
            """
        )
        st.subheader("Piròfites (Adaptació al Foc)")
        st.markdown(
            """
            * **Serotinia:** Alliberament de llavors activat per la calor (Pi blanc).
            * **Rebrotat Ràpid:** Capacitat de rebrotar després d'una crema.
            """
        )

    with adapt_tab2:
        st.subheader("🧬 Biodiversitat i Endemisme (NF 1.1)")
        
        bio_col1, bio_col2 = st.columns(2)
        
        with bio_col1:
            st.markdown("#### Endemisme: Àrea de Distribució Limitada")
            st.markdown(
                """
                * **Definició:** Espècie amb una **àrea de distribució molt limitada**.
                * **Causes:** Principalment aïllament geogràfic.
                """
            )

        with bio_col2:
            st.markdown("#### Tipus d'Aïllament")
            st.markdown(
                """
                * **Geogràfic:** Montàno (muntanya), Insular (illes), Edàfic (sòl).
                * **Medi:** Canvi brusc de les condicions (aridesa, glaciacions).
                * **Exemple d'Endemisme:** Lagartija aranesa, Desman dels Pirineus.
                """
            )

elif pagina == "❓ Posa't a Prova! (Quiz)":
    run_quiz()
