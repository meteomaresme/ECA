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
            "VERSION": "7.0.FINAL_DENSITY",
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
    
    # 12 Preguntes extretes directament dels PDFs
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
st.sidebar.title("🧬 Mòdul Bio-Explorador 7.0")
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
    
    # Ús d'una sola columna per maximitzar l'espai textual
    
    st.header("🎯 Matriu d'Objectius (NF 1.1, 1.2, 1.3)")
    st.markdown(
        """
        Aquesta aplicació cobreix els coneixements mínims requerits per la Unitat Formativa 1:
        * **NF 1.1:** Biomes, Climogrames, Biodiversitat i Endemismes.
        * **NF 1.2:** Regions Biogeogràfiques i Hàbitats de Catalunya (A3).
        * **NF 1.3:** Mecanismes de Protecció (CORINE, Xarxa Natura 2000).
        """
    )

    col_nf1, col_nf2 = st.columns(2)
    
    with col_nf1:
        st.subheader(">> NF 1.1 (Biomes, Climogrames, Biodiversitat)")
        st.markdown(
            """
            * **A1, A2 (Biomes):** El **Bioma** és un conjunt de comunitats amb vegetació climàtica uniforme i clima característic (NF1.1.BiomesdelaTerra_A1A2.pdf, p. 3). La **Biodiversitat** és la varietat d'éssers vius resultat de l'evolució i l'acció humana (NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf, p. 3).
            * **A3 (Climogrames):** Anàlisi de la relació Tº/P. La **Sequera** es dóna quan $P < 2 \times T$.
            """
        )
        st.subheader(">> NF 1.3 (Protecció i Classificació)")
        st.markdown(
            """
            * **CORINE Biotopes:** Classificació **jeràrquica** europea per a hàbitats naturals, seminaturals i artificialitzats (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 4).
            * **Xarxa Natura 2000:** Xarxa d'àrees de conservació amb **ZEC** (Hàbitats/Espècies) i **ZEPA** (Aus).
            """
        )
    
    with col_nf2:
        st.subheader(">> NF 1.2 (Hàbitats Peninsulars i Catalunya)")
        st.markdown(
            """
            * **A2 (Regions):** Eurosiberiana (Caducifolis, sense sequera), Mediterrània (Escleròfils, sequera estival), Macaronèsica (Alt endemisme), Alpina (Fred intens, Pi Negre).
            * **A3 (Catalunya):** Estudi de l'ecologia del Faig (clima subatlàntic, sòl àcid) i l'Alzinar (escleròfil, fulla perenne).
            * **Definicions:** **Biotop** (territori amb condicions ambientals adequades) i **Hàbitat** (conjunt de biòtops, espai físic amb aliment, refugi i aigua).
            """
        )
        st.info("EXECUCIÓ OK. Concentració de dades a l'àrea d'informació.")

elif pagina == "🌍 Biomes de la Terra (NF 1.1)":
    st.title("🌍 Cartografia Global: Biomes de la Terra (NF 1.1: A1, A2)")
    st.markdown("Unitats de gran extensió amb una vegetació climàtica uniforme i clima característic (NF1.1.BiomesdelaTerra_A1A2.pdf, p. 3).")

    with st.expander("Fitxa Tècnica: Bosc Escleròfil Mediterrani (Densitat Màxima)", expanded=True):
        
        tab_flora, tab_fauna, tab_estrategia = st.tabs(["[1] Detall Flora i Estructura", "[2] Detall Fauna", "[3] Clima i Sòl Crític"])
        
        with tab_flora:
            st.subheader("Estratègia Escleròfil·la i Estructura Vegetal (NF1.1, p. 31)")
            
            col_f1, col_f2 = st.columns(2)
            
            with col_f1:
                st.markdown("#### Arbres Dominants i Estratègics:")
                st.markdown("* La vegetació és principalment **escleròfil·la** (fulla dura) i **perenne** per a resistir la sequera estival.")
                st.markdown("* **Perennes Clau:** Alzines (*Quercus ilex*), Sureres, Garrofers, Oliveres, Arboç.")
                st.markdown("* **Caducifolis Secundaris:** Ametllers, Avellaners, Figueres (presentació mixta).")
            
            with col_f2:
                st.markdown("#### Rellevància dels Estrats Inferiors (Densa Varietat):")
                st.markdown("* L'estrat **Arbustiu**, **Herbaci** i **Lianoide** prenen gran rellevància.")
                st.markdown("* **Arbustiu Específic:** Galzeran, Llentiscle, Boix, Brucs, Estepes, Aladerns, Marfull.")
                st.markdown("* Hi ha una **gran abundància** d'espècies d'arbustos i herbes (NF1.1, p. 31).")
            
        with tab_fauna:
            st.subheader("Fauna Clau per Nínxol Ecològic (NF1.1, p. 32)")
            
            fauna_col1, fauna_col2, fauna_col3 = st.columns(3)
            
            with fauna_col1:
                st.markdown("#### Herbívors Específics")
                st.markdown("* Cabirols, Esquirols (altres mamífers).")
                st.markdown("* Llebres, Cabres salvatges (en zones més muntanyoses i de difícil accés).")
                
            with fauna_col2:
                st.markdown("#### Carnívors Clau")
                st.markdown("* Guineus (generalitzats).")
                st.markdown("* Geneta (carnívor nocturn, important en el control de rosegadors).")
                st.markdown("* **Linx Ibèric** (el carnívor més representatiu i amenaçat del bioma mediterrani).")
                
            with fauna_col3:
                st.markdown("#### Omnívors i Rosegadors")
                st.markdown("* Porc senglar (amb gran impacte al sotabosc).")
                st.markdown("* Rata de camp.")
                st.markdown("* Teixó.")

        with tab_estrategia:
            st.subheader("Clima i Sòl (Determinants del Bioma)")
            st.markdown(
                """
                * **Clima:** Mediterrani (estius secs i calorosos, hiverns suaus).
                * **Factor Determinant:** La **sequera estival** (període d'aridesa) i les altes temperatures.
                * **Sòl:** Tendeix a ser **pobre en matèria orgànica** i amb capacitat per absorbir ràpidament l'aigua de les pluges (NF1.1, p. 33).
                * **Estratègia Hídrica:** La fulla dura redueix al mínim la **transpiració** foliar durant els mesos secs.
                """
            )
            st.code(">>> REQUISIT: Fulla dura i perenne = Adaptació a l'estrès hídric.")


elif pagina == "📊 Climogrames i Distribució":
    st.title("📊 Anàlisi Gràfica Climàtica (NF 1.1: A3)")
    st.markdown("Eina essencial per caracteritzar un bioma mitjançant la combinació de Tº i P (NF1.1. Climogrames.pptx.pdf, p. 2).")

    with st.expander("Detall Tècnic: Interpretació i Regles Crítiques", expanded=True):
        st.header("Mòdul: Regla de Gaussen i Eixos de Lectura")
        
        col_eix1, col_eix2 = st.columns(2)
        
        with col_eix1:
            st.subheader("Eixos i Variables (NF1.1, p. 2)")
            st.markdown("* **Eix Horitzontal:** Mesos de l'any (G-D).")
            st.markdown("* **Eix Vertical Esquerre:** **Temperatura** (Tº en $^\circ C$) - Línia vermella/taronja.")
            st.markdown("* **Eix Vertical Dret:** **Precipitació** (P en mm) - Barres blaves.")
        
        with col_eix2:
            st.subheader("Relació de Gaussen (Dèficit Hídric)")
            st.code(">>> CONDICIÓ VITAL: P >= 2 x T")
            st.markdown("* L'equilibri hídric és favorable quan la precipitació duplica la temperatura ($P \ge 2T$).")
            st.markdown("* La **Sequera o Aridesa** es dóna quan $T > P$ (la línia de Tº supera les barres de P).")
            st.markdown("* Aquesta sequera estival és el tret distintiu del clima **Mediterrani**.")
    
    st.markdown("---")
    st.header("A3: Patrons Climàtics Globals (NF1.1, p. 10)")
    
    patron_col1, patron_col2, patron_col3 = st.columns(3)
    
    with patron_col1:
        st.subheader("Patró Polar (Ex: Thule)")
        st.code(">>> Tº: Constantment < 0°C")
        st.markdown("* Les temperatures són **molt baixes** tot l'any.")
        st.markdown("* Pluges escasses (normalment en forma de neu).")
        st.markdown("* Condició: Línia de Tº sota els $0^{\circ}C$ tota l'anualitat. Bioma: Tundra.")
        
    with patron_col2:
        st.subheader("Patró Temperat Oceànic")
        st.code(">>> Tº: Suau (sense extrems)")
        st.markdown("* No hi ha sequera (es compleix $P \ge 2T$).")
        st.markdown("* Precipitació abundant i distribuïda tot l'any.")
        st.markdown("* Clima ideal per als **Boscos Caducifolis** (Regió Eurosiberiana).")
        
    with patron_col3:
        st.subheader("Patró Tropical/Equatorial (Selva)")
        st.code(">>> Tº: Constantment alta i P: Constantment alta.")
        st.markdown("* Sense períodes d'aridesa ni de fred (NF1.1. Climogrames.pptx.pdf).")
        st.markdown("* Aquest clima permet la màxima expressió de la vida i desenvolupament vegetal (Selva Tropical).")


elif pagina == "🇪🇸 Hàbitats Peninsulars (NF 1.2)":
    st.title("🇪🇸 Regions Biogeogràfiques i Protecció (NF 1.2 & NF 1.3)")
    st.markdown("La península es divideix en 4 regions principals, definides pels seus factors climàtics i biogeogràfics (NF1.2.HabitatsaEspanya.pptx).")

    with st.expander("Mòdul NF 1.2: Anàlisi Densa de Regions Biogeogràfiques (A2)", expanded=True):
        
        reg_tab1, reg_tab2, reg_tab3, reg_tab4 = st.tabs(["[1] Eurosiberiana", "[2] Mediterrània", "[3] Macaronèsica", "[4] Alpina"])

        with reg_tab1:
            st.subheader("🟢 Regió Eurosiberiana (Espanya Humida)")
            st.markdown(
                """
                * **Localització:** Nord peninsular (Cornisa Cantàbrica, Galícia).
                * **Clima:** Temperat, humit, **sense aridesa estival** (clima Oceànic).
                * **Vegetació Clau:** Dominància de **Boscos Caducifolis** (Roures, Faigs).
                * **Adaptació:** Pèrdua de fulla a l'hivern com a mecanisme de resistència al fred.
                """
            )

        with reg_tab2:
            st.subheader("🟠 Regió Mediterrània (Espanya Seca)")
            st.markdown(
                """
                * **Localització:** Major part del territori (Centre, Sud i Est).
                * **Clima:** Estius secs i calorosos. Sequera estival present.
                * **Vegetació Clau:** **Boscos Perennifolis Escleròfils** (Alzinar, Surera, Pi).
                * **Adaptació:** Vegetació adaptada a l'estrès hídric i al foc.
                """
            )
        
        with reg_tab3:
            st.subheader("🌋 Regió Macaronèsica (Canàries)")
            st.markdown(
                """
                * **Particularitat:** Aïllament insular, que genera un **altíssim nivell d'endemisme**.
                * **Flora Única:** Laurissilva (bosc subtropical humit), Pi canari.
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

    with st.expander("Mòdul NF 1.3: Classificació i Protecció (Detall Extens)", expanded=True):
        
        col_p1, col_p2 = st.columns(2)
        
        with col_p1:
            st.subheader("Classificació (CORINE Biotopes)")
            st.code(">>> NF1.1. Habitats. Classificació Corinne.pptx.pdf (p. 4)")
            st.markdown(
                """
                * **Base Legal:** Sistema jeràrquic estandarditzat per la Unió Europea.
                * **Abast:** Classifica la totalitat dels hàbitats de la UE: **naturals**, **seminaturals** i **artificialitzats**.
                * **Objectiu:** Permet ordenar, cartografiar i comparar la diversitat d'hàbitats a escala continental.
                """
            )

        with col_p2:
            st.subheader("Xarxa Natura 2000 (ZEC i ZEPA)")
            st.code(">>> NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 16)")
            st.markdown(
                """
                Xarxa d'àrees de conservació establerta per la UE (Directiva Hàbitats / Directiva Ocells).
                * **ZEC:** Zones Especials de Conservació. Creades per protegir **hàbitats i espècies d'interès comunitari**.
                * **ZEPA:** Zones d'Especial Protecció per a les Aus.
                * **Funció:** Contribuir a garantir la conservació de la biodiversitat mitjançant la gestió de les àrees més sensibles.
                """
            )


elif pagina == "🏞️ Hàbitats de Catalunya (Detall)":
    st.title("🏞️ Fitxer d'Hàbitats Nacionals (NF 1.2: A3)")
    st.markdown("La gran varietat geogràfica de Catalunya resulta en una elevada diversitat d'hàbitats (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 10).")
    
    hab_tab1, hab_tab2, hab_tab3 = st.tabs(["[1] Boscos Caducifolis/Escleròfils (Extens)", "[2] Boscos de Pi i Arbustives (Extens)", "[3] Formacions Herbàcies (Extens)"])

    with hab_tab1:
        st.header("🌳 1. La Fageda (*Fagus sylvatica*)")
        fag_col1, fag_col2 = st.columns(2)
        
        with fag_col1:
            st.subheader("Ecologia del Faig (Medioeuropeu Subatlàntic)")
            st.markdown(
                """
                * **Arbre Dominant:** Faig (*Fagus sylvatica*). El bosc és força tancat (poca llum al sotabosc).
                * **Clima:** **Medioeuropeu subatlàntic** (molta humitat).
                * **Substrat:** Terrenys **àcids** o sòls acidificats (NF1.2.HabitatsaEspanya.pptx (2).pdf, p. 54).
                * **Ubicació:** Muntanya mitjana, típicament en vessants obacs i inclinats (per evitar l'excessiva insolació).
                """
            )
        with fag_col2:
            st.subheader("Composició Detallada del Sotabosc (Pobre)")
            st.markdown(
                """
                El sotabosc és pobre a causa de la manca de llum. Està compost principalment per plantes **acidòfiles** (NF1.2, p. 54).
                * **Estrat Arbori:** *Fagus sylvatica* (Faig).
                * **Estrat Arbustiu Clau:** Boix (*Buxus sempervirens*), Grèvol (*Ilex aquifolium*).
                * **Estrat Herbaci (Detaill):** Bruguerola (*Calluna vulgaris*), Falguera comuna (*Pteridium aquilinum*), *Deschampsia flexuosa*, *Calamagrostis arundinacea*, Te de muntanya (*Veronica officinalis*).
                """
            )

        st.header("🌲 2. L'Alzinar (*Quercus ilex*)")
        al_col1, al_col2 = st.columns(2)
        
        with al_col1:
            st.subheader("Tipus Escleròfil·le i Rols")
            st.markdown(
                """
                * **Tipus:** Bosc perennifoli **escleròfil** mediterrani.
                * **Funció de la Fulla:** La duresa redueix la **transpiració**, essencial per a sobreviure a la sequera estival.
                * **Distribució a Catalunya:** Zona Prelitoral i Central (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 10).
                """
            )

        with al_col2:
            st.subheader("Flora de Sotabosc Mediterrani")
            st.markdown(
                """
                * **Arbusts Específics:** Marfull, Arboç, Llentiscle.
                * **Lianes Comunes:** Arítjol.
                * **Observació:** L'Alzinar és un **clímax** potencial del clima mediterrani.
                """
            )

    with hab_tab2:
        st.header("🌳 Boscos de Pi (Diversitat Ecològica)")
        pi_col1, pi_col2 = st.columns(2)
        
        with pi_col1:
            st.subheader("Boscos de l'Alta Muntanya/Interior")
            st.markdown(
                """
                * **Pi Negre (*Pinus uncinata*):** Alta Muntanya (Estrat Subalpí/Alpí). Resistent al fred extrem i als vents. Forma el límit superior del bosc.
                * **Pi Roig (*Pinus sylvestris*):** Muntanya mitjana/interior.
                """
            )

        with pi_col2:
            st.subheader("Boscos del Litoral i Formacions Arbustives")
            st.markdown(
                """
                * **Pi Blanc (*Pinus halepensis*):** Característic del litoral/prelitoral. Fortament **piròfita** (Serotinia, obertura de pinyes per la calor).
                * **Suredes:** Associades a sòls silícics.
                * **Màquia:** Formació arbustiva densa (degradació de l'alzinar).
                * **Brolla:** Formació arbustiva més oberta (brucs, romaní).
                """
            )
            
    with hab_tab3:
        st.header("🌱 3. Formacions Herbàcies (Classificació Tècnica i Ubicació)")
        st.markdown("Classificació segons la seva estructura i densitat (NF1.2.HabitatsCatalunya.pptx, p. 54-55):")
        
        herb_col1, herb_col2 = st.columns(2)
        with herb_col1:
             st.subheader("Definicions Específiques")
             st.markdown("- **Prat:** Comunitat dominada per gramínies. Aspecte compacte i homogeni.")
             st.markdown("- **Pradell:** Prat de **reduïda extensió** o recobriment escàs (plantes menudes).")
             st.markdown("- **Gramenet/Gespa:** Prats on predominen les gramínies; la gespa és un gramenet format per plantes petites i molt atapeïdes.")
        with herb_col2:
             st.subheader("Tipus de Prats Clau")
             st.markdown("- **Prats Alpins:** Típics de la zona pirinenca, sobre el límit del bosc (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 10).")
             st.markdown("- **Prats Halòfils:** Associats a zones litorals o salines (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 10).")
             st.markdown("- **Aiguamolls:** També llocs amb alta biodiversitat. (NF1.1. Habitats. Classificació Corinne.pptx.pdf, p. 10).")


elif pagina == "🌱 Adaptacions i Biodiversitat":
    st.title("🌱 Adaptacions i Biodiversitat (NF 1.1)")
    st.markdown("Estudi de les respostes dels éssers vius als factors ambientals extrems i la seva distribució (ADAPTACIONS_FLORA.pdf, NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf).")

    with st.expander("Mòdul [1]: Adaptacions Tèrmiques i Hídriques (Detall Exhaustiu)", expanded=True):
        
        adapt_tab1, adapt_tab2, adapt_tab3 = st.tabs(["[A] Límits Tèrmics Crítics", "[B] Adaptacions a la Sequera (Xeròfiles)", "[C] Adaptacions al Fred i al Foc"])

        with adapt_tab1:
            st.subheader("Límits de Supervivència (NF1.1, p. 3)")
            st.code(">>> RANG VITAL: 0°C a 45°C")
            st.markdown(
                """
                * **Punt de Congelació (0°C):** Sota aquesta Tº, la planta **paralitza** l'activitat d'absorció i processament de l'aigua. No pot moure ni gestionar l'aigua.
                * **Tº Alta (45°C):** Per sobre, l'activitat vegetativa també es paralitza.
                * **Classificació:** **Euritermes** (ample rang de Tº) vs. **Estenotermes** (necessiten Tº més concretes).
                """
            )
        
        with adapt_tab2:
            st.subheader("Mecanismes Xeròfils (Evitar Pèrdua d'Aigua) - NF1.1, p. 5")
            
            xerofila_col1, xerofila_col2 = st.columns(2)
            
            with xerofila_col1:
                 st.markdown("#### Tàctiques de Reducció de Transpiració:")
                 st.markdown("* **Fulles petites** o transformades en **espines** (per reduir al màxim la superfície exposada).")
                 st.markdown("* **Protecció:** Presència de pèls i ceres per reduir la Tº foliar i l'efecte del vent.")
                 st.markdown("* **Fulles perennes i dures** (escleròfil·les, ex: *Olea europaea*).")
            
            with xerofila_col2:
                 st.markdown("#### Tàctiques de Reserva/Captació:")
                 st.markdown("* **Acumulació d'aigua** en teixits (plantes **suculentes** o crasses).")
                 st.markdown("* **Arrels profundes i llargues** (per captar aigua de les capes més interiors del sòl).")

        with adapt_tab3:
            st.subheader("Estratègies per al Fred (NF1.1, p. 4) i el Foc (NF1.1, p. 6)")
            col_ad1, col_ad2 = st.columns(2)
            with col_ad1:
                st.markdown("#### Adaptacions al Fred:")
                st.markdown("* **Morfologia:** Plantes petites i prop del terra (millor aprofitament de la calor del sòl).")
                st.markdown("* **Fisiologia:** Saba més espessa (ralentir la congelació).")
                st.markdown("* **Fenologia:** Manteniment latent a l'hivern (ex: *Betula Pendula*).")
            with col_ad2:
                st.markdown("#### Adaptacions al Foc (Piròfites):")
                st.markdown("* **Resistència Passiva:** Abundància d'aigua a les fulles (evita que morin).")
                st.markdown("* **Rebrotat Ràpid:** Capacitat de les plantes de tornar a créixer després d'una crema. ")
                st.markdown("* **Serotinia:** Mecanisme clau del Pi blanc (*Pinus halepensis*) on l'alliberament de llavors s'activa per l'alta Tº del foc.")
            

    with st.expander("Mòdul [2]: Biodiversitat i Endemisme (Detall Exhaustiu)", expanded=True):
        st.header("🧬 Endemisme: Factors d'Aïllament (NF 1.1)")
        st.markdown("L'endemisme és una espècie amb una **àrea de distribució molt limitada**, resultat de l'evolució i l'aïllament.")
        
        col_end1, col_end2 = st.columns(2)
        
        with col_end1:
            st.subheader("Causes d'Aïllament Comunes (NF1.1, p. 11):")
            st.markdown(
                """
                1.  **Aïllament Geogràfic:** Més freqüent. Pot ser **Montàno** (muntanya, ex: Desman), **Insular** (illes, ex: Canàries), **Edàfic** (sòl) o **Desèrtic**.
                2.  **Aïllament Genètic:** Interrupció de la comunicació amb comunitats veïnes.
                """
            )

        with col_end2:
            st.subheader("Factors Ambientals i Exemples:")
            st.markdown(
                """
                * **Canvi Brusc del Medi:** Causes importants, com l'augment de l'aridesa, les glaciacions o variacions extremes de Tº i humitat.
                * **Exemples Clau:** Endemismes montanos (Desman dels Pirineus, Lagartija aranesa) i insulars (Canàries).
                * **Contrast:** **Cosmopolita** (espècie distribuïda per tot el món, ex: alguns ocells migradors).
                """
            )

elif pagina == "❓ Posa't a Prova! (Quiz)":
    if 'system_status' not in st.session_state or st.session_state.system_status != "ONLINE":
        st.warning("El mòdul de Test requereix la inicialització completa del sistema.")
        st.info("Torna a la pàgina '🏠 Inici & Estat del Sistema' per començar la seqüència de boot.")
    else:
        run_quiz()
