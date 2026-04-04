import streamlit as st
import math

# Configuración de la página (La "cara" de la App)
st.set_page_config(page_title="Cerebro de Obra - Adrián Yépez", page_icon="🏗️")

st.title("🏗️ Sistema de Cómputos Métricos PRO")
st.markdown("### Desarrollado por: Adrián Yépez - Upata, Edo. Bolívar")
st.write("---")

# --- ENTRADA DE DATOS (Interfaz Visual) ---
st.sidebar.header("📐 Medidas de la Obra")
largo = st.sidebar.number_input("Largo (m)", min_value=0.0, value=10.0, step=0.1)
ancho = st.sidebar.number_input("Ancho (m)", min_value=0.0, value=6.0, step=0.1)
alto = st.sidebar.number_input("Altura de Paredes (m)", min_value=0.0, value=2.7, step=0.1)
tipo_techo = st.sidebar.selectbox("Tipo de Techo", ["Acerolit (Estructura Metálica)", "Platabanda (Concreto)"])

st.sidebar.header("💰 Precios de Mercado ($)")
p_cemento = st.sidebar.number_input("Saco de Cemento", value=8.5)
p_bloque = st.sidebar.number_input("Bloque (unidad)", value=0.65)
p_cabilla_12 = st.sidebar.number_input("Metro Cabilla 1/2", value=1.2)
p_cabilla_38 = st.sidebar.number_input("Metro Cabilla 3/8", value=0.8)
p_arena = st.sidebar.number_input("Metro Cúbico Arena", value=25.0)
p_punto_elec = st.sidebar.number_input("Punto Eléctrico (Materiales)", value=15.0)

# --- CÁLCULOS INTERNOS (Tu Cerebro de Obra) ---
area_piso = largo * ancho
perimetro = (largo + ancho) * 2
area_paredes = (perimetro * alto) - (area_piso * 0.12)
num_columnas = math.ceil(perimetro / 3) + 1

# Estructura
m3_excavacion = round(num_columnas * 0.5, 2)
cabilla_1_2 = math.ceil(num_columnas * 6) + math.ceil(perimetro * 1.5)
estribos_3_8 = math.ceil((perimetro + (num_columnas * alto)) / 0.20)
alambre = round((cabilla_1_2 + estribos_3_8) * 0.05, 1)

# Albañilería
bloques = math.ceil(area_paredes * 13)
cemento_total = math.ceil((area_piso * 1.2) + (area_paredes * 0.4) + (num_columnas * 1.5))
arena_total = round(area_piso * 0.35, 2)
pintura = math.ceil(area_paredes / 35)

# Electricidad
puntos = math.ceil(area_piso / 3.5)
cable_12 = math.ceil(puntos * 0.6 * 6)
cable_14 = math.ceil(puntos * 0.4 * 4)

# --- BOTÓN DE CÁLCULO ---
if st.button("🚀 GENERAR PRESUPUESTO PROFESIONAL"):
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏗️ Estructura y Albañilería")
        st.write(f"✅ *Excavación:* {m3_excavacion} m³")
        st.write(f"✅ *Bloques 15cm:* {bloques} und")
        st.write(f"✅ *Cemento:* {cemento_total} sacos")
        st.write(f"✅ *Cabilla 1/2:* {cabilla_1_2} m")
        st.write(f"✅ *Estribos 3/8:* {estribos_3_8} m")
        st.write(f"✅ *Alambre Amarre:* {alambre} kg")
    
    with col2:
        st.subheader("🔌 Electricidad y Acabados")
        st.write(f"✅ *Cable #12:* {cable_12} m")
        st.write(f"✅ *Cable #14:* {cable_14} m")
        st.write(f"✅ *Puntos Elec:* {puntos} (Cajetín/Tomas)")
        st.write(f"✅ *Pintura:* {pintura} cuñetes")

    # Techo
    st.subheader("🏠 Cubierta")
    if "Acerolit" in tipo_techo:
        laminas = math.ceil(area_piso / 2.8)
        tubos = math.ceil(area_piso * 1.5)
        st.write(f"✅ *Láminas:* {laminas} | *Tornillos:* {laminas*10}")
        st.write(f"✅ *Estructura (Tubo 2x1):* {tubos} metros")
    else:
        st.write("✅ *Platabanda:* Materiales incluidos en concreto y acero estructural.")

    # COSTO FINAL
    costo_total = (cemento_total * p_cemento) + (bloques * p_bloque) + \
                  (cabilla_1_2 * p_cabilla_12) + (estribos_3_8 * p_cabilla_38) + \
                  (puntos * p_punto_elec)
    
    st.divider()
    st.success(f"## 💰 TOTAL MATERIALES: ${costo_total:,.2f}")
    st.info("💡 Este presupuesto no incluye mano de obra. Precios calculados según mercado local.")