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

# Logo de l'institut (canvieu 'img/logo.png' per la ruta real de la vostra imatge)
# st.sidebar.image("img/logo.png", caption="Institut Mercè Rodoreda") 

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
st.sidebar.info("Creat a partir dels materials de la UF1 del MP02 de Medi Natural.")


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
            # st.image("img/celebracio.gif", caption="Espectacular! Ho saps tot!") # Recorda afegir aquesta imatge
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
    
    # Recorda afegir una imatge de benvinguda a la teva carpeta 'img'
    # st.image("img/benvinguda.jpg", caption="Un mosaic de la biodiversitat que estudiarem.") 

    st.header("Què trobaràs aquí?")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🌍 Biomes i Climogrames")
        st.markdown("Aprèn què és un bioma, com es classifiquen i la clau per entendre'ls: els climogrames.")
        # st.image("img/biomes_icon.png") # Icona de mostra

    with col2:
        st.subheader("🇪🇸🏞️ Hàbitats d'Espanya i Catalunya")
        st.markdown("Viatja des de les regions biogeogràfiques d'Espanya fins als boscos, pinedes i alzinars de Catalunya.")
        # st.image("img/catalunya_icon.png") # Icona de mostra

    with col3:
        st.subheader("🌱 Conceptes i Quiz")
        st.markdown("Domina conceptes com 'biodiversitat' i 'endemisme', entén les adaptacions de les plantes i posa't a prova!")
        # st.image("img/quiz_icon.png") # Icona de mostra


# 🌍 BIOMES DE LA TERRA
elif pagina == "🌍 Biomes de la Terra":
    st.title("🌍 Biomes de la Terra")
    st.markdown("Els grans paisatges del nostre planeta, definits pel clima i la vegetació que hi predomina.")

    with st.expander("Què és un Bioma? 🤔"):
        st.markdown(
            """
            * És el conjunt de comunitats (plantes, animals) que ocupen una mateixa àrea geogràfica.
            * Són unitats de gran extensió.
            * Presenten una vegetació climàtica uniforme i un clima característic.
            """
        )
    
    st.subheader("Classificació de Biomes (Whittaker)")
    st.markdown("Una de les maneres més famoses de classificar els biomes és el diagrama de Whittaker, que relaciona la **temperatura mitjana anual** i la **precipitació anual**.")
    
    # Recorda afegir el diagrama de Whittaker a 'img/whittaker.png'
    # st.image("img/whittaker.png", caption="Diagrama de Biomes de Whittaker") 

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
        # st.image("img/bosc_temperat.jpg", caption="Exemple de bosc de faigs a la tardor.") # Imatge de mostra
        st.markdown(
            """
            * **Clima:** Temperat, amb estacions molt marcades. Estius càlids i hiverns freds. Precipitacions abundants (750–1500 mm).
            * **Flora:** Arbres de fulla ampla que cau a la tardor (caduca), com roures, faigs, castanyers i aurons.
            * **Fauna:** Gran diversitat. Herbívors com cérvols i esquirols; carnívors com guineus i ossos.
            """
        )

    with tab2:
        st.subheader("🏜️ Desert")
        # st.image("img/desert.jpg", caption="Paisatge desèrtic amb cactus.") # Imatge de mostra
        st.markdown(
            """
            * **Clima:** Molt àrid, precipitacions escasses (< 250 mm/any). Pot ser molt calorós o molt fred.
            * **Flora:** Molt escassa i altament adaptada (plantes xeròfiles). Fulles petites o transformades en espines per evitar perdre aigua. Cactus, atzavares.
            * **Fauna:** Adaptada a la sequera i la calor. Molts rèptils. Animals amb hàbits nocturns o crepusculars.
            """
        )

    with tab3:
        st.subheader("🌴 Selva Tropical")
        # st.image("img/selva.jpg", caption="Exuberant selva tropical.") # Imatge de mostra
        st.markdown(
            """
            * **Clima:** Càlid i molt plujós durant tot l'any (2000-4000 mm). Poca variació de temperatura.
            * **Flora:** La més diversa del planeta. Vegetació molt densa i estructurada en "pisos" (estrats). Abunden les epífites (que viuen sobre altres plantes) i les lianes.
            * **Fauna:** Enorme biodiversitat, especialment d'insectes, amfibis i ocells.
            """
        )
        
    with tab4:
        st.subheader("🌱 Praderies (Estepa)")
        # st.image("img/praderia.jpg", caption="Extensa praderia americana.") # Imatge de mostra
        st.markdown(
            """
            * **Clima:** Semiàrid a semihumit. Grans diferències de temperatura entre estiu i hivern (gran amplitud tèrmica). Precipitacions de 300 a 1000 mm.
            * **Flora:** Domini de l'estrat herbaci (herbes, gramínies, cereals). Pocs arbres, limitats als cursos d'aigua.
            * **Fauna:** Grans herbívors com bisons, antílops o cavalls.
            """
        )

    with tab5:
        st.subheader("🌲 Bosc Mediterrani (Escleròfil)")
        # st.image("img/bosc_med.jpg", caption="Un alzinar típic del mediterrani.") # Imatge de mostra
        st.markdown(
            """
            * **Clima:** Estius calorosos i secs; hiverns suaus i plujosos.
            * **Flora:** Vegetació escleròfil·la (de fulla dura i perenne) per resistir la sequera estival. Arbres com alzines, sureres, pins. Estrat arbustiu molt ric (llentiscle, bruc, romaní).
            * **Fauna:** Adaptada a la sequera. Herbívors com el porc senglar, cabirols; carnívors com la guineu, geneta i el linx ibèric.
            """
        )


# 📊 CLIMOGRAMES
elif pagina == "📊 Climogrames":
    st.title("📊 Què és un Climograma?")
    st.markdown("És la eina més important per entendre el clima d'un lloc d'un cop d'ull. Ens diu quan fa calor, quan fa fred, quan plou i quan hi ha sequera.")

    st.header("Com llegir un Climograma?")
    st.markdown(
        """
        Un climograma combina dues dades clau en un sol gràfic: **Temperatura** i **Precipitació**.

        1.  **Eix Horitzontal (X):** Mostra els mesos de l'any (Gener, Febrer, Març...).
        2.  **Eix Vertical Esquerre (Tª):** Mostra les temperatures $(^{\circ}C)$. Normalment es representa com una **línia (vermella o taronja)**.
        3.  **Eix Vertical Dret (P):** Mostra les precipitacions (mm). Normalment es representa com **barres (blaves)**.
        
        **TRUC:** En molts climogrames (com els dels exemples), es diu que hi ha un **període d'aridesa** (sequera) quan la línia de temperatures $(T)$ passa per sobre de les barres de precipitació $(P)$.
        """
    )
    
    # st.image("img/climograma_exemple.png", caption="Exemple d'un climograma i les seves parts.") # Imatge de mostra

    st.header("Exemples de Climogrames")
    
    c_tab1, c_tab2, c_tab3, c_tab4 = st.tabs(["Clima Equatorial (Akassa)", "Clima Mediterrani (Nàpols)", "Clima Desèrtic (Alexandria)", "Clima Polar (Thule)"])
    
    with c_tab1:
        st.subheader("Clima Equatorial")
        st.markdown("*Temperatures altes i pluges abundants tot l'any. Línia de Tª gairebé recta i alta.*")
        # st.image("img/climo_equatorial.png", caption="Climograma d'Akassa (Congo)") # Imatge de mostra
    
    with c_tab2:
        st.subheader("Clima Mediterrani")
        st.markdown("*Estius secs i calorosos, hiverns suaus i plujosos. Fixa't en la 'vall' de pluja a l'estiu!*")
        # st.image("img/climo_mediterrani.png", caption="Climograma de Nàpols (Itàlia)") # Imatge de mostra

    with c_tab3:
        st.subheader("Clima Desèrtic")
        st.markdown("*Pluges gairebé inexistents (molt escasses) tot l'any.*")
        # st.image("img/climo_desertic.png", caption="Climograma d'Alexandria (Egipte)") # Imatge de mostra

    with c_tab4:
        st.subheader("Clima Polar")
        st.markdown("*Temperatures sempre molt baixes (línia per sota dels $0^{\circ}C$) i precipitacions escasses (en forma de neu).*")
        # st.image("img/climo_polar.png", caption="Climograma de Thule (Grenlàndia)") # Imatge de mostra


# 🇪🇸 HÀBITATS A ESPANYA
elif pagina == "🇪🇸 Hàbitats a Espanya":
    st.title("🇪🇸 Hàbitats d'Espanya")
    st.markdown("La Península Ibèrica és un punt calent de biodiversitat gràcies a la seva posició i relleu.")

    st.header("Les Grans Regions Biogeogràfiques")
    st.markdown("Espanya es divideix principalment en tres grans regions biogeogràfiques:")
    
    # st.image("img/mapa_bio_espanya.png", caption="Mapa de les regions biogeogràfiques d'Espanya") # Imatge de mostra
    
    bio_tab1, bio_tab2, bio_tab3 = st.tabs(["🟢 Regió Eurosiberiana", "🟠 Regió Mediterrània", "🌋 Regió Macaronèsica"])

    with bio_tab1:
        st.subheader("🟢 Regió Eurosiberiana")
        st.markdown("Correspon al nord de la península (la 'Espanya verda').")
        st.markdown(
            """
            * **Clima:** Temperatures suaus i estius humits.
            * **Vegetació:** Boscos caducifolis, principalment roures i faigs.
            """
        )
    
    with bio_tab2:
        st.subheader("🟠 Regió Mediterrània")
        st.markdown("Ocupa el 80% de la Península i les Balears.")
        st.markdown(
            """
            * **Clima:** Estius càlids i secs, que provoquen estrès hídric.
            * **Vegetació:** Boscos perennifolis (fulla dura), dominats per l'alzina i el pi blanc.
            """
        )

    with bio_tab3:
        st.subheader("🌋 Regió Macaronèsica")
        st.markdown("Correspon a les Illes Canàries.")
        st.markdown(
            """
            * **Clima:** Molt divers segons l'altitud i l'orientació (vents alisis).
            * **Vegetació:** Una gran diversitat, des de zones subdesèrtiques a boscos de laurisilva (perennifolis) i pinedes.
            """
        )

    st.header("Classificació i Protecció d'Hàbitats")
    
    with st.expander("El projecte CORINE Biotopes 🇪🇺"):
        st.markdown(
            """
            * És una iniciativa de la Unió Europea per **catalogar tots els hàbitats** naturals i seminaturals.
            * Utilitza un sistema jeràrquic de codis numèrics per classificar-los.
            * És la base per a moltes polítiques de conservació.
            * A Catalunya, s'han identificat molts hàbitats seguint aquesta classificació, adaptant-la a la realitat catalana.
            """
        )

    with st.expander("La Xarxa Natura 2000 🐦"):
        st.markdown(
            """
            * És la principal eina de protecció de la natura de la UE.
            * Està formada per àrees de conservació de la biodiversitat.
            * Es basa en dues directives:
                1.  **Directiva Ocells (ZEPA):** Zones d'Especial Protecció per a les Aus.
                2.  **Directiva Hàbitats (ZEC):** Zones Especials de Conservació, per protegir hàbitats i espècies (excepte ocells).
            """
        )

# 🏞️ HÀBITATS DE CATALUNYA
elif pagina == "🏞️ Hàbitats de Catalunya":
    st.title("🏞️ Hàbitats de Catalunya")
    st.markdown("Gràcies al seu relleu (Pirineus, Pre-litoral, Litoral) i la influència del Mediterrani, Catalunya té una riquesa d'hàbitats extraordinària.")
    
    st.info("Explorem alguns dels boscos més emblemàtics que s'esmenten als documents.")
    
    hab_tab1, hab_tab2, hab_tab3, hab_tab4 = st.tabs([
        "🌳 La Fageda", 
        "🌲 L'Alzinar", 
        "🌲 Pineda de Pi Negre", 
        "🌲 Pineda de Pi Roig"
    ])

    with hab_tab1:
        st.subheader("🌳 La Fageda (Bosc de Faigs)")
        # st.image("img/fageda.jpg", caption="Interior d'una fageda, com la Fageda d'en Jordà.") # Imatge de mostra
        st.markdown("Es troben a les àrees muntanyoses humides del nord-est (Montseny, Garrotxa...) i al Pirineu.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🌿 Flora Típica")
            st.markdown(
                """
                * **Arbre dominant:** Faig (*Fagus sylvatica*)
                * **Altres arbres:** Avet (*Abies alba*), Blada (*Acer opalus*)
                * **Arbusts:** Boix (*Buxus sempervirens*), Grèvol (*Ilex aquifolium*)
                * **Herbes:** Herba fetgera (*Hepatica nobilis*), Jolia (*Scilla lilio-hyacinthus*)
                """
            )
        with col2:
            st.markdown("#### 🐾 Fauna Típica")
            st.markdown(
                """
                * **Amfibis:** Salamandra (*Salamandra salamandra*), Gripau comú (*Bufo bufo*)
                * **Ocells:** Picot garser gros (*Dendrocopos major*), Mallerenga carbonera (*Parus major*)
                * **Mamífers:** Esquirol (*Sciurus vulgaris*), Guineu (*Vulpes vulpes*), Rata de bosc (*Apodemus sylvaticus*)
                """
            )

    with hab_tab2:
        st.subheader("🌲 L'Alzinar (Bosc d'Alzina)")
        # st.image("img/alzinar.jpg", caption="Un alzinar mediterrani, un bosc dens i perenne.") # Imatge de mostra
        st.markdown("És el bosc mediterrani per excel·lència, ocupant grans extensions de la terra baixa i la muntanya mitjana.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🌿 Flora Típica")
            st.markdown(
                """
                * **Arbre dominant:** Alzina (*Quercus ilex*)
                * **Arbusts:** Marfull (*Viburnum tinus*), Arboç (*Arbutus unedo*), Aladern (*Rhamnus alaternus*)
                * **Lianes:** Arítjol (*Smilax aspera*), Heura (*Hedera helix*)
                * **Herbes:** Falzia negra (*Asplenium adiantum-nigrum*)
                """
            )
        with col2:
            st.markdown("#### 🐾 Fauna Típica")
            st.markdown(
                """
                * **Ocells:** Gamarús (*Strix aluco*)
                * **Mamífers:** Porc senglar (*Sus scrofa*), Geneta (*Genetta genetta*), Musaranya (*Sorex araneus*)
                * *(La fauna és molt rica i comparteix moltes espècies amb altres boscos)*
                """
            )

    with hab_tab3:
        st.subheader("🌲 Pineda de Pi Negre (*Pinus mugo*)")
        # st.image("img/pi_negre.jpg", caption="Bosc de Pi Negre a gran altitud, al Pirineu.") # Imatge de mostra
        st.markdown("Forma el límit del bosc a l'alta muntanya pirinenca. És un bosc subalpí.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🌿 Flora Típica")
            st.markdown(
                """
                * **Arbre dominant:** Pi negre (*Pinus uncinata*)
                * **Arbusts:** Nabiu (*Vaccinium myrtillus*), Neret (*Rhododendron ferrugineum*), Ginebre (*Juniperus communis*)
                * **Herbes:** Ussona (*Festuca gautieri*)
                """
            )
        with col2:
            st.markdown("#### 🐾 Fauna Típica")
            st.markdown(
                """
                * **Rèptils:** Escurçó pirinenc (*Vipera aspis*), Sargantana vivípara (*Lacerta vivipara*)
                * **Ocells:** Picot negre (*Dryocopus martius*), Trencapinyes (*Loxia curvirostra*)
                * **Mamífers:** Isard (*Rupicapra pyrenaica*), Ós bru (*Ursus arctos*), Marmota (*Marmota marmota*)
                """
            )

    with hab_tab4:
        st.subheader("🌲 Pineda de Pi Roig (*Pinus sylvestris*)")
        # st.image("img/pi_roig.jpg", caption="Pi roig, característic pel seu tronc ataronjat.") # Imatge de mostra
        st.markdown("Bosc de muntanya mitjana, molt estès al Prepirineu, Pirineu i zones interiors.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🌿 Flora Típica")
            st.markdown(
                """
                * **Arbre dominant:** Pi roig (*Pinus sylvestris*)
                * **Arbusts:** Boixerola (*Arctostaphylos uva-ursi*), Boix (*Buxus sempervirens*), Nabiu (*Vaccinium myrtillus*)
                * **Herbes:** Herba fetgera (*Hepatica nobilis*), Falzia de bosc (*Asplenium onopteris*)
                """
            )
        with col2:
            st.markdown("#### 🐾 Fauna Típica")
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
        st.subheader("Què és la Biodiversitat?")
        st.markdown(
            """
            Segons el Conveni Internacional de la Diversitat Biològica (Rio 1992), és l'**àmplia varietat d'éssers vius sobre la Terra**.
            
            Comprèn 3 nivells:
            1.  **Diversitat Genètica:** La varietat de gens dins d'una mateixa espècie.
            2.  **Diversitat Específica:** La varietat d'espècies en una regió.
            3.  **Diversitat Ecològica (d'Ecosistemes):** La varietat d'hàbitats i comunitats biològiques.
            """
        )
        
        st.subheader("Què és un Endemisme?")
        st.markdown(
            """
            Un **endemisme** és una espècie (o tàxon) que té una àrea de distribució natural **molt limitada** a una regió geogràfica concreta i no es troba de forma natural enlloc més del món.
            
            * **Exemple:** La *Lagartija aranesa* (*Iberolacerta aranica*) només es troba en una petita zona dels Pirineus.
            * **Causa:** Sovint es formen per **aïllament geogràfic** (illes, muntanyes), que fa que una població evolucioni de manera diferent.
            """
        )
        # st.image("img/endemisme.jpg", caption="El Desman dels Pirineus (Galemys pyrenaicus), un endemisme pirinenc.") # Imatge de mostra

        st.subheader("Què són els 'Hotspots' (Punts Calents)?")
        st.markdown(
            """
            Són llocs del planeta que tenen una **concentració excepcionalment alta d'espècies**, especialment d'endemismes, però que alhora estan **molt amenaçats** per l'actiu humana.
            La Conca Mediterrània és un d'aquests 34 'hotspots' mundials.
            """
        )
        # st.image("img/hotspots.png", caption="Mapa dels 'hotspots' de biodiversitat del món.") # Imatge de mostra


    with conceptes_tab2:
        st.subheader("Com sobreviuen les plantes? Adaptacions de la Flora")
        st.markdown("Les plantes no es poden moure, així que han desenvolupat adaptacions increïbles per sobreviure a les condicions del seu hàbitat.")

        with st.expander("Adaptacions a la FALTA DE LLUM 💡 (ex: sotabosc de la selva)"):
            st.markdown(
                """
                * **Augment de la superfície foliar:** Fulles molt grans per captar la màxima llum possible.
                * **Més clorofil·la:** Fulles de color verd molt fosc per optimitzar la fotosíntesi amb poca llum.
                * **Trepar:** Estratègies per enfilar-se (lianes) i arribar a zones més altes i lluminoses.
                """
            )
        
        with st.expander("Adaptacions al FRED 🥶 (ex: alta muntanya)"):
            st.markdown(
                """
                * **Mida petita:** Creixen arran de terra per aprofitar la calor del sòl i protegir-se del vent.
                * **Perdre la fulla:** Els arbres caducifolis perden les fulles per evitar la congelació i estalviar energia.
                * **Saba espessa:** Concentren sucres a la saba per actuar com a "anticongelant".
                """
            )

        with st.expander("Adaptacions a la SEQUERA (Plantes Xeròfiles) 🥵 (ex: desert, mediterrani)"):
            st.markdown(
                """
                * **Fulles petites o espines:** Redueixen la superfície de transpiració per no perdre aigua (ex: cactus, pins).
                * **Acumulació d'aigua:** Teixits suculents (plantes crasses) que emmagatzemen aigua.
                * **Pèls i ceres:** Creen una capa protectora a la fulla (color grisós o blanquinós) que reflecteix la llum i redueix la pèrdua d'aigua.
                * **Arrels profundes:** Per anar a buscar aigua a capes molt profundes del sòl.
                """
            )
            # st.image("img/xerofiles.jpg", caption="L'Olea europaea (olivera) és un exemple de planta adaptada a la sequera.") # Imatge de mostra

        with st.expander("Adaptacions als INCENDIS 🔥 (Plantes Piròfites)"):
            st.markdown(
                """
                * **Rebrotada ràpida:** Capacitat de rebrotar des de la base o l'arrel després que la part aèria s'hagi cremat.
                * **Germinació post-foc:** Algunes plantes (com el *Pinus halepensis*) tenen pinyes seròtines que només s'obren i alliberen les llavors amb la calor del foc, assegurant la repoblació.
                """
            )

# ❓ POSA'T A PROVA! (Quiz)
elif pagina == "❓ Posa't a Prova! (Quiz)":
    run_quiz()
