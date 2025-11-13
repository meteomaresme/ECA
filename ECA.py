import streamlit as st

# --- 1. CONFIGURACIÓ DE LA PÀGINA ---------------------------------------------
st.set_page_config(
    page_title="Guia Definitiva: Hàbitats i Biomes",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. BARRA LATERAL (SIDEBAR) -----------------------------------------------
with st.sidebar:
    st.title("🎯 Guia d'Estudi Definitiva")
    st.markdown("UF1: Caracterització d'Hàbitats")
    st.caption("Contingut clau per a l'examen.")

    pagina = st.radio(
        "Índex de Continguts:",
        [
            "🏠 Portada",
            "📖 Conceptes Fonamentals",
            "🌍 Els Biomes de la Terra",
            "🧬 La Biodiversitat",
            "🇪🇸 Hàbitats a la Península",
            "🏞️ Hàbitats de Catalunya",
            "🛡️ Protecció d'Hàbitats",
            "🌱 Adaptacions de la Flora",
            "🏆 Examen Final"
        ],
        captions=[
            "Objectius i estructura",
            "La base de tot: bioma, hàbitat...",
            "Els grans ecosistemes del món",
            "Definició, amenaces i endemismes",
            "Les regions biogeogràfiques",
            "El nostre entorn natural",
            "Natura 2000, CORINE...",
            "Estratègies de supervivència",
            "Posa a prova els teus coneixements"
        ]
    )
    st.divider()
    st.info("Eina optimitzada per a la màxima retenció. Sort amb l'estudi!")

# --- 3. FUNCIÓ PER AL QUIZ (EXAMEN FINAL) ------------------------------------
def run_quiz():
    st.title("🏆 Examen Final")
    st.markdown("Avalua el teu domini sobre la matèria. Respon a totes les preguntes.")
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
        respostes_usuari[key] = st.radio("Selecciona la resposta:", options=value["opcions"], key=f"q{i}", label_visibility="collapsed")

    st.divider()
    if st.button("Finalitzar i Corregir Examen", use_container_width=True):
        score = sum(1 for key, value in preguntes.items() if respostes_usuari[key] == value["correcta"])
        total = len(preguntes)
        percentatge = score / total

        st.header("Resultats de l'Avaluació")
        st.progress(percentatge, text=f"Nota: {score} de {total} ({percentatge:.0%})")

        if percentatge == 1.0:
            st.success("🎉 **EXCEL·LENT (10/10)!** Domini absolut de la matèria. Estàs preparat/da!")
        elif percentatge >= 0.7:
            st.info("✅ **NOTABLE!** Molt bon resultat. Repassa només els errors.")
        elif percentatge >= 0.5:
            st.warning("👍 **APROVAT.** Has superat l'examen, però has de reforçar els punts febles.")
        else:
            st.error("❌ **CAL MILLORAR.** Repassa a fons els capítols on has fallat. Tu pots!")

        with st.container(border=True):
            st.subheader("Revisió detallada:")
            for key, value in preguntes.items():
                if respostes_usuari[key] == value["correcta"]:
                    st.write(f"✔️ **{key}:** Correcte.")
                else:
                    st.write(f"❌ **{key}:** Incorrecte. La resposta correcta era **'{value['correcta']}'**.")

# --- 4. CONTINGUT DE LES PÀGINES ---------------------------------------------

# 🏠 PORTADA
if pagina == "🏠 Portada":
    st.title("Guia Definitiva per a la UF1: Caracterització d'Hàbitats")
    st.markdown("Aquesta eina conté tota la informació essencial dels materials de l'assignatura, estructurada per a un aprenentatge eficaç i directe. L'objectiu és que assoleixis un 10 a l'examen.")
    st.success("**Instruccions:** Navega pels capítols en ordre mitjançant el menú lateral. Llegeix amb atenció i centra't en els conceptes destacats. Finalment, posa't a prova amb l'examen final.")
    st.header("Estructura de la Guia")
    st.markdown("""
    - **Conceptes Fonamentals:** Les definicions bàsiques que has de dominar.
    - **Els Biomes de la Terra:** Visió global dels grans ecosistemes.
    - **La Biodiversitat:** Què és, com es distribueix i quines amenaces té.
    - **Hàbitats a la Península:** Les grans regions que defineixen Espanya.
    - **Hàbitats de Catalunya:** Anàlisi detallada del nostre entorn.
    - **Protecció d'Hàbitats:** Marc legal i eines de conservació.
    - **Adaptacions de la Flora:** Estratègies de supervivència vegetal.
    - **Examen Final:** Test d'autoavaluació per comprovar el teu nivell.
    """)

# 📖 CONCEPTES FONAMENTALS
elif pagina == "📖 Conceptes Fonamentals":
    st.title("📖 Conceptes Fonamentals")
    st.markdown("Aquesta és la base terminològica. Domina aquestes definicions.")
    st.divider()

    st.subheader("1. Bioma")
    st.info("**Definició:** És el conjunt de comunitats (plantes, animals) que ocupen una mateixa àrea geogràfica. Són unitats de **gran extensió** amb una vegetació climàtica uniforme i un clima característic.")

    st.subheader("2. Biotop")
    st.info("**Definició:** Territori on les condicions ambientals (abiòtiques) són les adequades perquè s'hi desenvolupi una comunitat d'éssers vius (biocenosi). **Biotop (entorn) + Biocenosi (éssers vius) = Ecosistema**.")

    st.subheader("3. Hàbitat")
    st.info("**Definició:** És l'espai físic que reuneix les condicions necessàries per a la supervivència i reproducció d'una espècie. És, en essència, l'\"adreça\" o el \"domicili\" d'una espècie.")
    
    st.subheader("4. Nínxol Ecològic")
    st.info("**Definició:** És la **funció** o el \"paper\" que una espècie exerceix dins del seu hàbitat. Inclou com s'alimenta, com es comporta i com es relaciona amb altres espècies. És la seva \"professió\".")

# 🌍 ELS BIOMES DE LA TERRA
elif pagina == "🌍 Els Biomes de la Terra":
    st.title("🌍 Els Biomes de la Terra")
    st.markdown("La classificació dels biomes no és única, però sistemes com el de **Whittaker** són fonamentals. Aquest es basa en la relació entre **temperatura mitjana anual** i **precipitació anual**.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Whittaker_biomes_plot.svg/1200px-Whittaker_biomes_plot.svg.png", caption="El diagrama de Whittaker és una eina essencial per entendre la distribució dels biomes.")
    st.divider()

    st.header("Descripció dels Biomes Principals")

    st.subheader("🌳 Bosc Temperat Caducifoli")
    st.markdown("- **Clima:** Temperat, amb estacions molt marcades. Precipitacions de 750 a 1500 mm anuals.\n- **Flora:** Arbres de fulla ampla i caduca (roures, faigs, castanyers, aurons).\n- **Fauna:** Herbívors com cérvols i esquirols; carnívors com ossos i guineus.")
    st.divider()

    st.subheader("🌱 Praderies (Estepa / Sabana)")
    st.markdown("- **Clima:** Semiàrid, amb gran amplitud tèrmica entre estiu i hivern (-20ºC a 30ºC). Precipitacions de 300 a 1000 mm. La sequera estival afavoreix els incendis.\n- **Flora:** Domini de l'estrat herbaci (cereals, gespes). Els arbres són escassos.\n- **Fauna:** Grans herbívors (bisons, antílops, cavalls).")
    st.divider()

    st.subheader("🌴 Selva Tropical")
    st.markdown("- **Clima:** Càlid i molt plujós durant tot l'any (2000-4000 mm), amb poques variacions de temperatura.\n- **Flora:** Vegetació molt densa i diversa, estructurada en pisos (tridimensional). Abundància d'espècies epífites (viuen sobre altres plantes) i lianes. Una hectàrea pot contenir fins a 300 espècies d'arbres.\n- **Fauna:** La major diversitat animal del planeta, estretament lligada a la diversitat vegetal.")
    st.divider()

    st.subheader("🏜️ Desert")
    st.markdown("- **Clima:** Molt àrid, amb precipitacions inferiors a 250 mm/any. Grans oscil·lacions tèrmiques entre dia i nit.\n- **Flora:** Molt escassa i adaptada (xeròfila). Fulles petites o transformades en espines per evitar la pèrdua d'aigua. Metabolisme CAM (fixació de CO₂ durant la nit).\n- **Fauna:** Adaptada a les altes temperatures i la sequera, sovint amb comportaments crepusculars o nocturns. Rèptils són molt comuns.")
    st.divider()

    st.subheader("🌲 Bosc Mediterrani (Escleròfil)")
    st.markdown("- **Clima:** Estius calorosos i secs, hiverns suaus i plujosos.\n- **Flora:** Vegetació escleròfil·la (de fulla dura i perenne) per resistir la sequera. Arbres com alzines, sureres i pins. Estrat arbustiu molt ric.\n- **Fauna:** Adaptada a l'estacionalitat (porc senglar, guineu, linx ibèric, cabirols).")

# 🧬 LA BIODIVERSITAT
elif pagina == "🧬 La Biodiversitat":
    st.title("🧬 La Biodiversitat")
    st.markdown("La riquesa de la vida a la Terra, des dels gens fins als ecosistemes.")
    st.divider()

    st.subheader("Definició (Conveni de Rio, 1992)")
    st.success("Biodiversitat fa referència a l'**àmplia varietat d'éssers vius sobre la Terra**. És el resultat de milers de milions d'anys d'evolució, modelats per processos naturals i, cada cop més, per la influència humana.")
    
    st.subheader("Components de la Biodiversitat")
    st.markdown("""
    1.  **Diversitat Genètica:** Varietat en la informació genètica dins d'una mateixa espècie (intraespecífica) i entre diferents espècies (interespecífica).
    2.  **Diversitat Específica:** Varietat d'espècies que existeixen en una regió.
    3.  **Diversitat Ecològica:** Varietat d'ecosistemes, comunitats biològiques i els seus ambients.
    """)
    st.divider()

    st.subheader("Distribució i Amenaces")
    st.markdown("- **Distribució:** La vida no es distribueix de manera uniforme. La diversitat augmenta des dels pols cap a l'equador.\n- **Principals Amenaces d'Origen Antròpic:**\n  1. Pèrdua d'ecosistemes (urbanisme, industrialització).\n  2. Sobreexplotació de recursos naturals.\n  3. Espècies invasores.\n  4. Contaminació (sòl, aigua, aire).\n  5. Canvi climàtic.")
    st.divider()

    st.header("Conceptes Associats Clau")

    st.subheader("🔥 Hotspots (Punts Calents)")
    st.warning("**Definició:** Llocs del planeta amb una **concentració excepcionalment alta d'espècies endèmiques**, però que alhora estan **molt amenaçats** per l'activitat humana. Es reconeixen 34 hotspots, i la Conca Mediterrània n'és un.")

    st.subheader("📍 Endemismes")
    st.warning("**Definició:** Un tàxon (espècie, gènere...) que té una àrea de distribució natural **molt limitada** a una regió geogràfica concreta i no es troba de forma natural enlloc més.\n- **Causes de formació:**\n  - **Aïllament geogràfic:** La causa més comuna (illes, muntanyes, deserts).\n  - **Aïllament genètic:** Interrupció del flux genètic amb altres poblacions.\n  - **Canvis bruscos en el medi:** Glaciacions, augment de l'aridesa, etc.\n- **Exemples:** El *Desman dels Pirineus* o la *Lagartija aranesa* als Pirineus.")

# 🇪🇸 HÀBITATS A LA PENÍNSULA
elif pagina == "🇪🇸 Hàbitats a la Península":
    st.title("🇪🇸 Hàbitats a la Península: Regions Biogeogràfiques")
    st.markdown("Espanya es divideix en tres grans regions biogeogràfiques, cadascuna amb un clima i una vegetació característics.")
    st.divider()

    st.header("Les 3 Grans Regions")

    st.subheader("1. 🟢 Regió Eurosiberiana")
    st.markdown("- **Localització:** Nord i Nord-oest peninsular (la 'Espanya verda').\n- **Clima:** Temperatures suaus i estius humits, sense aridesa estival.\n- **Vegetació Dominant:** Boscos caducifolis, principalment de roures i faigs.")
    
    st.subheader("2. 🟠 Regió Mediterrània")
    st.markdown("- **Localització:** Ocupa el 80% de la Península i les Balears.\n- **Clima:** Estius càlids i secs que provoquen un notable estrès hídric.\n- **Vegetació Dominant:** Boscos perennifolis d'arbres escleròfils, on predomina l'alzina i el pi blanc.")

    st.subheader("3. 🌋 Regió Macaronèsica")
    st.markdown("- **Localització:** Illes Canàries.\n- **Clima:** Molt divers per l'altitud i la influència dels vents alisis, creant molts microclimes.\n- **Vegetació Dominant:** Gran diversitat i alts nivells d'endemismes. Destaquen els boscos de laurisilva i les pinedes de pi canari.")

# 🏞️ HÀBITATS DE CATALUNYA
elif pagina == "🏞️ Hàbitats de Catalunya":
    st.title("🏞️ Hàbitats de Catalunya")
    st.markdown("Catalunya, gràcies al seu relleu i la influència del Mediterrani, té una extraordinària riquesa d'hàbitats. Aquí analitzem els boscos més representatius.")
    st.divider()

    st.header("Principals Tipus de Boscos a Catalunya")

    st.subheader("🌳 La Fageda (Bosc de Faigs)")
    st.markdown("- **Arbre Dominant:** Faig (*Fagus sylvatica*).\n- **Flora Acompanyant:** Boix, grèvol, herba fetgera.\n- **Fauna Característica:** Salamandra, picot garser gros, esquirol.")
    st.divider()

    st.subheader("🌲 L'Alzinar (Bosc d'Alzina)")
    st.markdown("- **Arbre Dominant:** Alzina (*Quercus ilex*).\n- **Flora Acompanyant:** Marfull, arboç, arítjol (liana).\n- **Fauna Característica:** Gamarús, porc senglar, geneta.")
    st.divider()
    
    st.subheader("🌲 Pineda de Pi Negre")
    st.markdown("- **Arbre Dominant:** Pi negre (*Pinus uncinata*, sovint anomenat *P. mugo* als apunts).\n- **Localització:** Bosc subalpí, formant el límit arbori a l'alta muntanya pirinenca.\n- **Flora Acompanyant:** Nabiu, neret, ussona.\n- **Fauna Característica:** Escurçó pirinenc, picot negre, isard, ós bru.")
    st.divider()

    st.subheader("🌲 Pineda de Pi Roig")
    st.markdown("- **Arbre Dominant:** Pi roig (*Pinus sylvestris*).\n- **Localització:** Muntanya mitjana (Prepirineu, Pirineu).\n- **Flora Acompanyant:** Boixerola, boix, herba fetgera.\n- **Fauna Característica:** Astor, cérvol, cabirol, fagina.")

# 🛡️ PROTECCIÓ D'HÀBITATS
elif pagina == "🛡️ Protecció d'Hàbitats":
    st.title("🛡️ Protecció d'Hàbitats: Marc Normatiu Europeu")
    st.markdown("La conservació de la natura es regeix per un conjunt de normatives i eines de gestió a nivell europeu, estatal i autonòmic.")
    st.divider()
    
    st.header("Eines Clau de la Unió Europea")

    st.subheader("1. Projecte CORINE Biotopes")
    st.success("**Objectiu:** Crear un **inventari i catàleg** de tots els hàbitats naturals i seminaturals d'Europa. Estableix una classificació jeràrquica amb codis numèrics que serveix de base per a la gestió del territori.")

    st.subheader("2. Xarxa Natura 2000")
    st.success("**Definició:** És la **principal eina de protecció de la biodiversitat** de la UE. Consisteix en una xarxa d'àrees de conservació. Es basa en dues directives fonamentals:")
    st.markdown("""
    -   **Directiva Hàbitats:** El seu objectiu és protegir els tipus d'hàbitats i les espècies d'interès comunitari (excepte ocells). Per a això, es creen les **ZEC (Zones d'Especial Conservació)**.
    -   **Directiva Aus:** Se centra en la protecció de les aus silvestres. Per a això, es designen les **ZEPA (Zones d'Especial Protecció per a les Aus)**.
    """)
    st.warning("Una mateixa àrea pot ser ZEC i ZEPA alhora si compleix els criteris de les dues directives.")

# 🌱 ADAPTACIONS DE LA FLORA
elif pagina == "🌱 Adaptacions de la Flora":
    st.title("🌱 Adaptacions de la Flora: Estratègies de Supervivència")
    st.markdown("Les plantes, en no poder desplaçar-se, han desenvolupat mecanismes sorprenents per sobreviure a les condicions del seu entorn.")
    st.divider()

    st.subheader("🥵 Adaptacions a la Sequera (Plantes Xeròfiles)")
    st.info("- **Fulles petites, enrotllades o transformades en espines:** Per reduir la superfície de transpiració.\n- **Acumulació d'aigua:** En teixits suculents (plantes crasses).\n- **Pèls i ceres:** Creen una capa que reflecteix la llum i redueix la pèrdua d'aigua.\n- **Arrels profundes:** Per accedir a capes d'aigua subterrànies.")
    
    st.subheader("🔥 Adaptacions als Incendis (Plantes Piròfites)")
    st.info("- **Capacitat de rebrotar:** Des de l'arrel o la base després que la part aèria s'hagi cremat.\n- **Pinyes seròtines:** Estructures que només s'obren i alliberen les llavors amb la calor del foc, assegurant la regeneració (ex: Pi blanc).")

    st.subheader("🥶 Adaptacions al Fred")
    st.info("- **Mida petita i creixement arran de terra:** Per protegir-se del vent i aprofitar la calor del sòl.\n- **Fulles fosques:** Per absorbir més radiació solar.\n- **Saba amb 'anticongelants':** Alta concentració de sucres per evitar la congelació.\n- **Pèrdua de la fulla (caducifolis):** Per estalviar energia i evitar danys per congelació.")

    st.subheader("💡 Adaptacions a la Falta de Llum")
    st.info("- **Augment de la superfície foliar:** Fulles molt grans per captar la màxima llum possible.\n- **Augment de la clorofil·la:** Fulles de color verd fosc per ser més eficients.\n- **Estratègia de trepar (lianes i epífites):** Per créixer sobre altres plantes i arribar a les capçades, on hi ha més llum.")

# 🏆 EXAMEN FINAL
elif pagina == "🏆 Examen Final":
    run_quiz()
