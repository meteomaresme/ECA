import streamlit as st

# --- Configuració General de la Pàgina ---
st.set_page_config(
    page_title="Repàs Professional: Biogeografia, Edatisme i HIC 🇪🇺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Títol Principal ---
st.title("👨‍🔬 Repàs per a l'Examen: Biogeografia, Hàbitats i Conservació")
st.subheader("Anàlisi Sistemàtica dels Ecosistemes Terrestres i Ibèrics")

# ==========================================================================
# SECCIÓ 1: ECOLOGIA DE MACROESCALA (BIOMES I CLIMA)
# ==========================================================================
st.header("1. 🌐 ECOLOGIA DE MACROESCALA: Biomes i Factors Climàtics")
st.markdown("---")

st.subheader("1.1. 🌲 Bioma: El Climax Climàtic")
st.info("""
El **Bioma** és la màxima unitat biogeogràfica, una immensa àrea geogràfica que comparteix un **Clima Zonal** (determinant) i una **Vegetació Climàcica uniforme**. No és només la comunitat, sinó el conjunt de comunitats sota un mateix règim termohídric.
* **Definició Clau:** Conjunt de comunitats (flora i fauna) que presenten una **Vegetació Climàtica uniforme** i un **clima característic**.
* **Factors de Diferenciació:** Els biomes es distingeixen principalment per la **Temperatura** i la **Precipitació**.
""")

st.subheader("1.2. 🌡️ Climograma: Lectura del Clima (Walter)")
st.write("El climograma és la millor eina per entendre el clima d'un bioma, relacionant els cicles tèrmics i hídrics. ")
st.markdown("""
* **Funció:** Permet identificar el **Període d'Aridesa Fisiològica** (l'època seca) on la demanda d'evapotranspiració és superior a la precipitació disponible.
* **Criteri 1:2:** Si la línia de Temperatura ($10^{\circ}C$ equival a $20 mm$ de Precipitació), la corba T per sobre de la P indica sequera potencial.
* **Climes Típics:**
    * **Mediterrani:** Aridesa estival molt marcada (línia T alta per sobre de P a l'estiu).
    * **Eurosiberià:** Humitat constant; línia P sempre per sobre o molt a prop de T.
""")

st.subheader("1.3. 🌿 Adaptacions Morfològiques de la Flora")
st.write("Les formacions vegetals s'adapten per optimitzar l'ús de l'aigua i l'energia en el seu bioma:")
st.table({
    "Adaptació": ["**Escleròfil·la**", "**Caducifoli**", "**Xeròfita**", "**Higròfita**"],
    "Objectiu Principal": ["Reduir la pèrdua d'aigua per transpiració (sequera estival).", "Evitar la pèrdua d'aigua per congelació o adaptar-se a l'estrès de sequera/fred.", "Emmagatzemar aigua i minimitzar la superfície de transpiració.", "Maximitzar la superfície per a l'evapotranspiració (gran humitat)."],
    "Exemple de Bioma": ["Bosc Mediterrani (Alzina)", "Bosc Temperat (Roure, Faig)", "Desert, Estepa", "Selva Tropical Humida"]
})

# ==========================================================================
# SECCIÓ 2: BIODIVERSITAT, AMENACES I ESPECIACIÓ
# ==========================================================================
st.header("2. 🦋 BIODIVERSITAT I ESPECIACIÓ")
st.markdown("---")

st.subheader("2.1. Definició de Diversitat")
st.warning("""
La **Biodiversitat** és la varietat de la vida en tots els seus nivells d'organització.
* **Diversitat d'Hàbitats/Ecosistemes:** Varietat de biomes i paisatges geogràfics.
* **Diversitat d'Espècies:** Riquesa i abundància relativa de les espècies en una àrea (la més coneguda).
* **Diversitat Genètica:** Variació d'al·lels (gens) dins de les poblacions d'una mateixa espècie.
""")

st.subheader("2.2. Principals Amenaces (HIPPO)")
st.error("""
Les 5 grans forces que condueixen a la pèrdua de biodiversitat:
1.  **Pèrdua i Fragmentació d'Hàbitats:** La principal causa, ja que trenca el continu vital.
2.  **Espècies Invasores:** Competeixen o depredan les espècies natives, alterant l'equilibri ecològic.
3.  **Contaminació:** Degrada directament els ambients i afecta la salut dels organismes.
4.  **Sobreexplotació:** Ús extractiu insostenible de recursos (ex: pesca sense control).
5.  **Canvi Climàtic:** Modificació ràpida de les condicions ambientals a què les espècies no es poden adaptar a temps.
""")

st.subheader("2.3. 🔥 Endemisme i Hotspots")

st.markdown("#### Què és Endemisme i Com es Forma?")
st.write("L'**Endemisme** és la condició d'una espècie que es distribueix de **forma exclusiva** en una àrea molt limitada i concreta (ex: només a les Illes Balears).")
st.markdown("""
* **Com es Forma l'Endemisme:** El mecanisme principal és l'**aïllament geogràfic** (speciació al·lopàtrida). Una barrera física (aigua, muntanya, desert) talla el flux gènic i la població aïllada evoluciona de manera única.
* **Insularitat i Endemisme:** La **insularitat** (ser una illa o un hàbitat aïllat) és el factor que **més influeix**. L'aïllament limita la competència de noves espècies i permet que les espècies fundadores evolucionin lliurement, creant taxes d'endemisme altíssimes.
""")

st.markdown("#### Hotspots de Biodiversitat")
st.write("Un **Hotspot** és un terme tècnic de conservació que identifica àrees prioritàries per la seva riquesa (endemisme) i la seva alta vulnerabilitat:")
st.markdown("""
* **Criteris Clau (Myers):** 1) Mínim 1.500 espècies de plantes endèmiques, i 2) pèrdua d'almenys el 70% de la vegetació original.
""")

# ==========================================================================
# SECCIÓ 3: ECOLOGIA DE MICROESCALA (HÀBITAT, BIOTIP, NÍNXOL)
# ==========================================================================
st.header("3. 🏠 HÀBITAT, BIOTIP I NÍNXOL ECOLÒGIC")
st.markdown("---")

st.subheader("3.1. Hàbitat i la seva Funció Vital")
st.info("""
L'**Hàbitat** és el lloc físic amb els recursos i condicions necessàries per a la vida d'un organisme. És la seva "adreça" ecològica.
* **Importància:** Si l'hàbitat no proporciona els elements bàsics, l'espècie no pot persistir. La seva conservació és l'eix de la gestió ambiental.
* **Elements Essencials de l'Hàbitat:** **Aigua, Aliment, Refugi/Cobert** i **Llocs de Reproducció**.
""")

st.subheader("3.2. Diferenciació dels Conceptes")
st.table({
    "Concepte": ["**Biotip**", "**Hàbitat**", "**Nínxol Ecològic**"],
    "Explicació Sencilla": ["Conjunt d'organismes amb el mateix genotip (característiques genètiques).", "El lloc, el territori físic que ocupa l'espècie.", "La 'professió' de l'espècie: Què menja, qui el menja, com interactua, a quina hora és actiu, etc."],
    "Què Respon?": ["Qui (característiques genètiques)", "On (localització)", "Com i Què (funció i interaccions)"],
})

st.subheader("3.3. Hàbitats Semi-Naturals")
st.write("Són àrees modelades per activitats humanes tradicionals (ramaderia extensiva, agricultura de secà) que han mantingut o generat un alt valor ecològic i biodiversitat. Sovint requereixen la continuació d'aquesta gestió per subsistir.")
st.markdown("* **Exemples:** Les **Deveses** (bosc esclarissat per a pastura i alzinar), prats de sega de muntanya.")

# ==========================================================================
# SECCIÓ 4: HÀBITATS IBÈRICS I FACTORS LOCALS (EDAFISME)
# ==========================================================================
st.header("4. 🇪🇸 Biogeografia Ibèrica: Factors Condicionants")
st.markdown("---")

st.subheader("4.1. Factors que Condicionen els Hàbitats d'Espanya")
st.write("La riquesa d'hàbitats a la Península es deu a la superposició de tres factors:")
st.markdown("""
* **Clima (Zonal):** Domini Mediterrani, amb fortes influències Eurosiberianes (nord) i elevació (muntanya).
* **Orografia (Relief):** Les muntanyes creen gradients de temperatura i precipitació (efecte de solana vs. obaga).
* **Edatisme (Sòl):** La geologia local determina la química del sòl, la qual cosa selecciona la vegetació.
""")

st.subheader("4.2. Tipus de Sòl i Bioregions")
st.markdown("El **Tipus de Sòl** (**Edatisme**) és un factor determinant de la vegetació potencial. Els tipus principals són:")
st.table({
    "Tipus de Sòl": ["**Sòls Silicis** (Àcids)", "**Sòls Calcaris** (Bàsics)", "**Sòls Salins**"],
    "Composició": ["Rocs ígnis (granit, pissarra). Pobres en calci.", "Rocs sedimentaris (calcària, dolomia). Rics en calci.", "Altes concentracions de sals minerals (zones costaneres, conques endorreiques)."],
    "Flora Indicadora": ["Rouredes, Faig (en pH baix), Castanyer, *Quercus Pyrenaica*.", "Alzinars, Pins Blancs (*Pinus halepensis*), Sabines (Flora Calcícola).", "Vegetació Halòfita (Salicornies, Tamarius)."],
})

st.subheader("4.3. Regions Biogeogràfiques")
st.write("La Península Ibèrica és la frontera de dues grans regions europees, més la Macaronèsica a Canàries:")
st.markdown("""
| Regió | Clima | Vegetació Climax |
| :--- | :--- | :--- |
| **Mediterrània** | Estius secs i calorosos | Bosc Escleròfil·le (fulla perenne i dura) |
| **Eurosiberiana** | Humit i plujós tot l'any | Bosc Caducifoli (fulla cau a l'hivern) |
| **Macaronèsica** | Subtropical, Insular | Laurisilva, formacions de *Cardón-Tabaiba* (Endemismes) |
""")

# ==========================================================================
# SECCIÓ 5: VEGETACIÓ POTENCIAL I TIPUS DE FORMACIONS
# ==========================================================================
st.header("5. 🌳 Formacions Vegetals: Estructura i Noms Científics")
st.markdown("---")

st.subheader("5.1. Vegetació Potencial i Bosc Climax")
st.write("La **Vegetació Potencial** és la comunitat vegetal que es desenvoluparia de forma natural en una zona sota les condicions climàtiques i edàfiques actuals, sense la intervenció humana. Això ens dona la referència del **bosc (climax)** que hauria d'existir.")

st.subheader("5.2. Classificació de Boscos i Formacions")
st.write("Els hàbitats vegetals es defineixen per la seva estructura i espècies dominants:")

st.markdown("#### Tipus de Boscos i Espècies Predominants")
st.table({
    "Tipus de Bosc": ["**Bosc Caducifoli**", "**Bosc Mediterrani (Alzinars)**", "**Bosc de Ribera**", "**Boscos de Coníferes**"],
    "Regió / Zona": ["Eurosiberiana", "Mediterrània", "Azonal (Vora de l'aigua)", "Alta Muntanya / Boreal"],
    "Noms Científics Clau": ["*Fagus sylvatica* (Faig), *Quercus robur* (Roure)", "*Quercus ilex* (Alzina), *Quercus suber* (Suro)", "*Populus alba* (Àlber), *Salix alba* (Salze)", "*Pinus sylvestris* (Pi Roig), *Abies alba* (Avet)"],
})

st.markdown("#### Formacions de Substitució")
st.markdown("""
* **Sotabosc:** La capa vegetal inferior del bosc (arbustos, herbes, molses). Important per a la regeneració i refugi.
* **Formacions Arbustives (Matolls):** Dominades per arbustos. Solen ser estadis de degradació o successió del bosc:
    * **Màquia:** Matollar alt, dens, molt tancat (ex: estepa, bruguerar).
    * **Garriga:** Matollar baix, esclarissat, amb presència de roca i romaní.
* **Formacions Herbàcies:** Prats i estepes. Domini de gramínies i herbàcies; pot ser un estadi climàcic (estepa) o seminatural (prat de sega).
""")

# ==========================================================================
# SECCIÓ 6: GESTIÓ I CONSERVACIÓ (CORINE I HIC)
# ==========================================================================
st.header("6. 🇪🇺 Conservació: Projecte CORINE i Hàbitats d'Interès Comunitari")
st.markdown("---")

st.subheader("6.1. Projecte CORINE i Biòtops")
st.write("El projecte **CORINE (Coordination of Information on the Environment)** és el sistema de referència de la UE. El **CORINE Biotopes** va ser l'inventari dels llocs naturals d'interès que va servir de base per a la creació de la Xarxa Natura 2000.")

st.markdown("#### Principals Biòtops (Categories Generals):")
st.markdown("""
* Aigües Marines i Costaneres (platges, dunes).
* Aigües Continentals (rius, llacs, aiguamolls).
* Matolls i Prats (inclou garrigues i màquies).
* Boscos.
* Àrees Agrícoles i Zones Antropitzades.
""")

st.subheader("6.2. Hàbitats d'Interès Comunitari (HIC)")
st.warning("""
Els **Hàbitats d'Interès Comunitari (HIC)** són aquells hàbitats naturals o seminaturals que són essencials per a la biodiversitat europea (Annex I de la Directiva Hàbitats).
* **Objectiu:** Assegurar la seva conservació mitjançant la declaració de **Zones Especials de Conservació (ZEC)**, que integren la Xarxa Natura 2000.
""")

st.subheader("6.3. Factors que Condicionen la Selecció d'HIC a Espanya")
st.write("La llista d'HIC espanyola és extremadament àmplia perquè reflecteix la **transició biogeogràfica** i els factors locals (edafisme) únics:")
st.markdown("""
* **Transició de Regions:** S'han de seleccionar HIC per a la **Regió Mediterrània** (majoritària, ex: espartars, màquies de lentisc), HIC per a la **Regió Eurosiberiana** (ex: fagedes humides) i HIC **Macaronèsics** (Canàries, ex: laurisilva).
* **Edatisme (Sòl):** La selecció inclou categories que depenen directament de la roca (ex: boscos de ribera termòfils sobre sòls calcaris, o torberes en sòls àcids), assegurant la protecció de la variabilitat geològica.
* **HIC d'Ecosistemes Vitals:** Prioritzen hàbitats vulnerables i clau, com els **aiguamolls** o les **dunes costaneres**, ja que són essencials malgrat ser azonals.
""")

# --- Conclusió / Peude pàgina ---
st.markdown("---")
st.caption("Aquest document ha estat dissenyat per cobrir tots els aspectes del temari amb la màxima claredat acadèmica. 💯")
