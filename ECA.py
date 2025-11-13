import streamlit as st

# --- 1. CONFIGURACIÓ DE LA PÀGINA ---------------------------------------------
st.set_page_config(
    page_title="Explora Hàbitats i Biomes",
    page_icon="🌍", # Canviat per un emoji més global
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. BARRA LATERAL (SIDEBAR) -----------------------------------------------
with st.sidebar:
    st.title("🗺️ Menú de Navegació")
    st.markdown("Un recorregut per la vida a la Terra, des dels biomes globals fins als hàbitats de Catalunya.")

    # <<< CANVIA AQUÍ si vols un altre logo o imatge a la barra lateral
    st.image("https://www.svgrepo.com/show/493361/ecology-leaf-love.svg", width=120)
    st.caption("Materials de la UF1 - MP02 Medi Natural")

    pagina = st.radio(
        "Selecciona una secció:",
        [
            "🏠 Inici",
            "🌍 Biomes de la Terra",
            "📊 Climogrames",
            "🇪🇸 Hàbitats a Espanya",
            "🏞️ Hàbitats de Catalunya",
            "🌱 Conceptes Clau",
            "❓ Posa't a Prova!"
        ],
        captions=[
            "Benvinguda a l'aventura!",
            "Viatja pels grans ecosistemes.",
            "Aprèn a llegir el clima.",
            "Descobreix la diversitat peninsular.",
            "El nostre entorn més proper.",
            "Paraules que tot naturalista ha de saber.",
            "Demostra el que has après!"
        ]
    )

    st.divider()
    st.info("Aquesta app ha estat creada per ajudar-te a estudiar el contingut dels PDFs.")
    st.success("Versió millorada amb il·lustracions!")


# --- 3. FUNCIÓ PER AL QUIZ ----------------------------------------------------
def run_quiz():
    st.title("❓ Posa't a Prova!")
    st.markdown("És hora de comprovar què has après. Selecciona la resposta correcta per a cada pregunta.")
    st.divider()

    preguntes = {
        "Pregunta 1": {
            "pregunta": "Si un climograma mostra barres de precipitació molt baixes a l'estiu i una línia de temperatura alta, de quin clima és típic?",
            "opcions": ["Polar", "Mediterrani", "Equatorial", "Oceànic"], "correcta": "Mediterrani"
        },
        "Pregunta 2": {
            "pregunta": "Quin bioma es caracteritza per arbres que perden la fulla a l'hivern, com els roures i els faigs?",
            "opcions": ["Tundra", "Desert", "Bosc temperat caducifoli", "Selva tropical"], "correcta": "Bosc temperat caducifoli"
        },
        "Pregunta 3": {
            "pregunta": "Les plantes xeròfiles, amb fulles petites o que acumulen aigua, estan adaptades a...",
            "opcions": ["La falta de llum", "El fred intens", "La sequera", "Els incendis"], "correcta": "La sequera"
        },
        "Pregunta 4": {
            "pregunta": "Una espècie que només es troba en una regió molt concreta s'anomena...",
            "opcions": ["Endemisme", "Hotspot", "Bioma", "Espècie invasora"], "correcta": "Endemisme"
        },
        "Pregunta 5": {
            "pregunta": "Quin és l'arbre dominant en una 'fageda'?",
            "opcions": ["El pi (Pinus)", "L'alzina (Quercus ilex)", "El faig (Fagus sylvatica)", "El roure (Quercus robur)"], "correcta": "El faig (Fagus sylvatica)"
        },
        "Pregunta 6": {
            "pregunta": "Quina classificació europea s'utilitza per catalogar els hàbitats naturals i seminaturals?",
            "opcions": ["WWF", "Natura 2000", "CORINE Biotopes", "Whittaker"], "correcta": "CORINE Biotopes"
        }
    }

    respostes_usuari = {}
    with st.form(key="quiz_form"):
        for i, (key, value) in enumerate(preguntes.items()):
            st.subheader(f"{key}: {value['pregunta']}")
            respostes_usuari[key] = st.radio("Tria una opció:", options=value["opcions"], key=f"q{i}", label_visibility="collapsed")
        if st.form_submit_button("Envia Respostes 🚀", use_container_width=True):
            score = sum(1 for key, value in preguntes.items() if respostes_usuari[key] == value["correcta"])
            total = len(preguntes)
            st.header("Resultats del teu Quiz:")
            for key, value in preguntes.items():
                if respostes_usuari[key] == value["correcta"]:
                    st.success(f"**{key}:** Correcte! ✔️ La teva resposta va ser '{respostes_usuari[key]}'.")
                else:
                    st.error(f"**{key}:** Incorrecte. ❌ La resposta correcta era '{value['correcta']}', però vas triar '{respostes_usuari[key]}'.")

            st.divider()
            percentatge = score / total
            st.subheader(f"Puntuació Final: {score}/{total}")

            if percentatge == 1.0:
                st.balloons()
                st.success("🎉 **FELICITATS! Puntuació Perfecta!** 🎉")
                # <<< CANVIA AQUÍ el GIF si vols un altre
                st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3NqZzJjYjJtdG90Z3B4dDA2NnZobGgwem82ZHNlYnJzYjY4YWYwaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kyLYXonQYYfwY/giphy.gif", caption="Espectacular! Ho saps tot!")
            elif percentatge >= 0.7:
                st.info("Molt bona feina! Has dominat la majoria dels conceptes.")
            elif percentatge >= 0.5:
                st.warning("No està malament, però repassa les seccions on has fallat!")
            else:
                st.error("Sembla que necessites repassar una mica més. Torna a explorar les seccions!")

# --- 4. CONTINGUT DE LES PÀGINES ---------------------------------------------

# 🏠 PÀGINA D'INICI
if pagina == "🏠 Inici":
    st.title("🌿 Benvingut/da a l'Explorador d'Hàbitats!")
    st.markdown("Aquesta és la teva eina interactiva per estudiar la **UF1: Caracterització d'hàbitats**. Navega per les diferents seccions utilitzant el menú de l'esquerra.")

    # <<< CANVIA AQUÍ la URL de la imatge principal pels teus dibuixos
    st.image("https://cdni.iconscout.com/illustration/premium/thumb/environmental-conservation-5588326-4674828.png", caption="Un mosaic de la biodiversitat que estudiarem.")
    st.header("Què trobaràs aquí?")
    st.divider()

    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        st.subheader("🌍 Biomes i Climogrames")
        st.markdown("Aprèn què és un bioma, com es classifiquen i la clau per entendre'ls: els climogrames.")
        # <<< CANVIA AQUÍ
        st.image("https://www.svgrepo.com/show/447285/biome.svg", width=120)
    with col2:
        st.subheader("🏞️ Hàbitats Locals")
        st.markdown("Viatja des de les regions d'Espanya fins als boscos, pinedes i alzinars de Catalunya.")
        # <<< CANVIA AQUÍ
        st.image("https://www.svgrepo.com/show/458825/landscape-mountain-nature.svg", width=120)
    with col3:
        st.subheader("🌱 Conceptes i Quiz")
        st.markdown("Domina conceptes com 'biodiversitat' i 'adaptació', i posa a prova els teus coneixements!")
        # <<< CANVIA AQUÍ
        st.image("https://www.svgrepo.com/show/443213/quiz-game.svg", width=120)

# 🌍 PÀGINA DE BIOMES
elif pagina == "🌍 Biomes de la Terra":
    st.title("🌍 Biomes de la Terra")
    st.markdown("Els grans paisatges del nostre planeta, definits pel clima i la vegetació que hi predomina.")

    with st.expander("🤔 Què és un Bioma?"):
        st.markdown("* És el conjunt de comunitats (plantes, animals) que ocupen una mateixa àrea geogràfica.\n* Són unitats de gran extensió amb una vegetació i un clima característics.")
    st.subheader("Classificació de Biomes (Whittaker)")
    st.markdown("Una de les maneres més famoses de classificar els biomes és el diagrama de Whittaker, que relaciona la **temperatura mitjana anual** i la **precipitació anual**.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Whittaker_biomes_plot.svg/1200px-Whittaker_biomes_plot.svg.png", caption="Diagrama de Biomes de Whittaker (Això és un gràfic científic, no una foto!)")

    st.header("Explora alguns Biomes Principals")
    tab_names = ["🌳 Bosc Temperat", "🏜️ Desert", "🌴 Selva Tropical", "🌱 Praderies", "🌲 Bosc Mediterrani"]
    tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_names)

    with tab1:
        st.subheader("🌳 Bosc Temperat Caducifoli")
        # <<< CANVIA AQUÍ
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/autumn-season-3488582-2922253.png", caption="Il·lustració d'un bosc a la tardor.")
        st.markdown("* **Clima:** Temperat, amb estacions marcades. Precipitacions abundants.\n* **Flora:** Arbres de fulla caduca (roures, faigs, aurons).\n* **Fauna:** Cérvols, esquirols, guineus i ossos.")
    with tab2:
        st.subheader("🏜️ Desert")
        # <<< CANVIA AQUÍ
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/desert-2974248-2475143.png", caption="Il·lustració d'un paisatge desèrtic.")
        st.markdown("* **Clima:** Molt àrid (< 250 mm/any). Grans contrastos de temperatura.\n* **Flora:** Plantes xeròfiles (cactus, atzavares) adaptades a la sequera.\n* **Fauna:** Rèptils i animals nocturns per evitar la calor.")
    with tab3:
        st.subheader("🌴 Selva Tropical")
        # <<< CANVIA AQUÍ
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/jungle-7360589-5997931.png", caption="Il·lustració d'una selva exuberant.")
        st.markdown("* **Clima:** Càlid i molt plujós tot l'any. Poca variació de temperatura.\n* **Flora:** Enorme diversitat, vegetació molt densa, lianes i epífites.\n* **Fauna:** La major biodiversitat del planeta.")
    with tab4:
        st.subheader("🌱 Praderies (Estepa)")
        # <<< CANVIA AQUÍ
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/savanna-3995808-3306169.png", caption="Il·lustració d'una praderia.")
        st.markdown("* **Clima:** Semiàrid amb gran amplitud tèrmica (hiverns freds, estius càlids).\n* **Flora:** Domini d'herbes (gramínies). Pocs arbres.\n* **Fauna:** Grans herbívors com bisons, antílops o cavalls.")
    with tab5:
        st.subheader("🌲 Bosc Mediterrani (Escleròfil)")
        # <<< CANVIA AQUÍ
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/olive-tree-4034873-3337227.png", caption="Il·lustració d'un paisatge mediterrani.")
        st.markdown("* **Clima:** Estius calorosos i secs; hiverns suaus i plujosos.\n* **Flora:** Vegetació de fulla dura i perenne (alzines, sureres, pins).\n* **Fauna:** Adaptada a la sequera (porc senglar, guineu, linx).")

# 📊 PÀGINA DE CLIMOGRAMES
elif pagina == "📊 Climogrames":
    st.title("📊 Què és un Climograma?")
    st.markdown("És una eina gràfica per entendre el clima d'un lloc d'un cop d'ull. Mostra **Temperatura** i **Precipitació** al llarg de l'any.")

    st.info("""
    **Com llegir-lo?**
    *   **Línia (vermella):** Representa la temperatura mitjana mensual.
    *   **Barres (blaves):** Representen la precipitació total mensual.
    *   **TRUC:** Si la línia de temperatura està per sobre de les barres de pluja, indica un **període d'aridesa** (sequera).
    """, icon="💡")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Climograph_of_Alice_Springs%2C_Northern_Territory%2C_Australia.png/800px-Climograph_of_Alice_Springs%2C_Northern_Territory%2C_Australia.png", caption="Exemple de climograma (Alice Springs, Austràlia). Clarament desèrtic.")
    st.header("Exemples de Climogrames per Tipus de Clima")
    c_tab1, c_tab2, c_tab3, c_tab4 = st.tabs(["Clima Equatorial", "Clima Mediterrani", "Clima Desèrtic", "Clima Polar"])
    with c_tab1:
        st.subheader("Equatorial (Akassa)")
        st.markdown("*Temperatures altes i pluges constants tot l'any.*")
        st.image("https://i.imgur.com/LhBvW4f.png")
    with c_tab2:
        st.subheader("Mediterrani (Nàpols)")
        st.markdown("*Estius secs i calorosos, hiverns suaus i plujosos.*")
        st.image("https://i.imgur.com/1Gv2F1B.png")
    with c_tab3:
        st.subheader("Desèrtic (Alexandria)")
        st.markdown("*Pluges gairebé inexistents.*")
        st.image("https://i.imgur.com/Uf1C29X.png")
    with c_tab4:
        st.subheader("Polar (Thule)")
        st.markdown("*Temperatures quasi sempre sota 0°C i precipitacions escasses.*")
        st.image("https://i.imgur.com/U6LzJ7m.png")

# 🇪🇸 PÀGINA D'HÀBITATS A ESPANYA
elif pagina == "🇪🇸 Hàbitats a Espanya":
    st.title("🇪🇸 Hàbitats d'Espanya")
    st.markdown("La Península Ibèrica és un punt calent de biodiversitat gràcies a la seva posició i relleu.")
    st.header("Les Grans Regions Biogeogràfiques")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Regiones_biogeogr%C3%A1ficas_de_Espa%C3%B1a_2001.png/800px-Regiones_biogeogr%C3%A1ficas_de_Espa%C3%B1a_2001.png", caption="Mapa de les regions biogeogràfiques d'Espanya.")
    bio_tab1, bio_tab2, bio_tab3 = st.tabs(["🟢 Regió Eurosiberiana", "🟠 Regió Mediterrània", "🌋 Regió Macaronèsica"])
    with bio_tab1:
        st.subheader("Regió Eurosiberiana")
        st.markdown("Correspon al nord humit (la 'Espanya verda').\n* **Clima:** Suau i plujós.\n* **Vegetació:** Boscos caducifolis (roures, faigs).")
    with bio_tab2:
        st.subheader("Regió Mediterrània")
        st.markdown("Ocupa la major part de la península.\n* **Clima:** Estius càlids i secs.\n* **Vegetació:** Bosc perennifoli (alzina, pi).")
    with bio_tab3:
        st.subheader("Regió Macaronèsica")
        st.markdown("Correspon a les Illes Canàries.\n* **Clima:** Molt divers per l'altitud i els vents alisis.\n* **Vegetació:** Gran diversitat i endemismes (laurisilva, pi canari).")

# 🏞️ PÀGINA D'HÀBITATS DE CATALUNYA
elif pagina == "🏞️ Hàbitats de Catalunya":
    st.title("🏞️ Hàbitats de Catalunya")
    st.markdown("La nostra terra té una riquesa d'hàbitats extraordinària, des del Pirineu fins a la costa.")
    hab_tab1, hab_tab2, hab_tab3, hab_tab4 = st.tabs(["🌳 La Fageda", "🌲 L'Alzinar", "🌲 Pineda de Pi Negre", "🌲 Pineda de Pi Roig"])
    with hab_tab1:
        st.subheader("La Fageda (Bosc de Faigs)")
        # <<< CANVIA AQUÍ
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/beech-tree-5344400-4468641.png", caption="Il·lustració d'una fageda.")
        st.markdown("Boscos de muntanya humida (Montseny, Garrotxa).")
    with hab_tab2:
        st.subheader("L'Alzinar (Bosc d'Alzina)")
        # <<< CANVIA AQUÍ
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/oak-tree-5344402-4468643.png", caption="Il·lustració d'un alzinar.")
        st.markdown("El bosc mediterrani per excel·lència.")
    with hab_tab3:
        st.subheader("Pineda de Pi Negre")
        # <<< CANVIA AQUÍ
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/pine-tree-5344405-4468646.png", caption="Il·lustració de pins a l'alta muntanya.")
        st.markdown("Forma el límit del bosc a l'alta muntanya pirinenca.")
    with hab_tab4:
        st.subheader("Pineda de Pi Roig")
        # <<< CANVIA AQUÍ
        st.image("https://cdni.iconscout.com/illustration/premium/thumb/pine-trees-on-hill-6734187-5573448.png", caption="Il·lustració de pins de muntanya mitjana.")
        st.markdown("Bosc de muntanya mitjana, molt estès al Prepirineu i Pirineu.")

# 🌱 PÀGINA DE CONCEPTES CLAU
elif pagina == "🌱 Conceptes Clau":
    st.title("🌱 Conceptes Clau")
    st.markdown("Les paraules fonamentals per entendre l'ecologia i els hàbitats.")
    conceptes_tab1, conceptes_tab2 = st.tabs(["🌎 Biodiversitat i Endemismes", "🌿 Adaptacions de la Flora"])
    with conceptes_tab1:
        st.subheader("Què és la Biodiversitat?")
        st.markdown("És l'**àmplia varietat d'éssers vius** sobre la Terra. Comprèn la diversitat genètica, d'espècies i d'ecosistemes.")
        st.subheader("Què és un Endemisme?")
        st.markdown("Un **endemisme** és una espècie que només viu de forma natural en una regió geogràfica molt concreta del món.")
        # <<< CANVIA AQUÍ - He buscat una il·lustració científica en comptes d'una foto
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Galemys_pyrenaicus.png/800px-Galemys_pyrenaicus.png", caption="Il·lustració del Desman dels Pirineus, un endemisme.")
        st.subheader("Què són els 'Hotspots'?")
        st.markdown("Són llocs del planeta amb una **concentració excepcional d'endemismes** però que estan **molt amenaçats**.")
    with conceptes_tab2:
        st.subheader("Com sobreviuen les plantes? Adaptacions!")
        st.markdown("Les plantes han desenvolupat estratègies increïbles per sobreviure.")
        with st.expander("💡 Adaptacions a la FALTA DE LLUM"):
            st.markdown("* **Fulles grans:** per captar més llum.\n* **Trepar (lianes):** per arribar a zones més altes.")
        with st.expander("🥶 Adaptacions al FRED"):
            st.markdown("* **Mida petita:** per protegir-se del vent.\n* **Perdre la fulla:** per evitar la congelació.")
        with st.expander("🥵 Adaptacions a la SEQUERA (Xeròfiles)"):
            st.markdown("* **Fulles petites o espines:** per no perdre aigua.\n* **Acumular aigua:** en teixits suculents (plantes crasses).")
        with st.expander("🔥 Adaptacions als INCENDIS (Piròfites)"):
            st.markdown("* **Rebrotada ràpida:** des de l'arrel.\n* **Pinyes seròtines:** que s'obren amb la calor del foc per alliberar llavors.")

# ❓ PÀGINA DEL QUIZ
elif pagina == "❓ Posa't a Prova!":
    run_quiz()
