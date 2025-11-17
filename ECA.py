import streamlit as st

# --- Configuració General de la Pàgina ---
st.set_page_config(
    page_title="Repàs Acadèmic: Biomes, Biogeografia i Hàbitats Ibèrics 🇪🇸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Títol Principal ---
st.title("📚 Repàs Acadèmic: Biomes, Biodiversitat i Hàbitats d'Interès Comunitari")
st.subheader("Anàlisi Exhaustiva per a l'Examen")

# --------------------------------------------------------------------------
# SECCIÓ 1: BIOMES I CLIMA (MACROESCALA)
# --------------------------------------------------------------------------
st.header("1. 🌍 BIOMES: CLASSIFICACIÓ I ADAPTACIONS (MACROESCALA)")
st.markdown("---")

st.subheader("1.1. Bioma: Definició i Factors Determinants")
st.info("""
**Bioma:** Una unitat biogeogràfica d'escala global o subcontinental. És la màxima expressió de la relació **Clima-Vegetació**, caracteritzada per:
* **Uniformitat Climàtica:** Un clima zonal o regional propi.
* **Uniformitat de la Vegetació Climàcica:** Formacions vegetals adaptades a aquest clima dominant.
* **Components:** Conjunt d'ecosistemes amb comunitats que comparteixen espècies clau i dinàmiques similars.
""")

st.subheader("1.2. Climogrames: Interpretació Bioenergètica")
st.write("El climograma (Diagrama d'Ombrothermic de Walter) relaciona els paràmetres tèrmics i hídrics:")
st.markdown("""
* **Eix Tèrmic (T):** Línia de temperatura mitjana mensual.
* **Eix Hídric (P):** Barres de precipitació mitjana mensual.
* **Regla 1:2 (P en mm / T en °C):** Si la corba de Temperatura supera la de Precipitació (amb l'escala de 1°C = 2 mm), s'estableix un **període d'aridesa fisiològica** (època seca).
* **Interpretació de Climes:**
    * **Clima Mediterrani:** Línia de T molt per sobre de P a l'estiu (aridesa estival marcada).
    * **Clima Oceànic/Eurosiberià:** Corba de P sempre per sobre de T, o molt a prop (humitat constant).
""")

st.subheader("1.3. Adaptacions Morfològiques de la Flora")
st.markdown("La flora es classifica segons les adaptacions per superar l'estrès climàtic (aigua o fred):")
st.table({
    "Tipus d'Adaptació": ["**Xeròfita**", "**Higròfita**", "**Caducifoli**", "**Escleròfil·la**", "**Psicròfita**"],
    "Condició Dominant": ["Aridesa, estrès hídric", "Humitat excessiva", "Fred i/o sequera estacional", "Sequera estival i calor", "Fred extrem"],
    "Mecanismes": ["Estomes enfonsats, espines, succulència (carns)", "Fulles grans per transpiració, absència de cutícula gruixuda", "Pèrdua de fulla a l'època desfavorable", "Fulles petites, dures, amb cutícula gruixuda (ex: alzina)", "Port baix, protecció contra el vent i el gel"],
    "Exemple de Bioma": ["Desert, Estepa", "Selva Tropical", "Bosc Temperat Caducifoli", "Bosc Mediterrani", "Tundra, Alta Muntanya"],
})

# --------------------------------------------------------------------------
# SECCIÓ 2: BIODIVERSITAT, AMENACES I ENDEMISME
# --------------------------------------------------------------------------
st.header("2. 🦋 BIODIVERSITAT, AMENACES I ENDEMISME")
st.markdown("---")

st.subheader("2.1. Definició i Importància de la Diversitat")
st.warning("""
**Biodiversitat:** El grau de variació de la vida a la Terra en tots els seus nivells d'organització:
* **Diversitat Genètica (Alfa):** Variabilitat d'al·lels dins de les poblacions d'una mateixa espècie.
* **Diversitat d'Espècies (Beta):** Riquesa (nombre d'espècies) i abundància relativa.
* **Diversitat d'Ecosistemes (Gamma):** Varietat d'hàbitats, biomes i processos ecològics.
""")

st.subheader("2.2. Amenaces (Les 5 Grans Causes)")
st.error("""
Les principals causes de pèrdua de biodiversitat (interrelacionades):
1.  **Destrucció/Fragmentació d'Hàbitats:** La pèrdua d'espai vital és la causa número u.
2.  **Sobreexplotació:** Ús extractiu no sostenible (tala, pesca, caça).
3.  **Contaminació:** Afectació per productes químics, plàstics, etc.
4.  **Espècies Exòtiques Invasores (EEI):** Desplaçament i extinció d'espècies natives.
5.  **Canvi Climàtic:** Modificació ràpida de les condicions ambientals a escala global.
""")

st.subheader("2.3. Endemisme i Hotspots")
st.markdown("**Endemisme:**")
st.write("Estat d'una espècie l'àrea de distribució de la qual està confinada a una àrea geogràfica molt específica i restringida (exclusivitat).")

st.markdown("**Hotspot de Biodiversitat:**")
st.write("Una àrea biogeogràfica que, segons el criteri de Myers (2000), compleix:**")
st.markdown("""
* **Criteri de Riquesa:** Ha de contenir un mínim de 1.500 espècies de plantes vasculars endèmiques (alt endemisme).
* **Criteri d'Amenaça:** Ha d'haver perdut almenys el 70% del seu hàbitat original (alta vulnerabilitat).
""")

st.markdown("**Formació d'Endemismes (Mecanismes):**")
st.markdown("""
* **Aïllament Geogràfic (Especiació Al·lopàtrida):** El més comú. La separació física (illes, muntanyes) atura el flux gènic i permet l'evolució divergent.
* **Insularitat Endemisme:** La condició d'illa (o 'illa' ecològica) maximitza l'aïllament. Les illes tenen altes taxes d'endemisme per: 1) **Efecte fundador** (pocs individus inicials) i 2) **Absència de competidors/depredadors** que permeten la radiació adaptativa.
""")

# --------------------------------------------------------------------------
# SECCIÓ 3: HÀBITAT, BIOTIP I NÍNXOL ECOLÒGIC
# --------------------------------------------------------------------------
st.header("3. 🏡 HÀBITAT, BIOTIP I NÍNXOL ECOLÒGIC (MICROESCALA)")
st.markdown("---")

st.subheader("3.1. Hàbitat i els seus Elements Essencials")
st.info("""
**Hàbitat:** El lloc geogràfic i ambiental específic que un organisme (o població) ocupa.
* **Importància:** Defineix les condicions necessàries per a la supervivència. La seva destrucció o degradació és la principal amenaça a la biodiversitat.
* **Elements Essencials:**
    1.  **Recursos Alimentaris:** Energia i nutrients.
    2.  **Recursos Hídrics:** Aigua (en forma líquida o humitat).
    3.  **Refugi/Cobert:** Protecció contra depredadors i inclemències climàtiques.
    4.  **Llocs de Reproducció/Cria:** Espais segurs per a la propagació de l'espècie.
""")

st.subheader("3.2. Diferenciació Conceptual")
st.table({
    "Concepte": ["**Biotip**", "**Hàbitat**", "**Nínxol Ecològic**"],
    "Definició": ["Organismes amb el mateix genotip; un tipus d'organisme que viu en un hàbitat.", "El lloc físic o 'adreça' on viu l'organisme.", "El paper, la funció, o la 'professió' de l'organisme dins de l'ecosistema."],
    "Què Respon?": ["Qui (característiques genètiques)", "On (localització espacial)", "Com i Què fa (interaccions i recursos utilitzats)"],
})

st.subheader("3.3. Hàbitats Semi-Naturals")
st.write("Són hàbitats la fisonomia i dinàmica dels quals estan profundament influenciades per pràctiques humanes tradicionals (pastura, sega, conreu de baix impacte), i que han esdevingut **imprescindibles per a la subsistència de moltes espècies silvestres**.")
st.markdown("* **Exemples:** La Devesa (pastura extensiva), prats de sega de muntanya, sistemes d'aiguamolls gestionats per l'home.")

# --------------------------------------------------------------------------
# SECCIÓ 4: GEOGRAFIA I ECOLOGIA IBÈRICA
# --------------------------------------------------------------------------
st.header("4. 🇪🇸 HÀBITATS DE LA PENÍNSULA IBÈRICA: FACTORS I REGIONS")
st.markdown("---")

st.subheader("4.1. Factors que Afecten els Hàbitats d'Espanya")
st.markdown("""
1.  **Factor Climàtic (Macrometeorològic):** Domini del clima mediterrani, però amb una gradient climàtic molt fort entre el nord humit (Eurosiberià) i el sud sec (Mediterrani/Sub-saharià).
2.  **Factor Orogràfic (Relief):** Gran altitud mitjana i serralades orientades que creen barreres biogeogràfiques i zones amb efecte Föhn (Ombra Pluviomètrica).
3.  **Factor Edafològic (Sòl):** La geologia i la química del substrat condicionen la flora i, per tant, l'hàbitat.
""")

st.subheader("4.2. Regions Biogeogràfiques")
st.write("Espanya es divideix en tres grans regions, la superposició de les quals dóna una riquesa única:")
st.markdown("""
* **Regió Eurosiberiana (o Atlàntica):** Nord (Galícia, Cornisa Cantàbrica). Clima temperat i humit, vegetació potencial de **Bosc Caducifoli**.
* **Regió Mediterrània:** Interior i Sud de la Península. Clima amb aridesa estival, vegetació potencial **Escleròfil·la (perennifòlia)**.
* **Regió Macaronèsica:** Illes Canàries. Biota única, clima subtropical amb alt endemisme.
""")

st.subheader("4.3. Tipus de Sòl i Edatisme")
st.table({
    "Tipus de Sòl": ["**Sòls Silicis**", "**Sòls Calcaris**", "**Sòls Al·luvials**", "**Sòls Salins**"],
    "Composició/pH": ["Rocs àcids (Granit, Quarsita, Pissarra). pH àcid.", "Rocs bàsics (Calcària, Dolomia). pH bàsic/neutre.", "Sediments rics transportats per l'aigua. Neutre/Lleugerament bàsic.", "Alta concentració de sals (NaCl)."],
    "Flora Predominant": ["Castanyer, Roure, Bruc, Pins Silicis (*Pinus pinaster*)", "Alzina, Pi Blanc (*Pinus halepensis*), Savina, Boscos de Faig", "Boscos de Ribera (Àlbers, Salzes), Cultius Fèrtils", "Vegetació Halòfita (Salicornies, Tamarius)"],
})

# --------------------------------------------------------------------------
# SECCIÓ 5: VEGETACIÓ POTENCIAL I TIPUS DE BOSCOS
# --------------------------------------------------------------------------
st.header("5. 🌳 VEGETACIÓ: CLASSIFICACIÓ I FORMACIONS")
st.markdown("---")

st.subheader("5.1. Vegetació Potencial")
st.write("És la vegetació climax que s'establiria a la zona segons les condicions edafoclimàtiques, si no hi hagués hagut alteració humana o pertorbacions recents.")
st.markdown("* **Relevància:** El tipus de bosc o màquia potencial és la referència per a la restauració ecològica de l'hàbitat.")

st.subheader("5.2. Classificació de Formacions Arbòries i Inferiors")

st.markdown("#### **Tipus de Boscos Principals (Segons Clima)**")
st.table({
    "Nom Comú": ["**Bosc Caducifoli**", "**Bosc Mediterrani (Escleròfil·le)**", "**Bosc de Ribera**"],
    "Bioregions": ["Eurosiberiana, Zones d'Alta Muntanya", "Mediterrània", "Totes (Azonal)"],
    "Noms Científics Dominants": ["*Quercus robur* (Roure), *Fagus sylvatica* (Faig), *Tilia platyphyllos* (Til·ler)", "*Quercus ilex* (Alzina), *Quercus suber* (Suro), *Pinus halepensis* (Pi blanc)", "*Populus alba* (Àlber), *Salix alba* (Salze), *Fraxinus angustifolia* (Freixe)"],
})

st.markdown("#### **Formacions Inferiors (Estratègies Post-Boscoses o Climes Extrems)**")
st.table({
    "Formació": ["**Sotabosc**", "**Formacions Arbustives**", "**Formacions Herbàcies**", "**Matoll (Màquia/Garriga)**"],
    "Funció/Descripció": ["La capa vegetal sota el dosser; essencial per a la regeneració i refugi.", "Dominades per arbustos; estadi de substitució o zones de vent/fred.", "Dominades per gramínies; pastures, prats de sega.", "Formacions escleròfil·les, dures. **Màquia** (densa, alta), **Garriga** (baixa, clariana)."],
    "Exemples Clau": ["Heura, Galzeran", "Ginesta, Càdec", "Prats de dall", "Romaní, Estepa, Bruc"],
})

# --------------------------------------------------------------------------
# SECCIÓ 6: INVENTARIS I CONSERVACIÓ D'HÀBITATS
# --------------------------------------------------------------------------
st.header("6. 📋 INVENTARIS I HÀBITATS D'INTERÈS COMUNITARI")
st.markdown("---")

st.subheader("6.1. Projecte CORINE i l'Evolució de la Conservació")
st.write("El **Projecte CORINE Biotopes** (precursor) i **CORINE Land Cover** (ús del sòl) són eines clau:")
st.markdown("""
* **Objectiu:** Harmonitzar la informació ambiental entre estats membres de la Unió Europea.
* **CORINE Biotopes:** Va identificar els llocs naturals d'interès. Va ser la base per al desenvolupament de la **Directiva Hàbitats** (1992) i la creació de la **Xarxa Natura 2000**.
""")

st.subheader("6.2. Hàbitats d'Interès Comunitari (HIC)")
st.warning("""
**HIC:** Hàbitats recollits a l'Annex I de la Directiva Hàbitats 92/43/CEE. Són essencials per a la conservació i la biodiversitat de la UE.
* **Criteris:** Estan en perill, tenen un rang de distribució petit o són un exemple excel·lent de la seva regió biogeogràfica.
* **Objectiu de Conservació:** La seva presència obliga els estats a declarar **Zones Especials de Conservació (ZEC)**, que, juntament amb les ZEPA (Zones d'Especial Protecció per a les Aus), formen la **Xarxa Natura 2000**.
""")

st.subheader("6.3. Factors que Condicionen la Selecció d'HIC a Espanya")
st.markdown("La selecció dels HIC a Espanya reflecteix la transició entre regions:")
st.markdown("""
* **HIC Mediterranis:** Dominen (ex: garrigues amb *Juniperus* spp., boscos de ribera termòfils).
* **HIC Eurosiberians:** Restringits al nord i muntanyes (ex: fagedes calcícoles, rouredes acidòfiles).
* **HIC d'Ecosistemes Aquàtics:** Molt representats per la seva vulnerabilitat (ex: llacs temporanis mediterranis, dunes litorals).
""")

# --- Conclusió / Peude pàgina ---
st.markdown("---")
st.caption("Aquesta versió cobreix el temari amb una profunditat superior, ideal per a repassar conceptes de Biogeografia, Ecologia i Conservació. Molta sort! 💯")
