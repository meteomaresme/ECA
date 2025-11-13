import streamlit as st

# --- Configuració de la Pàgina ---
st.set_page_config(
    page_title="Explora Hàbitats i Biomes",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Barra Lateral (Sidebar) de Navegació ---
st.sidebar.title("Menú de Navegació 🗺️")
st.sidebar.markdown("Un recorregut per la vida a la Terra, des dels biomes globals fins als hàbitats de Catalunya.")

st.sidebar.image("https://raw.githubusercontent.com/streamlit/streamlit/develop/components/extras/images/streamlit-logo-primary-colormark-darktext.png", width=200)
st.sidebar.caption("Materials de la UF1 - MP02 Medi Natural") 

pagina = st.sidebar.radio(
    "Selecciona una secció:",
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
        "Benvinguda a l'aventura!",
        "Viatja pels grans ecosistemes.",
        "Aprèn a llegir el clima.",
        "Descobreix la diversitat peninsular.",
        "El nostre entorn més proper.",
        "Paraules que tot naturalista ha de saber.",
        "Demostra el que has après!"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Aquesta app ha estat creada per ajudar-te a estudiar el contingut dels PDFs.")


# --- Funció per al Quiz ---
def run_quiz():
    st.title("❓ Posa't a Prova! (Quiz)")
    st.markdown("És hora de comprovar què has après. Selecciona la resposta correcta per a cada pregunta.")

    # Diccionari amb les preguntes i respostes
    preguntes = {
        "Pregunta 1": {
            "pregunta": "Si un climograma mostra barres de precipitació molt baixes a l'estiu i una línia de temperatura alta, de quin clima és típic?",
            "opcions": ["Polar", "Mediterrani", "Equatorial", "Oceànic"],
            "correcta": "Mediterrani"
        },
        "Pregunta 2": {
            "pregunta": "Quin bioma es caracteritza per arbres que perden la fulla a l'hivern, com els roures i els faigs?",
            "opcions": ["Tundra", "Desert", "Bosc temperat caducifoli", "Selva tropical"],
            "correcta": "Bosc temperat caducifoli"
        },
        "Pregunta 3": {
            "pregunta": "Les plantes amb fulles petites, pèls o que acumulen aigua (suculentes) s'anomenen xeròfiles i estan adaptades a...",
            "opcions": ["La falta de llum", "El fred intens", "La sequera", "Els incendis"],
            "correcta": "La sequera"
        },
        "Pregunta 4": {
            "pregunta": "Una espècie que només es troba en una regió geogràfica molt concreta (com la *Lagartija aranesa* als Pirineus) s'anomena...",
            "opcions": ["Endemisme", "Hotspot", "Bioma", "Espècie invasora"],
            "correcta": "Endemisme"
        },
        "Pregunta 5": {
            "pregunta": "Quin és l'arbre dominant en una 'fageda'?",
            "opcions": ["El pi (Pinus)", "L'alzina (Quercus ilex)", "El faig (Fagus sylvatica)", "El roure (Quercus robur)"],
            "correcta": "El faig (Fagus sylvatica)"
        },
         "Pregunta 6": {
            "pregunta": "Quina classificació europea s'utilitza per catalogar els hàbitats naturals i seminaturals?",
            "opcions": ["WWF", "Natura 2000", "CORINE Biotopes", "Whittaker"],
            "correcta": "CORINE Biotopes"
        }
    }

    # Inicialitzar un lloc per desar les respostes de l'usuari
    respostes_usuari = {}

    with st.form(key="quiz_form"):
        for i, (key, value) in enumerate(preguntes.items()):
            st.subheader(f"{key}: {value['pregunta']}")
            respostes_usuari[key] = st.radio(
                "Selecciona la teva resposta:",
                options=value["opcions"],
                key=f"q{i}",
                label_visibility="collapsed"
            )
            st.markdown("---")
        
        submitted = st.form_submit_button("Envia Respostes 🚀")

    if submitted:
        score = 0
        total_preguntes = len(preguntes)
        
        st.header("Resultats del teu Quiz:")
        
        for key, value in preguntes.items():
            resposta_correcta = value["correcta"]
            resposta_usuari = respostes_usuari[key]
            
            if resposta_usuari == resposta_correcta:
                score += 1
                st.success(f"**{key}:** Correcte! ✔️\n*La teva resposta: {resposta_usuari}*")
            else:
                st.error(f"**{key}:** Incorrecte. ❌\n*La teva resposta: {resposta_usuari}*\n*Resposta correcta: {resposta_correcta}*")
        
        st.markdown("---")
        st.subheader(f"La teva puntuació final és: {score}/{total_preguntes}")
        
        percentatge = (score / total_preguntes)
        
        if percentatge == 1.0:
            st.balloons()
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3NqZzJjYjJtdG90Z3B4dDA2NnZobGgwem82ZHNlYnJzYjY4YWYwaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kyLYXonQYYfwY/giphy.gif", caption="Espectacular! Ho saps tot!") 
            st.success("🎉 **FELICITATS! Puntuació Perfecta!** 🎉")
        elif percentatge >= 0.7:
            st.success("Molt bona feina! Has dominat la majoria dels conceptes.")
        elif percentatge >= 0.5:
            st.warning("No està malament, però repassa les seccions on has fallat!")
        else:
            st.error("Sembla que necessites repassar una mica més. Torna a explorar les seccions!")

# --- Contingut de les Pàgines ---

# 🏠 INICI
if pagina == "🏠 Inici":
    st.title("🌿 Benvingut/da a l'Explorador d'Hàbitats!")
    st.markdown("Aquesta és la teva eina interactiva per estudiar la **UF1: Caracterització d'hàbitats**. Navega per les diferents seccions utilitzant el menú de l'esquerra.")
    
    st.image("https://images.pexels.com/photos/2341830/pexels-photo-2341830.jpeg", caption="Un mosaic de la biodiversitat que estudiarem.") 

    st.header("Què trobaràs aquí?")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🌍 Biomes i Climogrames")
        st.markdown("Aprèn què és un bioma, com es classifiquen i la clau per entendre'ls: els climogrames.")
        st.image("https://cdn-icons-png.flaticon.com/512/2103/2103639.png", width=100)

    with col2:
        st.subheader("🇪🇸🏞️ Hàbitats d'Espanya i Catalunya")
        st.markdown("Viatja des de les regions biogeogràfiques d'Espanya fins als boscos, pinedes i alzinars de Catalunya.")
        st.image("https://cdn-icons-png.flaticon.com/512/10549/10549171.png", width=100)

    with col3:
        st.subheader("🌱 Conceptes i Quiz")
        st.markdown("Domina conceptes com 'biodiversitat' i 'endemisme', entén les adaptacions de les plantes i posa't a prova!")
        st.image("https://cdn-icons-png.flaticon.com/512/2643/2643323.png", width=100)


# 🌍 BIOMES DE LA TERRA
elif pagina == "🌍 Biomes de la Terra":
    st.title("🌍 Biomes de la Terra")
    st.markdown("Els grans paisatges del nostre planeta, definits pel clima i la vegetació que hi predomina.")

    with st.expander("Què és un Bioma? 🤔"):
        st.markdown(
            """
            * [cite_start]És el conjunt de comunitats (plantes, animals) que ocupen una mateixa àrea geogràfica[cite: 27].
            * [cite_start]Són unitats de gran extensió[cite: 28].
            * [cite_start]Presenten una vegetació climàtica uniforme i un clima característic[cite: 28].
            """
        )
    
    st.subheader("Classificació de Biomes (Whittaker)")
    [cite_start]st.markdown("Una de les maneres més famoses de classificar els biomes és el diagrama de Whittaker, que relaciona la **temperatura mitjana anual** i la **precipitació anual**[cite: 47, 119].")
    
    [cite_start]st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Whittaker_biomes_plot.svg/1200px-Whittaker_biomes_plot.svg.png", caption="Diagrama de Biomes de Whittaker [cite: 47, 120]") 

    st.header("Explora alguns Biomes Principals")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🌳 Bosc Temperat Caducifoli", 
        "🏜️ Desert", 
        "🌴 Selva Tropical", 
        "🌱 Praderies (Estepa)",
        "🌲 Bosc Mediterrani (Escleròfil)"
    ])

    with tab1:
        st.subheader("🌳 Bosc Temperat Caducifoli")
        st.image("https://images.pexels.com/photos/1547813/pexels-photo-1547813.jpeg", caption="Exemple de bosc de faigs a la tardor.")
        st.markdown(
            """
            * [cite_start]**Clima:** Temperat, amb estacions molt marcades[cite: 126]. [cite_start]Estius càlids i hiverns freds[cite: 125]. [cite_start]Precipitacions abundants (750–1500 mm)[cite: 126].
            * [cite_start]**Flora:** Arbres de fulla ampla que cau a la tardor (caduca) [cite: 130][cite_start], com roures, faigs, castanyers i aurons[cite: 130].
            * **Fauna:** Gran diversitat. [cite_start]Herbívors com cérvols i esquirols; carnívors com guineus i ossos[cite: 132].
            """
        )

    with tab2:
        st.subheader("🏜️ Desert")
        st.image("https://images.pexels.com/photos/2470905/pexels-photo-2470905.jpeg", caption="Paisatge desèrtic amb cactus.")
        st.markdown(
            """
            * **Clima:** Molt àrid, precipitacions escasses (< 250 mm/any). Pot ser molt calorós (dia) o fred (nit).
            * [cite_start]**Flora:** Molt escassa i altament adaptada (plantes xeròfiles)[cite: 155]. [cite_start]Fulles petites o transformades en espines per evitar perdre aigua[cite: 155]. Cactus, atzavares.
            * [cite_start]**Fauna:** Adaptada a la sequera i la calor[cite: 161]. Molts rèptils. [cite_start]Animals amb hàbits nocturns o crepusculars[cite: 160].
            """
        )

    with tab3:
        st.subheader("🌴 Selva Tropical")
        st.image("https://images.pexels.com/photos/15286/pexels-photo.jpeg", caption="Exuberant selva tropical.")
        st.markdown(
            """
            * [cite_start]**Clima:** Càlid i molt plujós durant tot l'any (2000-4000 mm)[cite: 144]. [cite_start]Poca variació de temperatura[cite: 144].
            * [cite_start]**Flora:** La més diversa del planeta[cite: 148]. [cite_start]Vegetació molt densa i estructurada en "pisos" (estrats)[cite: 147]. [cite_start]Abunden les epífites (que viuen sobre altres plantes) i les lianes[cite: 149].
            * [cite_start]**Fauna:** Enorme biodiversitat, lligada a la diversitat vegetal[cite: 150].
            """
        )
        
    with tab4:
        st.subheader("🌱 Praderies (Estepa)")
        st.image("https://images.pexels.com/photos/60013/steppe-grass-grassland-large-60013.jpeg", caption="Extensa praderia.")
        st.markdown(
            """
            * [cite_start]**Clima:** Semiàrid a semihumit[cite: 134]. [cite_start]Grans diferències de temperatura entre estiu i hivern (gran amplitud tèrmica, de -20ºC a 30ºC)[cite: 136]. [cite_start]Precipitacions de 300 a 1000 mm[cite: 135].
            * [cite_start]**Flora:** Domini de l'estrat herbaci (herbes, gramínies, cereals)[cite: 139]. [cite_start]Pocs arbres, limitats als cursos d'aigua[cite: 141].
            * [cite_start]**Fauna:** Grans herbívors com bisons, antílops o cavalls[cite: 142].
            """
        )

    with tab5:
        st.subheader("🌲 Bosc Mediterrani (Escleròfil)")
        st.image("https://upload.wikimedia.org/wikipedia/commons/3/36/Alcornocal_de_la_Almoraima.JPG", caption="Un bosc mediterrani (suro) típic.")
        st.markdown(
            """
            * [cite_start]**Clima:** Estius calorosos i secs; hiverns suaus i plujosos[cite: 892, 906, 908].
            * [cite_start]**Flora:** Vegetació escleròfil·la (de fulla dura i perenne) per resistir la sequera estival[cite: 165]. [cite_start]Arbres com alzines, sureres, pins[cite: 165]. [cite_start]Estrat arbustiu molt ric (llentiscle, bruc, romaní)[cite: 165].
            * **Fauna:** Adaptada a la sequera. [cite_start]Herbívors com el porc senglar, cabirols; carnívors com la guineu, geneta i el linx ibèric[cite: 167].
            """
        )


# 📊 CLIMOGRAMES
elif pagina == "📊 Climogrames":
    st.title("📊 Què és un Climograma?")
    [cite_start]st.markdown("És la eina més important per entendre el clima d'un lloc d'un cop d'ull. Ens diu quan fa calor, quan fa fred, quan plou i quan hi ha sequera[cite: 759, 760].")

    st.header("Com llegir un Climograma?")
    st.markdown(
        """
        [cite_start]Un climograma combina dues dades clau en un sol gràfic: **Temperatura** i **Precipitació**[cite: 761].

        1.  [cite_start]**Eix Horitzontal (X):** Mostra els mesos de l'any (Gener, Febrer, Març...)[cite: 764].
        2.  **Eix Vertical Esquerre (Tª):** Mostra les temperatures $(^{\circ}C)$. [cite_start]Normalment es representa com una **línia (vermella o taronja)**[cite: 765].
        3.  **Eix Vertical Dret (P):** Mostra les precipitacions (mm). [cite_start]Normalment es representa com **barres (blaves)**[cite: 766].
        
        **TRUC:** En molts climogrames (com els dels exemples), es diu que hi ha un **període d'aridesa** (sequera) quan la línia de temperatures $(T)$ passa per sobre de les barres de precipitació $(P)$.
        """
    )
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Climograph_of_Alice_Springs%2C_Northern_Territory%2C_Australia.png/800px-Climograph_of_Alice_Springs%2C_Northern_Territory%2C_Australia.png", caption="Exemple d'un climograma (Alice Springs, Austràlia). Es veu un clima desèrtic/àrid.")

    st.header("Exemples de Climogrames")
    
    c_tab1, c_tab2, c_tab3, c_tab4 = st.tabs(["Clima Equatorial (Akassa)", "Clima Mediterrani (Nàpols)", "Clima Desèrtic (Alexandria)", "Clima Polar (Thule)"])
    
    with c_tab1:
        [cite_start]st.subheader("Clima Equatorial [cite: 773]")
        [cite_start]st.markdown("*Temperatures altes i pluges abundants tot l'any[cite: 777]. [cite_start]Línia de Tª gairebé recta i alta[cite: 778].*")
        # Imatge del document original
        [cite_start]st.image("https://i.imgur.com/LhBvW4f.png", caption="Climograma d'Akassa (Congo) [cite: 780]")
    
    with c_tab2:
        [cite_start]st.subheader("Clima Mediterrani [cite: 892]")
        [cite_start]st.markdown("*Estius secs i calorosos, hiverns suaus i plujosos[cite: 906, 908]. [cite_start]Fixa't en la 'vall' de pluja a l'estiu! [cite: 928]*")
        # Imatge del document original
        [cite_start]st.image("https://i.imgur.com/1Gv2F1B.png", caption="Climograma de Nàpols (Itàlia) [cite: 909]")

    with c_tab3:
        [cite_start]st.subheader("Clima Desèrtic [cite: 851]")
        [cite_start]st.markdown("*Pluges gairebé inexistents (molt escasses) tot l'any[cite: 852, 890].*")
        # Imatge del document original
        [cite_start]st.image("https://i.imgur.com/Uf1C29X.png", caption="Climograma d'Alexandria (Egipte) [cite: 854]")

    with c_tab4:
        [cite_start]st.subheader("Clima Polar [cite: 998]")
        [cite_start]st.markdown("*Temperatures sempre molt baixes (línia per sota dels $0^{\circ}C$ gairebé tot l'any) i precipitacions escasses (en forma de neu)[cite: 1002, 1004, 1005].*")
        # Imatge del document original
        [cite_start]st.image("https://i.imgur.com/U6LzJ7m.png", caption="Climograma de Thule (Grenlàndia) [cite: 1006]")


# 🇪🇸 HÀBITATS A ESPANYA
elif pagina == "🇪🇸 Hàbitats a Espanya":
    st.title("🇪🇸 Hàbitats d'Espanya")
    [cite_start]st.markdown("La Península Ibèrica és un punt calent de biodiversitat gràcies a la seva posició i relleu[cite: 683].")

    st.header("Les Grans Regions Biogeogràfiques")
    [cite_start]st.markdown("Espanya es divideix principalment en tres grans regions biogeogràfiques[cite: 594]:")
    
    [cite_start]st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Regiones_biogeogr%C3%A1ficas_de_Espa%C3%B1a_2001.png/800px-Regiones_biogeogr%C3%A1ficas_de_Espa%C3%B1a_2001.png", caption="Mapa de les regions biogeogràfiques d'Espanya [cite: 613]")
    
    bio_tab1, bio_tab2, bio_tab3 = st.tabs(["🟢 Regió Eurosiberiana", "🟠 Regió Mediterrània", "🌋 Regió Macaronèsica"])

    with bio_tab1:
        [cite_start]st.subheader("🟢 Regió Eurosiberiana [cite: 596]")
        [cite_start]st.markdown("Correspon al nord de la península (la 'Espanya verda')[cite: 597, 599].")
        st.markdown(
            """
            * [cite_start]**Clima:** Temperatures suaus i estius humits[cite: 598].
            * [cite_start]**Vegetació:** Boscos caducifolis, principalment roures i faigs[cite: 599].
            """
        )
    
    with bio_tab2:
        [cite_start]st.subheader("🟠 Regió Mediterrània [cite: 600]")
        [cite_start]st.markdown("Ocupa el 80% de la Península i les Balears[cite: 601].")
        st.markdown(
            """
            * [cite_start]**Clima:** Estius càlids i secs, que provoquen estrès hídric[cite: 602].
            * [cite_start]**Vegetació:** Boscos perennifolis (fulla dura), dominats per l'alzina i el pi blanc[cite: 603].
            """
        )

    with bio_tab3:
        [cite_start]st.subheader("🌋 Regió Macaronèsica [cite: 605]")
        [cite_start]st.markdown("Correspon a les Illes Canàries[cite: 606].")
        st.markdown(
            """
            * [cite_start]**Clima:** Molt divers segons l'altitud i l'orientació (vents alisis)[cite: 606, 607].
            * [cite_start]**Vegetació:** Una gran diversitat, des de zones subdesèrtiques a boscos de laurisilva (perennifolis) i pinedes[cite: 608, 609, 610].
            """
        )

    st.header("Classificació i Protecció d'Hàbitats")
    
    [cite_start]with st.expander("El projecte CORINE Biotopes 🇪🇺 [cite: 193]"):
        st.markdown(
            """
            * [cite_start]És una iniciativa de la Unió Europea per **catalogar tots els hàbitats** naturals i seminaturals[cite: 194].
            * [cite_start]Utilitza un sistema jeràrquic de codis numèrics per classificar-los[cite: 210, 211].
            * [cite_start]És la base per a moltes polítiques de conservació[cite: 195].
            * [cite_start]A Catalunya, s'han identificat molts hàbitats seguint aquesta classificació, adaptant-la a la realitat catalana[cite: 400, 401].
            """
        )

    [cite_start]with st.expander("La Xarxa Natura 2000 🐦 [cite: 623]"):
        st.markdown(
            """
            * [cite_start]És la principal eina de protecció de la natura de la UE[cite: 624].
            * [cite_start]Està formada per àrees de conservació de la biodiversitat[cite: 625].
            * Es basa en dues directives:
                1.  [cite_start]**Directiva Ocells (ZEPA):** Zones d'Especial Protecció per a les Aus[cite: 626].
                2.  [cite_start]**Directiva Hàbitats (ZEC):** Zones Especials de Conservació, per protegir hàbitats i espècies (excepte ocells)[cite: 626, 627].
            """
        )
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Natura_2000_logo.svg/1200px-Natura_2000_logo.svg.png", width=200)


# 🏞️ HÀBITATS DE CATALUNYA
elif pagina == "🏞️ Hàbitats de Catalunya":
    st.title("🏞️ Hàbitats de Catalunya")
    [cite_start]st.markdown("Gràcies al seu relleu (Pirineus, Pre-litoral, Litoral) i la influència del Mediterrani, Catalunya té una riquesa d'hàbitats extraordinària[cite: 220].")
    
    st.info("Explorem alguns dels boscos més emblemàtics que s'esmenten als documents.")
    
    hab_tab1, hab_tab2, hab_tab3, hab_tab4 = st.tabs([
        "🌳 La Fageda", 
        "🌲 L'Alzinar", 
        "🌲 Pineda de Pi Negre", 
        "🌲 Pineda de Pi Roig"
    ])

    with hab_tab1:
        [cite_start]st.subheader("🌳 La Fageda (Bosc de Faigs) [cite: 391, 478]")
        st.image("https://upload.wikimedia.org/wikipedia/commons/1/16/Fageda_d%27en_Jord%C3%A0_-_Olot.jpg", caption="Interior d'una fageda, com la Fageda d'en Jordà.")
        [cite_start]st.markdown("Es troben a les àrees muntanyoses humides del nord-est (Montseny, Garrotxa...) i al Pirineu[cite: 478].")
        
        col1, col2 = st.columns(2)
        with col1:
            [cite_start]st.markdown("#### 🌿 Flora Típica [cite: 480]")
            st.markdown(
                """
                * **Arbre dominant:** Faig (*Fagus sylvatica*)
                * **Altres arbres:** Avet (*Abies alba*), Blada (*Acer opalus*)
                * **Arbusts:** Boix (*Buxus sempervirens*), Grèvol (*Ilex aquifolium*)
                * **Herbes:** Herba fetgera (*Hepatica nobilis*), Jolia (*Scilla lilio-hyacinthus*)
                """
            )
        with col2:
            [cite_start]st.markdown("#### 🐾 Fauna Típica [cite: 481]")
            st.markdown(
                """
                * **Amfibis:** Salamandra (*Salamandra salamandra*), Gripau comú (*Bufo bufo*)
                * **Ocells:** Picot garser gros (*Dendrocopos major*), Mallerenga carbonera (*Parus major*)
                * **Mamífers:** Esquirol (*Sciurus vulgaris*), Guineu (*Vulpes vulpes*), Rata de bosc (*Apodemus sylvaticus*)
                """
            )

    with hab_tab2:
        [cite_start]st.subheader("🌲 L'Alzinar (Bosc d'Alzina) [cite: 392, 484]")
        st.image("https://upload.wikimedia.org/wikipedia/commons/8/87/Alzinar_amb_marfull_-_Montseny.jpg", caption="Un alzinar mediterrani amb marfull, un bosc dens i perenne.")
        st.markdown("És el bosc mediterrani per excel·lència, ocupant grans extensions de la terra baixa i la muntanya mitjana.")
        
        col1, col2 = st.columns(2)
        with col1:
            [cite_start]st.markdown("#### 🌿 Flora Típica [cite: 485, 486]")
            st.markdown(
                """
                * **Arbre dominant:** Alzina (*Quercus ilex*)
                * **Arbusts:** Marfull (*Viburnum tinus*), Arboç (*Arbutus unedo*), Aladern (*Rhamnus alaternus*)
                * **Lianes:** Arítjol (*Smilax aspera*), Heura (*Hedera helix*)
                * **Herbes:** Falzia negra (*Asplenium adiantum-nigrum*)
                """
            )
        with col2:
            [cite_start]st.markdown("#### 🐾 Fauna Típica [cite: 488]")
            st.markdown(
                """
                * **Ocells:** Gamarús (*Strix aluco*)
                * **Mamífers:** Porc senglar (*Sus scrofa*), Geneta (*Genetta genetta*), Musaranya (*Sorex araneus*)
                * *(La fauna és molt rica i comparteix moltes espècies amb altres boscos)*
                """
            )

    with hab_tab3:
        [cite_start]st.subheader("🌲 Pineda de Pi Negre (*Pinus mugo*) [cite: 393, 489]")
        st.image("https://upload.wikimedia.org/wikipedia/commons/e/e0/Bosc_de_pi_negre_%28Pinus_uncinata%29_a_la_plana_d%27An%C3%ADs.jpg", caption="Bosc de Pi Negre a gran altitud, al Pirineu.")
        st.markdown("Forma el límit del bosc a l'alta muntanya pirinenca. És un bosc subalpí.")
        
        col1, col2 = st.columns(2)
        with col1:
            [cite_start]st.markdown("#### 🌿 Flora Típica [cite: 492]")
            st.markdown(
                """
                * **Arbre dominant:** Pi negre (*Pinus uncinata*)
                * **Arbusts:** Nabiu (*Vaccinium myrtillus*), Neret (*Rhododendron ferrugineum*), Ginebre (*Juniperus communis*)
                * **Herbes:** Ussona (*Festuca gautieri*)
                """
            )
        with col2:
            [cite_start]st.markdown("#### 🐾 Fauna Típica [cite: 494]")
            st.markdown(
                """
                * **Rèptils:** Escurçó pirinenc (*Vipera aspis*), Sargantana vivípara (*Lacerta vivipara*)
                * **Ocells:** Picot negre (*Dryocopus martius*), Trencapinyes (*Loxia curvirostra*)
                * **Mamífers:** Isard (*Rupicapra pyrenaica*), Ós bru (*Ursus arctos*), Talpó muntanyenc (*Microtus agrestis*)
                """
            )

    with hab_tab4:
        [cite_start]st.subheader("🌲 Pineda de Pi Roig (*Pinus sylvestris*) [cite: 394, 497]")
        st.image("https://upload.wikimedia.org/wikipedia/commons/0/07/Pi_roig_%28Pinus_sylvestris%29_a_Lles_de_Cerdanya_01.jpg", caption="Pi roig, característic pel seu tronc ataronjat.")
        st.markdown("Bosc de muntanya mitjana, molt estès al Prepirineu, Pirineu i zones interiors.")
        
        col1, col2 = st.columns(2)
        with col1:
            [cite_start]st.markdown("#### 🌿 Flora Típica [cite: 500]")
            st.markdown(
                """
                * **Arbre dominant:** Pi roig (*Pinus sylvestris*)
                * **Arbusts:** Boixerola (*Arctostaphylos uva-ursi*), Boix (*Buxus sempervirens*), Nabiu (*Vaccinium myrtillus*)
                * **Herbes:** Herba fetgera (*Hepatica nobilis*), Falzia de bosc (*Asplenium onopteris*)
                """
            )
        with col2:
            [cite_start]st.markdown("#### 🐾 Fauna Típica [cite: 502]")
            st.markdown(
                """
                * **Amfibis:** Gripau comú (*Bufo bufo*), Salamandra (*Salamandra salamandra*)
                * **Ocells:** Astor (*Accipiter gentilis*), Picot negre (*Dryocopus martius*), Mallerenga petita (*Parus ater*)
                * **Mamífers:** Esquirol (*Sciurus vulgaris*), Cérvol (*Cervus elaphus*), Cabirol (*Capreolus capreolus*), Fagina (*Martes foina*)
                """
            )


# 🌱 CONCEPTES CLAU
elif pagina == "🌱 Conceptes Clau (Biodiversitat i Adaptacions)":
    st.title("🌱 Conceptes Clau")
    st.markdown("Les paraules fonamentals per entendre l'ecologia i els hàbitats.")

    conceptes_tab1, conceptes_tab2 = st.tabs(["Biodiversitat i Endemismes 🌎", "Adaptacions de la Flora 🌿"])

    with conceptes_tab1:
        [cite_start]st.subheader("Què és la Biodiversitat? [cite: 250]")
        st.markdown(
            """
            [cite_start]Segons el Conveni Internacional de la Diversitat Biològica (Rio 1992) [cite: 251][cite_start], és l'**àmplia varietat d'éssers vius sobre la Terra**[cite: 252].
            
            [cite_start]Comprèn 3 nivells[cite: 258]:
            1.  [cite_start]**Diversitat Genètica:** La varietat de gens dins d'una mateixa espècie (intraespecífica) i entre diferents espècies (interespecífica)[cite: 261, 262].
            2.  [cite_start]**Diversitat Específica:** La varietat d'espècies en una regió[cite: 259, 260].
            3.  [cite_start]**Diversitat Ecològica (d'Ecosistemes):** La varietat d'hàbitats i comunitats biològiques[cite: 263, 264].
            """
        )
        
        [cite_start]st.subheader("Què és un Endemisme? [cite: 350]")
        st.markdown(
            """
            [cite_start]Un **endemisme** és una espècie (o tàxon) que té una àrea de distribució natural **molt limitada** a una regió geogràfica concreta i no es troba de forma natural enlloc més del món[cite: 351].
            
            * [cite_start]**Exemple:** El *Desman dels Pirineus* (*Galemys pyrenaicus*) [cite: 368] [cite_start]o la *Lagartija aranesa* (*Iberolacerta aranica*) [cite: 369] són endemismes dels Pirineus.
            * [cite_start]**Causa:** Sovint es formen per **aïllament geogràfic** (illes, muntanyes), que fa que una població evolucioni de manera diferent[cite: 353, 364, 365].
            """
        )
        [cite_start]st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Galemys_pyrenaicus_MHNT_360.jpg/1024px-Galemys_pyrenaicus_MHNT_360.jpg", caption="El Desman dels Pirineus (Galemys pyrenaicus), un endemisme pirinenc[cite: 368].")

        [cite_start]st.subheader("Què són els 'Hotspots' (Punts Calents)? [cite: 300]")
        st.markdown(
            """
            [cite_start]Són llocs del planeta que tenen una **concentració excepcionalment alta d'espècies** [cite: 288][cite_start], especialment d'endemismes, però que alhora estan **molt amenaçats** per l'activitat humana[cite: 289].
            [cite_start]La Conca Mediterrània és un d'aquests 34 'hotspots' mundials[cite: 304].
            """
        )
        [cite_start]st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Biodiversity_Hotspots_Map_2016.svg/1280px-Biodiversity_Hotspots_Map_2016.svg.png", caption="Mapa dels 'hotspots' de biodiversitat del món[cite: 335, 344].")


    with conceptes_tab2:
        [cite_start]st.subheader("Com sobreviuen les plantes? Adaptacions de la Flora [cite: 706]")
        st.markdown("Les plantes no es poden moure, així que han desenvolupat adaptacions increïbles per sobreviure a les condicions del seu hàbitat.")

        [cite_start]with st.expander("Adaptacions a la FALTA DE LLUM 💡 (ex: sotabosc de la selva) [cite: 708]"):
            st.markdown(
                """
                * [cite_start]**Augment de la superfície foliar:** Fulles molt grans per captar la màxima llum possible[cite: 710].
                * [cite_start]**Més clorofil·la:** Fulles de color verd molt fosc per optimitzar la fotosíntesi amb poca llum[cite: 713].
                * [cite_start]**Trepar:** Estratègies per enfilar-se (lianes) i arribar a zones més altes i lluminoses[cite: 714].
                """
            )
            [cite_start]st.image("https://images.pexels.com/photos/1010519/pexels-photo-1010519.jpeg", caption="Plantes epífites (com les bromèlies) i lianes competint per la llum en una selva[cite: 715].")
        
        [cite_start]with st.expander("Adaptacions al FRED 🥶 (ex: alta muntanya) [cite: 725]"):
            st.markdown(
                """
                * [cite_start]**Mida petita:** Creixen arran de terra per aprofitar la calor del sòl i protegir-se del vent[cite: 726].
                * [cite_start]**Fulles fosques:** Per augmentar la captació de calor del sol[cite: 727].
                * [cite_start]**Perdre la fulla:** Els arbres caducifolis (com el bedoll, *Betula pendula*) perden les fulles per evitar la congelació i estalviar energia[cite: 729, 730].
                * [cite_start]**Saba espessa:** Concentren sucres a la saba per actuar com a "anticongelant"[cite: 727].
                """
            )
            [cite_start]st.image("https://upload.wikimedia.org/wikipedia/commons/e/eb/Betula_pendula_0609.jpg", caption="El bedoll (*Betula pendula*), un arbre adaptat a perdre la fulla en climes freds[cite: 730].")

        [cite_start]with st.expander("Adaptacions a la SEQUERA (Plantes Xeròfiles) 🥵 (ex: desert, mediterrani) [cite: 733]"):
            st.markdown(
                """
                * [cite_start]**Fulles petites o espines:** Redueixen la superfície de transpiració per no perdre aigua (ex: cactus, pins)[cite: 738, 739].
                * [cite_start]**Acumulació d'aigua:** Teixits suculents (plantes crasses) que emmagatzemen aigua[cite: 741].
                * [cite_start]**Pèls i ceres:** Creen una capa protectora a la fulla (color grisós o blanquinós) que reflecteix la llum i redueix la pèrdua d'aigua[cite: 742].
                * [cite_start]**Arrels profundes:** Per anar a buscar aigua a capes molt profundes del sòl[cite: 743].
                """
            )
            [cite_start]st.image("https://images.pexels.com/photos/162240/olive-tree-olive-branch-italy-olive-162240.jpeg", caption="L'Olea europaea (olivera) és un exemple perfecte de planta xeròfila adaptada a la sequera[cite: 744].")

        [cite_start]with st.expander("Adaptacions als INCENDIS 🔥 (Plantes Piròfites) [cite: 745]"):
            st.markdown(
                """
                * [cite_start]**Rebrotada ràpida:** Capacitat de rebrotar des de la base o l'arrel després que la part aèria s'hagi cremat[cite: 748].
                * [cite_start]**Germinació post-foc:** Algunes plantes (com el *Pinus halepensis*) tenen pinyes seròtines que només s'obren i alliberen les llavors amb la calor del foc, assegurant la repoblació[cite: 749, 752].
                """
            )
            [cite_start]st.image("https://upload.wikimedia.org/wikipedia/commons/5/5a/Pinus_halepensis_cones_serotinous.jpg", caption="Pinyes seròtines de Pi blanc (*Pinus halepensis*) tancades, esperant el foc per obrir-se[cite: 752].")

# ❓ POSA'T A PROVA! (Quiz)
elif pagina == "❓ Posa't a Prova! (Quiz)":
    run_quiz()
