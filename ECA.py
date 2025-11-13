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
            "VERSION": "5.0.FINAL",
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
            "INIT_CORE_SYSTEM": 0.10,
            "CORE_BIOMES_NF1.1": 0.25,
            "CLIMOGRAM_ENGINE": 0.40,
            "HABITAT_CAT_DB_PART1": 0.55,
            "BIOGEO_REGIONS_NF1.2": 0.70,
            "PROTECTION_PROTOCOLS_NF1.3": 0.85,
            "QUIZ_VALIDATOR_V2": 0.99
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
        st.success(f"✅ BOOT SEQUENCE COMPLETE. SYSTEM ONLINE.")
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


# --- FUNCIÓ PRINCIPAL DEL QUIZ (Mantenim el Quiz per a densitat i funcionalitat) ---
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
            "pregunta": "Quin estrat vegetal, a més de l'arbre dominant (Alzina), pren gran rellevància en el Bosc Mediterrani Escleròfil?",
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
st.sidebar.title("🧬 Mòdul Bio-Explorador 5.0")
st.sidebar.markdown("Un recorregut digital per la vida a la Terra. (**MP 02: Medi Natural**)")

pagina = st.sidebar.radio(
    "🖥️ SELECCIÓ DE MÒDUL (UF 1):",
    [
        "🏠 Inici & Estat del Sistema",
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
st.sidebar.info(f"Codi Generat | Versió: {st.session_state.config.get('VERSION', 'N/A')}\n\n© IMR Bio-Lab")


# --- Contingut de les Pàgines ---

if pagina == "🏠 Inici & Estat del Sistema":
    # **CONDICIÓ CLAU:** Només executem el boot si no s'ha fet o si l'estat és inicialitzant
    if 'system_status' not in st.session_state or st.session_state.system_status == "INITIALIZING":
        run_boot_sequence()
    
    # Contingut de la pàgina principal un cop el sistema està ONLINE
    st.title("🤖 Terminal de Caracterització d'Hàbitats (UF1)")
    st.markdown("---")

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
        
        st.subheader(">> NF 1.2 i 1.3 (Hàbitats Peninsulars i Protecció)")
        st.markdown(
            """
            * **A1, A2:** Anàlisi de regions biogeogràfiques (Eurosiberiana, Mediterrània, Macaronèsica i Alpina).
            * **A3:** Estudi detallat de l'ecologia de la Fageda, l'Alzinar i altres formacions de Catalunya.
            * **NF 1.3:** Entendre la funció de CORINE Biotopes i la Xarxa Natura 2000 (ZEC i ZEPA).
            """
        )

    with col_b:
        st.header("📊 Estatus Operatiu")
        st.metric(label="Mòduls Carregats", value="7/7", delta="ONLINE", delta_color="normal")
        st.metric(label="Versió del Codi", value=st.session_state.config.get('VERSION', 'N/A'), delta="Estable", delta_color="normal")
        st.code(">>> STATUS: SYSTEM_ONLINE")
        st.info("EXECUCIÓ OK. Tots els mòduls de dades de la UF1 estan disponibles per a la consulta.")

elif pagina == "🌍 Biomes de la Terra (NF 1.1)":
    st.title("🌍 Cartografia Global: Biomes de la Terra")
    st.markdown("Unitats de gran extensió amb una vegetació climàtica uniforme (NF 1.1: A1, A2).")

    with st.expander("Detall del Bioma: Bosc Escleròfil Mediterrani", expanded=True):
        
        tab_flora, tab_fauna, tab_estrategia = st.tabs(["[1] Detall Flora", "[2] Detall Fauna", "[3] Característiques del Sòl"])
        
        with tab_flora:
            st.subheader("Vegetació Clau (Escleròfil·la)")
            st.markdown(
                """
                La característica principal és la **vegetació escleròfil·la** (de fulla dura i perenne), adaptada a la sequera estival (NF1.1.BiomesdelaTerra_A1A2.pdf, p. 31).
                
                * **Arbres de fulla perenne:** Alzines (*Quercus ilex*), Sureres, Pins, Oliveres, Garrofers.
                * **Arbres Caducifolis (Secundaris):** Ametllers, Avellaners, Figueres.
                """
            )
            st.subheader("Gran Rellevància dels Estrats Inferiors (NF1.1, p. 31)")
            col_e1, col_e2 = st.columns(2)
            with col_e1:
                st.markdown("#### Estrat Arbustiu Clau:")
                st.markdown("* Galzeran")
                st.markdown("* Llentiscle")
                st.markdown("* Boix")
                st.markdown("* Brucs")
            with col_e2:
                st.markdown("#### Més Estrats:")
                st.markdown("* Estepes i Aladerns")
                st.markdown("* **Marfull** i **Arboç** (destacats)")
                st.markdown("* Estrats Herbaci i Lianoide (abundants en espècies)")
            
        with tab_fauna:
            st.subheader("Fauna Clau i Nínxol Ecològic (NF1.1, p. 32)")
            fauna_col1, fauna_col2, fauna_col3 = st.columns(3)
            
            with fauna_col1:
                st.markdown("#### Herbívors Principals")
                st.markdown("* Cabirols")
                st.markdown("* Esquirols")
                st.markdown("* Llebres")
                st.markdown("* Cabres salvatges")
                
            with fauna_col2:
                st.markdown("#### Carnívors Específics")
                st.markdown("* Guineus")
                st.markdown("* Geneta")
                st.markdown("* **Linx ibèric** (Carnívor Mediterrani Clau)")
                
            with fauna_col3:
                st.markdown("#### Omnívors i Rosegadors")
                st.markdown("* Porc senglar")
                st.markdown("* Rata de camp")
                st.markdown("* Teixó")

        with tab_estrategia:
            st.subheader("Estratègies del Sòl i Hídriques")
            st.markdown("Els sòls tendeixen a ser pobres. La flora té arrels profundes o adaptacions per retenir aigua i suportar la sequera estival (límits tèrmics: $0^{\circ}C$ - $45^{\circ}C$).")


elif pagina == "📊 Climogrames i Distribució":
    st.title("📊 Anàlisi Gràfica Climàtica (NF 1.1: A3)")
    st.markdown("Interpretació dels patrons de Tº i P per a la caracterització de biomes (NF1.1. Climogrames.pptx.pdf).")

    st.header("Mòdul: Regla de Sequera de Gaussen")
    col_info, col_arid = st.columns(2)
    
    with col_info:
        st.subheader("Interpretació dels Eixos")
        st.code(">>> Eix Esquerre: Temperatura (TºC)\n>>> Eix Dret: Precipitació (P mm)")
        st.markdown("La P (en mm) ha de ser el doble de la T (en ºC) per mantenir l'equilibri hídric favorable.")
    
    with col_arid:
        st.subheader("Determinació de Sequera (Període Arid)")
        st.code(">>> CONDICIÓ: T_LINE > P_BARS")
        st.markdown("Aquesta condició (la línia de Tº supera les barres de P) és l'indicador inequívoc de l'**aridesa estival** característica del clima Mediterrani.")
    
    st.markdown("---")
    st.header("A3: Patrons Climàtics Extrems")
    
    patron_col1, patron_col2 = st.columns(2)
    
    with patron_col1:
        st.subheader("Patró Polar (Ex: Thule)")
        st.code(">>> Tº: Constantment < 0°C")
        st.markdown("La línia de Tº es manté sota el punt de congelació (NF1.1. Climogrames.pptx.pdf, p. 10). La vida vegetal està severament limitada (Tundra).")
        
    with patron_col2:
        st.subheader("Patró Temperat Oceànic")
        st.code(">>> Tº: Suau (sense extrems)\n>>> P: Abundant i distribuïda tot l'any")
        st.markdown("Sense període d'aridesa. Clima ideal per als **Boscos Caducifolis** (Regió Eurosiberiana).")


elif pagina == "🇪🇸 Hàbitats Peninsulars (NF 1.2)":
    st.title("🇪🇸 Regions Biogeogràfiques i Protecció (NF 1.2 & NF 1.3)")

    st.header("Mòdul NF 1.2: Regions Biogeogràfiques (NF 1.2: A2)")
    
    reg_tab1, reg_tab2, reg_tab3, reg_tab4 = st.tabs(["[1] Eurosiberiana", "[2] Mediterrània", "[3] Macaronèsica", "[4] Alpina"])

    with reg_tab1:
        st.subheader("🟢 Regió Eurosiberiana (Espanya Humida)")
        st.markdown(
            """
            * **Localització:** Nord (Cornisa Cantàbrica, Galícia).
            * **Clima:** Temperat amb estius humits (sense sequera).
            * **Vegetació Dominant:** **Boscos Caducifolis** (Roures, Faigs).
            """
        )

    with reg_tab2:
        st.subheader("🟠 Regió Mediterrània (Espanya Seca)")
        st.markdown(
            """
            * **Localització:** Centre, Sud i Est peninsular.
            * **Vegetació Dominant:** **Boscos Perennifolis Escleròfils** (Alzinar, Surera).
            """
        )
    
    with reg_tab3:
        st.subheader("🌋 Regió Macaronèsica (Canàries)")
        st.markdown(
            """
            * **Endemisme:** Alta taxa d'endemismes per aïllament insular.
            * **Flora Clau:** Laurissilva, Pi canari.
            """
        )

    with reg_tab4:
        st.subheader("❄️ Regió Alpina (Pirineus, Sierra Nevada)")
        st.markdown(
            """
            * **Característiques:** Fred intens, altitud.
            * **Vegetació Clau:** Bosc Subalpí (Pi Negre) i Prats Alpins.
            """
        )

    st.header("Mòdul NF 1.3: Protocols de Protecció")
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.subheader("Classificació (CORINE Biotopes)")
        st.markdown(
            """
            * **Base UE:** El sistema jeràrquic més utilitzat per catalogar hàbitats (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 4).
            * **Abast:** Inclou hàbitats naturals, seminaturals i artificialitzats.
            """
        )

    with col_p2:
        st.subheader("Xarxa Natura 2000 (ZEC i ZEPA)")
        st.markdown(
            """
            Xarxa d'àrees de conservació establerta per la UE (NF1.2.HabitatsaEspanya.pptx (2).pdf, p. 16).
            * **ZEC:** Zones Especials de Conservació (protecció d'hàbitats i espècies).
            * **ZEPA:** Zones d'Especial Protecció per a les Aus.
            """
        )


elif pagina == "🏞️ Hàbitats de Catalunya (Detall)":
    st.title("🏞️ Fitxer d'Hàbitats Nacionals (NF 1.2: A3)")
    st.markdown("Anàlisi exhaustiva dels boscos i formacions de Catalunya (NF1.2.HabitatsCatalunya.pptx).")
    
    hab_tab1, hab_tab2, hab_tab3 = st.tabs(["[1] Boscos Caducifolis/Escleròfils", "[2] Boscos de Pi i Arbustives", "[3] Formacions Herbàcies (Detall)"])

    with hab_tab1:
        st.header("🌳 1. La Fageda (*Fagus sylvatica*)")
        fag_col1, fag_col2 = st.columns(2)
        
        with fag_col1:
            st.subheader("Ecologia del Faig (NF1.2, p. 54)")
            st.markdown(
                """
                * **Clima:** **Medioeuropeu subatlàntic** (molta humitat).
                * **Substrat:** Terrenys **àcids** (o sòls acidificats).
                * **Estructura:** Boscos generalment força tancats (poca llum).
                """
            )
        with fag_col2:
            st.subheader("Flora de Sotabosc (NF1.2, p. 56)")
            st.markdown(
                """
                * **Arbustiu:** Boix (*Buxus sempervirens*), Grèvol (*Ilex aquifolium*).
                * **Herbaci:** Falguera comuna (*Pteridium aquilinum*), Bruguerola (*Calluna vulgaris*), Te de muntanya (*Veronica officinalis*).
                """
            )

        st.header("🌲 2. L'Alzinar (*Quercus ilex*)")
        al_col1, al_col2 = st.columns(2)
        
        with al_col1:
            st.subheader("Tipus i Adaptació Escleròfil·la")
            st.markdown(
                """
                * **Tipus:** Bosc perennifoli **escleròfil** mediterrani.
                * **Funció:** Fulla dura per resistir la sequera estival (reducció de la transpiració).
                """
            )

        with al_col2:
            st.subheader("Associació Arbustiva (NF1.1, p. 31)")
            st.markdown(
                """
                * **Arbusts:** Marfull, Arboç, Llentiscle.
                * **Lianes:** Arítjol.
                """
            )

    with hab_tab2:
        st.header("🌳 Boscos de Pi i Formacions Arbustives")
        pi_col1, pi_col2 = st.columns(2)
        
        with pi_col1:
            st.subheader("Boscos de Pi Clau (NF1.2, p. 3)")
            st.markdown(
                """
                * **Pi Negre (*Pinus uncinata*):** Alta Muntanya (Estrat Subalpí/Alpí). Resistent al fred.
                * **Pi Blanc (*Pinus halepensis*):** Litoral/Prelitoral. Fortament **piròfita** (Serotinia).
                * **Pi Roig (*Pinus sylvestris*):** Muntanya mitjana/interior.
                """
            )

        with pi_col2:
            st.subheader("Formacions Arbustives (NF1.2, p. 3)")
            st.markdown(
                """
                * **Màquia:** Formació densa d'arbustos (aladerns, llentiscles).
                * **Brolla:** Més oberta (brucs, romaní, estepes).
                * **Origen:** Són formacions típiques de la degradació dels alzinars.
                """
            )
            
    with hab_tab3:
        st.header("🌱 3. Formacions Herbàcies (Detall NF1.2, p. 54-55)")
        st.markdown("Classificació segons la seva estructura i extensió:")
        
        herb_col1, herb_col2, herb_col3 = st.columns(3)
        with herb_col1:
             st.subheader("Prat")
             st.markdown("- Comunitat dominada per gramínies.")
             st.markdown("- Aspecte compacte i homogeni.")
        with herb_col2:
             st.subheader("Pradell")
             st.markdown("- Prat de **reduïda extensió**.")
             st.markdown("- Recobriment escàs.")
        with herb_col3:
             st.subheader("Gespa/Gramenet")
             st.markdown("- Predominen les gramínies.")
             st.markdown("- Format per plantes petites i molt atapeïdes.")


elif pagina == "🌱 Adaptacions i Biodiversitat":
    st.title("🌱 Adaptacions i Biodiversitat (NF 1.1)")

    st.header("Mòdul [1]: Adaptacions de la Flora (Termo/Hídriques)")
    
    adapt_tab1, adapt_tab2, adapt_tab3 = st.tabs(["[A] Límits Tèrmics", "[B] Adaptacions Hídriques (Xeròfiles)", "[C] Adaptacions al Foc"])

    with adapt_tab1:
        st.subheader("Límits de Supervivència (NF1.1, p. 3)")
        st.markdown(
            """
            * **Rang Vital:** Les plantes poden sobreviure entre els **$0^{\circ}C$** i els **$45^{\circ}C$**.
            * **Punt Crític:** Per sota de $0^{\circ}C$, es paralitza l'activitat d'absorció i processament de l'aigua.
            """
        )
        st.subheader("Classificació Tèrmica")
        st.markdown(
            """
            * **Euritermes:** Tolerància a un **ampli rang** de temperatures.
            * **Estenotermes:** Necessiten Tº **més concretes** (rang estret).
            """
        )

    with adapt_tab2:
        st.subheader("Mecanismes Xeròfils (Adaptació a la Sequera) - NF1.1, p. 5")
        xerofila_col1, xerofila_col2 = st.columns(2)
        
        with xerofila_col1:
             st.markdown("#### Reducció de Transpiració:")
             st.markdown("* Fulles petites (o transformades en espines).")
             st.markdown("* Presència de pèls i ceres (redueixen la Tº foliar).")
             st.markdown("* Fulles perennes (escleròfiles).")
        
        with xerofila_col2:
             st.markdown("#### Reserva i Captació:")
             st.markdown("* Acumulació d'aigua en teixits (**suculentes**).")
             st.markdown("* Arrels profundes i llargues.")
             st.markdown("* Fulles enfosquides per augmentar la insolació (fred).")

    with adapt_tab3:
        st.subheader("Piròfites (Resistència al Foc) - NF1.1, p. 6")
        st.markdown(
            """
            * **Resistència Passiva:** Abundància d'aigua a les fulles.
            * **Rebrotat Ràpid:** Capacitat de rebrotar després d'una crema.
            * **Serotinia:** Mecanisme clau en el Pi blanc (*Pinus halepensis*). L'alliberament de llavors s'activa per l'alta Tº.
            """
        )

    st.header("Mòdul [2]: Biodiversitat i Endemisme (NF 1.1)")
    
    col_bio1, col_bio2 = st.columns(2)
    
    with col_bio1:
        st.subheader("Definició de l'Endemisme")
        st.markdown(
            """
            Espècie amb una **àrea de distribució molt limitada**.
            * **Exemples:** Desman dels Pirineus (*Galemys pyrenaicus*), Lagartija aranesa (*Iberolacerta aranica*).
            """
        )

    with col_bio2:
        st.subheader("Causes de l'Aïllament (NF1.1, p. 11)")
        st.markdown(
            """
            * **Geogràfic:** Montàno (muntanya), Insular (illes), Edàfic (sòl).
            * **Genètic:** Interrupció de la comunicació amb comunitats veïnes.
            * **Medi:** Canvi brusc de les condicions (aridesa, glaciacions).
            """
        )

elif pagina == "❓ Posa't a Prova! (Quiz)":
    # **CONDICIÓ CLAU:** Si el sistema no ha passat el boot, el redirigim
    if 'system_status' not in st.session_state or st.session_state.system_status != "ONLINE":
        st.warning("El mòdul de Test requereix la inicialització completa del sistema.")
        st.info("Torna a la pàgina '🏠 Inici & Estat del Sistema' per començar la seqüència de boot.")
    else:
        run_quiz()
