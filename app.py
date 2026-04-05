import streamlit as st

st.set_page_config(page_title="Cerebro de Obra TOTAL - Adrián Yépez", layout="wide")

# Título con jerarquía profesional
st.title("🏗️ Cerebro de Obra: Control Maestro de Construcción")
st.subheader("Director de Obra: Adrián Yépez")

# --- BARRA LATERAL: CONFIGURACIÓN DINÁMICA ---
st.sidebar.header("📏 1. Dimensiones y Excavación")
largo = st.sidebar.number_input("Largo de la Obra (m)", min_value=1.0, value=6.0)
ancho = st.sidebar.number_input("Ancho de la Obra (m)", min_value=1.0, value=4.0)
alto_pared = st.sidebar.number_input("Alto de Paredes (m)", min_value=1.0, value=2.6)
prof_hueco = st.sidebar.selectbox("Profundidad de Huecos/Fundaciones (m)", [0.50, 0.80, 1.00, 1.50, 2.00, 2.50, 3.00], index=2)

st.sidebar.header("⚙️ 2. Estructura y Cerramiento")
tipo_soporte = st.sidebar.selectbox("Tipo de Soporte Vertical", ["Concreto Vaciado", "Tubo Estructural"])
medida_tubo = st.sidebar.selectbox("Medida del Tubo (Si aplica)", ["2x2", "3x3", "4x4", "6x6", "8x8"], index=2)
n_guias = st.sidebar.selectbox("Cabillas por Columna (Guías)", [4, 6, 8, 12])
dist_col = st.sidebar.selectbox("Separación entre Columnas (m)", [3.0, 3.5, 4.0, 5.0])
tipo_techo = st.sidebar.selectbox("Tipo de Cubierta/Techo", ["Acerolit / Zinc", "Platabanda (Losa)"])

st.sidebar.header("🚿 3. Instalaciones (Desplegable)")
# Aquí tienes lo que pediste: selección desplegable para baños
n_banos = st.sidebar.selectbox("¿Cuántos Baños llevará la obra?", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=1)
n_puntos_elec = st.sidebar.number_input("Cantidad de Puntos Eléctricos", min_value=1, value=12)

st.sidebar.header("💰 4. Precios del Mercado ($)")
p_cemento = st.sidebar.number_input("Saco Cemento", value=8.5)
p_bloque = st.sidebar.number_input("Bloque 15cm", value=0.65)
p_cabilla = st.sidebar.number_input("Cabilla 1/2", value=10.5)
p_tubo_est = st.sidebar.number_input(f"Tubo {medida_tubo} (6m)", value=35.0)
p_lamina = st.sidebar.number_input("Lámina de Techo", value=18.0)
p_kit_plomeria = st.sidebar.number_input("Kit Tuberías (Blanca/Negra) por Baño", value=150.0)
p_kit_electrico = st.sidebar.number_input("Kit Eléctrico (Cables/Tubos) por Punto", value=18.0)

# --- LÓGICA DE CÁLCULO DE MATERIALES ---
perimetro = (largo + ancho) * 2
area_piso = largo * ancho
n_col = round(perimetro / dist_col) + 1
largo_guia = prof_hueco + alto_pared + 0.50 

# Estructura de Acero
if tipo_soporte == "Concreto Vaciado":
    total_cabillas = round((n_col * n_guias * largo_guia + (perimetro * 8)) / 6)
    total_tubos = 0
else:
    total_tubos = round(((n_col * alto_pared) + perimetro) / 6)
    total_cabillas = round(n_col * 2)

# Albañilería
bloques_total = round(((perimetro * alto_pared) - 4) * 12.5)
cem_pegar = round(bloques_total / 80)
cem_friso = round((perimetro * alto_pared * 2) * 0.12)

# Concreto y Agregados
vol_fund = n_col * ((0.6 * 0.6 * 0.3) + (0.25 * 0.25 * (prof_hueco - 0.3)))
vol_vigas = (perimetro * 0.20 * 0.20) + (area_piso * 0.05) 
vol_total_concreto = vol_fund + vol_vigas
cem_vaciado = round(vol_total_concreto * 8.5)
m3_lavada = round(vol_total_concreto * 0.55, 1)
m3_piedra = round(vol_total_concreto * 0.85, 1)
m3_mina = round((cem_pegar + cem_friso) * 0.1, 1)

# Instalaciones (Aguas y Electricidad)
costo_plomeria = n_banos * p_kit_plomeria
costo_electricidad = n_puntos_elec * p_kit_electrico
n_laminas = round((area_piso * 1.15) / 3.6) if tipo_techo == "Acerolit / Zinc" else 0

# --- REPORTE TÉCNICO DETALLADO ---
st.header("📋 Reporte Detallado de Insumos")
c1, c2 = st.columns(2)

with c1:
    with st.expander("🏗️ Estructura y Fundaciones", expanded=True):
        st.write(f"*Columnas:* {n_col} unidades")
        st.write(f"*Huecos:* {prof_hueco}m de profundidad")
        st.write(f"*Concreto en Bases:* {round(vol_fund, 2)} m3")
        st.write(f"*Cabillas 1/2:* {total_cabillas} piezas de 6m")
        if total_tubos > 0:
            st.write(f"*Tubos Estructurales {medida_tubo}:* {total_tubos} piezas")

    with st.expander("🧱 Paredes y Acabados"):
         st.write(f"**Bloques de 15cm:**{bloques_total} unidades")
