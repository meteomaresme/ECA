import streamlit as st

# --- 1. CONFIGURACIÓ DE LA PÀGINA ---------------------------------------------
st.set_page_config(
    page_title="BioExplorer | Hàbitats i Biomes",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. BARRA LATERAL (SIDEBAR) -----------------------------------------------
with st.sidebar:
    st.title("🧭 BioExplorer")
    st.markdown("La teva aventura interactiva pel medi natural.")
    # <<< POSA EL TEU DIBUIX/LOGO AQUÍ
    st.image("https://www.svgrepo.com/show/485308/eco-nature-leaves.svg", width=120)
    st.caption("Materials de la UF1 - MP02 Medi Natural")

    pagina = st.radio(
        "Selecciona la teva missió:",
        ["🏠 Inici", "🌍 Biomes Globals", "📊 Anàlisi Climàtica", "🇪🇸 Hàbitats d'Espanya", "🏞️ Hàbitats de Catalunya", "🧬 Conceptes Essencials", "🏆 Desafiament Final"],
        captions=["Punt de partida", "Explora els grans ecosistemes", "Interpreta el clima", "La diversitat peninsular", "El nostre entorn proper", "El vocabulari del naturalista", "Posa't a prova!"]
    )
    st.divider()
    st.info("Dissenyat per fer l'estudi més visual i entretingut.")


# --- 3. FUNCIÓ PER AL QUIZ (DESAFIAMENT FINAL) -------------------------------
def run_quiz():
    st.title("🏆 Desafiament Final: Posa't a Prova!")
    st.markdown("Has explorat els biomes i après els conceptes clau. És hora de demostrar el que saps!")

    preguntes = {
        # ... (les preguntes es mantenen igual)
    }

    # Inicialització de l'estat de la sessió per al quiz
    if 'score' not in st.session_state:
        st.session_state.score = 0
        st.session_state.submitted = False
        st.session_state.respostes_usuari = {}

    with st.form(key="quiz_form"):
        for i, (key, value) in enumerate(preguntes.items()):
            st.subheader(f"Pregunta {i+1}: {value['pregunta']}")
            st.session_state.respostes_usuari[key] = st.radio("Tria una opció:", options=value["opcions"], key=f"q{i}", label_visibility="collapsed")
        
        submitted = st.form_submit_button("Corregeix el meu desafiament! 🚀", use_container_width=True)

    if submitted:
        st.session_state.submitted = True
        st.session_state.score = sum(1 for key, value in preguntes.items() if st.session_state.respostes_usuari[key] == value["correcta"])

    if st.session_state.submitted:
        st.header("Resultats del Desafiament")
        total = len(preguntes)
        percentatge = st.session_state.score / total

        st.progress(percentatge, text=f"La teva puntuació: {st.session_state.score}/{total}")

        if percentatge == 1.0:
            st.balloons()
            st.success("🎉 **EXCEL·LENT! PUNTUACIÓ PERFECTA!** Ets un autèntic expert/a en hàbitats! 🎉")
        elif percentatge >= 0.7:
            st.info("🌟 **MOLT BONA FEINA!** Tens un gran domini sobre la matèria.")
        elif percentatge >= 0.5:
            st.warning("👍 **APROVAT!** Vas pel bon camí, però repassa els errors per millorar.")
        else:
            st.error("📉 **NECESSITES REPASSAR.** No et desanimis! Torna a explorar les seccions i intenta-ho de nou.")

        st.divider()
        st.subheader("Revisió detallada:")
        for key, value in preguntes.items():
            if st.session_state.respostes_usuari[key] == value["correcta"]:
                st.success(f"**{key}:** Correcte! ✔️ La teva resposta va ser '{st.session_state.respostes_usuari[key]}'.")
            else:
                st.error(f"**{key}:** Incorrecte. ❌ La resposta correcta era '{value['correcta']}', però vas triar '{st.session_state.respostes_usuari[key]}'.")
        
        if st.button("Tornar a intentar el Desafiament 🔄", use_container_width=True):
            st.session_state.submitted = False
            st.rerun()

# --- 4. CONTINGUT DE LES PÀGINES ---------------------------------------------

# 🏠 PÀGINA D'INICI
if pagina == "🏠 Inici":
    st.title("🌿 Benvingut/da a BioExplorer!")
    st.markdown("#### La teva eina interactiva per dominar la caracterització d'hàbitats.")
    st.divider()

    # <<< POSA EL TEU DIBUIX PRINCIPAL AQUÍ
    st.image("https://cdni.iconscout.com/illustration/premium/thumb/save-earth-and-environment-8111248-6483162.png", caption="El nostre planeta està ple de vida per descobrir.")
    
    st.header("Què pots fer aquí?")
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        st.metric(label="Explora", value="6 Biomes", delta="Globals")
        st.markdown("- Viatja per selves, deserts i boscos.\n- Entén el seu clima, flora i fauna.")
    with col2:
        st.metric(label="Analitza", value="4 Climogrames", delta="Interactius")
        st.markdown("- Aprèn a llegir el clima com un professional.\n- Identifica períodes de sequera i pluja.")
    with col3:
        st.metric(label="Domina", value="+15 Conceptes", delta="Clau")
        st.markdown("- Entén què és la biodiversitat, l'endemisme i molt més.\n- Posa't a prova amb el desafiament final.")
    st.success("Comença la teva exploració utilitzant el menú de l'esquerra! 🧭")

# 🌍 PÀGINA DE BIOMES GLOBALS
elif pagina == "🌍 Biomes Globals":
    st.title("🌍 Biomes Globals: Els Grans Ecosistemes de la Terra")
    st.markdown("Cada bioma és un món en si mateix, amb unes regles climàtiques i uns habitants únics.")

    with st.expander("🤔 Què és exactament un Bioma?"):
        st.info("Un **bioma** és una comunitat a gran escala d'organismes (plantes i animals) que comparteixen característiques comunes per a l'entorn en què existeixen. Es defineixen principalment pel **clima** i la **vegetació dominant**.")
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Whittaker_biomes_plot.svg/1200px-Whittaker_biomes_plot.svg.png", caption="El Diagrama de Whittaker classifica els biomes segons temperatura i precipitació.")

    tab_names = ["🌳 Bosc Temperat", "🏜️ Desert", "🌴 Selva Tropical", "🌱 Praderies", "🌲 Bosc Mediterrani"]
    tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_names)

    with tab1:
        col1, col2 = st.columns([1, 2])
        with col1:
            st.subheader("🌳 Bosc Temperat Caducifoli")
            # <<< POSA EL TEU DIBUIX AQUÍ
            st.image("https://cdni.iconscout.com/illustration/premium/thumb/autumn-season-3488582-2922253.png")
        with col2:
            st.markdown("- **Clima:** 4 estacions ben definides.\n- **Flora Típica:** Roures, faigs, aurons (perden la fulla a l'hivern).\n- **Fauna Clau:** Ós bru, cérvol, llop.")
            with st.container(border=True):
                st.markdown("🧠 **Sabies que...?** El canvi de color de les fulles a la tardor es deu a la pèrdua de clorofil·la, que revela altres pigments com els carotenoides (taronges) i les antocianines (vermells).")

    # ... (pots seguir aquest mateix patró per a la resta de biomes)

# 📊 PÀGINA D'ANÀLISI CLIMÀTICA
elif pagina == "📊 Anàlisi Climàtica":
    st.title("📊 Anàlisi Climàtica: Llegeix el Temps")
    st.markdown("Un **climograma** és la radiografia del clima d'un lloc. Aprenem a interpretar-lo.")

    col1, col2 = st.columns(2)
    with col1:
        st.info("""
        #### Com llegir-lo?
        *   **Línia Vermella (🌡️):** Temperatura mitjana.
        *   **Barres Blaves (💧):** Precipitació mensual.
        *   **El Truc de l'Aridesa:** Quan la línia de temperatura supera les barres de pluja (`Tª > 2P`), hi ha **estrès hídric** o sequera.
        """)
    with col2:
        # <<< POSA EL TEU DIBUIX AQUÍ
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/weather-forecast-5208453-4351337.png")

    st.divider()
    
    # Element interactiu: Selectbox
    clima_seleccionat = st.selectbox(
        "Selecciona un exemple de clima per analitzar el seu climograma:",
        ["Clima Mediterrani (Nàpols)", "Clima Equatorial (Akassa)", "Clima Desèrtic (Alexandria)", "Clima Polar (Thule)"]
    )
    
    climogrames = {
        "Clima Mediterrani (Nàpols)": ("https://i.imgur.com/1Gv2F1B.png", "Observa la caiguda dràstica de les pluges a l'estiu, coincidint amb el pic de temperatures. Aquest és el patró mediterrani clàssic!"),
        "Clima Equatorial (Akassa)": ("https://i.imgur.com/LhBvW4f.png", "Temperatures altes i constants, i pluges torrencials durant tot l'any. No hi ha estació seca."),
        "Clima Desèrtic (Alexandria)": ("https://i.imgur.com/Uf1C29X.png", "Les barres de precipitació són gairebé invisibles. L'aridesa és extrema durant tot l'any."),
        "Clima Polar (Thule)": ("https://i.imgur.com/U6LzJ7m.png", "La línia de temperatura està gairebé sempre per sota de 0°C. Les precipitacions són molt escasses i en forma de neu.")
    }

    url, descripcio = climogrames[clima_seleccionat]
    st.image(url, caption=f"Climograma de: {clima_seleccionat.split('(')[1][:-1]}")
    st.success(f"**Anàlisi ràpida:** {descripcio}")

# ... (I així successivament per a la resta de pàgines, seguint aquesta línia de disseny visual i interactiu)

# 🧬 PÀGINA DE CONCEPTES ESSENCIALS
elif pagina == "🧬 Conceptes Essencials":
    st.title("🧬 Conceptes Essencials: El teu Diccionari de Naturalista")
    st.markdown("Domina aquests termes i parlaràs el llenguatge de l'ecologia.")

    with st.expander("🌍 **Biodiversitat**: La riquesa de la vida"):
        st.markdown("És la **varietat d'éssers vius** a la Terra. Inclou 3 nivells:\n1.  **Genètica:** La varietat dins d'una mateixa espècie.\n2.  **Específica:** El nombre d'espècies diferents.\n3.  **Ecològica:** La varietat d'ecosistemes.")
        # <<< POSA EL TEU DIBUIX AQUÍ
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/biodiversity-3995801-3306162.png", width=300)

    with st.expander("📍 **Endemisme**: Tresors locals"):
        st.markdown("Un **endemisme** és una espècie que viu **exclusivament en una regió geogràfica concreta** del món i enlloc més. Solen aparèixer en llocs aïllats com illes o muntanyes.")
        # <<< POSA EL TEU DIBUIX AQUÍ
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Galemys_pyrenaicus.png/800px-Galemys_pyrenaicus.png", caption="El Desman dels Pirineus, un endemisme.")
        
    with st.expander("🔥 **Hotspot**: Punts calents de biodiversitat"):
        st.markdown("Són regions amb una **concentració altíssima d'endemismes** que, alhora, estan **greument amenaçades** per l'activitat humana. La Conca Mediterrània n'és un.")

    with st.expander("🌱 **Adaptacions de la Flora**: L'enginy de les plantes"):
        st.markdown("Com que no es poden moure, les plantes han desenvolupat estratègies sorprenents per sobreviure:")
        st.info("🌿 **Plantes Xeròfiles (contra la sequera):** Fulles petites o espines, acumulació d'aigua, pèls protectors.")
        st.info("🔥 **Plantes Piròfites (contra el foc):** Capacitat de rebrotar, pinyes que s'obren amb la calor (seròtines).")
        st.info("🥶 **Plantes contra el fred:** Mida petita, saba amb 'anticongelants', pèrdua de la fulla.")
        
# 🏆 PÀGINA DEL DESAFIAMENT FINAL
elif pagina == "🏆 Desafiament Final":
    run_quiz()
