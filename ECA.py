import streamlit as st

# --- Configuració General de la Pàgina ---
st.set_page_config(
    page_title="Repàs Didàctic: Biogeografia, Hàbitats i HIC",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Títol Principal ---
st.title("📚 Repàs Minimalista i Didàctic: Tots els Conceptes Clau")
st.subheader("Explicacions Clares per a l'Examen")

# ==========================================================================
# SECCIÓ 1: ECOLOGIA DE MACROESCALA (BIOMES I CLIMA)
# ==========================================================================
st.header("1. 🌍 BIOMES I CLIMA")
st.markdown("---")

st.subheader("Bioma: Definició i Diferenciació")
st.markdown("""
* **Definició:** És la unitat biogeogràfica més gran. Representa un conjunt de comunitats que ocupen una àrea extensa amb un **clima zonal (característic)** i una **vegetació climàtica uniforme**. Són la màxima expressió de la relació clima-vegetació.
* **Diferenciació:** Els principals biomes es distingeixen gairebé exclusivament pels valors mitjans de **Temperatura** i **Precipitació** (ex: Selva vs. Tundra).
""")

st.subheader("Climograma: Funcionament i Interpretació")
st.markdown("""
* **Com Funciona:** Representa la **Temperatura mitjana** (línia) i la **Precipitació total** (barres) al llarg de l'any. S'utilitza l'escala $1^{\circ}C \approx 2 mm$ de pluja.
* **Què Indica:** Ajuda a identificar l'**Aridesa Fisiològica** (època seca). Si la línia de Temperatura queda visiblement per sobre de la de Precipitació, la demanda d'evaporació supera l'aigua disponible.
* **Clima Mediterrani:** L'exemple clàssic amb una **aridesa estival** molt marcada (T alta per sobre de P a l'estiu).
""")

st.subheader("Adaptacions Morfològiques de la Flora")
st.table({
    "Adaptació": ["**Escleròfil·la**", "**Caducifoli**", "**Xeròfita**"],
    "Què és (Mecanisme)": ["Fulles dures, petites i amb cutícula gruixuda.", "Pèrdua de fulla a l'hivern.", "Emmagatzematge d'aigua (succulència) o transformació en espines."],
    "Per a Què Serveix": ["Reduir al màxim la **transpiració** durant la sequera estival.", "Evitar la pèrdua d'aigua per **congelació** o l'estrès de sequera hivernal.", "Garantir la supervivència en ambients amb **estrès hídric extrem**."],
})

# ==========================================================================
# SECCIÓ 2: BIODIVERSITAT I ESPECIACIÓ
# ==========================================================================
st.header("2. 🦋 BIODIVERSITAT, AMENACES I ENDEMISME")
st.markdown("---")

st.subheader("Diversitat (Biodiversitat)")
st.markdown("""
* **Definició:** La **varietat de vida** a la Terra. Es mesura a tres nivells interconnectats: **Genètica** (dins l'espècie), d'**Espècies** (riquesa i abundància) i d'**Ecosistemes** (varietat d'hàbitats).
""")

st.subheader("Principals Amenaces")
st.markdown("""
* Les cinc grans amenaces (HIPPO):
    1.  **Pèrdua i Fragmentació d'Hàbitat:** La causa principal a nivell global.
    2.  **Sobreexplotació:** Ús extractiu no sostenible de recursos.
    3.  **Contaminació:** Degradació química i física dels medis.
    4.  **Espècies Invasores:** Desplaçament de les espècies natives.
    5.  **Canvi Climàtic:** Alteració ràpida de les condicions ambientals.
""")

st.subheader("Endemisme i Hotspots")
st.markdown("""
* **Endemisme:** Condició d'una espècie que es troba de forma **exclusiva i natural** en una regió geogràfica molt concreta (ex: només a Mallorca).
* **Com es Forma:** El mecanisme principal és l'**aïllament geogràfic**, que atura el flux gènic i permet a la població aïllada evolucionar de manera divergent (especiació al·lopàtrida).
* **Insularitat-Endemisme:** La condició d'illa (o 'illa ecològica', com una muntanya alta) és el **factor que més l'afavoreix** per l'extrem aïllament que proporciona.
* **Hotspot:** Regió amb un **alt endemisme** (mínim 1.500 plantes endèmiques) i una **alta amenaça** (pèrdua del 70% de l'hàbitat). Són prioritats de conservació.
""")

# ==========================================================================
# SECCIÓ 3: ECOLOGIA DE MICROESCALA (HÀBITAT, BIOTIP, NÍNXOL)
# ==========================================================================
st.header("3. 🏠 HÀBITAT, BIOTIP I NÍNXOL ECOLÒGIC")
st.markdown("---")

st.subheader("Hàbitat")
st.markdown("""
* **Definició:** És el **lloc físic** on viu un organisme o una població; la seva "adreça" ecològica.
* **Elements Essencials:** Un hàbitat ha de proporcionar els recursos bàsics per a la vida: **Aigua, Aliment, Refugi (Cobert)** i **Llocs de Reproducció**.
""")

st.subheader("Biotip - Hàbitat - Nínxol Ecològic")
st.table({
    "Concepte": ["**Biotip**", "**Hàbitat**", "**Nínxol Ecològic**"],
    "Explicació Senzilla": ["Qui és l'organisme (característiques genètiques).", "On viu (el lloc físic).", "Què fa l'organisme (la seva funció, rols i interaccions a l'ecosistema)."],
})

st.subheader("Hàbitats Semi-Naturals")
st.markdown("""
* Són hàbitats que han estat creats o mantinguts per l'**activitat humana tradicional** (ex: pastura o sega). Han adquirit un valor ecològic que depèn de la continuïtat d'aquesta gestió (ex: la **Devesa**).
""")

# ==========================================================================
# SECCIÓ 4: BIOGEOGRAFIA IBÈRICA: FACTORS I SÒL
# ==========================================================================
st.header("4. 🇪🇸 HÀBITATS DE LA PENÍNSULA IBÈRICA")
st.markdown("---")

st.subheader("Factors que Condicionen els Hàbitats d'Espanya")
st.markdown("""
* **Regions Biogeogràfiques:** Espanya és la **transició** entre la regió **Mediterrània** (dominant) i l'**Eurosiberiana** (nord), més la **Macaronèsica** (Canàries). Aquesta barreja produeix una alta riquesa.
* **Tipus de Sòl (Edatisme):** La geologia (roca mare) és clau, ja que determina la flora:
    * **Sòls Silicis (àcids):** Per roques com el granit. Afavoreix la flora **acidòfila** (ex: Roure, Castanyer).
    * **Sòls Calcaris (bàsics):** Per roques com la calcària. Afavoreix la flora **calcícola** (ex: Alzina, Pi Blanc).
""")

# ==========================================================================
# SECCIÓ 5: VEGETACIÓ I FORMACIONS
# ==========================================================================
st.header("5. 🌳 FORMACIONS VEGETALS: Boscos i Biòtops")
st.markdown("---")

st.subheader("Vegetació Potencial i Bosc")
st.markdown("""
* **Vegetació Potencial:** La vegetació clímax que es desenvoluparia sense interferència humana, determinada pel clima i el sòl.
* **Bosc:** Formació amb alta densitat d'arbres que crea un dosser tancat.
""")

st.subheader("Tipus de Boscos i Noms Científics")
st.table({
    "Tipus de Bosc": ["**Bosc Caducifoli**", "**Bosc Mediterrani (Escleròfil·le)**", "**Bosc de Ribera**"],
    "Regió / Característica": ["Eurosiberiana (humit i fred).", "Mediterrània (sec i calorós a l'estiu).", "Azonal (lligat a l'aigua freàtica)."],
    "Noms Científics Dominants": ["*Quercus robur* (Roure), *Fagus sylvatica* (Faig).", "*Quercus ilex* (Alzina), *Quercus suber* (Suro).", "*Populus alba* (Àlber), *Salix sp.* (Salze)."],
})

st.subheader("Formacions Arbustives, Herbàcies i Estrats")
st.markdown("""
* **Sotabosc:** L'estrat vegetal que creix sota el dosser dels arbres (arbustos i herbes).
* **Formacions Arbustives (Matoll):** Són estadis de substitució del bosc potencial.
    * **Màquia:** Matollar alt i dens.
    * **Garriga:** Matollar baix i esclarissat (sovint sobre sòls calcaris).
* **Formacions Herbàcies:** Dominades per gramínies (Prats i Estepes).
* **Principals Biòtops:** Classificacions de grans hàbitats: Boscos, Matolls, Aigües continentals, Costes, etc.
""")

# ==========================================================================
# SECCIÓ 6: INVENTARIS I CONSERVACIÓ
# ==========================================================================
st.header("6. 🇪🇺 INVENTARIS I CONSERVACIÓ (HIC)")
st.markdown("---")

st.subheader("Projecte CORINE")
st.markdown("""
* **Què és?:** El sistema d'inventari ambiental de la UE. El **CORINE Biotopes** va ser la base per identificar els llocs naturals d'interès, donant lloc a la **Xarxa Natura 2000**.
""")

st.subheader("Hàbitats d'Interès Comunitari (HIC)")
st.markdown("""
* **Què són?:** Hàbitats naturals o seminaturals recollits a l'Annex I de la Directiva Hàbitats (92/43/CEE) que es consideren essencials per a la biodiversitat europea.
* **Importància:** La seva presència obliga a designar **Zones Especials de Conservació (ZEC)**.
""")

st.subheader("Factors de Selecció dels HIC a Espanya")
st.markdown("""
* La selecció reflecteix la **transició biogeogràfica** del territori (necessitat de protegir tant hàbitats mediterranis com eurosiberians i macaronèsics).
* Inclou HIC que depenen de la roca (Factors Edàfics), protegint boscos i matolls lligats específicament a **sòls calcaris** o **sòls silicis**.
""")
