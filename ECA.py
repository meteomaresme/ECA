import streamlit as st
import pandas as pd

# --- Configuració de la Pàgina ---
st.set_page_config(
    page_title="Guia d'Estudi RA1",
    page_icon="🌍",
    layout="wide"
)

# --- Barra Lateral de Navegació ---
st.sidebar.title("Temari RA1: Medi Ambient")
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
    "Posa't a Prova! (Test)"
]
seleccio = st.sidebar.radio("Navegació del Temari:", temari_options)

st.sidebar.markdown("---")
st.sidebar.info("Aquesta app t'ajuda a preparar l'examen sobre impacte ambiental.")


# --- Contingut de les Pàgines ---

if seleccio == "Inici":
    st.title("Guia d'Estudi: Impacte Ambiental (RA1) 🌳")
    st.markdown("### Benvingut/da a la teva eina d'estudi interactiva.")
    st.write("Fes servir el menú de l'esquerra per navegar entre les diferents teories del curs.")
    st.write("Quan et sentis preparat/da, ves a la secció **'Posa't a Prova!'** per fer un petit examen d'autoavaluació.")
    
    st.image("https://images.unsplash.com/photo-1473916174681-b64817445276?q=80&w=2070", 
             caption="", 
             use_column_width=True)

# --- TEORIA 1 ---
elif seleccio == "TEORIA 1: Activitats Humanes":
    st.header("TEORIA 1: Principals Activitats Humanes que Afecten el Medi Ambient")
    
    st.markdown("""
    1. Industria/Energia
    2. Agricultura, Ramaderia i Silvicultura
    3. Indústria, els plàstics
    4. Turisme i activitats recreatives
    5. Transport
    6. Infraestructures
    7. Desertització
    """)

    st.subheader("1. Fonts de generació d'energia més perjudicials")
    with st.expander("CENTRALS TÈRMIQUES"):
        st.write("Crema de combustibles fòssils (carbó o petroli).")
        st.write("● **Impactes:** Emissions de CO₂, efecte hivernacle global i pluja àcida.")
    with st.expander("ENERGIA NUCLEAR"):
        st.write("Residus radioactius molt perillosos, difícils i cars de tractar.")
    with st.expander("CICLES COMBINATS (Gas Natural)"):
        st.write("L’explotació dels jaciments contamina aigües i sòls i danya els ecosistemes que travessen els gasoductes.")
    with st.expander("ENERGIA BIOMASSA"):
        st.write("Provoca contaminació de l’aire, pèrdua de vegetació, destrucció de biodiversitat, erosió del sòl i menys retenció d’aigua.")
    with st.expander("ENERGIA EÒLICA"):
        st.write("Afecta la fauna local i empobreix la terra.")
    with st.expander("ENERGIA HIDRÀULICA"):
        st.write("La construcció d’embassaments i preses provoca fragmentació i pèrdua d’hàbitats, i pertorba la flora i la fauna.")

    st.subheader("2. Treballs agrícoles, ramaders i silvícoles")
    st.markdown("#### 2.1 L'agricultura")
    st.markdown("""
    * **Aliments per a tots:** gran ús de superfície
    * **Aigua:** recurs escàs i essencial
    * **Adobs i pesticides:** possible contaminació
    * **Fitosanitaris:** eliminació de plagues i males herbes
    * **Fertilitzants:** ús massiu per enriquir la terra
    * **Transgènics i cultius energètics:** pèrdua de diversitat genètica
    * **Sòl:** degradació i pèrdua
    """)
    
    st.markdown("#### 2.2 Ramaderia")
    st.markdown("""
    * **Emissions GEH:** contribueix al 12–14,5% del canvi climàtic global.
    * **Desforestació i biodiversitat:** s’eliminen boscos per pastures.
    * **Contaminació:** fertilitzants, plaguicides i dejeccions.
    * **Aigua:** es necessita molta aigua.
    * **Salut humana:** excés de carn, ús d’antibiòtics.
    * **Benestar animal:** condicions d’estrès i confinament.
    """)

    st.markdown("#### 2.3 Silvicultura")
    col1, col2 = st.columns(2)
    with col1:
        st.info("Funcions de Protecció")
        st.markdown("""
        * **Clima:** absorbeixen CO₂.
        * **Genètica:** protegeix la diversitat.
        * **Terra:** evita l’erosió.
        * **Hàbitats humans:** produeixen oxigen.
        """)
    with col2:
        st.warning("Problemes Ambientals Associats")
        st.markdown("""
        * **Desforestació**
        * **Erosió del sòl**
        * **Canvi climàtic** (menys boscos, més CO₂)
        * **Alteració del cicle de l’aigua**
        * **Pèrdua de biodiversitat**
        * **Ús de químics**
        """)

    st.subheader("3. Indústria i els plàstics")
    col1, col2 = st.columns(2)
    with col1:
        st.success("BIODEGRADABLE")
        st.write("Substàncies que els bacteris i fongs descomponen ràpidament.")
    with col2:
        st.error("NO BIODEGRADABLE")
        st.write("Substàncies que no es descomposen o ho fan de manera molt lenta.")
    st.markdown("""
    * **Contaminants Biodegradables:** Deixalles orgàniques (compostatge, metanització -> biogàs).
    * **Contaminants No Biodegradables:** Plàstics, metalls pesants, piles.
    * **Plàstics com a deixalles:** No biodegradables, transportats fàcilment, baixa densitat, impacte visual.
    """)
    
    st.subheader("4. Turisme i activitats recreatives")
    st.markdown("""
    **Causes dels Impactes:**
    * L'ocupació del territori.
    * La mobilitat dels turistes.
    * La generació de residus sòlids urbans.
    * El consum de recursos hídrics.
    * L'activitat de les empreses turístiques.
    * Els comportaments dels mateixos turistes.
    """)
    with st.expander("Sostenibilitat i Turisme Sostenible"):
        st.markdown("""
        * **Sostenibilitat:** Procés on factors interconnectats generen formes de vida eficients i respectuoses.
        * **Desenvolupament Sostenible:** Satisfà les necessitats del present sense comprometre les de les generacions futures.
        * **Turisme Sostenible (OMT):** Satisfà necessitats actuals, protegint recursos i oportunitats per al futur.
        """)
    with st.expander("Turisme de Masses vs. Sostenible"):
        st.markdown("""
        | TURISME DE MASSES | TURISME SOSTENIBLE |
        | :--- | :--- |
        | 1. Ús intensiu dels recursos | 1. Consideració recursos |
        | 2. Usos inadequats | 2. Capacitat de càrrega |
        | 3. Massificació | 3. Minimització impactes |
        | 4. Beneficis econòmics | 4. Beneficis econòmics, però no a qualsevol preu |
        """)

    st.subheader("5. Transport")
    st.markdown("Veure detalls a Teoria 3 (Impactes i Mesures)")
    
    st.subheader("6. Infraestructures")
    st.markdown("Veure detalls a Teoria 3 (Impactes i Mesures)")

    st.subheader("7. Desertització")
    col1, col2 = st.columns(2)
    with col1:
        st.warning("Desertització (Procés Natural)")
        st.write("Zona humida passa a desèrtica sense intervenció humana.")
        st.write("**Causes:** Astronòmiques (Cicles de Milankovic), Geomorfològiques (Orogènia), Dinàmiques.")
    with col2:
        st.error("Desertificació (Causa Humana)")
        st.write("Zona fèrtil perd capacitat de producció per causes humanes i naturals.")
        st.write("**Causes Antròpiques:** Deforestació, agricultura intensiva, urbanització.")
        st.write("**Causes Naturals:** Sequera, canvis climàtics.")
    
    with st.expander("Impacte Ambiental i Mitigació de la Desertificació"):
        st.markdown("""
        **Impactes:**
        * Pèrdua de biodiversitat
        * Degradació i Erosió del sòl
        * Canvis en el clima local
        * Escassetat d’aigua
        * Conflictes socials i Migració forçada
        
        **Mesures de Mitigació:**
        * Reforestació
        * Pràctiques agrícoles sostenibles
        * Maneig sostenible de l’aigua
        * Educació i conscienciació
        """)

# --- TEORIA 2 ---
elif seleccio == "TEORIA 2: Identificació d'Impactes":
    st.header("TEORIA 2: Identificació i Magnitud dels Impactes")
    st.info("Impacte ambiental: qualsevol canvi en el medi ambient causat per accions humanes o naturals.")
    
    st.subheader("1. Segons el seu Caràcter")
    col1, col2 = st.columns(2)
    with col1:
        st.success("POSITIU")
        st.write("Milloren el medi (Restauració, campanyes).")
        st.success("IMPACTE MÍNIM O LLEU")
        st.write("Efectes petits o reversibles.")
    with col2:
        st.error("NEGATIU")
        st.write("Perjudica el medi (Erosió, contaminació).")
        st.error("IMPACTE NOTABLE O SIGNIFICATIU")
        st.write("Efectes greus o apreciables.")
        
    st.subheader("2. Segons Relació Causa-Efecte")
    st.markdown("""
    * **IMPACTE DIRECTE:** Immediat (vessament d'olis).
    * **IMPACTE INDIRECTE:** Conseqüència d'un directe (animals afectats pel sòl contaminat).
    """)

    st.subheader("3. Segons Extensió")
    st.markdown("""
    * **IMPACTE PUNTUAL:** Zona petita (abocament tòxic al riu).
    * **IMPACTE PARCIAL:** Afecta només una part de l’ecosistema.
    * **IMPACTE EXTREM:** Alteracions greus, irreversibles, afecta gran part.
    * **UBICACIÓ CRÍTICA:** Lloc molt sensible (abocament aigües amunt d'una presa).
    """)

    st.subheader("4. Segons Persistència")
    st.markdown("""
    * **IMPACTE TEMPORAL:** Dura temps limitat, el medi es pot recuperar.
    * **IMPACTE PERMANENT:** Dura indefinidament, irreversible.
    """)

    st.subheader("5. Segons Capacitat de Recuperació")
    st.markdown("""
    * **REVERSIBLE:** El medi pot tornar al seu estat original.
    * **IRREVERSIBLE:** No es pot corregir.
    * **IRRECUPERABLE:** Es perd un valor únic (espècie endèmica).
    * **RECUPERABLE:** Pot revertir-se amb restauració o temps.
    * **FUGAÇ:** Dura molt poc, sense conseqüències (pols puntual).
    * **MITIGABLE:** Pot reduir-se (pantalles antisoroll).
    """)

    st.subheader("6. Segons la seva Manifestació")
    st.markdown("""
    * **IMPACTE SIMPLE:** Una sola causa, un efecte directe.
    * **IMPACTE ACUMULATIU:** Suma d'impactes repetits al llarg del temps.
    * **IMPACTE SINÈRGIC:** Diversos impactes es combinen i el resultat és **més greu** que la suma de les parts.
    * **IMPACTE LATENT:** Apareix temps després de l'acció.
    * **IMPACTE IMMEDIAT:** Es nota just quan passa l'acció.
    * **IMPACTE DE MOMENT CRÍTIC:** Passa en un moment especialment vulnerable (nidificació d'aus).
    """)

# --- TEORIA 3 ---
elif seleccio == "TEORIA 3: Mesures (Prev, Corr, Comp)":
    st.header("TEORIA 3: Mesures Preventives, Correctores i Compensatòries")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("MESURES PREVENTIVES")
        st.write("Eviten l'aparició de l'efecte, modificant l'activitat (tecnologia, disseny, localització...).")
    with col2:
        st.warning("MESURES CORRECTORES")
        st.write("Accions per anul·lar, reduir o modificar els efectes sobre el medi.")
    with col3:
        st.error("MESURES COMPENSATORIES")
        st.write("Compensen impactes irrecuperables o inevitables, sense eliminar-los.")

    st.subheader("Mesures de Recuperació Ambiental")
    st.markdown("""
    * **Objectiu:** Estètic i ambiental.
    * **Exemples:** Revegetació, restaurar talussos, ajardinament.
    """)
    
    st.subheader("Impactes a la Fauna i Mesures")
    st.markdown("""
    * **Ocells:** Salva-pàjaros en línies elèctriques.
    * **Carreteres:** Tancaments, dispositius de sortida.
    * **Mamífers:** Mallat, tancaments, passos inferiors/superiors.
    * **Fauna aquàtica:** Escales de peixos en preses.
    """)
    
    st.subheader("Impactes sobre Arqueologia")
    st.markdown("""
    * **Problema:** Incertesa en la localització.
    * **Solució:** Estudi previ (cartografia, bibliografia, prospecció).
    * **Tècniques:** Prospecció superficial (inspecció de camp) o intensiva (quadrícules).
    """)

# --- TEORIA 4 ---
elif seleccio == "TEORIA 4: Esgotament de Recursos":
    st.header("TEORIA 4: Esgotament dels Recursos i Jerarquia de Gestió de Residus")
    
    st.subheader("Ordre de Preferència Ambiental de la Gestió")
    st.info("""
    1.  **MINIMITZACIÓ:** Reduir la quantitat i/o perillositat.
    2.  **VALORITZACIÓ:** Recuperar recursos materials (reciclatge) o energètics (combustible).
    3.  **TRACTAMENT:** Modificar propietats (neutralitzar, detoxificar).
    4.  **DIPÒSIT:** Abocament a un terreny.
    """)

    st.subheader("10 Raons per Minimitzar Residus")
    with st.expander("Veure les 10 raons"):
        st.markdown("""
        1.  Cost de gestió (abocador, incineració).
        2.  Residus = productes no venuts, matèries primeres no aprofitades.
        3.  Inversions en minimització s’amortitzen ràpid.
        4.  Racionalització de processos i costums.
        5.  Reducció de risc ambiental, de salut i accidents.
        6.  Adaptació a normatives.
        7.  Millora de la situació ambiental i legal.
        8.  Millora de relacions (Administració, clients, veïns).
        9.  Opció a subvencions.
        10. Avantatge competitiu.
        """)

# --- TEORIA 5 ---
elif seleccio == "TEORIA 5: El Sòl":
    st.header("TEORIA 5: El sòl com a recurs no renovable")
    
    st.error("SÒL CONTAMINAT: Conté contaminants en concentracions altes que comporten un risc real o potencial.")
    
    st.subheader("Origen dels Sòls Contaminats")
    st.markdown("""
    * **Mala gestió de residus:** Abocaments incontrolats.
    * **Males pràctiques:** Emmagatzematge incorrecte, fuites.
    * **Accidents:** Transport, producció.
    """)
    
    st.subheader("Procés de Gestió dels Sòls Contaminats a Catalunya")
    st.markdown("""
    * **1ª FASE: Reconeixement preliminar:** Reunir dades, avaluar si pot estar contaminat.
    * **2ª FASE: Avaluació preliminar:** Si hi ha indicis, fer informe amb mostreig i comparació amb Nivells Genèrics de Referència (NGR).
    * **3ª FASE: Avaluació detallada:** Valorar l'abast i el risc. Es determina si el risc és **acceptable** (sòl no contaminat) o **inacceptable** (sòl contaminat).
    * **4ª FASE: Recuperació:** Redacció i execució d'un projecte de recuperació.
    """)

# --- TEORIA 6 ---
elif seleccio == "TEORIA 6: Deixalleries":
    st.header("TEORIA 6: Deixalleries / Punt Verd")
    
    st.info("""
    * **Funció:** Recepció i emmagatzematge selectiu de residus municipals no recollits a domicili.
    * **Obligació:** Municipis amb > 5.000 habitants.
    * **Objectiu:** Recuperar i reciclar al màxim.
    """)
    
    st.markdown("""
    **No s'hi duen:** Matèria orgànica, materials perillosos (explosius, sanitaris).
    
    **Gestió:**
    * Administració: Gestor local.
    * Transport: Gestor logístic comú (CIRESA).
    
    **Costos:**
    * Ciutadans: Gratuït fins a 500 kg.
    * Comerçants i petites empreses: Taxes segons quantitat.
    """)

# --- TEORIA 7 ---
elif seleccio == "TEORIA 7: Gestió de Residus":
    st.header("TEORIA 7: Gestió de Residus Municipals (RM)")
    
    st.markdown("""
    * **Competència:** Responsabilitat del municipi.
    * **Obligacions:** Recollida, transport, valorització, disposició del rebuig.
    """)
    
    st.subheader("Sistemes de Recollida")
    
    with st.expander("Recollida Pneumàtica"):
        st.markdown("""
        **Avantatges:** Desapareixen contenidors, menys soroll, menys olors, horari flexible.
        **Desavantatges:** Inversió elevada, car d'implantar en zones consolidades, reparacions cares, alt consum energètic.
        """)
    
    with st.expander("Recollida amb Contenidors Soterrats"):
        st.markdown("""
        **Avantatges:** Integració estètica, horaris flexibles, cost de recollida baix.
        **Desavantatges:** Cost d'intervenció alt, menys àrees (més desplaçament), nivells de recuperació baixos, anonimat.
        """)

    with st.expander("Recollida Tradicional (Contenidors al Carrer)"):
        st.markdown("""
        **Avantatges:** Sistema conegut, horaris flexibles, cost de recollida baix.
        **Inconvenients:** Problemes d'olors, ocupen espai, ús indegut.
        """)

    with st.expander("Recollida Porta a Porta (PaP)"):
        st.markdown("""
        **Avantatges:** **Nivells més alts de recollida selectiva**, es retiren contenidors, desapareix l'anonimat, permet pagament per generació, cost de reciclatge menor.
        **Inconvenients:** Subjecte a horari de lliurament.
        """)


# --- PÀGINA DE TEST ---
elif seleccio == "Posa't a Prova! (Test)":
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
