import streamlit as st
import pandas as pd

# --- Configuració de la Pàgina ---
st.set_page_config(
    page_title="Guia d'Estudi RA1",
    page_icon="🌍",
    layout="wide"
)

# --- Barra Lateral de Navegació ---
st.sidebar.title("Temari RA1: Medi Ambient 🌍")
st.sidebar.markdown("Selecciona la secció que vols estudiar o posa't a prova.")

temari_options = [
    "Inici",
    "TEORIA 1: Activitats Humanes",
    "TEORIA 2: Identificació d'Impactes",
    "TEORIA 3: Mesures (Prev, Corr, Comp)",
    "TEORIA 4: Esgotament de Recursos",
    "TEORIA 5: El Sòl",
    "TEORIA 6: Deixalleries",
    "TEORIA 7: Gestió de Residus",
    "---",
    "Posa't a Prova! (Test) 🎓"
]
seleccio = st.sidebar.radio("Navegació del Temari:", temari_options)

st.sidebar.markdown("---")
st.sidebar.info("Aquesta app t'ajuda a preparar l'examen sobre impacte ambiental. Molta sort!")


# --- Contingut de les Pàgines ---

if seleccio == "Inici":
    st.title("Guia d'Estudi: Impacte Ambiental (RA1) 🌳")
    st.markdown("### Benvingut/da a la teva eina d'estudi interactiva.")
    
    st.image("https://images.unsplash.com/photo-1500382017468-9049fed747ef?q=80&w=2832", 
             caption="", 
             use_column_width=True)
    
    st.info("💡 Fes servir el menú de l'esquerra per navegar entre les diferents teories del curs. Quan et sentis preparat/da, ves a la secció **'Posa't a Prova!'**.")


# --- TEORIA 1 ---
elif seleccio == "TEORIA 1: Activitats Humanes":
    st.header("TEORIA 1: Activitats Humanes que Afecten el Medi Ambient 🏭")
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "1. Indústria/Energia", 
        "2. Agricultura i Ramaderia", 
        "3. Plàstics", 
        "4. Turisme", 
        "5. Transport", 
        "6. Infraestructures", 
        "7. Desertització"
    ])

    with tab1:
        st.subheader("1. Fonts de generació d'energia més perjudicials")
        st.error("CENTRALS TÈRMIQUES")
        st.write("● **Impactes:** Emissions de CO₂, efecte hivernacle i pluja àcida.")
        
        st.error("ENERGIA NUCLEAR")
        st.write("● **Impactes:** Residus radioactius molt perillosos.")
        
        st.warning("CICLES COMBINATS (Gas Natural)")
        st.write("● **Impactes:** L’explotació contamina aigües i sòls; danya ecosistemes.")
        
        st.warning("ENERGIA BIOMASSA")
        st.write("● **Impactes:** Contaminació aire, pèrdua vegetació, destrucció biodiversitat, erosió.")

        st.info("ENERGIA EÒLICA")
        st.write("● **Impactes:** Afecta la fauna local i empobreix la terra.")

        st.info("ENERGIA HIDRÀULICA")
        st.write("● **Impactes:** Fragmentació i pèrdua d’hàbitats per preses i embassaments.")

    with tab2:
        st.subheader("2. Treballs agrícoles, ramaders i silvícoles")
        st.markdown("#### 2.1 L'agricultura")
        st.markdown("""
        * **Aigua:** recurs escàs i essencial.
        * **Adobs i pesticides:** possible contaminació.
        * **Transgènics i cultius energètics:** pèrdua de diversitat genètica.
        * **Sòl:** degradació i pèrdua.
        """)
        
        st.markdown("#### 2.2 Ramaderia")
        st.markdown("""
        * **Emissions GEH:** 12–14,5% del canvi climàtic global.
        * **Desforestació:** S’eliminen boscos per pastures.
        * **Contaminació:** Dejeccions (amoníac).
        * **Salut humana:** Ús d’antibiòtics genera resistència bacteriana.
        """)

        st.markdown("#### 2.3 Silvicultura")
        col1, col2 = st.columns(2)
        with col1:
            st.success("Funcions de Protecció")
            st.markdown("""
            * **Clima:** absorbeixen CO₂.
            * **Genètica:** protegeix la diversitat.
            * **Terra:** evita l’erosió.
            """)
        with col2:
            st.warning("Problemes Ambientals")
            st.markdown("""
            * **Desforestació**
            * **Erosió del sòl**
            * **Pèrdua de biodiversitat**
            * **Ús de químics**
            """)

    with tab3:
        st.subheader("3. Indústria i els plàstics")
        col1, col2 = st.columns(2)
        with col1:
            st.success("BIODEGRADABLE")
            st.write("Bacteris i fongs descomponen ràpidament.")
            st.markdown("""
            **Contaminants Biodegradables:**
            * Deixalles orgàniques.
            * **Compostatge:** amb oxigen.
            * **Metanització:** sense oxigen -> biogàs.
            """)
        with col2:
            st.error("NO BIODEGRADABLE")
            st.write("No es descomponen o ho fan molt lentament.")
            st.markdown("""
            **Contaminants No Biodegradables:**
            * Plàstics, metalls pesants, piles.
            * Problemes: temps i despesa energètica.
            """)
        st.warning("Els plàstics com a deixalles: No són biodegradables, s’escampen fàcilment, impacte visual.")

    with tab4:
        st.subheader("4. Impactes del Turisme")
        st.markdown("""
        **Causes dels Impactes:**
        * Ocupació del territori.
        * Mobilitat dels turistes (transport).
        * Generació de residus sòlids urbans.
        * Consum de recursos hídrics.
        """)
        
        with st.expander("Turisme Sostenible vs. Turisme de Masses"):
            st.markdown("""
            * **Desenvolupament Sostenible:** Satisfà les necessitats del present sense comprometre les de les generacions futures.
            * **Turisme Sostenible:** Respecta cultura, ecosistemes i biodiversitat.
            
            | TURISME DE MASSES | TURISME SOSTENIBLE |
            | :--- | :--- |
            | 1. Ús intensiu dels recursos | 1. Consideració recursos |
            | 2. Massificació | 2. Capacitat de càrrega |
            | 3. Beneficis econòmics | 4. Beneficis econòmics, però no a qualsevol preu |
            """)
        
        with st.expander("Per què pot ser insostenible el turisme?"):
            st.markdown("""
            * **Desplaçament massiu** → molta contaminació (transports).
            * **Ocupació del territori** → construcció d’infraestructures.
            * **Comportament dels turistes** → falta de consciència.
            * **Estratègies empresarials** → prioritat al benefici econòmic.
            """)

    with tab5:
        st.subheader("5. Impactes del Transport")
        st.error("Impactes Negatius")
        st.markdown("""
        * **Emissions de GEH:** (CO₂) contribueixen al canvi climàtic.
        * **Contaminació de l’aire:** (NOx, partícules) afecten la salut.
        * **Contaminació acústica:** El soroll perjudica la salut mental i la fauna.
        * **Impacte en ecosistemes:** Fragmenten hàbitats.
        """)
        st.success("Impactes Positius i Mitigació")
        st.markdown("""
        * **Positiu:** Connectivitat, mobilitat sostenible (transport públic, bici), innovacions (vehicles elèctrics).
        * **Mitigació:** Foment del transport públic, incentius per a vehicles nets, disseny urbà sostenible.
        """)
        
    with tab6:
        st.subheader("6. Impactes de les Infraestructures")
        st.error("Impactes Negatius")
        st.markdown("""
        * **Desforestació i pèrdua de biodiversitat.**
        * **Contaminació:** Aire, aigua i sòl.
        * **Alteració d’ecosistemes:** Modificació del paisatge.
        * **Erosió del sòl.**
        """)
        st.success("Impactes Positius i Mitigació")
        st.markdown("""
        * **Positiu:** Millora de serveis (aigua, llum), desenvolupament econòmic, conservació (parcs naturals), eficiència energètica.
        * **Mitigació:** Avaluacions d'impacte ambiental (estudis previs), disseny sostenible, ús de materials sostenibles, rehabilitació d’àrees afectades.
        """)
    
    with tab7:
        st.subheader("7. Desertització i Desertificació")
        col1, col2 = st.columns(2)
        with col1:
            st.warning("Desertització (Procés Natural)")
            st.write("Zona humida passa a desèrtica **sense intervenció humana**.")
            st.write("**Causes:** Astronòmiques (Cicles de Milankovic), Geomorfològiques (Orogènia).")
        with col2:
            st.error("Desertificació (Causa Humana)")
            st.write("Zona fèrtil perd capacitat de producció per **causes humanes** (i naturals).")
            st.write("**Causes Antròpiques:** Deforestació, agricultura intensiva, urbanització.")
        
        st.subheader("Impacte i Mitigació de la Desertificació")
        st.markdown("**Impactes:** Pèrdua de biodiversitat, degradació del sòl, escassetat d’aigua, conflictes socials.")
        st.markdown("**Mesures de Mitigació:** Reforestació, pràctiques agrícoles sostenibles, maneig sostenible de l’aigua.")

# --- TEORIA 2 ---
elif seleccio == "TEORIA 2: Identificació d'Impactes":
    st.header("TEORIA 2: Identificació i Magnitud dels Impactes 🔍")
    st.info("Impacte ambiental: qualsevol canvi en el medi ambient causat per accions humanes o naturals.")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "1. Caràcter", 
        "2. Causa-Efecte", 
        "3. Extensió", 
        "4. Persistència", 
        "5. Recuperació", 
        "6. Manifestació"
    ])
    
    with tab1:
        st.subheader("1. Segons el seu Caràcter")
        col1, col2 = st.columns(2)
        with col1:
            st.success("POSITIU")
            st.write("Milloren el medi (Restauració).")
            st.success("IMPACTE MÍNIM O LLEU")
            st.write("Efectes petits o reversibles.")
        with col2:
            st.error("NEGATIU")
            st.write("Perjudica el medi (Erosió).")
            st.error("IMPACTE NOTABLE O SIGNIFICATIU")
            st.write("Efectes greus o apreciables.")
            
    with tab2:
        st.subheader("2. Segons Relació Causa-Efecte")
        st.markdown("#### IMPACTE DIRECTE")
        st.write("Immediat (vessament d'olis).")
        st.markdown("#### IMPACTE INDIRECTE")
        st.write("Conseqüència d'un directe (animals afectats pel sòl contaminat).")

    with tab3:
        st.subheader("3. Segons Extensió")
        st.markdown("""
        * **PUNTUAL:** Zona petita (abocament tòxic al riu).
        * **PARCIAL:** Afecta només una part de l’ecosistema.
        * **EXTREM:** Alteracions greus, irreversibles, afecta gran part.
        * **UBICACIÓ CRÍTICA:** Lloc molt sensible (abocament aigües amunt d'una presa).
        """)

    with tab4:
        st.subheader("4. Segons Persistència")
        st.markdown("""
        * **TEMPORAL:** Dura temps limitat, el medi es pot recuperar.
        * **PERMANENT:** Dura indefinidament, irreversible.
        """)

    with tab5:
        st.subheader("5. Segons Capacitat de Recuperació")
        st.markdown("""
        * **REVERSIBLE:** El medi pot tornar al seu estat original.
        * **IRREVERSIBLE:** No es pot corregir.
        * **IRRECUPERABLE:** Es perd un valor únic (espècie endèmica).
        * **RECUPERABLE:** Pot revertir-se amb restauració o temps.
        * **FUGAÇ:** Dura molt poc, sense conseqüències (pols puntual).
        * **MITIGABLE:** Pot reduir-se (pantalles antisoroll).
        """)

    with tab6:
        st.subheader("6. Segons la seva Manifestació")
        st.markdown("""
        * **SIMPLE:** Una sola causa, un efecte directe.
        * **ACUMULATIU:** Suma d'impactes repetits al llarg del temps.
        * **SINÈRGIC:** Diversos impactes es combinen i el resultat és **més greu** que la suma de les parts.
        * **LATENT:** Apareix temps després de l'acció.
        * **IMMEDIAT:** Es nota just quan passa l'acció.
        * **DE MOMENT CRÍTIC:** Passa en un moment especialment vulnerable (nidificació d'aus).
        """)

# --- TEORIA 3 ---
elif seleccio == "TEORIA 3: Mesures (Prev, Corr, Comp)":
    st.header("TEORIA 3: Mesures Preventives, Correctores i Compensatòries 🛡️")

    tab1, tab2, tab3, tab4 = st.tabs([
        "Tipus de Mesures", 
        "Recuperació Ambiental", 
        "Impactes a la Fauna", 
        "Impactes Arqueologia"
    ])

    with tab1:
        st.subheader("Definició de Mesures")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("MESURES PREVENTIVES")
            st.write("Eviten l'aparició de l'efecte, modificant l'activitat (tecnologia, disseny, localització...).")
        with col2:
            st.warning("MESURES CORRECTORES")
            st.write("Accions per anul·lar, reduir o modificar els efectes sobre el medi.")
        with col3:
            st.error("MESURES COMPENSATÒRIES")
            st.write("Compensen impactes irrecuperables o inevitables, sense eliminar-los. EX: replantació d’arbres en una zona diferent.")

    with tab2:
        st.subheader("Mesures de Recuperació Ambiental")
        st.markdown("""
        * **Objectiu:** Estètic i ambiental. Restaurar l'aspecte i condicions.
        * **Exemples:**
            * Revegetació per frenar erosió.
            * Restaurar talussos, escombreres o abocadors.
            * Ajardinament en indústries, rotondes o pantalles verdes.
        """)
    
    with tab3:
        st.subheader("Impactes a la Fauna i Mesures")
        st.markdown("""
        * **Ocells:** Salva-pàjaros en línies elèctriques.
        * **Carreteres:** Tancaments per evitar accés; dispositius de sortida.
        * **Petits mamífers:** Mallat progressiu.
        * **Grans mamífers:** Tancaments alts.
        * **Fauna aquàtica:** Escales de peixos en preses.
        * **Passos per animals:** Inferiors (naturals) o Superiors (amb vegetació).
        """)
        
        st.warning("Mesures Compensatòries (Fauna)")
        st.markdown("""
        * Construcció de nous hàbitats en un altre lloc.
        * Trasllat de grans nius.
        * Captura i trasllat d'animals (camaleons, amfibis).
        * Creació de nous frezaderos (zones de posta de peixos).
        """)
    
    with tab4:
        st.subheader("Impactes sobre Arqueologia")
        st.markdown("""
        * **Problema:** Incertesa en la localització; cal evitar que apareguin durant les obres.
        * **Solució:** Estudi previ (cartografia, bibliografia, tècniques de prospecció).
        * **Tècniques de Prospecció:**
            * **Superficial:** Inspecció de camp.
            * **Superficial Intensiva:** Inspecció sistemàtica per quadrícules (més lenta).
        """)

# --- TEORIA 4 ---
elif seleccio == "TEORIA 4: Esgotament de Recursos":
    st.header("TEORIA 4: Esgotament dels Recursos ♻️")
    
    st.subheader("Ordre de Preferència Ambiental (Jerarquia de Gestió de Residus)")
    
    st.info("""
    **1. MINIMITZACIÓ (El més important)**
    * Reduir la quantitat i/o perillositat.
    * Reciclar en origen (dins de fàbrica).
    
    **2. VALORITZACIÓ**
    * **Material:** Reciclatge i reutilització.
    * **Energètica:** Aprofitament com a combustible.
    
    **3. TRACTAMENT**
    * Modificar propietats (neutralitzar, detoxificar, inertització).
    
    **4. DIPÒSIT**
    * Abocament (última opció).
    """)

    st.subheader("10 Raons per Minimitzar Residus")
    with st.expander("Fes clic per veure les 10 raons"):
        st.markdown("""
        1.  **Cost:** La gestió (abocador, incineració) és un cost important.
        2.  **Productes:** Residus = productes no venuts, matèries primeres no aprofitades.
        3.  **Amortització:** Inversions en minimització s’amortitzen ràpid.
        4.  **Racionalització:** Millora processos i costums.
        5.  **Risc:** Redueix risc ambiental, de salut i accidents.
        6.  **Normativa:** Adaptació a les lleis.
        7.  **Situació Legal:** Millora la situació de l'empresa.
        8.  **Relacions:** Millora relacions (Administració, clients, veïns).
        9.  **Subvencions:** Es pot optar a ajudes.
        10. **Competència:** Avantatge i element diferenciador.
        """)

# --- TEORIA 5 ---
elif seleccio == "TEORIA 5: El Sòl":
    st.header("TEORIA 5: El sòl com a recurs no renovable 🍂")
    
    st.error("**SÒL CONTAMINAT:** Conté contaminants en concentracions altes que comporten un **risc real o potencial** per a les persones o el medi.")
    
    tab1, tab2 = st.tabs(["Origen", "Procés de Gestió (Fases)"])

    with tab1:
        st.subheader("Origen dels Sòls Contaminats")
        st.markdown("""
        * **Mala gestió de residus:** Abocaments incontrolats, abandonament d'indústries.
        * **Males pràctiques:** Emmagatzematge incorrecte, fuites en conduccions i tancs.
        * **Accidents:** En transport, emmagatzematge i producció.
        """)
    
    with tab2:
        st.subheader("Procés de Gestió dels Sòls Contaminats a Catalunya")
        
        st.info("**1ª FASE: Reconeixement preliminar**")
        st.write("Reunir dades per avaluar si el sòl pot estar contaminat. Identificar fonts i activitats.")
        
        st.warning("**2ª FASE: Avaluació preliminar**")
        st.write("Si hi ha indicis, fer informe amb mostreig. Es comparen els resultats amb els **Nivells Genèrics de Referència (NGR)**.")
        
        st.error("**3ª FASE: Avaluació detallada**")
        st.write("Valorar l'abast i el risc. Aquí es determina si el risc és:")
        st.markdown("""
        1. **Acceptable** (sòl no contaminat).
        2. **Inacceptable** (sòl contaminat).
        """)
        
        st.success("**4ª FASE: Recuperació**")
        st.write("Redacció i execució d'un projecte de recuperació, amb seguiment i comprovació final.")


# --- TEORIA 6 ---
elif seleccio == "TEORIA 6: Deixalleries":
    st.header("TEORIA 6: Deixalleries / Punt Verd 🗑️")
    
    st.info("""
    * **Funció:** Recepció i emmagatzematge selectiu de residus municipals **no recollits a domicili**.
    * **Obligació:** Municipis amb **> 5.000 habitants**.
    * **Objectiu:** Recuperar i reciclar al màxim.
    """)
    
    st.error("**NO S’HI DUEN:** Matèria orgànica, materials perillosos (explosius, sanitaris).")
    
    st.subheader("Gestió i Costos")
    st.markdown("""
    * **Administració:** Gestor local.
    * **Transport a tractament:** Gestor logístic comú (CIRESA).
    * **Cost Ciutadans:** Gratuït fins a 500 kg.
    * **Cost Comerços/Empreses:** Taxes segons quantitat.
    """)

# --- TEORIA 7 ---
elif seleccio == "TEORIA 7: Gestió de Residus":
    st.header("TEORIA 7: Gestió de Residus Municipals (RM) 🚛")
    
    st.info("**Competència:** És responsabilitat del **municipi**.")
    st.markdown("**Obligacions:** Recollida, transport, valorització, disposició del rebuig.")
    
    st.subheader("Sistemes de Recollida")
    
    with st.expander("1. Recollida Pneumàtica"):
        col1, col2 = st.columns(2)
        with col1:
            st.success("Avantatges")
            st.markdown("""
            * Desapareixen contenidors.
            * Més silenciós.
            * Reducció de males olors.
            * Horari flexible.
            """)
        with col2:
            st.error("Desavantatges")
            st.markdown("""
            * Inversió molt elevada.
            * Difícil en zones consolidades.
            * Reparacions cares.
            * Alt consum energètic.
            """)
    
    with st.expander("2. Recollida amb Contenidors Soterrats"):
        col1, col2 = st.columns(2)
        with col1:
            st.success("Avantatges")
            st.markdown("""
            * Integració estètica.
            * Horaris flexibles.
            * Cost de recollida baix.
            """)
        with col2:
            st.error("Desavantatges")
            st.markdown("""
            * Cost d'intervenció alt.
            * Menys àrees (més desplaçament).
            * Nivells de recuperació baixos.
            * Anonimat (dificulta control).
            """)

    with st.expander("3. Recollida Tradicional (Contenidors al Carrer)"):
        col1, col2 = st.columns(2)
        with col1:
            st.success("Avantatges")
            st.markdown("""
            * Sistema conegut.
            * Horaris flexibles.
            * Cost de recollida baix.
            """)
        with col2:
            st.error("Inconvenients")
            st.markdown("""
            * Problemes d'olors.
            * Ocupen espai públic.
            * Ús indegut (lliurament fora d'horari).
            """)

    with st.expander("4. Recollida Porta a Porta (PaP)"):
        st.write("Lliurar els residus al servei davant de la porta de casa, en dies i hores determinats.")
        col1, col2 = st.columns(2)
        with col1:
            st.success("Avantatges")
            st.markdown("""
            * **Nivells més alts de recollida selectiva.**
            * Es retiren contenidors de la via.
            * **Desapareix l’anonimat.**
            * Permet taxes de pagament per generació.
            * Cost de reciclatge menor.
            """)
        with col2:
            st.error("Inconvenients")
            st.markdown("""
            * Subjecte a un horari de lliurament.
            """)


# --- PÀGINA DE TEST ---
elif seleccio == "Posa't a Prova! (Test) 🎓":
    st.header("Posa't a Prova! 🧠")
    st.markdown("Respon a les preguntes per veure què has après. No pateixis, no és un examen real!")

    # Definir les preguntes, opcions i respostes correctes
    preguntes = [
        {
            "pregunta": "Quina font d'energia és coneguda per generar residus radioactius perillosos?",
            "opcions": ["Centrals Tèrmiques", "Energia Eòlica", "Energia Nuclear", "Cicles Combinats"],
            "correcta": "Energia Nuclear",
            "explicacio": "L'Energia Nuclear genera residus radioactius molt perillosos i cars de tractar."
        },
        {
            "pregunta": "Segons la Teoria 2, un impacte que combina diversos factors i el resultat és 'més greu que la suma de les parts' s'anomena:",
            "opcions": ["Impacte Acumulatiu", "Impacte Sinèrgic", "Impacte Latent", "Impacte Extrem"],
            "correcta": "Impacte Sinèrgic",
            "explicacio": "L'Impacte Sinèrgic és quan diversos impactes es combinen i el resultat és molt més greu que si es comptessin per separat."
        },
        {
            "pregunta": "La 'Desertificació' és un procés principalment...",
            "opcions": ["Natural, causat per cicles astronòmics", "Humà, causat per la desforestació i l'agricultura intensiva", "Exclusivament causat per la construcció", "Un sinònim de sequera"],
            "correcta": "Humà, causat per la desforestació i l'agricultura intensiva",
            "explicacio": "La 'Desertificació' és la pèrdua de capacitat productiva per causes humanes (i naturals). La 'Desertització' és el procés natural."
        },
        {
            "pregunta": "Posar pantalles antisoroll al costat d'una autopista és una mesura...",
            "opcions": ["Preventiva", "Correctora", "Compensatòria", "De recuperació"],
            "correcta": "Correctora",
            "explicacio": "És una mesura Correctora, ja que busca reduir o modificar un efecte (el soroll) que ja s'està produint."
        },
        {
            "pregunta": "Quin és el primer pas (el més preferible) en la jerarquia de gestió de residus?",
            "opcions": ["Valorització Energètica", "Dipòsit", "Tractament", "Minimització"],
            "correcta": "Minimització",
            "explicacio": "L'ordre de preferència és: 1. Minimització, 2. Valorització, 3. Tractament, 4. Dipòsit."
        },
        {
            "pregunta": "En el procés de gestió de sòls contaminats, en quina fase es decideix si el risc és 'acceptable' o 'inacceptable'?",
            "opcions": ["1ª Fase: Reconeixement preliminar", "2ª Fase: Avaluació preliminar", "3ª Fase: Avaluació detallada", "4ª Fase: Recuperació"],
            "correcta": "3ª Fase: Avaluació detallada",
            "explicacio": "A la 3a Fase (Avaluació detallada) es valora el risc i es determina si és acceptable o inacceptable (sòl contaminat)."
        },
        {
            "pregunta": "Les deixalleries són obligatòries per a municipis amb més de...",
            "opcions": ["1.000 habitants", "5.000 habitants", "10.000 habitants", "50.000 habitants"],
            "correcta": "5.000 habitants",
            "explicacio": "La llei obliga als municipis de més de 5.000 habitants a tenir una deixalleria."
        },
        {
            "pregunta": "Quin sistema de recollida de residus aconsegueix els nivells més alts de recollida selectiva?",
            "opcions": ["Porta a Porta", "Contenidors Soterrats", "Recollida Pneumàtica", "Contenidors al Carrer"],
            "correcta": "Porta a Porta",
            "explicacio": "El sistema 'Porta a Porta' té els nivells més alts de recollida selectiva i recuperació, ja que elimina l'anonimat."
        },
        {
            "pregunta": "Un impacte que apareix molt de temps després de l'acció que el causa s'anomena:",
            "opcions": ["Impacte Immediat", "Impacte Fugaç", "Impacte Latent", "Impacte de Moment Crític"],
            "correcta": "Impacte Latent",
            "explicacio": "L'Impacte Latent apareix temps després de l'acció que el causa (ex: acumulació de pesticides al sòl)."
        },
        {
            "pregunta": "El turisme de masses es caracteritza per...",
            "opcions": ["Minimització d'impactes", "Respecte per la capacitat de càrrega", "Ús intensiu dels recursos i massificació", "Beneficis econòmics per a la població local"],
            "correcta": "Ús intensiu dels recursos i massificació",
            "explicacio": "El turisme de masses es defineix per l'ús intensiu de recursos, usos inadequats i massificació, prioritzant el benefici econòmic."
        }
    ]

    # Guardar les respostes de l'usuari a 'session_state'
    if 'respostes_usuari' not in st.session_state:
        st.session_state.respostes_usuari = {}
    
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    def reset_quiz():
        st.session_state.respostes_usuari = {}
        st.session_state.submitted = False

    # Formulari del test
    with st.form("quiz_form"):
        for i, q in enumerate(preguntes):
            st.subheader(f"Pregunta {i+1}")
            st.write(q["pregunta"])
            # Utilitza 'index=None' per a cap opció preseleccionada
            st.session_state.respostes_usuari[i] = st.radio(
                "Selecciona la teva resposta:", 
                q["opcions"], 
                key=f"q_{i}",
                index=None
            )
            st.markdown("---")
        
        submitted = st.form_submit_button("Corregir el Test")

    if submitted:
        st.session_state.submitted = True

    if st.session_state.submitted:
        score = 0
        total_preguntes = len(preguntes)
        
        # Comprovar si s'han respost totes les preguntes
        if len(st.session_state.respostes_usuari) != total_preguntes or None in st.session_state.respostes_usuari.values():
            st.warning("Si us plau, respon a totes les preguntes abans de corregir.")
            # Reiniciem 'submitted' per forçar a l'usuari a respondre tot
            st.session_state.submitted = False
        else:
            st.header("Resultats del Test")
            for i, q in enumerate(preguntes):
                resposta_usuari = st.session_state.respostes_usuari[i]
                resposta_correcta = q["correcta"]
                
                if resposta_usuari == resposta_correcta:
                    score += 1
                    st.success(f"**Pregunta {i+1}: Correcte!** 👍")
                    st.write(f"Has triat: {resposta_usuari}")
                else:
                    st.error(f"**Pregunta {i+1}: Incorrecte.** ❌")
                    st.write(f"La teva resposta: {resposta_usuari}")
                    st.write(f"**Resposta correcta:** {resposta_correcta}")
                    st.info(f"**Explicació:** {q['explicacio']}")
                st.markdown("---")
            
            # Mostrar puntuació final
            st.subheader(f"Puntuació Final: {score} de {total_preguntes}")
            percentatge = (score / total_preguntes) * 100
            
            if percentatge == 100:
                st.balloons()
                st.success("**Perfecte! Ho has clavat!**")
            elif percentatge >= 50:
                st.warning(f"**Molt bé! ({percentatge:.0f}%)** Continua repassant.")
            else:
                st.error(f"**Cal repassar una mica més. ({percentatge:.0f}%)** Ànims!")
            
            st.button("Tornar a intentar", on_click=reset_quiz)
