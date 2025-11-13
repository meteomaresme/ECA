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
            "VERSION": "6.0.DENSITY",
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
            "INIT_CORE_SYSTEM (10%)": 0.10,
            "NF1.1_BIOMES_A1_A2 (15%)": 0.25,
            "NF1.1_CLIMOGRAM_ENGINE_A3 (15%)": 0.40,
            "NF1.2_HABITAT_PENINSULAR_A2 (15%)": 0.55,
            "NF1.2_HABITAT_CAT_A3_PART1 (15%)": 0.70,
            "NF1.3_PROTECTION_PROTOCOLS (15%)": 0.85,
            "NF1.1_BIODIVERSITY_ADAPTATIONS (14%)": 0.99
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
        /* La classe 1c7v0s correspon a st.columns / st.container / st.expander */
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
st.sidebar.title("🧬 Mòdul Bio-Explorador 6.0")
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
    if 'system_status' not in st.session_state or st.session_state.system_status == "INITIALIZING":
        run_boot_sequence()
    
    st.title("🤖 Terminal de Caracterització d'Hàbitats (UF1)")
    st.markdown("---")

    col_a, col_b = st.columns([2, 1])
    
    with col_a:
        st.header("🎯 Matriu d'Objectius (NF 1.1, 1.2, 1.3)")
        st.markdown(
            """
            Aquesta aplicació cobreix els coneixements mínims requerits per la Unitat Formativa 1:
            * **NF 1.1:** Biomes, Climogrames, Biodiversitat i Endemismes.
            * **NF 1.2:** Regions Biogeogràfiques i Hàbitats de Catalunya.
            * **NF 1.3:** Mecanismes de Protecció (CORINE, Xarxa Natura 2000).
            """
        )

        st.subheader(">> NF 1.1 (Biomes, Climogrames, Biodiversitat)")
        st.markdown(
            """
            * **A1, A2:** Classificació dels Biomes segons Tº i P. Definició de **Bioma** (conjunt de comunitats amb vegetació climàtica uniforme) i **Biodiversitat** (varietat d'éssers vius resultat de l'evolució).
            * **A3:** Interpretació de Climogrames (eixos de Tº i P, Regla de Gaussen). Distribució global dels biomes.
            """
        )
        
        st.subheader(">> NF 1.2 i 1.3 (Hàbitats Peninsulars i Protecció)")
        st.markdown(
            """
            * **A1, A2:** Anàlisi de regions biogeogràfiques (Eurosiberiana, Mediterrània, Macaronèsica i Alpina). Entendre el concepte de **Biotop** i **Hàbitat** (NF1.2.HabitatsaEspanya.pptx).
            * **A3:** Estudi detallat de l'ecologia de la Fageda, l'Alzinar i altres formacions clau a Catalunya (Boscos de Pi, Màquia, Brolla, Prats).
            * **NF 1.3:** Entendre la funció de **CORINE Biotopes** (classificació jeràrquica UE) i la **Xarxa Natura 2000** (ZEC i ZEPA).
            """
        )

    with col_b:
        st.header("📊 Estatus Operatiu")
        st.code(f"PROJECT_ID: {st.session_state.config.get('PROJECT_NAME')}")
        st.metric(label="Mòduls Carregats", value="7/7", delta="ONLINE", delta_color="normal")
        st.metric(label="Versió del Codi", value=st.session_state.config.get('VERSION', 'N/A'), delta="Estable (Alpha)", delta_color="normal")
        st.code(">>> STATUS: SYSTEM_ONLINE")
        st.warning("**ALERTA:** Mantenir els paràmetres tèrmics entre $0^{\circ}C$ i $45^{\circ}C$ per a l'activitat vegetativa.")

elif pagina == "🌍 Biomes de la Terra (NF 1.1)":
    st.title("🌍 Cartografia Global: Biomes de la Terra (NF 1.1: A1, A2)")
    st.markdown("Unitats de gran extensió amb una vegetació climàtica uniforme i clima característic.")

    with st.expander("Fitxa Tècnica: Bosc Escleròfil Mediterrani (Màxima Densitat)", expanded=True):
        
        tab_flora, tab_fauna, tab_clima = st.tabs(["[1] Detall Flora (NF1.1, p. 31)", "[2] Detall Fauna (NF1.1, p. 32)", "[3] Clima i Sòl"])
        
        with tab_flora:
            st.subheader("Vegetació Clau (Escleròfil·la i Perenne)")
            st.markdown(
                """
                La característica principal és la **vegetació escleròfil·la** (de fulla dura, perenne) per adaptar-se a l'aridesa estival.
                
                * **Arbres de fulla perenne (Escleròfils):** Alzines (*Quercus ilex*), Sureres, Garrofers, Oliveres. La densitat foliar és una adaptació crucial.
                * **Arbres Caducifolis (Secundaris):** Ametllers, Avellaners, Figueres, presents en menor mesura o en àrees menys àrides.
                """
            )
            st.subheader("Estratègia dels Estrats Inferiors (Gran Rellevància)")
            col_e1, col_e2 = st.columns(2)
            with col_e1:
                st.markdown("#### Estrat Arbustiu (Llista Densa):")
                st.markdown("* Galzeran")
                st.markdown("* Llentiscle")
                st.markdown("* Boix")
                st.markdown("* Brucs (diverses espècies)")
            with col_e2:
                st.markdown("#### Més Estrats Essencials:")
                st.markdown("* Estepes i Aladerns")
                st.markdown("* **Marfull** i **Arboç** (destacats, part de la barreja d'arbres)")
                st.markdown("* Estrats Herbaci i Lianoide (abundància de diverses espècies)")
                st.markdown("> **Clau:** La gran varietat d'arbustos i herbes és un tret distintiu (NF1.1, p. 31).")
            
        with tab_fauna:
            st.subheader("Fauna Clau per Nínxol Ecològic")
            fauna_col1, fauna_col2, fauna_col3 = st.columns(3)
            
            with fauna_col1:
                st.markdown("#### Herbívors Principals")
                st.markdown("* Cabirols")
                st.markdown("* Esquirols")
                st.markdown("* Llebres")
                st.markdown("* Cabres salvatges (en zones més muntanyoses)")
                
            with fauna_col2:
                st.markdown("#### Carnívors Terrestres")
                st.markdown("* Guineus")
                st.markdown("* Geneta (carnívor nocturn)")
                st.markdown("* **Linx Ibèric** (Carnívor Clau, el més amenaçat)")
                
            with fauna_col3:
                st.markdown("#### Omnívors i Rosegadors")
                st.markdown("* Porc senglar (gran impacte al sòl)")
                st.markdown("* Rata de camp")
                st.markdown("* Teixó")

        with tab_clima:
            st.subheader("Clima i Sòl (Estratègies del Bioma)")
            st.markdown(
                """
                * **Clima:** Mediterrani (estius secs i calorosos, hiverns suaus).
                * **Sòl:** Tendeix a ser **pobre en matèria orgànica** i té capacitat per absorbir ràpidament l'aigua de les pluges.
                * **Estratègia:** Les fulles escleròfil·les minimitzen la **transpiració** durant els mesos d'aridesa.
                """
            )


elif pagina == "📊 Climogrames i Distribució":
    st.title("📊 Anàlisi Gràfica Climàtica (NF 1.1: A3)")
    st.markdown("Eina per reconèixer si una zona és seca, humida, càlida o freda (NF1.1. Climogrames.pptx.pdf, p. 2).")

    st.header("Mòdul: Interpretació Tècnica dels Eixos")
    col_eix1, col_eix2 = st.columns(2)
    
    with col_eix1:
        st.subheader("Eix Horitzontal i Vertical Esquerre")
        st.code(">>> Eix H: Mesos de l'any (G-D)")
        st.code(">>> Eix V Esquerre: Temperatura (TºC)")
        st.markdown("* Representada per una línia vermella/taronja. La línia alta indica calor, la baixa, fred.")
    
    with col_eix2:
        st.subheader("Eix Vertical Dret i Relació")
        st.code(">>> Eix V Dret: Precipitació (P mm)")
        st.code(">>> CONDICIÓ VITAL: P >= 2 x T")
        st.markdown("* Representada per barres blaves. Barres molt altes = molta pluja.")
        st.markdown("* **Regla de Gaussen (Equilibri Hídric):** Si $P < 2 \times T$, el període és considerat d'aridesa/sequera (NF1.1. Climogrames.pptx.pdf).")
    
    st.markdown("---")
    st.header("Patrons Climàtics Extrems i Clau")
    
    patron_col1, patron_col2, patron_col3 = st.columns(3)
    
    with patron_col1:
        st.subheader("Patró Polar (Ex: Thule)")
        st.code(">>> Tº: Constantment < 0°C")
        st.markdown("La línia de Tº es manté sota el punt de congelació (NF1.1. Climogrames.pptx.pdf, p. 10). Pluja escassa, normalment en forma de neu.")
        
    with patron_col2:
        st.subheader("Patró Tropical (Ex: Selva)")
        st.code(">>> Tº: Constantment alta\n>>> P: Constantment alta")
        st.markdown("Sense períodes d'aridesa ni de fred. Condicions òptimes per a una biodiversitat extrema i gran desenvolupament vegetal.")
        
    with patron_col3:
        st.subheader("Patró Mediterrani")
        st.code(">>> Tº: Estius Alts\n>>> P: Hivern/Primavera")
        st.markdown("La característica clau és la **Sequera Estival**, on $T > P$. Això determina les adaptacions escleròfil·les de la flora (NF1.1.BiomesdelaTerra_A1A2.pdf).")


elif pagina == "🇪🇸 Hàbitats Peninsulars (NF 1.2)":
    st.title("🇪🇸 Regions Biogeogràfiques i Protecció (NF 1.2 & NF 1.3)")
    st.markdown("L'Espanya es divideix en 4 regions principals, cadascuna amb característiques pròpies (NF1.2.HabitatsaEspanya.pptx).")

    st.header("Mòdul NF 1.2: Regions Biogeogràfiques (A2)")
    
    reg_tab1, reg_tab2, reg_tab3, reg_tab4 = st.tabs(["[1] Eurosiberiana", "[2] Mediterrània", "[3] Macaronèsica", "[4] Alpina"])

    with reg_tab1:
        st.subheader("🟢 Regió Eurosiberiana (Espanya Humida)")
        st.markdown(
            """
            * **Localització:** Nord peninsular (Cornisa Cantàbrica, Galícia).
            * **Clima:** Temperat amb estius humits. Clima Oceànic, sense aridesa estival.
            * **Vegetació Dominant:** **Boscos Caducifolis** (Roures, Faigs). Predomini de la pèrdua de fulla a l'hivern per fred.
            """
        )

    with reg_tab2:
        st.subheader("🟠 Regió Mediterrània (Espanya Seca)")
        st.markdown(
            """
            * **Localització:** Major part del territori (Centre, Sud i Est).
            * **Clima:** Estius secs i calorosos.
            * **Vegetació Dominant:** **Boscos Perennifolis Escleròfils** (Alzinar, Surera, Pi). Adaptació al foc i la sequera.
            """
        )
    
    with reg_tab3:
        st.subheader("🌋 Regió Macaronèsica (Canàries)")
        st.markdown(
            """
            * **Particularitat:** Fort aïllament insular, que provoca una **taxa d'endemisme altíssima**.
            * **Flora Clau:** Laurissilva, Pi canari, Cardó.
            """
        )

    with reg_tab4:
        st.subheader("❄️ Regió Alpina (Alta Muntanya)")
        st.markdown(
            """
            * **Ubicació:** Zones d'alta altitud (Pirineus, Sierra Nevada).
            * **Condicions:** Fred intens, vent, baixa Tº (per sobre de la zona subalpina).
            * **Vegetació Clau:** Bosc Subalpí (Pi Negre) i Prats Alpins (per sobre del límit forestal).
            """
        )

    st.header("Mòdul NF 1.3: Protocols de Protecció (Densitat Alta)")
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.subheader("Classificació (CORINE Biotopes)")
        st.code(">>> NF1.1. Habitats. Classificació Corinne.pptx.pdf (p. 4)")
        st.markdown(
            """
            * **Objectiu:** Establir una classificació **jeràrquica** de tots els hàbitats (naturals, seminaturals i artificialitzats) a escala de la Unió Europea.
            * **Utilitat:** Permet ordenar i comparar la diversitat d'hàbitats a escala continental.
            """
        )

    with col_p2:
        st.subheader("Xarxa Natura 2000 (Directiva Hàbitats/Ocells)")
        st.code(">>> NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 16)")
        st.markdown(
            """
            Xarxa d'àrees de conservació europea.
            * **ZEC:** Zones Especials de Conservació. Creades per protegir hàbitats i espècies d'interès comunitari.
            * **ZEPA:** Zones d'Especial Protecció per a les Aus. Enfocades a la conservació d'espècies d'ocells.
            """
        )


elif pagina == "🏞️ Hàbitats de Catalunya (Detall)":
    st.title("🏞️ Fitxer d'Hàbitats Nacionals (NF 1.2: A3)")
    st.markdown("Anàlisi exhaustiva dels boscos i formacions de Catalunya, reflectint la seva alta diversitat geogràfica i climàtica (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 10).")
    
    hab_tab1, hab_tab2, hab_tab3 = st.tabs(["[1] Boscos Caducifolis/Escleròfils (Detall)", "[2] Boscos de Pi i Arbustives (Detall)", "[3] Formacions Herbàcies (Detall)"])

    with hab_tab1:
        st.header("🌳 1. La Fageda (*Fagus sylvatica*)")
        fag_col1, fag_col2 = st.columns(2)
        
        with fag_col1:
            st.subheader("Ecologia del Faig (NF1.2, p. 54)")
            st.markdown(
                """
                * **Arbre:** Faig (*Fagus sylvatica*). El bosc és força tancat.
                * **Clima:** **Medioeuropeu subatlàntic** (molta humitat).
                * **Substrat:** Terrenys **àcids** (o sòls acidificats); sòl poc profund.
                * **Ubicació:** Muntanya mitjana, típicament vessants obacs (NF1.2, p. 54).
                """
            )
        with fag_col2:
            st.subheader("Flora Associada (Sotabosc Pobre - NF1.2, p. 56)")
            st.markdown(
                """
                El sotabosc és pobre a causa de l'ombra.
                * **Estrat Arbustiu Clau:** Boix (*Buxus sempervirens*), Grèvol (*Ilex aquifolium*).
                * **Estrat Herbaci Clau:** Falguera comuna (*Pteridium aquilinum*), Bruguerola (*Calluna vulgaris*), Te de muntanya (*Veronica officinalis*).
                * **Altres:** *Deschampsia flexuosa*, *Calamagrostis arundinacea* (plantes acidòfiles).
                """
            )

        st.header("🌲 2. L'Alzinar (*Quercus ilex*)")
        al_col1, al_col2 = st.columns(2)
        
        with al_col1:
            st.subheader("Tipus i Adaptació Escleròfil·la")
            st.markdown(
                """
                * **Tipus:** Bosc perennifoli **escleròfil** mediterrani.
                * **Funció:** La fulla dura (escleròfil·la) redueix la pèrdua d'aigua (transpiració) en la sequera estival.
                * **Ubicació:** Zona Prelitoral i Central (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 10).
                """
            )

        with al_col2:
            st.subheader("Associació Arbustiva i Lianoide")
            st.markdown(
                """
                * **Arbusts Típics:** Marfull, Arboç, Llentiscle.
                * **Lianes Comuns:** Arítjol.
                * **Observació:** El caràcter escleròfil s'estén a la majoria d'arbustos del sotabosc.
                """
            )

    with hab_tab2:
        st.header("🌳 Boscos de Pi (Diversitat Ecològica)")
        pi_col1, pi_col2 = st.columns(2)
        
        with pi_col1:
            st.subheader("Boscos de l'Alta Muntanya")
            st.markdown(
                """
                * **Pi Negre (*Pinus uncinata*):** Típic de l'Alta Muntanya (Estrat Subalpí/Alpí). Resistent al fred extrem i als vents.
                * **Pi Roig (*Pinus sylvestris*):** Muntanya mitjana/interior.
                """
            )

        with pi_col2:
            st.subheader("Boscos del Litoral/Prelitoral")
            st.markdown(
                """
                * **Pi Blanc (*Pinus halepensis*):** Característic de la zona litoral. Fortament **piròfita** (Serotinia, obertura de pinyes per la calor).
                * **Suredes:** Boscos de Surera (Quercus suber), adaptats a sòls silícics i zones amb humitat atmosfèrica.
                """
            )
            st.subheader("Formacions Arbustives Derivades")
            st.markdown(
                """
                * **Màquia:** Formació densa d'arbustos (aladerns, llentiscles).
                * **Brolla:** Més oberta (brucs, romaní, estepes). **Origen:** Degradació dels boscos mediterranis.
                """
            )
            
    with hab_tab3:
        st.header("🌱 3. Formacions Herbàcies (Classificació Tècnica)")
        st.markdown("Classificació segons la seva estructura i densitat (NF1.2.HabitatsCatalunya.pptx, p. 54-55):")
        
        herb_col1, herb_col2 = st.columns(2)
        with herb_col1:
             st.subheader("Prat, Pradell, Gramenet")
             st.markdown("- **Prat:** Comunitat dominada per gramínies. Aspecte compacte i homogeni.")
             st.markdown("- **Pradell:** Prat de reduïda extensió o recobriment escàs (plantes menudes).")
             st.markdown("- **Gramenet:** Prats on predominen les gramínies o plantes graminoides.")
        with herb_col2:
             st.subheader("Gespa i Prats Clau")
             st.markdown("- **Gespa:** Gramenet integrat per plantes petites i molt atapeïdes.")
             st.markdown("- **Prats Alpins:** (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 10) Típics de la zona pirinenca, sobre el límit del bosc.")
             st.markdown("- **Prats Halòfils:** (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 10) Associats a zones litorals o salines.")


elif pagina == "🌱 Adaptacions i Biodiversitat":
    st.title("🌱 Adaptacions i Biodiversitat (NF 1.1)")
    st.markdown("Com les espècies s'ajusten al medi i quina n'és la distribució (NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf).")

    st.header("Mòdul [1]: Adaptacions de la Flora (Termo/Hídriques)")
    
    adapt_tab1, adapt_tab2, adapt_tab3 = st.tabs(["[A] Límits Tèrmics i Tº Freda", "[B] Adaptacions Hídriques (Xeròfiles)", "[C] Endemisme i Aïllament"])

    with adapt_tab1:
        st.subheader("Límits Tèrmics Crítics (NF1.1, p. 3)")
        st.code(">>> RANG OPTIM: 0°C a 45°C")
        st.markdown(
            """
            * **Límit Inferior (0°C):** Sota aquest punt, la planta paralitza l'activitat d'absorció i processament d'aigua (perill de congelació).
            * **Límit Superior (45°C):** Per sobre d'això, l'activitat vegetativa es paralitza.
            """
        )
        st.subheader("Estratègies per al Fred (NF1.1, p. 4)")
        st.markdown(
            """
            * **Morfologia:** Plantes petites i prop del terra (millor aprofitament de la calor del terra).
            * **Fisiologia:** Saba més espessa (ralentir la congelació). Fulles enfosquides (augmentar la insolació).
            * **Fenologia:** Creixement en èpoques favorables; manteniment latent a l'hivern (ex: *Betula Pendula*).
            """
        )

    with adapt_tab2:
        st.subheader("Mecanismes Xeròfils (Adaptació a la Sequera) - NF1.1, p. 5")
        st.markdown("Les plantes que eviten la pèrdua d'aigua s'anomenen **xeròfiles**:")
        xerofila_col1, xerofila_col2 = st.columns(2)
        
        with xerofila_col1:
             st.markdown("#### Tàctiques de Reducció:")
             st.markdown("* **Reducció foliar:** Fulles petites o transformades en **espines** (per reduir la superfície de transpiració).")
             st.markdown("* **Protecció:** Presència de pèls i ceres (redueixen la Tº foliar i el vent).")
             st.markdown("* **Fulles perennes:** Fulles verdes tot l'any (escleròfil·les, ex: *Olea europaea*).")
        
        with xerofila_col2:
             st.markdown("#### Tàctiques de Reserva/Captació:")
             st.markdown("* **Reserves:** Acumulació de l'aigua en els teixits (**suculentes**).")
             st.markdown("* **Arrels:** Arrels profundes i llargues (per captar aigua de capes inferiors del sòl).")
             st.markdown("* **Piròfites:** Serotinia (Pi blanc) i Rebrotat ràpid (NF1.1, p. 6).")

    with adapt_tab3:
        st.subheader("🧬 Endemisme: Àrea de Distribució Limitada")
        st.code(">>> L'endemisme és resultat de l'evolució i l'aïllament.")
        
        col_end1, col_end2 = st.columns(2)
        
        with col_end1:
            st.markdown("#### Causes de l'Aïllament (NF1.1, p. 11):")
            st.markdown(
                """
                1.  **Aïllament Geogràfic (Més Comú):** Montàno (muntanya), Insular (illes), Edàfic (sòl), Desèrtic.
                2.  **Aïllament Genètic:** Interrupció de la comunicació amb comunitats veïnes.
                """
            )

        with col_end2:
            st.markdown("#### Factors Ambientals:")
            st.markdown(
                """
                * **Canvi Brusc del Medi:** Glaciacions, augment de l'aridesa, variacions extremes de Tº i humitat.
                * **Exemples a la Península:** Endemismes montanos (Desman, Llagardaix aranès) i insulars (Canàries).
                """
            )

elif pagina == "❓ Posa't a Prova! (Quiz)":
    if 'system_status' not in st.session_state or st.session_state.system_status != "ONLINE":
        st.warning("El mòdul de Test requereix la inicialització completa del sistema.")
        st.info("Torna a la pàgina '🏠 Inici & Estat del Sistema' per començar la seqüència de boot.")
    else:
        run_quiz()
