import streamlit as st

# --- Configuració General de la Pàgina ---
st.set_page_config(
    page_title="Repàs TOTAL: Biogeografia, Ecologia i Hàbitats Ibèrics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Títol Principal ---
st.title("💯 REPAS TOTAL I DEFINITIU: Biogeografia, Ecologia i Conservació")
st.subheader("Cobertura Exhaustiva de TOTS els Conceptes de l'Examen")

# ==========================================================================
# SECCIÓ 1: ECOLOGIA DE MACROESCALA (BIOMES I CLIMA)
# ==========================================================================
st.header("1. 🌍 BIOMES: L'Expressió del Clima")
st.markdown("---")

st.subheader("1.1. Bioma: Definició i Diferenciació dels Principals")
st.markdown("""
* **Definició:** El **Bioma** és la major unitat biogeogràfica. És el conjunt de comunitats que ocupen una mateixa **àrea geogràfica d'extensió continental**. Presenta una **vegetació climàtica uniforme** i un **clima característic**.
* **Diferenciació:** Els principals biomes es distingeixen fonamentalment per la combinació dels seus paràmetres zonals: **Temperatura** i **Precipitació** (ex: Selva Tropical, Desert, Bosc Temperat, Tundra).
""")

st.subheader("1.2. Climograma i Bioclimatologia")
st.markdown("""
* **Climograma (Walter):** Representació gràfica de la **Temperatura** (línia) i la **Precipitació** (barres) mensual.
* **Com Funciona:** Utilitza l'escala $1^{\circ}C \approx 2 mm$ de P. Si la línia de T supera P, hi ha **Aridesa Fisiològica** (època seca).
* **Climes Resultants:** Permet identificar el règim i les possibles formacions vegetals.
""")

st.subheader("1.3. Adaptacions Morfològiques de la Flora")
st.table({
    "Adaptació": ["**Escleròfil·la**", "**Caducifoli**", "**Xeròfita**"],
    "Estratègia": ["Fulles dures i perennes per reduir la transpiració.", "Pèrdua de fulles a l'hivern per evitar pèrdua d'aigua per gelada/estrès estacional.", "Emmagatzematge d'aigua (succulència) i minimització de la superfície d'evaporació."],
    "Bioma/Condició": ["Bosc Mediterrani (sequera estival).", "Bosc Eurosiberià (fred hivernal/estacionalitat).", "Desert, Estepa (estrès hídric extrem)."],
})

# ==========================================================================
# SECCIÓ 2: BIODIVERSITAT, ESPECIACIÓ I AMENACES
# ==========================================================================
st.header("2. 🦋 BIODIVERSITAT, ENDEMISME I CONSERVACIÓ")
st.markdown("---")

st.subheader("2.1. Definició de Diversitat")
st.markdown("""
La **Biodiversitat** és la varietat de la vida a la Terra, estudiada a tres nivells interconnectats: **Genètica**, d'**Espècies** i d'**Ecosistemes/Hàbitats**.
""")

st.subheader("2.2. Amenaces Principals")
st.markdown("""
* Les **Amenaces Principals** són la **Pèrdua i Fragmentació d'Hàbitat** (la causa número u), la **Sobreexplotació**, la **Contaminació**, les **Espècies Invasores** i el **Canvi Climàtic**.
""")

st.subheader("2.3. Endemisme i Hotspots")
st.markdown("""
* **Endemisme:** Condició d'una espècie o tàxon que es distribueix **exclusivament** en una àrea geogràfica molt restringida.
* **Com es Forma:** El mecanisme principal és l'**aïllament geogràfic** (Especiació Al·lopàtrida), que impedeix el flux gènic i permet l'evolució única.
* **Insularitat-Endemisme:** La condició d'illa (o 'illa' ecològica) és el **factor que més influeix** per l'aïllament sever i constant que proporciona.
* **Hotspot:** Regió biogeogràfica amb **alt endemisme** ($>$ 1.500 plantes) i **alta amenaça** (pèrdua del 70% de l'hàbitat original). Són prioritats de conservació.
""")

# ==========================================================================
# SECCIÓ 3: ECOLOGIA DE MICROESCALA (HÀBITAT, BIOTIP, NÍNXOL)
# ==========================================================================
st.header("3. 🏠 HÀBITAT, BIOTIP I NÍNXOL ECOLÒGIC")
st.markdown("---")

st.subheader("3.1. Hàbitat i els seus Elements Essencials")
st.markdown("""
* **Hàbitat:** El **lloc físic o l'entorn** on viu un organisme; la seva "adreça" ecològica.
* **Elements Essencials:** Ha de proporcionar els recursos i condicions per a la vida: **Aigua, Aliment, Refugi (Cobert)** i **Llocs de Reproducció**.
* **Importància:** La pèrdua de l'hàbitat trenca el cicle vital de l'espècie.
""")

st.subheader("3.2. Diferenciació Conceptual")
st.table({
    "Concepte": ["**Biotip**", "**Hàbitat**", "**Nínxol Ecològic**"],
    "Funció": ["Qui és l'organisme (unitat genètica).", "On viu (lloc físic i recursos).", "Què fa (funció, interaccions, rols)."],
})

st.subheader("3.3. Hàbitats Semi-Naturals")
st.markdown("""
* Són hàbitats modelats i mantinguts per l'**acció humana tradicional** (ex: pastura, sega). Tenen un valor ecològic important i depenen de la continuïtat d'aquesta activitat per subsistir (ex: **Deveses**).
""")

# ==========================================================================
# SECCIÓ 4: BIOGEOGRAFIA IBÈRICA I FACTORS LOCALS
# ==========================================================================
st.header("4. 🇪🇸 HÀBITATS DE LA PENÍNSULA: Factors i Regions")
st.markdown("---")

st.subheader("4.1. Regions Biogeogràfiques")
st.markdown("""
* **Cruïlla Biogeogràfica:** Espanya és la transició entre la **Regió Mediterrània** (dominant), l'**Eurosiberiana** (o Atlàntica, al nord) i la **Macaronèsica** (Canàries).
""")

st.subheader("4.2. Factors que Condicionen els Hàbitats (Factors Edàfics)")
st.markdown("""
* **Edatisme (Tipus de Sòl):** La química del substrat (roca mare) és clau per determinar la flora:
    * **Sòls Silicis (àcids):** Per roques com Granit. Flora **calcífuga** (Roure, Castanyer).
    * **Sòls Calcaris (bàsics):** Per roques com Calcària. Flora **calcícola** (Alzina, Pi Blanc).
* **Orografia:** El relleu crea climes locals (microclimes) i barreres (ex: Solanes més seques que Obagues).
""")

# ==========================================================================
# SECCIÓ 5: VEGETACIÓ POTENCIAL I FORMACIONS
# ==========================================================================
st.header("5. 🌳 VEGETACIÓ: Potencial, Boscos i Biòtops")
st.markdown("---")

st.subheader("5.1. Vegetació Potencial")
st.markdown("""
* És la formació vegetal clímax que s'establiria sense interferència humana, sota les condicions climàtiques i edàfiques actuals.
""")

st.subheader("5.2. Classificació de Boscos i Estrats")
st.table({
    "Tipus de Bosc/Estrat": ["**Bosc Caducifoli**", "**Bosc Mediterrani**", "**Bosc de Ribera**", "**Sotabosc**"],
    "Noms Científics Clau": ["*Quercus robur* (Roure), *Fagus sylvatica* (Faig).", "*Quercus ilex* (Alzina), *Quercus suber* (Suro).", "*Populus alba* (Àlber), *Salix sp.* (Salze).", "Arbusts i herbes sota el dosser arbori."],
})

st.subheader("5.3. Formacions Arbustives i Herbàcies")
st.markdown("""
* **Formacions Arbustives (Matolls):** Estadis de degradació o hàbitats climàcics en zones seques/ventoses. Ex: **Màquia** (matollar alt i dens) o **Garriga** (matollar baix i esclarissat).
* **Formacions Herbàcies:** Prats (sega/pastura) i Estepes (dominades per gramínies).
""")

st.subheader("5.4. Principals Biòtops")
st.markdown("""
* Són les grans categories d'hàbitats presents a la Península, usades per a la classificació (ex: Boscos, Matolls/Prats, Aigües continentals, Costes/Dunes, Roques i Coves).
""")

# ==========================================================================
# SECCIÓ 6: INVENTARIS I HÀBITATS D'INTERÈS COMUNITARI
# ==========================================================================
st.header("6. 🇪🇺 INVENTARIS I HIC")
st.markdown("---")

st.subheader("6.1. Projecte CORINE")
st.markdown("""
* El **Projecte CORINE Biotopes** va ser l'inventari dels llocs naturals d'interès a la UE, sent la base per a la creació de la **Xarxa Natura 2000** i la **Directiva Hàbitats**.
""")

st.subheader("6.2. Hàbitats d'Interès Comunitari (HIC)")
st.markdown("""
* **HIC:** Hàbitats recollits a l'Annex I de la Directiva Hàbitats. Són essencials per a la biodiversitat europea i estan en perill.
* **Conservació:** Requereixen la designació de **Zones Especials de Conservació (ZEC)**, part de Natura 2000.
* **Factors que Condicionen la Selecció d'HIC a Espanya:**
    * La selecció reflecteix la **transició biogeogràfica** (protegint les peculiaritats de les regions Mediterrània, Eurosiberiana i Macaronèsica).
    * La llista és detallada per incloure hàbitats lligats a l'**Edatisme** (ex: HIC de boscos sobre calcàries vs. sobre silicats).
""")

st.markdown("---")
st.caption("Aquest document cobreix de forma exhaustiva TOTS els temes sol·licitats amb el màxim detall acadèmic. Bona sort! 🍀")
