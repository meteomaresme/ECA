import streamlit as st

# --- Configuració del Tema Futurista amb CSS Injectat ---
# Aquesta funció injecta CSS personalitzat per a un look "futurista/dark mode"
# Utilitzant colors neó (Cyan) sobre un fons fosc per donar un aspecte de terminal.
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
            text-shadow: 0 0 5px rgba(0, 255, 255, 0.5); /* Efecte "glow" */
            font-family: 'Consolas', 'Courier New', monospace; /* Tipografia digital */
            border-bottom: 2px solid var(--primary-color-800);
            padding-bottom: 5px;
        }
        
        /* 3. Subtítols i Headings (Línia d'accent) */
        h2, h3, h4, h5, h6 {
            color: #E0E0E0; /* Gris clar per contrast */
            border-left: 5px solid var(--primary-color); /* Línia d'accent a l'esquerra */
            padding-left: 10px;
            margin-top: 20px;
        }

        /* 4. Estil de la Barra Lateral (Sidebar) */
        /* Aquesta classe pot canviar lleugerament amb futures versions de Streamlit */
        .st-emotion-cache-vk3ypz { 
            background-color: #1A1A1A; /* Fons més fosc per a la sidebar */
            border-right: 1px solid var(--primary-color-800);
        }
        
        /* 5. Estil dels Missatges (Quiz Resultats) */
        .stSuccess {
            background-color: rgba(0, 255, 0, 0.1); /* Fons verd translúcid */
            border-left: 5px solid #00FF00;
        }
        .stError {
            background-color: rgba(255, 0, 0, 0.1); /* Fons vermell translúcid */
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

# Injectar l'estil personalitzat al principi de l'execució
inject_futuristic_style()

# --- Funció per al Quiz (Lògica de Test Ampliada) ---
def run_quiz():
    st.header("❓ Posa't a Prova! (Terminal de Test)")
    st.markdown("---")
    st.info("🟢 **EXECUTANT TEST DE VALIDACIÓ DE CONEIXEMENTS...**")
    st.markdown("Selecciona la resposta correcta per a cada pregunta. Cobreix Biomes, Climogrames, Adaptacions, Hàbitats i Protecció.")

    # Diccionari amb les preguntes i respostes, extretes dels materials (NF1.1 i NF1.2)
    preguntes = {
        "Q1: Climograma": {
            "pregunta": "Si un climograma mostra barres de precipitació molt baixes a l'estiu i una línia de temperatura alta, de quin clima és típic?",
            "opcions": ["Polar", "Mediterrani", "Equatorial", "Oceànic"],
            "correcta": "Mediterrani"
        },
        "Q2: Bioma": {
            "pregunta": "Quin bioma es caracteritza per arbres que perden la fulla a l'hivern (caducifolis), com els roures i els faigs?",
            "opcions": ["Tundra", "Desert", "Bosc temperat caducifoli", "Selva tropical"],
            "correcta": "Bosc temperat caducifoli"
        },
        "Q3: Adaptació (Sequera)": {
            "pregunta": "Les plantes amb fulles petites, pèls o que acumulen aigua (suculentes) s'anomenen xeròfiles i estan adaptades a...",
            "opcions": ["La falta de llum", "El fred intens", "La sequera", "Els incendis"],
            "correcta": "La sequera"
        },
        "Q4: Biodiversitat": {
            "pregunta": "Una espècie que només es troba en una regió geogràfica molt concreta (com la *Lagartija aranesa*) s'anomena...",
            "opcions": ["Endemisme", "Hotspot", "Bioma", "Espècie invasora"],
            "correcta": "Endemisme"
        },
        "Q5: Hàbitat Catalunya": {
            "pregunta": "Quin és l'arbre dominant i que dona nom a una 'fageda'?",
            "opcions": ["El pi (Pinus)", "L'alzina (Quercus ilex)", "El faig (Fagus sylvatica)", "El roure (Quercus robur)"],
            "correcta": "El faig (Fagus sylvatica)"
        },
        "Q6: Protecció": {
            "pregunta": "Quin sistema de classificació europeu s'utilitza per catalogar els hàbitats naturals i seminaturals, i que és la base per a la Xarxa Natura 2000?",
            "opcions": ["WWF", "Ramsar", "CORINE Biotopes", "Whittaker"],
            "correcta": "CORINE Biotopes"
        },
        "Q7: Fauna Mediterrània": {
            "pregunta": "Quin d'aquests animals és un carnívor típic esmentat de la fauna del Bosc Mediterrani (Escleròfil)?",
            "opcions": ["Cabirol", "Rata de camp", "Linx ibèric", "Esquirol"],
            "correcta": "Linx ibèric"
        },
        "Q8: Límits Tèrmics": {
            "pregunta": "Per sota de quina temperatura la planta no té opcions d'absorbir aigua, eliminar-la o processar-la eficaçment, segons els materials d'adaptacions?",
            "opcions": ["$10^{\circ}C$", "$45^{\circ}C$", "$0^{\circ}C$", "$-5^{\circ}C$"],
            "correcta": "$0^{\circ}C$"
        },
        "Q9: Regions Biogeogràfiques": {
            "pregunta": "Quina de les grans regions biogeogràfiques d'Espanya es caracteritza per boscos caducifolis (roures i faigs) i estius humits?",
            "opcions": ["Regió Macaronèsica", "Regió Eurosiberiana", "Regió Mediterrània", "Regió Alpina"],
            "correcta": "Regió Eurosiberiana"
        },
        "Q10: Adaptació Escleròfil·la": {
            "pregunta": "En l'Alzinar, els arbustos com el Marfull i l'Arboç són exemples de la vegetació perenne adaptada al clima...",
            "opcions": ["Polar", "Atlàntic", "Mediterrani", "Continental"],
            "correcta": "Mediterrani"
        }
    }

    # Inicialitzar un lloc per desar les respostes de l'usuari
    respostes_usuari = {}

    with st.form(key="quiz_form_ampliat"):
        for i, (key, value) in enumerate(preguntes.items()):
            st.subheader(f"⚡ {key}")
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


# --- Barra Lateral (Sidebar) de Navegació ---
st.sidebar.title("🧬 Mòdul Bio-Explorador 2.0")
st.sidebar.markdown("Un recorregut digital per la vida a la Terra (UF1: Caracterització d'hàbitats).")

pagina = st.sidebar.radio(
    "🖥️ SELECCIÓ DE MÒDUL:",
    [
        "🏠 Inici",
        "🌍 Biomes de la Terra",
        "📊 Climogrames",
        "🇪🇸 Hàbitats a Espanya",
        "🏞️ Hàbitats de Catalunya",
        "🌱 Conceptes Clau (Biodiversitat i Adaptacions)",
        "❓ Posa't a Prova! (Quiz)"
    ],
    captions=[
        "Terminal d'accés principal.",
        "Cartografia Global d'Ecosistemes.",
        "Anàlisi Gràfica de Dades Climàtiques.",
        "Ruta Biogeogràfica Peninsular.",
        "Fitxer d'Hàbitats Nacionals.",
        "Glossari Tècnic de Supervivència.",
        "Test de Validació de Coneixements."
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Codi Generat | Versió: MP02\_UF1\_V2.1")


# --- Contingut de les Pàgines ---

# 🏠 INICI
if pagina == "🏠 Inici":
    st.title("🤖 Accés al Terminal de Caracterització d'Hàbitats (UF1)")
    st.markdown("---")
    st.markdown("Benvingut/da a la interfície d'aprenentatge interactiva. Utilitza el menú lateral per navegar i analitzar les dades de la Unitat Formativa 1: **Caracterització d'Hàbitats**.")
    
    st.header("🎯 Objectius de Mòdul")
    st.markdown(
        """
        * **[A1]** Entendre i classificar els **Biomes** segons variables climàtiques (Whittaker).
        * **[A2]** Dominar la lectura i interpretació dels **Climogrames**.
        * **[A3]** Analitzar les **Adaptacions** de la flora i els conceptes de **Biodiversitat**.
        """
    )
    st.header("💾 Estat del Sistema")
    st.code(">>> STATUS: READY_TO_EXECUTE\n>>> Carregant 10 de 10 mòduls de dades OK\n>>> Interfície visualitzada. Esperant entrada de l'usuari.")


# 🌍 BIOMES DE LA TERRA
elif pagina == "🌍 Biomes de la Terra":
    st.title("🌍 Cartografia Global: Biomes de la Terra")
    st.markdown("Les unitats d'anàlisi de macro-ecosistemes definides pel clima i la vegetació dominant.")

    with st.expander("INFO: Definició de Bioma"):
        st.markdown("És el conjunt de comunitats que ocupen una mateixa àrea geogràfica. Presenten una vegetació climàtica uniforme i un clima característic.")
    
    st.subheader("Claus d'Anàlisi (Whittaker)")
    st.markdown("La classificació es basa en la interacció de dos factors crítics: **Temperatura Mitjana Anual** i **Precipitació Anual**.")

    st.header("Fitxes de Biomes (MODE TERMINAL)")
    
    tab1, tab2, tab3 = st.tabs(["🌳 Bosc Temperat", "🌲 Bosc Mediterrani (Escleròfil)", "🌴 Selva Tropical"])

    with tab2:
        st.subheader("🌲 Bosc Mediterrani (Escleròfil)")
        st.markdown(
            """
            * **CLIMA:** Estius calorosos i secs. Hiverns suaus i plujosos.
            * **VEGETACIÓ:** Escleròfil·la (fulla dura i perenne). Ex: Alzines, Sureres, Pins.
            * **FAUNA CLAU:** Carnívors (**Linx ibèric**, geneta); Omnívors (porc senglar).
            """
        )
# 📊 CLIMOGRAMES
elif pagina == "📊 Climogrames":
    st.title("📊 Anàlisi Gràfica de Dades Climàtiques")
    st.markdown("Eina essencial per a la caracterització d'hàbitats: el Climograma.")

    st.header("Interpretació de Dades")
    st.markdown(
        """
        Un climograma combina dues dades: **Temperatura** $(^{\circ}C)$ (Línia) i **Precipitació** (mm) (Barres).
        
        > **[ALERTA HÍDRICA]:** Quan la Línia de Temperatura supera les Barres de Precipitació (T > P), s'identifica un **Període d'Aridesa (Sequera)**.
        
        """
    )

# 🇪🇸 HÀBITATS A ESPANYA
elif pagina == "🇪🇸 Hàbitats a Espanya":
    st.title("🇪🇸 Ruta Biogeogràfica Peninsular")
    st.markdown("Divisió del territori espanyol segons els patrons climàtics i de vegetació.")

    st.header("Regions Biogeogràfiques")
    
    bio_tab1, bio_tab2 = st.tabs(["🟢 Eurosiberiana", "🟠 Mediterrània"])

    with bio_tab1:
        st.subheader("🟢 Regió Eurosiberiana (La 'Espanya Verda')")
        st.markdown(
            """
            * **Localització:** Nord (Cornisa Cantàbrica).
            * **Vegetació Dominant:** **Boscos Caducifolis** (Roures, Faigs).
            """
        )

    st.header("Protocol Europeu de Protecció")
    
    with st.expander("Xarxa Natura 2000 i CORINE Biotopes"):
        st.markdown(
            """
            * **CORINE Biotopes:** Sistema de classificació europeu per catalogar i identificar els hàbitats.
            * **Xarxa Natura 2000:** Xarxa d'àrees de conservació (ZEPA - Ocells i ZEC - Hàbitats/Espècies).
            """
        )

# 🏞️ HÀBITATS DE CATALUNYA
elif pagina == "🏞️ Hàbitats de Catalunya":
    st.title("🏞️ Fitxer d'Hàbitats Nacionals (Catalunya)")
    st.markdown("Anàlisi dels boscos més significatius de Catalunya.")
    
    hab_tab1, hab_tab2 = st.tabs(["🌳 Fageda", "🌲 Alzinar"])

    with hab_tab1:
        st.subheader("🌳 Fageda (Bosc de Faigs - *Fagus sylvatica*)")
        st.markdown("Bosc de muntanya mitjana (Montseny, Garrotxa).")
        st.markdown(
            """
            * **Arbre dominant:** Faig (*Fagus sylvatica*).
            * **Ecologia:** Clima Medioeuropeu subatlàntic. Sòls àcids.
            """
        )

# 🌱 CONCEPTES CLAU
elif pagina == "🌱 Conceptes Clau (Biodiversitat i Adaptacions)":
    st.title("🌱 Glossari Tècnic de Supervivència")
    st.markdown("Terminologia clau per a l'ecologia i la botànica.")

    conceptes_tab1, conceptes_tab2 = st.tabs(["Biodiversitat i Endemismes 🌎", "Adaptacions de la Flora 🌿"])

    with conceptes_tab1:
        st.subheader("🧬 Diversitat i Endemisme")
        st.markdown(
            """
            * **Biodiversitat:** Varietat d'éssers vius (genètic, específic i d'ecosistemes).
            * **Endemisme:** Espècie amb una **àrea de distribució molt limitada** (causat per aïllament geogràfic).
            """
        )

    with conceptes_tab2:
        st.subheader("⚙️ Adaptacions al Medi")
        st.markdown("El rang de supervivència de les plantes se situa entre els $0^{\circ}C$ i els $45^{\circ}C$.")

        st.markdown("#### **Adaptacions Hídriques (Sequera - Xeròfiles)**")
        st.markdown(
            """
            * **Mecanismes:** Fulles petites/espines (reduir transpiració), acumulació d'aigua (suculentes), pèls/ceres.
            """
        )
        
        st.markdown("#### **Adaptacions al Foc (Piròfites)**")
        st.markdown("Capacitat de rebrotar ràpidament o obertura de pinyes (seròtines) amb la calor.")

# ❓ POSA'T A PROVA! (Quiz)
elif pagina == "❓ Posa't a Prova! (Quiz)":
    run_quiz()
