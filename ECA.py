import streamlit as st

# --- Configuració General de la Pàgina ---
st.set_page_config(
    page_title="Repàs MASTER: Biogeografia, Edatisme i HIC (ULTRA COMPLET)",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Títol Principal ---
st.title("👑 REPAS MASTER D'EXAMEN: Tots els Temes Amb Detall Extès")
st.subheader("Anàlisi Rigorosa amb Exemples Específics de la Península Ibèrica")

# ==========================================================================
# SECCIÓ 1: ECOLOGIA DE MACROESCALA (BIOMES I CLIMA)
# ==========================================================================
st.header("1. 🌍 BIOMES: L'Estructura Climàtica del Planeta")
st.markdown("---")

st.subheader("1.1. Bioma: Definició Taxonòmica i Factors Zonal")
st.markdown("""
El **Bioma** és la màxima unitat biogeogràfica, una àrea extensa definida pel seu **Clima Zonal** dominant.
* **Definició Clàssica:** És el conjunt de comunitats (flora i fauna) que ocupen una mateixa **àrea geogràfica**. La seva gran extensió fa que tinguin una **vegetació climàtica uniforme** i un **clima característic**.
* **Diferenciació:** Els biomes es distingeixen per l'amplitud i les mitjanes de **Temperatura** i **Precipitació**.
    * **Exemple de Diferenciació:** La **Taigà** (fred, P baixa) es diferencia de la **Selva Tropical** (càlid, P alta).
""")

st.subheader("1.2. Climograma: Interpretació Bioclimàtica Avançada")
st.markdown("""
El Climograma permet determinar si un clima és sec o humit i la seva estacionalitat.
* **Funcionament:** La línia de T i les barres de P. La regla $1^{\circ}C \approx 2 mm$ (Walter) indica l'estrés hídric.
* **Clima Mediterrani (Exemple):** La seva clau és l'**Aridesa Estival** marcada. Això ha forçat l'evolució de la flora escleròfil·la.
""")

st.subheader("1.3. Adaptacions Morfològiques de la Flora (Profundització)")
st.table({
    "Adaptació": ["**Escleròfil·la**", "**Caducifoli**", "**Xeròfita**", "**Conífera (Aciculifòlia)**"],
    "Mecanisme": ["Fulles perennes, dures i petites amb espessiment de la cutícula.", "Pèrdua programada de fulles (abscisió) a l'època desfavorable.", "Reducció de la superfície foliar (espines) o òrgans d'emmagatzematge (succulència).", "Fulles en forma d'agulla amb baixa superfície de transpiració."],
    "Exemple i Bioma": ["Alzina (*Q. ilex*) - Mediterrani.", "Faig (*Fagus sylvatica*) - Eurosiberià.", "Cactus - Desert/Estepa.","Pi Roig (*P. sylvestris*) - Taigà/Alta Muntanya."],
})

# ==========================================================================
# SECCIÓ 2: BIODIVERSITAT, ESPECIACIÓ I AMENACES
# ==========================================================================
st.header("2. 🦋 BIODIVERSITAT, ENDEMISME I CONSERVACIÓ")
st.markdown("---")

st.subheader("2.1. Definició de Diversitat i Amplitud")
st.markdown("""
La **Diversitat (Biodiversitat)** és la varietat de la vida en tots els seus nivells.
* **Nivells:**
    1.  **Genètica:** La variació d'al·lels dins d'una població (ex: la varietat de pomes que existeix).
    2.  **Espècies:** Riquesa (nombre d'espècies) i equitat (abundància relativa).
    3.  **Ecosistemes/Hàbitats:** Varietat de biomes i processos ecològics (ex: un manglar és diferent d'una devesa).
""")

st.subheader("2.2. Amenaces Principals (Les 5 Grans Causes)")
st.markdown("""
Les **Amenaces Principals** són d'origen antropogènic (humans):
* **Pèrdua i Fragmentació d'Hàbitats:** **La causa número u.** La construcció d'infraestructures (carreteres, urbanitzacions) redueix la mida i aïlla les poblacions (efecte illa/vora).
* **Sobreexplotació:** Ús extractiu no sostenible (ex: la sobrepesca o la tala il·legal).
* **Espècies Invasores:** Espècies introduïdes que causen danys ecològics o econòmics (ex: el musclo zebrat o la vespa asiàtica).
""")

st.subheader("2.3. Endemisme, Factors i Hotspots")
st.markdown("""
* **Endemisme:** Condició d'un tàxon amb distribució **exclusivament limitada** a una àrea específica.
* **Com es Forma:** Per **aïllament geogràfic** (barrera física) que impedeix el flux gènic i porta a l'**Especiació Al·lopàtrida** (ex: la formació de l'endemisme *Baleàrica majorica* a les Balears).
* **Insularitat-Endemisme:** L'aïllament físic extrem de les illes, massissos muntanyosos o valls aïllades és el **factor que més influeix**, actuant com a laboratori evolutiu.
* **Hotspot:** Àrees amb alt **endemisme** i alta **amenaça** (ja han perdut >70% de la vegetació original). Són punts de màxima prioritat de conservació.
""")

# ==========================================================================
# SECCIÓ 3: ECOLOGIA DE MICROESCALA (HÀBITAT, BIOTIP, NÍNXOL)
# ==========================================================================
st.header("3. 🏠 CONCEPTES FUNCIONALS: Hàbitat, Biotip i Nínxol")
st.markdown("---")

st.subheader("3.1. Hàbitat i els seus Elements Essencials")
st.markdown("""
* **Hàbitat:** El **lloc físic i ambiental** on viu un organisme. La seva "adreça" biològica.
* **Elements Essencials (4 pilars):**
    1.  **Aigua:** Disponibilitat hídrica (pluja, humitat).
    2.  **Aliment:** Recursos tròfics (que menja l'espècie).
    3.  **Refugi/Cobert:** Protecció contra depredadors i inclemències (ex: espessos matolls, coves).
    4.  **Llocs de Reproducció:** Espais segurs per a la posta, nidificació o cria.
""")

st.subheader("3.2. Diferenciació Conceptual Rigorosa")
st.table({
    "Concepte": ["**Biotip**", "**Hàbitat**", "**Nínxol Ecològic**"],
    "Què Respon?": ["Qui (unitat genètica i morfològica).", "On (condicions físiques i localització).", "Com i Què fa (la funció trófica i les interaccions biòtiques)."],
})

st.subheader("3.3. Hàbitats Semi-Naturals")
st.markdown("""
* Són ecosistemes el manteniment dels quals depèn de l'**acció humana tradicional continuada**. Sense aquesta gestió (sega, pastura), l'hàbitat canviaria (ex: una pastura es convertiria en bosc).
* **Exemple:** La **Devesa andalusa i extremenya** (bosc aclarit de *Quercus* sp. per a ramaderia extensiva).
""")

# ==========================================================================
# SECCIÓ 4: BIOGEOGRAFIA IBÈRICA: FACTORS LOCALS
# ==========================================================================
st.header("4. 🇪🇸 HÀBITATS DE LA PENÍNSULA: Edatisme i Regions")
st.markdown("---")

st.subheader("4.1. Factors que Condicionen els Hàbitats d'Espanya")
st.markdown("""
La diversitat d'hàbitats ibèrics es deu a l'orografia, el clima i, fonamentalment, l'**Edatisme** (la ciència del sòl):
* **Edatisme (Tipus de Sòl):** La geologia (roca mare) és el factor que, després del clima, més limita la flora.
    * **Sòls Silicis (Àcids):** Derivats de granit, pissarra. Flora **Calcífuga** (ex: *Quercus pyrenaica*, castanyer).
    * **Sòls Calcaris (Bàsics):** Derivats de calcària. Flora **Calcícola** (ex: *Quercus ilex*, savina).
""")

st.subheader("4.2. Regions Biogeogràfiques Espanyoles")
st.table({
    "Regió": ["**Mediterrània**", "**Eurosiberiana (Atlàntica)**", "**Macaronèsica**"],
    "Característica": ["Dominant. Clima estival sec. Flora Escleròfil·la.", "Nord i muntanyes. Clima humit i temperat. Flora Caducifòlia.", "Illes Canàries. Biota única i alts endemismes."],
})

# ==========================================================================
# SECCIÓ 5: VEGETACIÓ POTENCIAL I FORMACIONS
# ==========================================================================
st.header("5. 🌳 FORMACIONS VEGETALS: Estructura i Nomenclatura")
st.markdown("---")

st.subheader("5.1. Vegetació Potencial (Climax)")
st.markdown("""
* És la formació vegetal que es desenvoluparia sense interferència humana, sota les condicions edafoclimàtiques actuals.
""")

st.subheader("5.2. Tipus de Boscos i Noms Científics Dominants")
st.table({
    "Tipus de Bosc": ["**Bosc Caducifoli (Ombròfil)**", "**Bosc Mediterrani (Escleròfil)**", "**Bosc de Ribera (Azonal)**"],
    "Dominants Científics": ["*Fagus sylvatica* (Faig), *Quercus robur* (Roure).", "*Quercus ilex* (Alzina), *Quercus suber* (Suro).", "*Populus alba* (Àlber), *Salix sp.* (Salze, per l'alta humitat freàtica)."],
})

st.subheader("5.3. Estrats i Formacions Inferiors")
st.markdown("""
* **Sotabosc:** L'estrat inferior, crucial per a la regeneració i refugi. Inclou arbustos, lianes i herbàcies que creixen sota el dosser.
* **Formacions Arbustives (Matolls):**
    * **Màquia:** Matollar alt i dens (>2m). Típic estadi de recuperació del bosc.
    * **Garriga:** Matollar baix i esclarissat. Freqüent en zones calcaries amb poc sòl.
* **Formacions Herbàcies:** **Prats** (amb domini de gramínies, sovint seminaturals) i **Estepes** (zones molt seques amb vegetació herbàcia discontínua).
* **Principals Biòtops:** Classificació de grans hàbitats naturals (ex: Roques/Coves, Litorals, Aigües continentals, etc.).
""")

# ==========================================================================
# SECCIÓ 6: GESTIÓ I CONSERVACIÓ (CORINE I HIC)
# ==========================================================================
st.header("6. 🇪🇺 INVENTARIS I HIC: Eines de Conservació Europea")
st.markdown("---")

st.subheader("6.1. Projecte CORINE")
st.markdown("""
* **CORINE (Coordination of Information on the Environment):** El sistema d'inventari ambiental de la UE.
* **CORINE Biotopes:** Va ser l'inventari dels llocs naturals d'interès, establint una classificació harmonitzada i sent el precursor directe de la **Directiva Hàbitats**.
""")

st.subheader("6.2. Hàbitats d'Interès Comunitari (HIC)")
st.markdown("""
* **HIC:** Hàbitats naturals o seminaturals recollits a l'Annex I de la Directiva Hàbitats (92/43/CEE). Són considerats essencials per a la conservació europea.
* **Protecció:** La seva presència obliga els estats a declarar **Zones Especials de Conservació (ZEC)**, integrant la **Xarxa Natura 2000**.
* **Factors que Condicionen la Selecció d'HIC a Espanya:**
    * **Transició Biogeogràfica:** Es protegeixen HIC de les tres regions per cobrir la totalitat del territori (ex: Laurisilva de Macaronèsica, Prats d'alta muntanya eurosiberians).
    * **Edatisme:** Es seleccionen HIC amb dependència estricta de la roca mare, com els "Boscos de Faig sobre substrats calcaris" o "Boscos de Teix sobre substrats silicis".
""")
