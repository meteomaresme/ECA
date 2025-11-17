import streamlit as st

# --- Configuració General de la Pàgina ---
st.set_page_config(
    page_title="Repàs TOTAL: Biogeografia, Ecologia i Conservació 👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Títol Principal ---
st.title("👑 EINA MESTRA: Repàs Exhaustiu de Biogeografia i Hàbitats")
st.subheader("Cobertura TOTAL i Rigor Acadèmic de Cadascun dels Temes")

# ==========================================================================
# SECCIÓ 1: ECOLOGIA DE MACROESCALA (BIOMES I CLIMA)
# ==========================================================================
st.header("1. 🌍 BIOMES, CLIMA I ADAPTACIONS")
st.markdown("---")

st.subheader("1.1. Bioma: Definició i Diferenciació dels Principals")
st.markdown("""
* **Definició de Bioma:** És el **conjunt de comunitats** que ocupen una mateixa **àrea geogràfica** d'extensió continental. Al ser unitats de gran extensió, presenten una **vegetació climàtica uniforme** i un **clima característic** (factors zonals).
* **Principals Biomes Diferenciats:** Es defineixen per la combinació de **Temperatura** i **Precipitació**.
    * **Exemples:** Selva Tropical (càlid, humit), Desert (càlid, sec), Tundra (fred, sec), Bosc Temperat Caducifoli (temperat, estacional).
""")

st.subheader("1.2. Climograma: Funcionament, Interpretació i Climes")
st.markdown("""
* **Com Funciona (Senzill):** Representa la **Temperatura mitjana** (línia) i la **Precipitació total** (barres) mensual. L'escala $1^{\circ}C \approx 2 mm$ de P permet identificar el dèficit hídric.
* **Què Ens Ajuda a Entendre:** Quan la línia de T queda per sobre de P (època seca), es dóna **Aridesa Fisiològica** (la planta perd més aigua per transpiració de la que rep).
* **Climes Resultants:** Permet determinar climes com el **Mediterrani** (aridesa estival marcada) o l'**Oceànic** (humitat constant).
""")

st.subheader("1.3. Adaptacions de la Flora")
st.table({
    "Adaptació": ["**Escleròfil·la**", "**Caducifoli**", "**Xeròfita**", "**Higròfita**"],
    "Mecanisme": ["Fulles dures, cutícula gruixuda, perennes.", "Pèrdua de fulla estacional.", "Succulència (emmagatzematge), espines.", "Fulles amples, poca cutícula."],
    "Condició Superada": ["Sequera i calor estival.", "Fred o sequera estacional.", "Estrès hídric extrem.", "Humitat excessiva."],
})

# ==========================================================================
# SECCIÓ 2: BIODIVERSITAT, ESPECIACIÓ I AMENACES
# ==========================================================================
st.header("2. 🦋 DIVERSITAT, ENDEMISME I AMENACES")
st.markdown("---")

st.subheader("2.1. Definició de Diversitat")
st.markdown("""
* **Definició de Diversitat:** La **varietat de la vida** a la Terra en tots els seus nivells.
* **Nivells:** **Diversitat Genètica**, **Diversitat d'Espècies** (riquesa), i **Diversitat d'Ecosistemes/Hàbitats** (varietat).
""")

st.subheader("2.2. Amenaces i Hotspots")
st.markdown("""
* **Principals Amenaces:** Les cinc grans causes: **Pèrdua i Fragmentació d'Hàbitats** (la més important), **Sobreexplotació**, **Contaminació**, **Espècies Invasores** i **Canvi Climàtic**.
* **Hotspots de Biodiversitat:** Regions amb **alt endemisme** ($>$ 1.500 plantes) i **alta amenaça** (pèrdua de $>70\%$ de l'hàbitat original). Són prioritats globals de conservació.
""")

st.subheader("2.3. Endemisme, Factors i Insularitat")
st.markdown("""
* **Què és Endemisme:** Condició d'un tàxon amb distribució **exclusivament limitada** a una àrea geogràfica concreta.
* **Com es Forma un Endemisme:** Principalment per **aïllament geogràfic** (barrera física), que provoca l'**Especiació Al·lopàtrida** (divergència genètica).
* **Factors que Influeixen:** Aïllament geogràfic, mida petita de l'àrea, i condicions edàfiques extremes.
* **Insularitat-Endemisme:** La condició d'illa (o d'altes muntanyes) és el **factor que més influeix** ja que l'aïllament permanent accelera l'evolució i l'especialització.
""")

# ==========================================================================
# SECCIÓ 3: ECOLOGIA DE MICROESCALA (HÀBITAT, BIOTIP, NÍNXOL)
# ==========================================================================
st.header("3. 🏠 CONCEPTES FUNCIONALS I HÀBITAT")
st.markdown("---")

st.subheader("3.1. Hàbitat: Definició i Importància")
st.markdown("""
* **Què és un Hàbitat:** El **lloc físic i ambiental** on viu un organisme o població.
* **Elements Essencials d'un Hàbitat:** Ha de proporcionar els 4 pilars per a la vida: **Aigua, Aliment, Refugi/Cobert** i **Llocs de Reproducció**.
* **Importància:** La **pèrdua d'hàbitat** és la causa principal d'extinció, ja que l'espècie no pot completar el seu cicle vital.
""")

st.subheader("3.2. Biotip - Hàbitat - Nínxol Ecològic")
st.table({
    "Concepte": ["**Biotip**", "**Hàbitat**", "**Nínxol Ecològic**"],
    "Explicació Clau": ["Qui és l'organisme (genotip/unitat genètica).", "On viu (el lloc, les condicions).", "Què fa l'organisme (la funció, el rol i les interaccions biòtiques)."],
})

st.subheader("3.3. Projecte CORINE, Biotips i Hàbitats Semi-Naturals")
st.markdown("""
* **Projecte CORINE:** Inventari dels llocs naturals d'interès a la UE (CORINE Biotopes), base per a la **Directiva Hàbitats**.
* **Principals Biòtops:** Grans categories d'hàbitats naturals a la Península (Boscos, Matolls/Prats, Aigües continentals, Litorals, Roques/Coves).
* **Hàbitats Semi-Naturals:** Són hàbitats que han adquirit valor ecològic gràcies a l'**acció humana tradicional continuada** (ex: Deveses, prats de sega).
""")

# ==========================================================================
# SECCIÓ 4: GEOGRAFIA, REGIONS I FACTORS LOCALS
# ==========================================================================
st.header("4. 🇪🇸 HÀBITATS DE LA PENÍNSULA: Factors i Sòls")
st.markdown("---")

st.subheader("4.1. Factors que Afecten els Hàbitats d'Espanya")
st.markdown("""
Els hàbitats d'Espanya (Hàbitats Peninsulars) estan definits per tres factors principals:
1.  **Clima:** Transició climàtica **Mediterrània**-**Eurosiberiana**.
2.  **Orografia:** Altes muntanyes que creen barreres i microclimes.
3.  **Edatisme (Sòl):** La geologia i el tipus de sòl.
""")

st.subheader("4.2. Regions Biogeogràfiques (Regions Biològiques)")
st.table({
    "Regió d'Hàbitats": ["**Mediterrània**", "**Eurosiberiana**", "**Macaronèsica**"],
    "Clima / Vegetació": ["Estius secs. Vegetació Escleròfil·la (Alzina).", "Humit, temperat. Vegetació Caducifòlia (Faig, Roure).", "Subtropical, insular. Alts endemismes (Laurisilva)."],
})

st.subheader("4.3. Tipus de Sòl (Edatisme)")
st.markdown("""
* **Sòls Silicis (Àcids):** Derivats de roques com granit. Flora **calcífuga** (ex: Roure, Castanyer).
* **Sòls Calcaris (Bàsics):** Derivats de roques com calcària. Flora **calcícola** (ex: Pi Blanc, Savina).
""")

# ==========================================================================
# SECCIÓ 5: VEGETACIÓ POTENCIAL I FORMACIONS
# ==========================================================================
st.header("5. 🌳 FORMACIONS VEGETALS: Boscos i Estrats")
st.markdown("---")

st.subheader("5.1. Vegetació Potencial")
st.markdown("""
* **Què és:** La formació vegetal **clímax** que s'establiria en una zona sense la interferència humana actual, depenent només de les condicions edafoclimàtiques.
""")

st.subheader("5.2. Tipus de Boscos i Noms Científics Predominants")
st.markdown("""
* **Què és un Bosc:** Una comunitat arbòria amb una alta densitat que forma un dosser tancat.
* **Bosc Caducifoli (Eurosiberià):** Domini de *Fagus sylvatica* (Faig) i *Quercus robur* (Roure).
* **Bosc Mediterrani (Escleròfil·le):** Domini d'*Quercus ilex* (Alzina) i *Quercus suber* (Suro).
* **Bosc de Ribera (Azonal):** Lligat a l'aigua freàtica. Domini de *Populus alba* (Àlber) i *Salix sp.* (Salze).
* **Sotabosc:** L'estrat inferior que creix sota el dosser dels arbres. Essencial per a la regeneració.
""")

st.subheader("5.3. Formacions Arbustives i Herbàcies")
st.markdown("""
* **Formacions Arbustives (Matolls):** Estadis de substitució. Ex: **Màquia** (alt i dens) i **Garriga** (baix i esclarissat, sobre calcàries).
* **Formacions Herbàcies:** **Prats** (usats per sega o pastura) i **Estepes** (zones àrides, domini de gramínies).
""")

# ==========================================================================
# SECCIÓ 6: CONSERVACIÓ I HIC
# ==========================================================================
st.header("6. 🇪🇺 HÀBITATS D'INTERÈS COMUNITARI (HIC)")
st.markdown("---")

st.subheader("6.1. Quins Són els Hàbitats d'Interès Comunitari (HIC)")
st.markdown("""
* **HIC:** Hàbitats naturals o semi-naturals recollits a l'Annex I de la Directiva Hàbitats (92/43/CEE) que es consideren essencials per a la conservació de la biodiversitat europea.
* **Objectiu:** La seva protecció obliga a crear **Zones Especials de Conservació (ZEC)**, part de la Xarxa Natura 2000.
""")

st.subheader("6.2. Factors que Condicionen la Selecció d'HIC a Espanya")
st.markdown("""
* La selecció d'HIC a Espanya reflecteix la seva condició de **transició biogeogràfica** (protegint la barreja d'hàbitats Eurosiberians, Mediterranis i Macaronèsics).
* És crucial protegir la diversitat lligada a l'**Edatisme**, incloent HIC que depenen estrictament de la composició del sòl (ex: boscos de faig sobre substrats àcids o bàsics).
""")
