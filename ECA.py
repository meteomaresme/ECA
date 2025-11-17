import streamlit as st

# --- Configuració General de la Pàgina ---
st.set_page_config(
    page_title="Repàs Rigorós: Biogeografia, Conservació i HIC",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Títol Principal ---
st.title("🔬 Repàs Exhaustiu: Biomes, Biodiversitat i Hàbitats (Nivell Avançat)")
st.subheader("Anàlisi Densa de Conceptes i Factors Edafo-climàtics")

# ==========================================================================
# SECCIÓ 1: ECOLOGIA DE MACROESCALA (BIOMES I CLIMA)
# ==========================================================================
st.header("1. 🌍 BIOMES I CLIMA: L'Escala Geogràfica")
st.markdown("---")

st.subheader("1.1. Bioma: Definició Taxonòmica i Factors Zonal")
st.markdown("""
El **Bioma** és la major unitat d'organització ecològica terrestre, representant un sistema amb una estructura d'ecosistemes semblants.
* **Definició Clàssica:** Conjunt d'organismes i comunitats que ocupen una àrea geogràfica d'extensió continental.
* **Característiques:** Establerts per un **Clima Zonal** dominant i la conseqüent **Vegetació Climax uniforme** (determinada pels paràmetres tèrmics i hídrics).
* **Principals Biomes (Diferenciació):** Es classifiquen segons la combinació de **Temperatura** i **Precipitació**. Això dona lloc a la distribució de Boscos Tropicals, Deserts, Tundres, etc., seguint els gradients latitudinals i altitudinals.
""")

st.subheader("1.2. Climograma i Bioclimatologia")
st.markdown("""
El Climograma (o diagrama Ombrothermic de Walter) és la síntesi gràfica del règim termohídric.
* **Funció Clau:** Permet determinar la **bioclimatologia** del lloc i la presència de l'**Aridesa Fisiològica** (època seca).
* **Regla 1:2:** Escala on $1^{\circ}C$ equival a $2 mm$ de precipitació. Si la corba de T supera P, hi ha un dèficit hídric on la demanda evapotranspirativa supera l'aportació.
* **Climes Ibèrics:** S'evidencia la diferència entre el règim **Mediterrani** (T alta > P a l'estiu) i l'**Eurosiberià** (T < P durant gran part de l'any).
""")

st.subheader("1.3. Adaptacions Morfològiques de la Flora")
st.table({
    "Adaptació": ["**Escleròfil·la**", "**Caducifoli**", "**Xeròfita**", "**Psicròfita**"],
    "Mecanisme Fisiològic": ["Fulles dures, amb cutícula gruixuda i reducció de la superfície.", "Abscisió (pèrdua de fulla) estacional.", "Succulència (emmagatzematge), estomes enfonsats, espines.", "Port baix, protecció contra el vent i l'estrès per gelada."],
    "Condició Superada": ["Estrès per sequera i calor estival (Mediterrani).", "Estrès per fred o sequera estacional (Eurosiberià).", "Aridesa extrema i dèficit hídric permanent (Desert).", "Temperatures molt baixes i vents (Alta Muntanya, Tundra)."],
})

# ==========================================================================
# SECCIÓ 2: BIODIVERSITAT, ESPECIACIÓ I AMENACES
# ==========================================================================
st.header("2. 🦋 BIODIVERSITAT, AMENACES I ENDEMISME")
st.markdown("---")

st.subheader("2.1. Definició Multifacètica de Diversitat")
st.markdown("""
La **Biodiversitat** és la variació de la vida en tots els seus nivells d'organització.
* **Diversitat Genètica (Alfa):** Variabilitat d'al·lels dins d'una mateixa espècie o població. Essencial per a l'adaptació evolutiva.
* **Diversitat d'Espècies (Beta/Gamma):** Mesura la riquesa (nombre d'espècies) i l'equitat (abundància relativa).
* **Diversitat d'Ecosistemes/Hàbitats:** Varietat de comunitats, processos i ambients a un nivell paisatgístic.
""")

st.subheader("2.2. Amenaces Antropogèniques (Causes Primàries)")
st.markdown("""
Les **Amenaces Principals** a la biodiversitat són d'origen humà (antropogènic):
* **Pèrdua i Fragmentació d'Hàbitats:** El motor principal de la crisi. La reducció de l'àrea d'hàbitat i la seva divisió en petits fragments (efecte vora) aïllen les poblacions.
* **Espècies Invasores:** L'entrada d'espècies exòtiques que competeixen amb les natives o les depredan.
* **Canvi Climàtic:** Alteració ràpida dels règims climàtics, superant la capacitat d'adaptació evolutiva de moltes espècies.
""")

st.subheader("2.3. Endemisme, Insularitat i Hotspots")
st.markdown("""
* **Endemisme:** Condició d'un tàxon (espècie, subespècie) amb una àrea de distribució **exclusivament limitada** a una àrea geogràfica concreta.
* **Formació de l'Endemisme:** Resulta principalment de l'**Especiació Al·lopàtrida**, on una barrera geogràfica aïlla poblacions, interrompent el flux gènic i permetent la divergència evolutiva.
* **Insularitat:** El factor **més influent** en la gènesi d'endemismes. Un aïllament geogràfic sever (illes, massissos muntanyosos) facilita la colonització, l'aïllament i la posterior evolució in situ.
* **Hotspot de Biodiversitat:** Regió biogeogràfica que compleix simultàniament dos criteris: **Alta Riquesa** (mínim 1.500 plantes endèmiques) i **Alta Amenaça** (pèrdua >70% de vegetació original). Són llocs clau per a la inversió en conservació.
""")

# ==========================================================================
# SECCIÓ 3: ECOLOGIA DE MICROESCALA (HÀBITAT, BIOTIP, NÍNXOL)
# ==========================================================================
st.header("3. 🏡 ECOLOGIA DE MICROESCALA: Hàbitat, Biotip i Nínxol")
st.markdown("---")

st.subheader("3.1. Hàbitat i Requisits Vitals")
st.markdown("""
L'**Hàbitat** és el lloc físic definit pels seus factors abiòtics i biòtics on un organisme o població viu i es desenvolupa.
* **Importància:** Si l'hàbitat es perd, l'espècie no pot complir el seu cicle vital.
* **Elements Essencials de l'Hàbitat:** Són els factors necessaris per a la supervivència i la reproducció: **Aigua**, **Aliment/Nutrients**, **Refugi/Cobert** (protecció contra depredadors i clima) i **Llocs de Reproducció/Cria** (nidificació, posta, etc.).
""")

st.subheader("3.2. Diferenciació Conceptual Rigorosa")
st.table({
    "Concepte": ["**Biotip**", "**Hàbitat**", "**Nínxol Ecològic**"],
    "Explicació": ["Conjunt d'organismes amb el mateix **genotip** (molt específic). Unitat genètica.", "El **lloc físic** o l'entorn definit pels factors fisicoquímics i biològics. L'adreça ecològica.", "El **rol o funció** de l'espècie en l'ecosistema, definit per tots els seus requisits i interaccions biòtiques i abiòtiques. La 'professió' ecològica."],
})

st.subheader("3.3. Hàbitats Semi-Naturals")
st.markdown("""
Són ecosistemes que han evolucionat sota una **influència humana sostinguda i de baixa intensitat** (ús tradicional). Tot i estar modificats, tenen un alt valor de biodiversitat. La seva conservació sovint requereix el manteniment de l'activitat humana tradicional.
* **Exemple Clàssic:** Les **Deveses** ibèriques (pastura extensiva en bosc aclarit).
""")

# ==========================================================================
# SECCIÓ 4: BIOGEOGRAFIA IBÈRICA: FACTORS I SÒL
# ==========================================================================
st.header("4. 🇪🇸 BIOGEOGRAFIA IBÈRICA: Factors i Condicionants")
st.markdown("---")

st.subheader("4.1. Factors Conditionants dels Hàbitats d'Espanya")
st.markdown("""
La gran riquesa d'hàbitats es deu a la confluència de tres factors principals:
1.  **Clima (Zonal):** Domini Mediterrani, amb forts gradients climàtics cap al nord (Eurosiberià).
2.  **Orografia (Relief):** Massissos muntanyosos que actuen com a barreres biogeogràfiques i creen climes microzonals (solana/obaga).
3.  **Edatisme (Sòl):** La composició química de la roca mare és determinant per la flora.
""")

st.subheader("4.2. Tipus de Sòl (Edatisme) i Flora Indicadora")
st.table({
    "Tipus de Sòl": ["**Sòls Silicis**", "**Sòls Calcaris**", "**Sòls Al·luvials**"],
    "Composició/pH": ["Rocs àcids (granit, pissarra, quarsita). pH àcid.", "Rocs bàsics (calcària, dolomia). pH bàsic/neutre.", "Sediments transportats per l'aigua. Rics en nutrients."],
    "Flora Indicadora (Calcífuga/Calcícola)": ["Roure (*Q. robur*), Castanyer (*C. sativa*), Bruc (Flora Calcífuga).", "Alzina (*Q. ilex*), Pi Blanc (*P. halepensis*), Savina (Flora Calcícola).", "Bosc de Ribera (Àlbers, Salzes)."],
})

st.subheader("4.3. Regions Biogeogràfiques")
st.markdown("""
* **Regió Mediterrània:** Clima amb sequera estival (adaptació escleròfil·la).
* **Regió Eurosiberiana (o Atlàntica):** Clima humit i temperat (adaptació caducifòlia).
* **Regió Macaronèsica:** Clima subtropical insular (endemismes com la Laurisilva a Canàries).
""")

# ==========================================================================
# SECCIÓ 5: VEGETACIÓ I FORMACIONS
# ==========================================================================
st.header("5. 🌳 FORMACIONS VEGETALS: Estructura i Biòtops")
st.markdown("---")

st.subheader("5.1. Bosc (Climax) i Estrats")
st.markdown("""
* **Vegetació Potencial:** La formació vegetal clímax que s'establiria en absència de pertorbacions. És la referència ecològica de la zona.
* **Bosc:** Comunitat arbòria amb dosser tancat.
    * **Sotabosc:** L'estrat inferior (arbusts, herbes) sota la volta arbòria. Crucial per a la regeneració.
    * **Bosc de Ribera (Azonal):** Hàbitats vegetals lligats a cursos d'aigua (rius, torrents) on la disponibilitat hídrica és constant, independentment del clima zonal.
""")

st.subheader("5.2. Classificació de Formacions Arbustives i Herbàcies")
st.markdown("""
* **Formacions Arbustives (Matolls):** Solen ser estadis de degradació del bosc o hàbitats climàcics en condicions extremes (vent, fred).
    * **Màquia:** Matollar alt, dens i sovint escleròfil·le (ex: Llorer, Càdec).
    * **Garriga:** Matollar baix i esclarissat, típicament sobre sòls calcaris (ex: Romaní, Estepa).
* **Formacions Herbàcies:** Prats (amb domini de gramínies) que poden ser naturals o seminaturals (prats de sega).
* **Principals Biòtops:** Classificació de grans hàbitats naturals a la Península (Costes i Dunes, Aigües Marines, Boscos, Matolls, Roques i Coves).
""")

# ==========================================================================
# SECCIÓ 6: INVENTARIS I CONSERVACIÓ (HIC)
# ==========================================================================
st.header("6. 🇪🇺 GESTIÓ I CONSERVACIÓ: CORINE i HIC")
st.markdown("---")

st.subheader("6.1. Projecte CORINE i Natura 2000")
st.markdown("""
* **Projecte CORINE Biotopes:** L'inventari de llocs d'interès que va precedir la Directiva Hàbitats (92/43/CEE). Va establir una classificació harmonitzada dels hàbitats europeus.
* **Xarxa Natura 2000:** Xarxa ecològica europea formada per les **ZEC** (Zones Especials de Conservació, creades pels HIC) i les **ZEPA** (Zones d'Especial Protecció per a les Aus).
""")

st.subheader("6.2. Hàbitats d'Interès Comunitari (HIC)")
st.markdown("""
* **HIC:** Hàbitats naturals o seminaturals recollits a l'Annex I de la Directiva Hàbitats. Són crucials per a la biodiversitat europea i requereixen la designació de ZEC.
* **Factors de Selecció a Espanya:** La llista reflecteix la **transició biogeogràfica** (protecció d'hàbitats eurosiberians únics al sud) i la dependència del substrat geològic (HIC lligats a sòls silicats vs. calcaris).
""")
