import streamlit as st

# --- Configuració del Tema Futurista amb CSS Injectat ---
def inject_futuristic_style():
    st.markdown(
        """
        <style>
        /* 1. Definició del Color Primari (Neó Cyan) */
        :root {
            --primary-color: #00FFFF; /* Vibrant Cyan */
            --primary-color-800: #00CCCC;
        }

        /* 2. Estil de Títols (Títol principal amb "Glow") */
        h1 {
            color: var(--primary-color); 
            text-shadow: 0 0 5px rgba(0, 255, 255, 0.5); 
            font-family: 'Consolas', 'Courier New', monospace; 
            border-bottom: 2px solid var(--primary-color-800);
            padding-bottom: 5px;
        }
        
        /* 3. Subtítols i Headings (Línia d'accent) */
        h2, h3, h4, h5, h6 {
            color: #E0E0E0; 
            border-left: 5px solid var(--primary-color); 
            padding-left: 10px;
            margin-top: 20px;
        }

        /* 4. Estil de la Barra Lateral (Sidebar) */
        .st-emotion-cache-vk3ypz { 
            background-color: #1A1A1A; 
            border-right: 1px solid var(--primary-color-800);
        }
        
        /* 5. Estil dels Missatges i Alertes */
        .stSuccess {
            background-color: rgba(0, 255, 0, 0.1); 
            border-left: 5px solid #00FF00;
        }
        .stError {
            background-color: rgba(255, 0, 0, 0.1); 
            border-left: 5px solid #FF0000;
        }
        .stInfo {
            border-left: 5px solid var(--primary-color);
        }
        
        /* 6. Estil dels Ràdios (Opcions del Quiz) */
        .stRadio div[role="radiogroup"] label span {
             color: var(--primary-color); 
        }

        </style>
        """,
        unsafe_allow_html=True
    )

# --- Configuració de la Pàgina ---
st.set_page_config(
    page_title="Explora Hàbitats i Biomes | UF1",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Injectar l'estil personalitzat
inject_futuristic_style()

# --- Funció per al Quiz (Lògica de Test Ampliada amb dades dels PDFs) ---
def run_quiz():
    st.header("❓ Posa't a Prova! (Terminal de Test)")
    st.markdown("---")
    st.info("🟢 **EXECUTANT TEST DE VALIDACIÓ DE CONEIXEMENTS...**")
    
    # Preguntes extretes directament dels PDFs
    preguntes = {
        "Q1: Climograma": {
            "pregunta": "En un climograma, quina situació representa un **Període d'Aridesa (Sequera)**?",
            "opcions": ["La línia de Tº està per sota de la barra de P.", "La línia de Tº supera la barra de P. (T > P).", "Les barres de P. estan constantment per sobre dels 100 mm."],
            "correcta": "La línia de Tº supera la barra de P. (T > P)."
        },
        "Q2: Bioma (Fauna Mediterrània)": {
            "pregunta": "Quin d'aquests animals és un carnívor típic de la fauna del **Bosc Mediterrani Escleròfil**?",
            "opcions": ["Esquirol", "Cabirol", "Linx ibèric", "Rata de camp"],
            "correcta": "Linx ibèric" # NF1.1.BiomesdelaTerra_A1A2.pdf (p. 32)
        },
        "Q3: Adaptació (Sequera)": {
            "pregunta": "Les plantes amb fulles dures i petites, fulla perenne i que redueixen la transpiració s'anomenen **xeròfiles** i són adaptades a...",
            "opcions": ["La manca de llum", "El fred intens", "La sequera", "Les inundacions"],
            "correcta": "La sequera" # ADAPTACIONS_FLORA.pdf (p. 5)
        },
        "Q4: Biodiversitat": {
            "pregunta": "Una espècie amb una **àrea de distribució molt limitada**, sovint causada per aïllament geogràfic (insular o montàno), s'anomena:",
            "opcions": ["Espècie invasora", "Cosmopolita", "Endemisme", "Hotspot"],
            "correcta": "Endemisme" # NF1.1. Biodiversidad, endemismes i biogeografia.pptx.pdf (p. 11, 13)
        },
        "Q5: Protecció d'Hàbitats": {
            "pregunta": "Quin sistema de classificació jeràrquica s'utilitza a la UE com a base per a identificar hàbitats i la Xarxa Natura 2000?",
            "opcions": ["Ramsar", "CORINE Biotopes", "Whittaker", "ZEPA"],
            "correcta": "CORINE Biotopes" # NF1.1. Habitats. Classificació Corinne.pptx.pdf (p. 4)
        },
        "Q6: Límits Tèrmics": {
            "pregunta": "Segons els materials d'adaptacions, per sota de quina temperatura la planta **no té opcions** d'absorbir aigua, eliminar-la o processar-la eficaçment?",
            "opcions": ["$10^{\circ}C$", "$45^{\circ}C$", "$0^{\circ}C$", "$-5^{\circ}C$"],
            "correcta": "$0^{\circ}C$" # ADAPTACIONS_FLORA.pdf (p. 3)
        },
        "Q7: Hàbitats Catalunya (Fageda)": {
            "pregunta": "Quin és l'arbre dominant d'una Fageda i en quina mena de clima es troba típicament?",
            "opcions": ["El Faig; Clima Medioeuropeu subatlàntic", "L'Alzina; Clima Mediterrani", "El Roure; Clima Eurosiberià"],
            "correcta": "El Faig; Clima Medioeuropeu subatlàntic" # NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 54, 56)
        },
        "Q8: Bosc Mediterrani (Flora)": {
            "pregunta": "A part de l'alzina, quin tipus d'estrat (flora) pren una gran rellevància en el Bosc Mediterrani escleròfil?",
            "opcions": ["L'estrat arbori secundari", "Els estrats arbustiu, herbaci i lianoide", "Només l'estrat herbaci"],
            "correcta": "Els estrats arbustiu, herbaci i lianoide" # NF1.1.BiomesdelaTerra_A1A2.pdf (p. 31)
        },
        "Q9: Hàbitats Espanya": {
            "pregunta": "Quina regió biogeogràfica es caracteritza pels Boscos Caducifolis (roures i faigs) i els estius humits?",
            "opcions": ["Regió Mediterrània", "Regió Eurosiberiana", "Regió Macaronèsica"],
            "correcta": "Regió Eurosiberiana" # NF1.2.HabitatsaEspanya.pptx (2).pdf (p. 9)
        },
        "Q10: Adaptació (Foc)": {
            "pregunta": "La capacitat d'obrir les pinyes per alliberar llavors (serotinia) amb la calor és una adaptació al foc (piròfita) que es troba al:",
            "opcions": ["Pi blanc (*Pinus halepensis*)", "Faig (*Fagus sylvatica*)", "Alzina (*Quercus ilex*)"],
            "correcta": "Pi blanc (*Pinus halepensis*)" # ADAPTACIONS_FLORA.pdf (p. 6)
        }
    }

    # Inicialitzar un lloc per desar les respostes de l'usuari
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
            st.success("🎉 **VALIDACIÓ COMPLETA! Codi 100% Acceptat!** 🎉 Domini dels conceptes de la UF1.")
        elif percentatge >= 0.7:
            st.success("VALIDACIÓ PARCIALMENT OK. Repassa els punts febles.")
        else:
            st.error("ERROR CRÍTIC. Repassa la UF1 abans de tornar a executar el test.")


# --- Barra Lateral (Sidebar) de Navegació ---
st.sidebar.title("🧬 Mòdul Bio-Explorador 2.0")
st.sidebar.markdown("Un recorregut digital per la vida a la Terra. (**MP 02: Medi Natural**)")

pagina = st.sidebar.radio(
    "🖥️ SELECCIÓ DE MÒDUL (UF 1):",
    [
        "🏠 Inici & Objectius",
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
st.sidebar.info("Codi Generat | Versió: MP02\_UF1\_V3.0\n\n© IMR Bio-Lab")


# --- Contingut de les Pàgines ---

# 🏠 INICI
if pagina == "🏠 Inici & Objectius":
    st.title("🤖 Terminal de Caracterització d'Hàbitats (UF1)")
    st.markdown("---")
    st.markdown("Benvingut/da a la interfície d'aprenentatge interactiva. Aquesta UF cobreix els continguts de les Normes Formatives NF 1.1, NF 1.2 i NF 1.3.")
    
    st.header("🎯 Objectius de Mòdul (UF 1)")
    st.markdown(
        """
        * **NF 1.1: Els Biomes de la Terra:** Caracteritzar els biomes segons el clima i la vegetació dominant (A1, A2).
        * **NF 1.2: Hàbitats Peninsulars:** Identificar les regions biogeogràfiques d'Espanya i els hàbitats de Catalunya (A3).
        * **NF 1.3: Protecció d'Hàbitats:** Conèixer els mecanismes de protecció europeus, estatals i autonòmics.
        """
    )
    st.header("💾 Estat del Sistema")
    st.code(">>> STATUS: READY_TO_EXECUTE\n>>> Carregant 10 de 10 mòduls de dades OK\n>>> Interfície visualitzada.")


# 🌍 BIOMES DE LA TERRA (NF 1.1)
elif pagina == "🌍 Biomes de la Terra (NF 1.1)":
    st.title("🌍 Cartografia Global: Biomes de la Terra")
    st.markdown("Unitats de gran extensió amb una vegetació climàtica uniforme i un clima característic.")

    with st.expander("INFO: Definició i Classificació"):
        st.markdown(
            """
            * **Bioma:** Conjunt de comunitats que ocupen una mateixa àrea geogràfica.
            * **Factors Clau (Whittaker):** La classificació depèn principalment de la **Temperatura Mitjana Anual** i la **Precipitació Anual**.
            """
        )
    
    st.header("Fitxa de Bioma: Bosc Mediterrani (Escleròfil)")
    
    st.subheader("Clima i Vegetació")
    st.markdown(
        """
        * **CLIMA:** Estius calorosos i secs. Hiverns suaus i plujosos.
        * **VEGETACIÓ:** **Escleròfil·la (de fulla dura)**.
            * Barreja d'arbres de fulla perenne (Alzina, Surera) amb caducifolis (Figueres, Ametllers).
            * **Gran rellevància** dels estrats **arbustiu** (Marfull, Arboç, Boix, Brucs), **herbaci** i **lianoide**.
        """
    )

    st.subheader("Fauna Clau")
    st.markdown(
        """
        * **Herbívors:** Cabirols, Esquirols, Llebres.
        * **Carnívors:** Guineus, Geneta, **Linx ibèric**.
        * **Omnívors:** Porc senglar, Rata de camp.
        """
    )


# 📊 CLIMOGRAMES i Distribució (NF 1.1 - A3)
elif pagina == "📊 Climogrames i Distribució":
    st.title("📊 Anàlisi Gràfica de Dades Climàtiques")
    st.markdown("El climograma: mostra el clima d'un lloc combinant Temperatura ($^{\circ}C$) i Precipitació (mm).")

    st.header("Protocol d'Interpretació")
    st.markdown(
        """
        * **Eixos:** Horitzontal (mesos), Vertical Esquerre (**Temperatura**, Línia), Vertical Dret (**Precipitació**, Barres).
        * **Sequera (Aridesa):** S'identifica quan la **Línia de Temperatura supera les Barres de Precipitació** (T > P).
        """
    )

    st.header("Exemples de Climes Típics")
    
    c_tab1, c_tab2 = st.tabs(["Clima Mediterrani (Típic)", "Clima Polar (Thule)"])
    
    with c_tab1:
        st.subheader("PATRÓ: Sequera Estival")
        st.markdown("Estiu (J, L, A) amb aridesa molt marcada. El patró clau per als biomes escleròfils.")
    
    with c_tab2:
        st.subheader("PATRÓ: Fred Extrèmic")
        st.markdown("Temperatures molt baixes tot l'any. La línia de Tº es manté constantment **per sota dels $0^{\circ}C$**. Pluges escasses (neu).")


# 🇪🇸 HÀBITATS PENINSULARS (NF 1.2 - A2)
elif pagina == "🇪🇸 Hàbitats Peninsulars (NF 1.2)":
    st.title("🇪🇸 Ruta Biogeogràfica i Protecció (NF 1.2 & NF 1.3)")
    st.markdown("Divisió del territori espanyol en regions segons les condicions ambientals.")

    st.header("Regions Biogeogràfiques d'Espanya")
    
    bio_tab1, bio_tab2, bio_tab3 = st.tabs(["🟢 Eurosiberiana", "🟠 Mediterrània", "🌋 Macaronèsica"])

    with bio_tab1:
        st.subheader("🟢 Regió Eurosiberiana (La 'Espanya Verda')")
        st.markdown(
            """
            * **Localització:** Nord (Cornisa Cantàbrica, Galícia).
            * **Clima:** Temperat amb estius humits.
            * **Vegetació Dominant:** **Boscos Caducifolis** (Roures, Faigs).
            """
        )

    with bio_tab2:
        st.subheader("🟠 Regió Mediterrània")
        st.markdown(
            """
            * **Localització:** Centre, Sud i Est peninsular.
            * **Vegetació Dominant:** **Boscos Perennifolis Escleròfils** (Alzinar, Surera).
            """
        )
    
    st.header("Protocol Europeu de Protecció (NF 1.3)")
    
    with st.expander("Sistemes de Classificació i Xarxes"):
        st.markdown(
            """
            * **CORINE Biotopes:** Sistema de classificació jeràrquica utilitzat a la UE per catalogar hàbitats (base de la protecció).
            * **Xarxa Natura 2000:** Xarxa d'àrees de conservació, formada per:
                * **ZEPA:** Zones d'Especial Protecció per a les Aus.
                * **ZEC:** Zones Especials de Conservació (per a hàbitats i espècies).
            """
        )

# 🏞️ HÀBITATS DE CATALUNYA (NF 1.2 - A3)
elif pagina == "🏞️ Hàbitats de Catalunya":
    st.title("🏞️ Fitxer d'Hàbitats Nacionals (Catalunya)")
    st.markdown("Catalunya presenta una gran varietat d'hàbitats segons la zona (litoral, prelitoral, pirinenca).")
    
    hab_tab1, hab_tab2 = st.tabs(["🌳 La Fageda", "🌲 L'Alzinar"])

    with hab_tab1:
        st.subheader("🌳 Fageda (Bosc de Faigs - *Fagus sylvatica*)")
        st.markdown("Típic de la muntanya mitjana (Ex: Fageda d'en Jordà).")
        st.markdown(
            """
            * **Arbre dominant:** Faig (*Fagus sylvatica*).
            * **Ecologia:** Clima **Medioeuropeu subatlàntic**.
            * **Sòl:** Terrenys àcids, sòl poc profund.
            * **Estrat Arbustiu:** Pobre, compost principalment per plantes acidòfiles (Boix, Bruguerola).
            """
        )

    with hab_tab2:
        st.subheader("🌲 L'Alzinar (Bosc d'Alzina - *Quercus ilex*)")
        st.markdown("Bosc perennifoli escleròfil mediterrani.")
        st.markdown(
            """
            * **Arbre dominant:** Alzina (*Quercus ilex*).
            * **Vegetació associada:** Arbusts escleròfils (Marfull, Arboç) i lianes (Arítjol).
            * **Adaptació:** Fulla dura (escleròfil·la) per resistir la **sequera estival**.
            """
        )

# 🌱 CONCEPTES CLAU (Adaptacions i Biodiversitat - NF 1.1)
elif pagina == "🌱 Adaptacions i Biodiversitat":
    st.title("🌱 Glossari Tècnic: Adaptacions i Biodiversitat")
    st.markdown("Conceptes fonamentals per entendre la distribució de les espècies.")

    conceptes_tab1, conceptes_tab2 = st.tabs(["Biodiversitat i Endemismes", "Adaptacions de la Flora (Termo/Hídriques/Foc)"])

    with conceptes_tab1:
        st.subheader("🧬 Biodiversitat i Endemisme")
        st.markdown(
            """
            * **Biodiversitat:** L'àmplia varietat d'éssers vius a la Terra (genètic, específic i d'ecosistemes).
            * **Endemisme:** Espècie amb una **àrea de distribució molt limitada**. Causes típiques: **aïllament geogràfic** (montàno, insular) o canvi brusc de les condicions del medi. (Ex: *Lagartija aranesa*).
            * **Espècie Cosmopolita:** Espècie amb una distribució molt àmplia a nivell global.
            """
        )

    with conceptes_tab2:
        st.subheader("⚙️ Adaptacions al Medi")
        st.markdown(
            """
            **Rang de Supervivència Tèrmica:** Les plantes poden sobreviure entre els **$0^{\circ}C$** (per sota, es paralitza l'absorció i processament de l'aigua) i els **$45^{\circ}C$**.
            """
        )

        st.markdown("#### **Adaptacions Hídriques (Sequera - Xeròfiles)**")
        st.markdown(
            """
            * **Mecanismes (Plantes Xeròfiles):** Fulles petites, transformació en espines, acumulació d'aigua (suculentes), presència de pèls i ceres, arrels profundes.
            """
        )
        
        st.markdown("#### **Adaptacions al Foc (Piròfites)**")
        st.markdown(
            """
            * **Mecanismes:** **Resistència Passiva** (aigua en les fulles), **Rebrotat Ràpid**, o mecanismes de **Serotinia** (obertura de pinyes amb la calor per alliberar llavors, ex: Pi blanc - *Pinus halepensis*).
            """
        )

# ❓ POSA'T A PROVA! (Quiz)
elif pagina == "❓ Posa't a Prova! (Quiz)":
    run_quiz()
