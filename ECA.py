import streamlit as st

# --- Funcions per a les Seccions ---

def mostrar_biomes():
    st.header("🌍 Biomes de la Terra")
    st.markdown("Conjunt de comunitats que ocupen una àrea geogràfica extensa amb una **vegetació climàtica uniforme** i un clima característic.")
    
    biomes_data = {
        "Selva Tropical": "Clima càlid i molt humit tot l'any. Vegetació exuberant, perennifòlia, molt estratificada.",
        "Desert": "Molt àrid, gran oscil·lació tèrmica. Plantes **xeròfiles**, adaptades a la sequera.",
        "Taigà (Bosc Coníferes)": "Fred (hivern llarg) i humit. Boscos densos de coníferes perennifòlies (pins, avets).",
        "Tundra": "Temperatures molt baixes, sòl amb permagel. Molses, líquens, herbes i arbustos nans.",
        "Bosc Mediterrani": "Estius secs i calorosos, hiverns suaus. Vegetació **escleròfil·la** (fulla dura, perenne)."
    }

    for bioma, descripcio in biomes_data.items():
        with st.expander(f"**{bioma}**"):
            st.write(descripcio)

def mostrar_climogrames():
    st.header("📊 Anàlisi de Climogrames")
    st.markdown("Gràfic que mostra el clima d'un lloc combinant la **Temperatura mitjana mensual** ($\text{T}$ en $^{\circ}\text{C}$) i la **Precipitació mensual** ($\text{P}$ en $\text{mm}$).")
    
    st.subheader("Regla Clau: Període Sec/Humit")
    st.markdown("""
    Aquesta regla s'aplica utilitzant els dos eixos (T en $^\circ C$ i P en mm) amb l'escala 1:2.
    """)
    st.code("Període Sec: T (°C) > 2 · P (mm) ➡️ La línia de T queda per sobre de les barres de P.")
    st.code("Període Humit: T (°C) < 2 · P (mm) ➡️ La línia de T queda per sota de les barres de P.")

    st.subheader("Elements d'Interpretació")
    st.markdown("""
    * **Eix Horitzontal:** Mesos de l'any.
    * **Línia (T):** Eix esquerre. Indica si fa calor o fred.
    * **Barres (P):** Eix dret. Indica si plou molt o poc.
    """)

def mostrar_adaptacions():
    st.header("🌿 Adaptacions de la Flora")
    st.markdown("Les plantes s'adapten a les condicions ambientals extremes de l'hàbitat (l'objectiu és la supervivència i la reproducció).")
    
    adaptacions_data = {
        "Sequera i T. Altes (Xeròfiles)": [
            "Fulles petites, transformació en espines, pèls i ceres per reduir la transpiració.",
            "Acumulació d'aigua en els teixits (succulència).",
            "Arrels profundes i llargues (ex: Olea europaea).",
        ],
        "Temperatura Freda": [
            "Plantes petites i arrapades al terra (millor aprofitament del calor i resistència al vent).",
            "Saba més espessa per ralentir la congelació.",
            "Pèrdua de fulla a l'hivern (caducifolis).",
        ],
        "Falta de Llum": [
            "Augment de la superfície foliar.",
            "Augment de la concentració de clorofil·la.",
            "Mecanismes per a trepar i accedir a la llum (liana, gènere *Bromelia*).",
        ],
        "Incendis (Pirofítiques)": [
            "Resistència passiva al foc (aigua a les fulles).",
            "Rebrotat ràpid després d'un incendi."
        ]
    }

    for condicio, llista_adaptacions in adaptacions_data.items():
        with st.expander(f"**Adaptacions a: {condicio}**"):
            for adaptacio in llista_adaptacions:
                st.markdown(f"- {adaptacio}")
                
def mostrar_classificacio():
    st.header("🗺️ Hàbitats i Classificació CORINE")
    
    st.subheader("1. Classificació CORINE Biotopes")
    with st.expander("Què és?"):
        st.markdown("""
        * **Sistema de classificació d'hàbitats** més utilitzat a la Unió Europea.
        * Estableix una taxonomia jeràrquica per a hàbitats naturals, seminaturals i artificialitzats.
        * Objectiu: **Ordenar i comparar la diversitat d'hàbitats** a escala europea.
        """)

    st.subheader("2. Hàbitats Clau a Catalunya")
    st.markdown("La diversitat geogràfica i climàtica crea hàbitats únics:")
    
    hàbitats_cat = {
        "Zona Litoral": "Dunes, aiguamolls, prats halòfils.",
        "Zona Prelitoral i Central": "Boscos de fulla dura: **Alzinars** (fulla perenne), **suredes**, brolles mediterrànies.",
        "Zona Pirinenca": "**Fagedes** (típicament vessants obacs i sòls àcids), avetoses, prats alpins."
    }
    
    for zona, exemples in hàbitats_cat.items():
        st.markdown(f"**{zona}**: {exemples}")
        
    st.subheader("3. Endemismes")
    with st.expander("Conceptes Clau d'Endemismes"):
        st.markdown("""
        * **Endemisme:** Espècie que es troba de manera natural **només** en una àrea geogràfica molt concreta (un sol país, una illa, etc.).
        * **Causes Comunes de l'Aïllament:**
            * **Geogràfic:** Muntanyenc, insular, edàfic (sòl).
            * **Ambiental:** Canvis bruscos de les condicions (glaciacions, aridesa).
        """)

# --- Estructura Principal de l'App ---
def main():
    st.set_page_config(
        page_title="UF1 - Caracterització d'Hàbitats",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("📚 Aplicació d'Estudi Interactiva: UF 1 - Caracterització d'Hàbitats")
    st.markdown("---")

    # Sidebar per a informació ràpida
    with st.sidebar:
        st.header("🎯 Objectius de la UF1")
        st.info("""
        Repàs estructurat dels conceptes principals de la unitat:
        - Biomes i la seva distribució global.
        - Lectura i interpretació de Climogrames.
        - Adaptacions de la Flora a diferents condicions.
        - Classificació (CORINE) i Hàbitats a Catalunya.
        """)
        st.image("https://images.unsplash.com/photo-1546960143-690a6cc33c3a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", caption="Diversitat d'hàbitats. Font: Unsplash", use_column_width=True) 
        st.markdown("---")
        st.write("Codi generat per Gemini (Google)")


    # Navegació principal amb Pestanyes
    tab1, tab2, tab3, tab4 = st.tabs([
        "🌍 Biomes de la Terra",
        "📊 Climogrames",
        "🌿 Adaptacions Flora",
        "🗺️ Classificació i Hàbitats Catalunya"
    ])

    with tab1:
        mostrar_biomes()

    with tab2:
        mostrar_climogrames()

    with tab3:
        mostrar_adaptacions()

    with tab4:
        mostrar_classificacio()

if __name__ == "__main__":
    main()
