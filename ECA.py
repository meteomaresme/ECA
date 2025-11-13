import streamlit as st

# --- 1. CONFIGURACIÓ DE LA PÀGINA ---------------------------------------------
st.set_page_config(
    page_title="BioEstudi | L'Eina Definitiva",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. BARRA LATERAL (SIDEBAR) -----------------------------------------------
with st.sidebar:
    st.title("📚 BioEstudi")
    st.markdown("La guia completa d'hàbitats i biomes.")
    st.caption("Materials de la UF1 - MP02 Medi Natural")

    pagina = st.radio(
        "Selecciona el capítol:",
        ["🏠 Portada", "🌍 Biomes del Món", "📊 Anàlisi Climàtica", "🇪🇸 Hàbitats d'Espanya", "🏞️ Hàbitats de Catalunya", "🧬 Conceptes Essencials", "🏆 Examen Final"],
        captions=["Inici i resum", "Els grans ecosistemes terrestres", "Interpretació de climogrames", "Regions biogeogràfiques", "El nostre entorn natural", "El vocabulari imprescindible", "Avalua el teu coneixement"]
    )
    st.divider()
    st.info("Versió optimitzada per a la lectura: tot el contingut a la vista, sense distraccions.")

# --- 3. FUNCIÓ PER AL QUIZ (EXAMEN FINAL) ------------------------------------
def run_quiz():
    st.title("🏆 Examen Final")
    st.markdown("Demostra que has assolit tots els coneixements. Sort!")
    st.divider()

    preguntes = {
        "Pregunta 1": {"pregunta": "Un climograma amb estius molt secs i temperatures altes és típic del clima...", "opcions": ["Polar", "Mediterrani", "Equatorial", "Oceànic"], "correcta": "Mediterrani"},
        "Pregunta 2": {"pregunta": "Els roures i els faigs, arbres de fulla caduca, són dominants al bioma de...", "opcions": ["Tundra", "Desert", "Bosc temperat caducifoli", "Selva tropical"], "correcta": "Bosc temperat caducifoli"},
        "Pregunta 3": {"pregunta": "Les plantes xeròfiles estan adaptades principalment a sobreviure a...", "opcions": ["La falta de llum", "El fred intens", "La sequera", "Els incendis"], "correcta": "La sequera"},
        "Pregunta 4": {"pregunta": "La 'Lagartija aranesa', que només viu als Pirineus, és un exemple clar de...", "opcions": ["Endemisme", "Hotspot", "Bioma", "Espècie invasora"], "correcta": "Endemisme"},
        "Pregunta 5": {"pregunta": "L'arbre que defineix una 'fageda' és...", "opcions": ["El pi (Pinus)", "L'alzina (Quercus ilex)", "El faig (Fagus sylvatica)", "El roure (Quercus robur)"], "correcta": "El faig (Fagus sylvatica)"},
        "Pregunta 6": {"pregunta": "La classificació europea per catalogar hàbitats naturals i seminaturals s'anomena...", "opcions": ["WWF", "Natura 2000", "CORINE Biotopes", "Whittaker"], "correcta": "CORINE Biotopes"}
    }

    if 'respostes_usuari' not in st.session_state:
        st.session_state.respostes_usuari = {key: None for key in preguntes}

    for i, (key, value) in enumerate(preguntes.items()):
        st.subheader(f"{i+1}. {value['pregunta']}")
        st.session_state.respostes_usuari[key] = st.radio("Selecciona la resposta:", options=value["opcions"], key=f"q{i}", label_visibility="collapsed")

    st.divider()
    if st.button("Finalitzar i Corregir Examen  M'examino!", use_container_width=True):
        score = sum(1 for key, value in preguntes.items() if st.session_state.respostes_usuari[key] == value["correcta"])
        total = len(preguntes)
        percentatge = score / total

        st.header("Resultats de l'Avaluació")
        st.progress(percentatge, text=f"Nota: {score} de {total}")

        if percentatge == 1.0:
            st.success("🎉 **MATRÍCULA D'HONOR!** Domini absolut de la matèria. Felicitats!")
        elif percentatge >= 0.7:
            st.info("✅ **NOTABLE!** Molt bon resultat. Tens els conceptes clars.")
        elif percentatge >= 0.5:
            st.warning(" aprobar **APROVAT.** Has superat l'examen, però revisa els errors per consolidar coneixements.")
        else:
            st.error("❌ **NECESSITA MILLORAR.** Repassa els capítols on has fallat. No et rendeixis!")

        with st.container(border=True):
            st.subheader("Revisió detallada:")
            for key, value in preguntes.items():
                resposta_usuari = st.session_state.respostes_usuari[key]
                resposta_correcta = value["correcta"]
                if resposta_usuari == resposta_correcta:
                    st.write(f"✔️ **{key}:** Correcte. La teva resposta '{resposta_usuari}' és la correcta.")
                else:
                    st.write(f"❌ **{key}:** Incorrecte. La resposta correcta era **'{resposta_correcta}'** (vas marcar '{resposta_usuari}').")

# --- 4. CONTINGUT DE LES PÀGINES ---------------------------------------------

# 🏠 PORTADA
if pagina == "🏠 Portada":
    st.title("📚 Benvingut/da a BioEstudi")
    st.markdown("#### La teva plataforma definitiva per estudiar els hàbitats i biomes de la UF1.")
    st.info("Navega pels capítols utilitzant el menú de l'esquerra. Tot el contingut és visible directament per facilitar una lectura contínua i sense interrupcions.", icon="💡")
    
    st.header("Contingut de la Guia")
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        st.metric(label="Biomes a Estudiar", value="5 Tipus")
        st.markdown("- Bosc Temperat\n- Desert\n- Selva Tropical\n- Praderies\n- Bosc Mediterrani")
    with col2:
        st.metric(label="Hàbitats de Catalunya", value="4 Boscos")
        st.markdown("- La Fageda\n- L'Alzinar\n- Pineda de Pi Negre\n- Pineda de Pi Roig")
    with col3:
        st.metric(label="Conceptes Clau", value="+15 Termes")
        st.markdown("- Biodiversitat\n- Endemisme\n- Hotspots\n- Adaptacions i més")

# 🌍 BIOMES DEL MÓN
elif pagina == "🌍 Biomes del Món":
    st.title("🌍 Biomes del Món")
    st.markdown("Els grans ecosistemes de la Terra, definits pel clima i la vegetació.")
    
    with st.container(border=True):
        st.subheader("🤔 Què és un Bioma?")
        st.write("És el conjunt de comunitats de plantes i animals que ocupen una mateixa àrea geogràfica. Són unitats de gran extensió amb una vegetació climàtica uniforme i un clima característic.")
    
    st.subheader("📖 Classificació de Biomes (Whittaker)")
    st.markdown("El diagrama de Whittaker és un dels sistemes de classificació més utilitzats. Relaciona la **temperatura mitjana anual** i la **precipitació anual** per definir els diferents biomes.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Whittaker_biomes_plot.svg/1200px-Whittaker_biomes_plot.svg.png", caption="Gràfic de Whittaker. Eina clau, no una imatge decorativa.")
    st.divider()

    st.header("Exploració dels Biomes Principals")

    # Bosc Temperat Caducifoli
    st.subheader("🌳 Bosc Temperat Caducifoli")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- **Clima:** Temperat, amb 4 estacions marcades. Precipitacions abundants (750–1500 mm).\n- **Flora:** Arbres de fulla caduca com roures, faigs i aurons.\n- **Fauna:** Gran diversitat, incloent cérvols, esquirols, guineus i ossos.")
    with col2:
        st.info("🧠 **Dada Clau:** La paraula 'caducifoli' ve del llatí 'cadūcus' (caure) i 'folium' (fulla). La caiguda de les fulles a la tardor és una adaptació per conservar energia i aigua durant l'hivern fred.")
    st.divider()

    # Desert
    st.subheader("🏜️ Desert")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- **Clima:** Molt àrid (< 250 mm/any). Grans oscil·lacions tèrmiques entre el dia i la nit.\n- **Flora:** Plantes xeròfiles altament adaptades, com cactus i suculentes, amb fulles petites o espines.\n- **Fauna:** Animals adaptats a la sequera, sovint amb hàbits nocturns, com rèptils, escorpins i petits rosegadors.")
    with col2:
        st.info("🧠 **Dada Clau:** No tots els deserts són calorosos. N'hi ha de freds, com el desert del Gobi a l'Àsia, on les temperatures hivernals poden baixar fins a -40°C.")
    st.divider()
    
    # Selva Tropical
    st.subheader("🌴 Selva Tropical")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- **Clima:** Càlid i molt plujós durant tot l'any, sense estacions marcades.\n- **Flora:** La més diversa del planeta, estructurada en estrats (pisos). Abunden les lianes i les plantes epífites.\n- **Fauna:** Enorme biodiversitat, amb milions d'espècies d'insectes, amfibis, rèptils i mamífers.")
    with col2:
        st.info("🧠 **Dada Clau:** Tot i que només cobreixen un 6% de la superfície terrestre, les selves tropicals alberguen més de la meitat de totes les espècies de plantes i animals del món.")
    st.divider()

    # Praderies
    st.subheader("🌱 Praderies (Estepa)")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- **Clima:** Semiàrid amb gran amplitud tèrmica (estius calorosos, hiverns freds).\n- **Flora:** Domini absolut de les herbes (gramínies). Els arbres són escassos, limitats a les ribes dels rius.\n- **Fauna:** Grans mamífers herbívors com bisons, antílops i cavalls salvatges.")
    with col2:
        st.info("🧠 **Dada Clau:** Els sòls de les praderies són extremadament fèrtils, motiu pel qual moltes d'aquestes àrees s'han convertit en les principals zones agrícoles del món (el "graner del món").")
    st.divider()

    # Bosc Mediterrani
    st.subheader("🌲 Bosc Mediterrani (Escleròfil)")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- **Clima:** Estius calorosos i secs; hiverns suaus i plujosos.\n- **Flora:** Vegetació escleròfil·la (de fulla dura i perenne) adaptada a la sequera estival, com alzines, sureres i pins.\n- **Fauna:** Adaptada a la sequera, com el porc senglar, la guineu, la geneta i el linx ibèric.")
    with col2:
        st.info("🧠 **Dada Clau:** Moltes plantes mediterrànies són piròfites, és a dir, estan adaptades al foc. Algunes, com l'estepa, necessiten la calor d'un incendi per germinar les seves llavors.")

# 📊 ANÀLISI CLIMÀTICA
elif pagina == "📊 Anàlisi Climàtica":
    st.title("📊 Anàlisi Climàtica mitjançant Climogrames")
    st.markdown("El climograma és la millor eina per visualitzar les dades de clima d'una regió. A continuació s'analitzen els patrons principals.")
    
    with st.container(border=True):
        st.subheader("📖 Com llegir un Climograma?")
        st.markdown("""
        1.  **Eix Horitzontal (X):** Els mesos de l'any.
        2.  **Eix Vertical Esquerre (🌡️):** Temperatura en `°C`, representada per una **línia vermella**.
        3.  **Eix Vertical Dret (💧):** Precipitació en `mm`, representada per **barres blaves**.
        
        **Regla Clau:** Es considera que hi ha **període d'aridesa** quan la línia de temperatures està per sobre de les barres de precipitació.
        """)
    st.divider()

    st.header("Exemples de Climogrames per Clima")

    # Equatorial
    st.subheader("📈 Climograma Equatorial (Akassa, Congo)")
    st.image("https://i.imgur.com/LhBvW4f.png", caption="Climograma d'Akassa.")
    st.success("**Anàlisi:** Temperatures altes i estables durant tot l'any (línia gairebé plana). Precipitacions extremadament abundants i constants, sense cap mes sec. Correspon a la selva tropical.")

    # Mediterrani
    st.subheader("📉 Climograma Mediterrani (Nàpols, Itàlia)")
    st.image("https://i.imgur.com/1Gv2F1B.png", caption="Climograma de Nàpols.")
    st.success("**Anàlisi:** Hiverns suaus i plujosos. Estius calorosos i molt secs, amb un clar període d'aridesa on la línia de temperatura supera les precipitacions. Aquesta "depressió" estival de la pluja és la seva característica principal.")
    
    # Desèrtic
    st.subheader("🏜️ Climograma Desèrtic (Alexandria, Egipte)")
    st.image("https://i.imgur.com/Uf1C29X.png", caption="Climograma d'Alexandria.")
    st.success("**Anàlisi:** Precipitacions gairebé inexistents durant tot l'any (barres molt baixes). L'aridesa és la norma. Les temperatures poden ser altes, com en aquest cas.")

    # Polar
    st.subheader("❄️ Climograma Polar (Thule, Grenlàndia)")
    st.image("https://i.imgur.com/U6LzJ7m.png", caption="Climograma de Thule.")
    st.success("**Anàlisi:** Temperatures extremadament baixes. La línia està per sota dels 0°C la major part de l'any. Precipitacions molt escasses i sempre en forma de neu.")

# 🇪🇸 HÀBITATS D'ESPANYA
elif pagina == "🇪🇸 Hàbitats d'Espanya":
    st.title("🇪🇸 Hàbitats d'Espanya")
    st.markdown("La Península Ibèrica, per la seva ubicació i relleu, és un dels 'hotspots' de biodiversitat d'Europa.")
    
    st.header("Les Grans Regions Biogeogràfiques")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Regiones_biogeogr%C3%A1ficas_de_Espa%C3%B1a_2001.png/800px-Regiones_biogeogr%C3%A1ficas_de_Espa%C3%B1a_2001.png", caption="Mapa oficial de les regions biogeogràfiques d'Espanya.")
    
    st.subheader("🟢 Regió Eurosiberiana")
    st.markdown("Correspon al nord de la península (la 'Espanya verda': Galícia, Astúries, Cantàbria, País Basc i Pirineus).")
    st.markdown("- **Clima:** Temperat i humit, sense aridesa a l'estiu.\n- **Vegetació:** Boscos caducifolis, principalment rouredes i fagedes.")

    st.subheader("🟠 Regió Mediterrània")
    st.markdown("Ocupa el 80% de la Península i les Illes Balears. És la regió més extensa.")
    st.markdown("- **Clima:** Mediterrani, amb estius càlids i secs que provoquen estrès hídric a la vegetació.\n- **Vegetació:** Boscos perennifolis (de fulla dura), dominats per l'alzinar i les pinedes de pi blanc.")

    st.subheader("🌋 Regió Macaronèsica")
    st.markdown("Correspon a les Illes Canàries.")
    st.markdown("- **Clima:** Molt divers i complex per l'altitud i la influència dels vents alisis.\n- **Vegetació:** Gran riquesa i endemismes. Destaca el bosc de laurisilva (un fòssil vivent) i les pinedes de pi canari.")
    st.divider()

    st.header("Eines de Classificació i Protecció d'Hàbitats")
    
    st.subheader("🇪🇺 El projecte CORINE Biotopes")
    st.info("És una iniciativa de la Unió Europea per **inventariar i catalogar tots els hàbitats** naturals i seminaturals del continent. Utilitza un sistema de codis numèrics jeràrquics i serveix de base per a les polítiques de conservació.")

    st.subheader("🐦 La Xarxa Natura 2000")
    st.info("És la principal eina de protecció de la biodiversitat de la UE. Està formada per una xarxa d'espais protegits i es basa en dues directives clau:\n- **Directiva Ocells (ZEPA):** Zones d'Especial Protecció per a les Aus.\n- **Directiva Hàbitats (ZEC):** Zones Especials de Conservació per a la resta d'hàbitats i espècies.")

# 🏞️ HÀBITATS DE CATALUNYA
elif pagina == "🏞️ Hàbitats de Catalunya":
    st.title("🏞️ Hàbitats de Catalunya")
    st.markdown("Un recorregut pels boscos més emblemàtics del nostre territori, des del Pirineu fins a la costa.")
    st.divider()

    st.header("Boscos Representatius")

    # La Fageda
    st.subheader("🌳 La Fageda (Bosc de Faigs - *Fagus sylvatica*)")
    st.markdown("Es troba a les àrees muntanyoses humides del nord-est (Montseny, Garrotxa) i al Pirineu.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🌿 Flora Típica")
        st.markdown("- **Arbres:** Faig (*Fagus sylvatica*), Avet (*Abies alba*).\n- **Arbusts:** Boix (*Buxus sempervirens*), Grèvol (*Ilex aquifolium*).")
    with col2:
        st.markdown("#### 🐾 Fauna Típica")
        st.markdown("- **Amfibis:** Salamandra.\n- **Ocells:** Picot garser gros.\n- **Mamífers:** Esquirol, Guineu.")
    st.divider()

    # L'Alzinar
    st.subheader("🌲 L'Alzinar (Bosc d'Alzina - *Quercus ilex*)")
    st.markdown("És el bosc mediterrani per excel·lència. Ocupa grans extensions de terra baixa i muntanya mitjana.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🌿 Flora Típica")
        st.markdown("- **Arbres:** Alzina (*Quercus ilex*).\n- **Arbusts:** Marfull (*Viburnum tinus*), Arboç (*Arbutus unedo*).\n- **Lianes:** Arítjol (*Smilax aspera*).")
    with col2:
        st.markdown("#### 🐾 Fauna Típica")
        st.markdown("- **Ocells:** Gamarús.\n- **Mamífers:** Porc senglar, Geneta.")
    st.divider()
    
    # Pineda de Pi Negre
    st.subheader("🌲 Pineda de Pi Negre (*Pinus uncinata*)")
    st.markdown("Forma el límit superior del bosc a l'alta muntanya pirinenca (bosc subalpí).")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🌿 Flora Típica")
        st.markdown("- **Arbres:** Pi negre (*Pinus uncinata*).\n- **Arbusts:** Nabiu (*Vaccinium myrtillus*), Neret (*Rhododendron ferrugineum*).")
    with col2:
        st.markdown("#### 🐾 Fauna Típica")
        st.markdown("- **Ocells:** Picot negre, Trencapinyes.\n- **Mamífers:** Isard, Ós bru.")
    st.divider()

    # Pineda de Pi Roig
    st.subheader("🌲 Pineda de Pi Roig (*Pinus sylvestris*)")
    st.markdown("Bosc de muntanya mitjana, molt estès al Prepirineu, Pirineu i zones interiors.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🌿 Flora Típica")
        st.markdown("- **Arbres:** Pi roig (*Pinus sylvestris*).\n- **Arbusts:** Boixerola (*Arctostaphylos uva-ursi*), Boix.")
    with col2:
        st.markdown("#### 🐾 Fauna Típica")
        st.markdown("- **Ocells:** Astor, Picot negre.\n- **Mamífers:** Esquirol, Cérvol, Cabirol.")

# 🧬 CONCEPTES ESSENCIALS
elif pagina == "🧬 Conceptes Essencials":
    st.title("🧬 Conceptes Essencials")
    st.markdown("El vocabulari que tot estudiant del medi natural ha de dominar.")
    st.divider()

    st.header("Conceptes de Diversitat i Distribució")

    st.subheader("🌍 Què és la Biodiversitat?")
    st.success("Segons el Conveni Internacional de la Diversitat Biològica (Rio 1992), és l'**àmplia varietat d'éssers vius sobre la Terra**. Comprèn 3 nivells:\n1.  **Diversitat Genètica:** Varietat de gens dins i entre espècies.\n2.  **Diversitat Específica:** Nombre total d'espècies en una regió.\n3.  **Diversitat Ecològica:** Varietat d'hàbitats i ecosistemes.")
    
    st.subheader("📍 Què és un Endemisme?")
    st.success("És una espècie que té una àrea de distribució natural **molt limitada** a una regió geogràfica concreta i no es troba de forma natural enlloc més del món. **Exemple:** El *Desman dels Pirineus*.")
    
    st.subheader("🔥 Què són els 'Hotspots' (Punts Calents)?")
    st.success("Són llocs del planeta amb una **concentració excepcionalment alta d'endemismes**, però que alhora estan **molt amenaçats** per l'activitat humana. La Conca Mediterrània és un dels 34 'hotspots' mundials.")
    st.divider()
    
    st.header("Adaptacions de la Flora")
    st.markdown("Estratègies desenvolupades per les plantes per sobreviure en condicions adverses.")
    
    st.subheader("🥵 Adaptacions a la SEQUERA (Plantes Xeròfiles)")
    st.info("- **Fulles petites o transformades en espines:** Per reduir la pèrdua d'aigua per transpiració (pins, cactus).\n- **Acumulació d'aigua:** En teixits suculents (plantes crasses).\n- **Pèls i ceres:** Per reflectir la llum i crear una capa aïllant (olivera).\n- **Arrels profundes:** Per buscar aigua a capes més profundes.")
    
    st.subheader("🔥 Adaptacions als INCENDIS (Plantes Piròfites)")
    st.info("- **Rebrotada ràpida:** Capacitat de rebrotar des de la base o l'arrel després del foc (alzina).\n- **Germinació post-foc:** Llavors que necessiten la calor per germinar. El cas més famós són les **pinyes seròtines** del pi blanc (*Pinus halepensis*), que només s'obren amb la calor d'un incendi.")

    st.subheader("🥶 Adaptacions al FRED")
    st.info("- **Mida petita i creixement arran de terra:** Per aprofitar la calor del sòl i protegir-se del vent.\n- **Pèrdua de la fulla (caducifolis):** Per evitar la congelació i estalviar energia.\n- **Saba espessa:** Concentració de sucres que actua com a 'anticongelant' natural.")

    st.subheader("💡 Adaptacions a la FALTA DE LLUM")
    st.info("- **Fulles molt grans:** Per captar la màxima llum possible al sotabosc.\n- **Més clorofil·la:** Per optimitzar la fotosíntesi amb poca llum.\n- **Estratègia de trepar (lianes):** Per enfilar-se cap a la llum.")

# 🏆 EXAMEN FINAL
elif pagina == "🏆 Examen Final":
    run_quiz()
