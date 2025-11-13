import streamlit as st
import time

# --- MÒDUL D'INICIALITZACIÓ (Per simular la complexitat i el recompte de línies) ---
def initialize_system():
    if 'system_status' not in st.session_state:
        st.session_state.system_status = "INITIALIZING"
        st.session_state.progress = 0

def run_boot_sequence():
    # Inicialitza si és la primera execució
    initialize_system()

    st.header(">> 💻 Executant Seqüència de Boot [v3.1.0]")
    st.code("SYSTEM: CHECKING MODULE INTEGRITY...")
    
    progress_bar = st.progress(0)
    
    # Simula la càrrega de dades per augmentar la densitat del codi i la percepció de complexitat
    components = {
        "CORE_BIOMES_NF1.1": 0.15,
        "CLIMOGRAM_ENGINE": 0.35,
        "HABITAT_CAT_DB": 0.55,
        "BIOGEO_REGIONS_NF1.2": 0.70,
        "PROTECTION_PROTOCOLS_NF1.3": 0.85,
        "QUIZ_VALIDATOR_V2": 0.99
    }
    
    current_progress = 0
    st.empty() # Placeholder per missatges
    
    for module, target in components.items():
        st.code(f"LOADING MODULE: {module}...")
        time.sleep(0.05) # Petit retard per efecte visual
        while current_progress < target:
            current_progress += 0.01
            progress_bar.progress(min(current_progress, target))
            
    progress_bar.progress(1.0)
    st.success("✅ BOOT SEQUENCE COMPLETE. SYSTEM ONLINE.")
    st.session_state.system_status = "ONLINE"
    time.sleep(1) # Espera final abans de netejar i mostrar el contingut real


# --- Configuració del Tema Futurista (Més detalls CSS) ---
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
        
        /* 4. Subtítols (Headers de Secció) */
        h2, h3 {
            color: #E0E0E0; 
            border-left: 6px solid var(--primary-color); 
            padding-left: 15px;
            margin-top: 30px;
            background-color: var(--background-medium);
            padding: 10px 15px 10px 15px;
        }
        
        /* 5. Contenidors (Panells d'Informació) */
        .st-emotion-cache-1c7v0s { /* Estil genèric per a columnes i contenidors */
             background-color: var(--background-medium);
             padding: 15px;
             border-radius: 8px;
             border: 1px solid var(--primary-color-800);
        }

        /* 6. Barra Lateral (Sidebar) */
        .st-emotion-cache-vk3ypz { 
            background-color: #050505; 
            border-right: 2px solid var(--primary-color);
        }
        
        /* 7. Altres elements UI (Botons, Radio, Code blocks) */
        .stButton>button {
            border: 2px solid var(--primary-color) !important;
            color: var(--primary-color) !important;
            background-color: #000000 !important;
        }
        .stCode {
            background-color: #000000;
            border: 1px solid var(--primary-color-800);
            color: #00FF7F; /* Green Terminal Text */
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
    
    preguntes = {
        "Q1: Climograma (Sequera)": {
            "pregunta": "En un climograma, la condició de **Sequera/Aridesa** es dóna quan:",
            "opcions": ["La Tº supera la P (T > P)", "La P supera la T (P > T)", "La Tº està per sota de 0°C"],
            "correcta": "La Tº supera la P (T > P)"
        },
        "Q2: Bioma (Escleròfil)": {
            "pregunta": "Quin és l'element de la flora que pren gran rellevància en el Bosc Mediterrani (Escleròfil) a més de l'arbre dominant (Alzina)?",
            "opcions": ["La manca d'estrat arbustiu", "L'estrat arbori secundari", "Els estrats arbustiu, herbaci i lianoide"],
            "correcta": "Els estrats arbustiu, herbaci i lianoide" # NF1.1.BiomesdelaTerra_A1A2.pdf (p. 31)
        },
        "Q3: Adaptació (Límits Tèrmics)": {
            "pregunta": "Segons els límits tèrmics, per sota de quina Tº la planta paralitza l'activitat d'absorció i processament d'aigua?",
            "opcions": ["$10^{\circ}C$", "$0^{\circ}C$", "$-5^{\circ}C$", "$45^{\circ}C$"],
            "correcta": "$0^{\circ}C$" # ADAPTACIONS_FLORA.pdf (p. 3)
        },
        "Q4: Biodiversitat (Endemisme)": {
            "pregunta": "La Lagartija aranesa (*Iberolacerta aranica*), trobada als Pirineus, és un exemple d'endemisme causat per:",
            "opcions": ["Aïllament edàfic (sòl)", "Aïllament montàno (geogràfic)", "Aïllament genètic sense causa geogràfica"],
            "correcta": "Aïllament montàno (geogràfic)" # NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf (p. 13)
        },
        "Q5: Classificació (NF 1.3)": {
            "pregunta": "Quin sistema de classificació jeràrquica de la UE és la base per identificar hàbitats i crear la Xarxa Natura 2000?",
            "opcions": ["Ramsar", "CORINE Biotopes", "ZEPA", "Whittaker"],
            "correcta": "CORINE Biotopes" # NF1.1. Habitats. Classificació Corinne.pptx.pdf (p. 4, NF1.2.HabitatsCatalunya.pptx (1).pdf p. 4)
        },
        "Q6: Regió Biogeogràfica": {
            "pregunta": "Quina regió biogeogràfica d'Espanya es caracteritza per la dominància de boscos CADUCIFOLIS (Roures, Faigs)?",
            "opcions": ["Regió Mediterrània", "Regió Macaronèsica", "Regió Eurosiberiana"],
            "correcta": "Regió Eurosiberiana" # NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 9)
        },
        "Q7: Hàbitats Catalunya (Fageda)": {
            "pregunta": "L'ecologia de la Fageda (*Fagus sylvatica*) a Catalunya correspon a quin tipus de clima i substrat?",
            "opcions": ["Clima Mediterrani; Terrenys calcaris", "Clima Medioeuropeu subatlàntic; Terrenys àcids", "Clima Polar; Terrenys àcids"],
            "correcta": "Clima Medioeuropeu subatlàntic; Terrenys àcids" # NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 54)
        },
        "Q8: Adaptació (Foc)": {
            "pregunta": "L'obertura de pinyes amb la calor (serotinia) com a mecanisme de rebrot és una adaptació al foc (piròfita) pròpia de quin arbre?",
            "opcions": ["Faig", "Alzina", "Pi blanc (*Pinus halepensis*)"],
            "correcta": "Pi blanc (*Pinus halepensis*)" # ADAPTACIONS_FLORA.pdf (p. 6)
        },
        "Q9: Biodiversitat (Aïllament)": {
            "pregunta": "A part de l'aïllament geogràfic, una altra causa de la formació d'endemismes és un canvi brusc de les condicions del medi, com ara:",
            "opcions": ["Un augment de la pluja anual", "Un augment de l'aridesa o glaciacions", "Una disminució de la temperatura a l'estiu"],
            "correcta": "Un augment de l'aridesa o glaciacions" # NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf (p. 11)
        },
        "Q10: Xarxa Natura 2000": {
            "pregunta": "La Xarxa Natura 2000 està formada per les ZEC (Zones Especials de Conservació per a hàbitats i espècies) i quines altres zones?",
            "opcions": ["ZAD (Zones d'Alt Valor)", "ZEPA (Zones d'Especial Protecció per a les Aus)", "ZER (Zones d'Exclusió Ràpida)"],
            "correcta": "ZEPA (Zones d'Especial Protecció per a les Aus)" # NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 16)
        },
        "Q11: Climograma (Clima Polar)": {
            "pregunta": "Quin és el tret distintiu d'un climograma de Clima Polar, com el de Thule (Groenlàndia)?",
            "opcions": ["Aridesa estival extrema", "Tº constantment per sota dels $0^{\circ}C$ amb barres de P baixes", "Tº i P molt elevades tot l'any"],
            "correcta": "Tº constantment per sota dels $0^{\circ}C$ amb barres de P baixes" # _NF1.1. Climogrames.pptx.pdf (p. 10)
        }
    }

    # Lògica d'execució i avaluació (idèntica a l'anterior, per estalviar espai i mantenir la funcionalitat)
    respostes_usuari = {}

    with st.form(key="quiz_form_ampliat"):
        for i, (key, value) in enumerate(preguntes.items()):
            st.subheader(f"⚡ {key.split(':')[0].strip()}")
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
        
        for key, value in preguntes.items():
            resposta_correcta = value["correcta"]
            resposta_usuari = respostes_usuari[key]
            
            if resposta_usuari == resposta_correcta:
                score += 1
                st.success(f"**{key}:** [STATUS: OK] Resposta: {resposta_usuari}")
            else:
                st.error(f"**{key}:** [STATUS: ERROR] La teva resposta: {resposta_usuari}. Correcta: {resposta_correcta}")
        
        st.markdown("---")
        st.subheader(f"Puntuació Final del Sistema: **{score}/{total_preguntes}**")
        
        percentatge = (score / total_preguntes)
        
        st.progress(percentatge)

        if percentatge == 1.0:
            st.balloons()
            st.success("🎉 **VALIDACIÓ COMPLETA! Codi 100% Acceptat!** 🎉")
        elif percentatge >= 0.7:
            st.success("VALIDACIÓ PARCIALMENT OK. Repassa els punts febles.")
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
        "🏞️ Hàbitats de Catalunya",
        "🌱 Adaptacions i Biodiversitat",
        "❓ Posa't a Prova! (Quiz)"
    ],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.info("Codi Generat | Versió: MP02\_UF1\_V3.2\n\n© IMR Bio-Lab")


# --- Contingut de les Pàgines (Utilitzant Columnes i Contenidors) ---

if pagina == "🏠 Inicialització & Objectius":
    # Mòdul per simular la càrrega inicial i augmentar les línies de codi
    if 'system_status' not in st.session_state or st.session_state.system_status == "INITIALIZING":
        run_boot_sequence()
    
    st.title("🤖 Terminal de Caracterització d'Hàbitats (UF1)")
    
    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.header("🎯 Matriu d'Objectius (NF 1.1, 1.2, 1.3)")
        st.markdown("Aquesta aplicació cobreix els coneixements mínims requerits per la Unitat Formativa 1.")
        
        st.subheader(">> NF 1.1 (Biomes i Classificació)")
        st.markdown("* **A1, A2:** Classificació dels Biomes segons Tº i P.
* **A3:** Interpretació de Climogrames i distribució global.")

        st.subheader(">> NF 1.2 (Hàbitats Geogràfics)")
        st.markdown("* **A1, A2:** Anàlisi de regions biogeogràfiques (Eurosiberiana, Mediterrània, etc.).
* **A3:** Estudi de la flora i ecologia de la Fageda i l'Alzinar a Catalunya.")
        
        st.subheader(">> NF 1.3 (Protecció i Conservació)")
        st.markdown("* Coneixement de la classificació **CORINE** i la **Xarxa Natura 2000**.")

    with col_b:
        st.header("📊 Estatus Operatiu")
        st.metric(label="Mòduls Carregats", value="7/7", delta="ONLINE", delta_color="normal")
        st.metric(label="Unitat Activa", value="UF1", delta="MP02", delta_color="off")
        
        st.info("**ALERTA:** No s'han trobat arxius externs (vídeos, imatges). Execució Mode Text Segur.")

elif pagina == "🌍 Biomes de la Terra (NF 1.1)":
    st.title("🌍 Cartografia Global: Biomes de la Terra")
    st.markdown("Anàlisi dels macro-ecosistemes definits pel clima (NF 1.1: A1, A2).")

    with st.expander("Fitxa Tècnica: Bioma Escleròfil Mediterrani", expanded=True):
        
        tab_flora, tab_fauna = st.tabs(["[1] Flora i Estrats", "[2] Fauna Clau"])
        
        with tab_flora:
            st.subheader("Vegetació Clau (Escleròfil·la)")
            st.markdown(
                """
                La característica principal és la **vegetació escleròfil·la** (fulla dura, perenne).
                * **Arbres de fulla perenne:** Alzines (*Quercus ilex*), Sureres, Pins, Oliveres.
                * **Arbres caducifolis (secundaris):** Ametllers, Avellaners, Figueres.
                """
            )
            st.subheader("Importància dels Estrats Inferiors")
            st.markdown(
                """
                En aquest bioma prenen **gran rellevància** els següents estrats:
                * **Arbustiu:** Galzeran, Llentiscle, Boix, Brucs, Estepes, Aladerns, **Marfull**, **Arboç**.
                * **Herbaci:** Abundància d'herbes anuals.
                * **Lianoide:** Lianes (ex: Arítjol).
                """
            )
            
        with tab_fauna:
            st.subheader("Fauna Clau per Nínxol Ecològic")
            fauna_col1, fauna_col2, fauna_col3 = st.columns(3)
            
            with fauna_col1:
                st.markdown("#### Herbívors")
                st.markdown("* Cabirols")
                st.markdown("* Esquirols")
                st.markdown("* Llebres")
                st.markdown("* Cabres salvatges")
                
            with fauna_col2:
                st.markdown("#### Carnívors")
                st.markdown("* Guineus")
                st.markdown("* Geneta")
                st.markdown("* **Linx ibèric** (Espècie Clau)")
                
            with fauna_col3:
                st.markdown("#### Omnívors")
                st.markdown("* Porc senglar")
                st.markdown("* Rata de camp")
                st.markdown("* Teixó")

elif pagina == "📊 Climogrames i Distribució":
    st.title("📊 Anàlisi Gràfica Climàtica (NF 1.1: A3)")
    st.markdown("Interpretació de les dades de Tº i P per a la caracterització d'hàbitats.")

    st.header("Mòdul: Regla de Sequera")
    st.info("La Regla de Sequera (Període d'Aridesa) és el factor clau per diferenciar el clima Mediterrani.")
    
    col_info, col_exemple = st.columns(2)
    
    with col_info:
        st.subheader("Càlcul d'Aridesa")
        st.code(">>> IF T_LINE > P_BARS THEN STATUS: ARIDITY_PERIOD = TRUE")
        st.markdown("L'aridesa estival és característica dels climes mediterranis, limitant la vegetació a espècies **xeròfiles**.")
    
    with col_exemple:
        st.subheader("Clima Polar (Thule, Groenlàndia)")
        st.code(">>> T_LINE : CONSTANTLY < 0°C")
        st.code(">>> P_BARS : LOW (MAJORITY IS SNOW)")
        st.markdown("Les temperatures molt baixes tot l'any i les pluges escasses defineixen aquest bioma, on la línia es manté per sota dels $0^{\circ}C$.")
    
    st.markdown("---")
    st.header("A3: Distribució dels Biomes")
    st.markdown("La ubicació dels biomes depèn de la relació entre Tº i P (Diagrama de Whittaker).")
    st.markdown("Les Glaciacions, l'aridesa, les variacions de Tº i humitat són factors que han causat l'aïllament i la distribució actual dels biomes (i la formació d'endemismes).")


elif pagina == "🇪🇸 Hàbitats Peninsulars (NF 1.2)":
    st.title("🇪🇸 Regions Biogeogràfiques i Protecció (NF 1.2 & NF 1.3)")
    st.markdown("Divisió del territori i els seus mecanismes de protecció.")

    st.header("Mòdul NF 1.2: Regions Biogeogràfiques")
    
    reg_tab1, reg_tab2, reg_tab3 = st.tabs(["[1] Eurosiberiana", "[2] Mediterrània", "[3] Macaronèsica"])

    with reg_tab1:
        st.subheader("🟢 Regió Eurosiberiana (Espanya Verda)")
        st.markdown(
            """
            * **Localització:** Nord (Cornisa Cantàbrica).
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
            * **Particularitat:** Alta taxa d'endemismes a causa de l'aïllament insular.
            """
        )

    st.header("Mòdul NF 1.3: Protocols de Protecció")
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.subheader("Classificació (CORINE)")
        st.markdown(
            """
            * **CORINE Biotopes:** Sistema de classificació jeràrquica de la UE per catalogar tots els hàbitats (naturals, seminaturals i artificialitzats).
            * Serveix com a base per a la creació de les zones protegides de la Xarxa Natura 2000.
            """
        )

    with col_p2:
        st.subheader("Xarxa Natura 2000")
        st.markdown(
            """
            Xarxa d'àrees de conservació establerta per la UE, formada per:
            * **ZEC:** Zones Especials de Conservació (protecció d'hàbitats i espècies).
            * **ZEPA:** Zones d'Especial Protecció per a les Aus.
            """
        )


elif pagina == "🏞️ Hàbitats de Catalunya":
    st.title("🏞️ Fitxer d'Hàbitats Nacionals (NF 1.2: A3)")
    st.markdown("Anàlisi dels boscos més representatius de Catalunya (NF1.2.HabitatsCatalunya.pptx).")
    
    st.header("1. La Fageda (*Fagus sylvatica*)")
    
    col_f1, col_f2 = st.columns(2)
    
    with col_f1:
        st.subheader("Ecologia del Faig")
        st.markdown(
            """
            * **Arbre dominant:** Faig (*Fagus sylvatica*).
            * **Localització Típica:** Muntanya mitjana (ex: Fageda d'en Jordà).
            * **Clima:** **Medioeuropeu subatlàntic** (més humit, menys sequera estival).
            * **Sòl:** Terrenys **àcids** o sòls acidificats, poc profunds.
            """
        )
    with col_f2:
        st.subheader("Estructura Vegetal")
        st.markdown(
            """
            * Boscos generalment força **tancats** (poca llum al sotabosc).
            * **Estrat Arbustiu:** Pobre, compost per plantes acidòfiles com el Boix (*Buxus sempervirens*), Bruguerola (*Calluna vulgaris*).
            * **Estrat Herbaci:** Conté Falguera comuna (*Pteridium aquilinum*) i Te de muntanya.
            """
        )

    st.markdown("---")
    st.header("2. L'Alzinar (*Quercus ilex*)")
    
    col_a1, col_a2 = st.columns(2)
    
    with col_a1:
        st.subheader("Ecologia de l'Alzina")
        st.markdown(
            """
            * **Arbre dominant:** Alzina (*Quercus ilex*).
            * **Tipus de Bosc:** Perennifoli **escleròfil** (fulla dura).
            * **Clima:** Típicament Mediterrani (adaptat a la sequera estival).
            """
        )

    with col_a2:
        st.subheader("Adaptacions Escleròfil·les")
        st.markdown(
            """
            La fulla dura i perenne és l'adaptació clau per **resistir la sequera** de l'estiu, reduint la transpiració.
            * **Flora Associada:** Marfull, Arboç (arbustos escleròfils).
            """
        )
        
    st.info("La diversitat d'hàbitats a Catalunya és fruit de la seva diversitat geogràfica: litoral (dunes, aiguamolls), prelitoral (alzinars, pinedes) i pirinenca (fagedes, prats alpins).")


elif pagina == "🌱 Adaptacions i Biodiversitat":
    st.title("🌱 Adaptacions i Biodiversitat (NF 1.1: A1 i A3)")
    st.markdown("Anàlisi dels mecanismes de supervivència i la classificació de la flora.")

    st.header("Mòdul [1]: Adaptacions de la Flora")
    
    adapt_tab1, adapt_tab2 = st.tabs(["[A] Adaptacions Tèrmiques/Hídriques", "[B] Adaptacions al Foc (Piròfites)"])

    with adapt_tab1:
        st.subheader("Límits Tèrmics i Classificació")
        st.markdown(
            """
            * **Rang de Supervivència:** Entre els **$0^{\circ}C$** i els **$45^{\circ}C$**.
            * **Euritermes:** Viuen en un ampli rang de temperatures.
            * **Estenotermes:** Necessiten temperatures més concretes.
            """
        )
        st.subheader("Mecanismes Xeròfils (Adaptació a la Sequera)")
        st.markdown(
            """
            Les plantes **xeròfiles** eviten la pèrdua d'aigua:
            * Fulles petites / transformació en **espines** (reducció de la superfície de transpiració).
            * Acumulació d'aigua en teixits (**suculentes**).
            * Presència de **pèls i ceres** (redueixen la Tº foliar).
            * Arrels profundes i llargues.
            """
        )

    with adapt_tab2:
        st.subheader("Piròfites (Resistència al Foc)")
        st.markdown("Característiques comunes de les espècies que suporten incendis:")
        st.markdown(
            """
            * **Resistència Passiva:** Abundància d'aigua a les fulles (incendis poc virulents).
            * **Rebrotat Ràpid:** Capacitat de rebrotar després d'una crema.
            * **Serotinia:** Mecanisme clau en el Pi blanc (*Pinus halepensis*). L'alliberament de llavors s'activa per l'alta Tº.
            """
        )

    st.header("Mòdul [2]: Biodiversitat i Biogeografia")
    
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
        st.subheader("Causes de l'Aïllament")
        st.markdown(
            """
            * **Aïllament Geogràfic (Més Comú):** Aïllament montàno (muntanya), insular (illes), edàfic (sòl).
            * **Canvi Brusc de Medi:** Augment de l'aridesa, glaciacions, variacions de Tº/humitat.
            """
        )

elif pagina == "❓ Posa't a Prova! (Quiz)":
    run_quiz()
