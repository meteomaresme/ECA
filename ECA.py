import streamlit as st

# --- 1. CONFIGURACIÓ DE LA PÀGINA ---------------------------------------------
st.set_page_config(
    page_title="BioEstudi | La Guia Definitiva",
    page_icon="⚡",
    layout="wide"
)

# --- TÍTOL PRINCIPAL DE L'APLICACIÓ -----------------------------------------
st.title("⚡ BioEstudi: La Guia Definitiva")
st.markdown("#### UF1: Caracterització d'Hàbitats. L'eina minimalista per a una nota de 10.")
st.divider()

# --- 2. NAVEGACIÓ SUPERIOR AMB PESTANYES -------------------------------------
tab_portada, tab_conceptes, tab_biomes, tab_biodiversitat, tab_habitats_peninsulars, tab_habitats_catalunya, tab_proteccio, tab_adaptacions, tab_examen = st.tabs([
    "🎯 Portada",
    "📖 Conceptes Clau",
    "🌍 Biomes",
    "🧬 Biodiversitat",
    "🇪🇸 Hàbitats Peninsulars",
    "🏞️ Hàbitats de Catalunya",
    "🛡️ Protecció d'Hàbitats",
    "🌱 Adaptacions",
    "🏆 Examen Final"
])

# --- PESTANYA 1: PORTADA -----------------------------------------------------
with tab_portada:
    st.header("Benvingut/da a l'eina d'estudi definitiva.")
    st.markdown("Aquesta guia interactiva conté **tota la informació essencial** que necessites, presentada de manera clara, directa i sense distraccions. Navega per les pestanyes superiors per explorar cada capítol.")
    
    st.subheader("Objectiu: Assolir un 10")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("#### 1. Aprèn els Conceptes")
        st.markdown("Domina les definicions clau: bioma, hàbitat, nínxol, endemisme, etc.")
    with col2:
        st.info("#### 2. Entén les Estructures")
        st.markdown("Compara els diferents biomes, regions biogeogràfiques i boscos de Catalunya.")
    with col3:
        st.info("#### 3. Posa't a Prova")
        st.markdown("Enfronta't a l'examen final per comprovar que has assolit tot el coneixement.")

# --- PESTANYA 2: CONCEPTES FONAMENTALS ----------------------------------------
with tab_conceptes:
    st.header("📖 Conceptes Fonamentals")
    st.markdown("La base terminològica que has de dominar a la perfecció.")
    st.divider()

    st.subheader("Bioma")
    st.success("**Definició:** Conjunt de comunitats (plantes, animals) que ocupen una **àrea geogràfica de gran extensió**. Es caracteritza per una vegetació climàtica uniforme i un clima propi.")
    
    st.subheader("Hàbitat")
    st.success("**Definició:** L'espai físic que reuneix les condicions ambientals necessàries per a la **supervivència i reproducció d'una espècie**. És la seva \"adreça\".")

    st.subheader("Nínxol Ecològic")
    st.success("**Definició:** La **funció o \"professió\"** que una espècie exerceix dins del seu hàbitat. Inclou com s'alimenta, com es comporta i com es relaciona amb altres éssers vius.")

# --- PESTANYA 3: BIOMES -------------------------------------------------------
with tab_biomes:
    st.header("🌍 Els Biomes de la Terra")
    st.markdown("La classificació de **Whittaker**, basada en la **temperatura** i la **precipitació**, és una eina clau per entendre la seva distribució.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Whittaker_biomes_plot.svg/1200px-Whittaker_biomes_plot.svg.png", caption="Diagrama de Whittaker: relació entre clima i bioma.")
    st.divider()

    st.subheader("🌳 Bosc Temperat Caducifoli")
    st.markdown("- **Clima:** 4 estacions, precipitacions de 750-1500 mm.\n- **Flora:** Arbres de fulla caduca (roures, faigs).\n- **Dada Clau:** La caiguda de la fulla és una adaptació per sobreviure a l'hivern.")
    
    st.subheader("🌱 Praderies (Estepa)")
    st.markdown("- **Clima:** Semiàrid, gran amplitud tèrmica.\n- **Flora:** Domini d'herbes (gramínies).\n- **Dada Clau:** Els seus sòls són molt fèrtils, convertits en grans zones agrícoles.")

    st.subheader("🌴 Selva Tropical")
    st.markdown("- **Clima:** Càlid i plujós tot l'any (2000-4000 mm).\n- **Flora:** Màxima diversitat mundial, estructurada en pisos.\n- **Dada Clau:** Alberga més del 50% de les espècies del planeta.")

    st.subheader("🏜️ Desert")
    st.markdown("- **Clima:** Àrid (<250 mm/any), gran oscil·lació tèrmica diària.\n- **Flora:** Escassa i adaptada (xeròfila), amb fulles reduïdes a espines.\n- **Dada Clau:** Molts animals tenen hàbits nocturns per evitar la calor extrema.")

    st.subheader("🌲 Bosc Mediterrani")
    st.markdown("- **Clima:** Estius secs i calorosos, hiverns suaus i plujosos.\n- **Flora:** De fulla dura i perenne (escleròfil·la) per suportar la sequera.\n- **Dada Clau:** Moltes de les seves plantes són piròfites (adaptades al foc).")

# --- PESTANYA 4: BIODIVERSITAT -----------------------------------------------
with tab_biodiversitat:
    st.header("🧬 Biodiversitat")
    st.markdown("La varietat de la vida a la Terra, definida al Conveni de Rio (1992).")
    st.divider()

    st.subheader("Components de la Biodiversitat")
    st.markdown("1.  **Genètica:** Varietat de gens.\n2.  **Específica:** Varietat d'espècies.\n3.  **Ecològica:** Varietat d'ecosistemes.")
    st.divider()

    st.subheader("🔥 Hotspots (Punts Calents)")
    st.warning("**Definició:** Llocs amb una **concentració excepcional d'endemismes** que, alhora, estan **molt amenaçats**. La Conca Mediterrània n'és un.")
    
    st.subheader("📍 Endemismes")
    st.warning("**Definició:** Espècie que viu **exclusivament en una regió geogràfica concreta** del món. La causa principal de la seva formació és l'aïllament geogràfic.")

# --- PESTANYA 5: HÀBITATS PENINSULARS ---------------------------------------
with tab_habitats_peninsulars:
    st.header("🇪🇸 Hàbitats a la Península: Regions Biogeogràfiques")
    st.markdown("La Península Ibèrica es divideix en tres grans regions:")
    
    st.subheader("1. 🟢 Regió Eurosiberiana (El Nord)")
    st.markdown("- **Clima:** Humit, sense sequera a l'estiu.\n- **Vegetació:** Boscos caducifolis (rouredes, fagedes).")

    st.subheader("2. 🟠 Regió Mediterrània (La major part)")
    st.markdown("- **Clima:** Estius càlids i secs.\n- **Vegetació:** Bosc perennifoli (alzinar).")

    st.subheader("3. 🌋 Regió Macaronèsica (Illes Canàries)")
    st.markdown("- **Clima:** Molt variable per l'altitud.\n- **Vegetació:** Gran riquesa d'endemismes (laurisilva).")

# --- PESTANYA 6: HÀBITATS DE CATALUNYA --------------------------------------
with tab_habitats_catalunya:
    st.header("🏞️ Hàbitats de Catalunya: Boscos Principals")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🌳 La Fageda")
        st.markdown("- **Arbre:** Faig (*Fagus sylvatica*).\n- **Fauna:** Salamandra, esquirol.")
        
        st.subheader("🌲 Pineda de Pi Negre")
        st.markdown("- **Arbre:** Pi negre (*Pinus uncinata*).\n- **Localització:** Alta muntanya pirinenca.\n- **Fauna:** Isard, ós bru.")
    with col2:
        st.subheader("🌲 L'Alzinar")
        st.markdown("- **Arbre:** Alzina (*Quercus ilex*).\n- **Fauna:** Porc senglar, geneta.")
        
        st.subheader("🌲 Pineda de Pi Roig")
        st.markdown("- **Arbre:** Pi roig (*Pinus sylvestris*).\n- **Localització:** Muntanya mitjana.\n- **Fauna:** Cérvol, cabirol.")

# --- PESTANYA 7: PROTECCIÓ D'HÀBITATS ---------------------------------------
with tab_proteccio:
    st.header("🛡️ Protecció d'Hàbitats")
    st.markdown("Eines de la Unió Europea per a la conservació de la natura.")
    
    st.subheader("1. Projecte CORINE Biotopes")
    st.success("**Què és?** Un **inventari i catàleg** de tots els hàbitats europeus, classificats amb un sistema de codis.")
    
    st.subheader("2. Xarxa Natura 2000")
    st.success("**Què és?** La **principal eina de protecció**, una xarxa d'espais protegits que es basa en dues directives:")
    st.markdown("- **Directiva Hàbitats:** Crea les **ZEC** (Zones d'Especial Conservació) per protegir hàbitats i espècies.\n- **Directiva Aus:** Crea les **ZEPA** (Zones d'Especial Protecció per a les Aus).")

# --- PESTANYA 8: ADAPTACIONS ------------------------------------------------
with tab_adaptacions:
    st.header("🌱 Adaptacions de la Flora")
    st.markdown("Mecanismes de supervivència de les plantes davant condicions adverses.")

    st.subheader("🥵 A la Sequera (Xeròfiles)")
    st.info("- **Fulles petites o espines** (menys transpiració).\n- **Acumulació d'aigua** (plantes crasses).")
    
    st.subheader("🔥 Als Incendis (Piròfites)")
    st.info("- **Capacitat de rebrotar** des de l'arrel.\n- **Pinyes seròtines** que s'obren amb la calor.")
    
    st.subheader("🥶 Al Fred")
    st.info("- **Mida petita** per protegir-se del vent.\n- **Perdre la fulla** (caducifolis) per estalviar energia.")

    st.subheader("💡 A la Falta de Llum")
    st.info("- **Fulles molt grans** per captar més llum.\n- **Trepar (lianes)** per arribar a les capçades.")

# --- PESTANYA 9: EXAMEN FINAL -----------------------------------------------
with tab_examen:
    # Aquesta funció conté tota la lògica del quiz
    def run_final_exam():
        st.header("🏆 Examen Final")
        st.markdown("És el moment de demostrar tot el que has après. Sort!")
        st.divider()

        preguntes = {
            "Pregunta 1": {"pregunta": "Un climograma amb estius molt secs i temperatures altes és típic del clima...", "opcions": ["Polar", "Mediterrani", "Equatorial", "Oceànic"], "correcta": "Mediterrani"},
            "Pregunta 2": {"pregunta": "Els roures i els faigs, arbres de fulla caduca, són dominants al bioma de...", "opcions": ["Tundra", "Desert", "Bosc temperat caducifoli", "Selva tropical"], "correcta": "Bosc temperat caducifoli"},
            "Pregunta 3": {"pregunta": "Les plantes xeròfiles estan adaptades principalment a sobreviure a...", "opcions": ["La falta de llum", "El fred intens", "La sequera", "Els incendis"], "correcta": "La sequera"},
            "Pregunta 4": {"pregunta": "Una espècie que només es troba de manera natural en una àrea geogràfica molt concreta s'anomena...", "opcions": ["Endemisme", "Hotspot", "Bioma", "Espècie invasora"], "correcta": "Endemisme"},
            "Pregunta 5": {"pregunta": "L'arbre que defineix una 'fageda' és...", "opcions": ["El pi (Pinus)", "L'alzina (Quercus ilex)", "El faig (Fagus sylvatica)", "El roure (Quercus robur)"], "correcta": "El faig (Fagus sylvatica)"},
            "Pregunta 6": {"pregunta": "La classificació europea per inventariar i catalogar hàbitats naturals i seminaturals s'anomena...", "opcions": ["WWF", "Natura 2000", "CORINE Biotopes", "Whittaker"], "correcta": "CORINE Biotopes"}
        }

        respostes_usuari = {}
        for i, (key, value) in enumerate(preguntes.items()):
            st.subheader(f"{i+1}. {value['pregunta']}")
            respostes_usuari[key] = st.radio("Tria la resposta correcta:", options=value["opcions"], key=f"q_exam_{i}", label_visibility="collapsed")

        st.divider()
        if st.button("Finalitzar i Corregir Examen", use_container_width=True):
            score = sum(1 for key, value in preguntes.items() if respostes_usuari[key] == value["correcta"])
            total = len(preguntes)
            percentatge = score / total

            st.subheader("Resultats de l'Avaluació")
            st.progress(percentatge, text=f"Nota: {score}/{total} ({percentatge:.0%})")

            if percentatge == 1.0:
                st.balloons()
                st.success("🎉 **EXCEL·LENT (10/10)!** Domini absolut. Estàs 100% preparat/da!")
            elif percentatge >= 0.7:
                st.info("✅ **NOTABLE!** Molt bon resultat. Repassa només els errors per arribar al 10.")
            elif percentatge >= 0.5:
                st.warning("👍 **APROVAT.** Has superat el mínim. Reforça els conceptes on has fallat.")
            else:
                st.error("❌ **CAL MILLORAR.** Repassa a fons els capítols. No et rendeixis!")
            
            with st.container(border=True):
                st.write("Revisió detallada:")
                for key, value in preguntes.items():
                    if respostes_usuari[key] != value["correcta"]:
                        st.write(f"❌ **{key}:** La resposta correcta era **'{value['correcta']}'**.")
    
    # Executem la funció del quiz dins de la pestanya
    run_final_exam()

# --- PEU DE PÀGINA ------------------------------------------------------------
st.divider()
st.caption("BioEstudi | Una eina creada per a l'excel·lència acadèmica.")
