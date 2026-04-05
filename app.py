[11:19 a.m., 5/4/2026] zury Nuñez: import streamlit as st

st.set_page_config(page_title="Cerebro de Obra TOTAL - Adrián Yépez", layout="wide")

st.title("🏗️ Cerebro de Obra: Presupuesto Maestro Global")
st.write("Cálculo integral: Estructura, Excavación, Albañilería, Plomería y Electricidad.")

# --- BARRA LATERAL: CONFIGURACIÓN DE OBRA ---
st.sidebar.header("📏 1. Medidas y Excavación")
largo = st.sidebar.number_input("Largo (m)", min_value=1.0, value=6.0)
ancho = st.sidebar.number_input("Ancho (m)", min_value=1.0, value=4.0)
alto_pared = st.sidebar.number_input("Alto Pared (m)", min_value=1.0, value=2.6)

# BOTÓN DESPLEGABLE PARA HUECOS (De 0.50m a 3.00m)
prof_hueco = st.sidebar.selectbox("Profundidad del Hueco (m)", [0.50, 0.80, 1.00, 1.50, 2.00, 2.50, 3.00], index=2)

st.sidebar.header(…
[11:24 a.m., 5/4/2026] zury Nuñez: import streamlit as st

st.set_page_config(page_title="Cerebro de Obra TOTAL - Adrián Yépez", layout="wide")

st.title("🏗️ Cerebro de Obra: Presupuesto Maestro Global")

# --- BARRA LATERAL ---
st.sidebar.header("📏 1. Medidas y Excavación")
largo = st.sidebar.number_input("Largo (m)", min_value=1.0, value=6.0)
ancho = st.sidebar.number_input("Ancho (m)", min_value=1.0, value=4.0)
alto_pared = st.sidebar.number_input("Alto Pared (m)", min_value=1.0, value=2.6)
prof_hueco = st.sidebar.selectbox("Profundidad del Hueco (m)", [0.50, 0.80, 1.00, 1.50, 2.00, 2.50, 3.00], index=2)

st.sidebar.header("⚙️ 2. Detalles Técnicos")
tipo_soporte = st.sidebar.selectbox("Tipo de Estructura", ["Concreto Vaciado", "Tubo Estructural"])
medida_tubo = st.sidebar.selectbox("Medida del Tubo (Pulgadas)", ["2x2", "3x3", "4x4", "6x6", "8x8"])
n_guias = st.sidebar.selectbox("Cabillas (Guías) por Columna", [4, 6, 8, 12, 16])
dist_col = st.sidebar.selectbox("Distancia entre Columnas (m)", [3.0, 3.5, 4.0, 5.0])
tipo_techo = st.sidebar.selectbox("Tipo de Techo", ["Acerolit / Zinc", "Platabanda (Losa)"])

# --- PRECIOS ---
st.sidebar.header("💰 3. Precios del Día ($)")
p_cemento = st.sidebar.number_input("Saco Cemento", value=8.5)
p_bloque = st.sidebar.number_input("Bloque 15cm", value=0.65)
p_cabilla = st.sidebar.number_input("Cabilla 1/2 (6m)", value=10.5)
p_tubo_est = st.sidebar.number_input(f"Tubo {medida_tubo} (6m)", value=35.0)
p_lamina = st.sidebar.number_input("Lámina de Zinc/Acerolit", value=18.0)
p_arena_mina = st.sidebar.number_input("M3 Arena Mina", value=25.0)
p_arena_lavada = st.sidebar.number_input("M3 Arena Lavada", value=30.0)
p_piedra = st.sidebar.number_input("M3 Piedra Picada", value=35.0)

# --- CÁLCULO ---
perimetro = (largo + ancho) * 2
area_piso = largo * ancho
n_col = round(perimetro / dist_col) + 1
largo_guia = prof_hueco + alto_pared + 0.50 

# Acero
if tipo_soporte == "Concreto Vaciado":
    total_cabillas = round((n_col * n_guias * largo_guia + (perimetro * 8)) / 6)
    total_tubos = 0
else:
    total_tubos = round(((n_col * alto_pared) + perimetro) / 6)
    total_cabillas = round((n_col * 2) / 1)

# Materiales
bloques_total = round(((perimetro * alto_pared) - 4) * 12.5)
cem_pegar = round(bloques_total / 80)
cem_friso = round((perimetro * alto_pared * 2) * 0.12)
vol_total_concreto = (n_col * ((0.6 * 0.6 * 0.3) + (0.25 * 0.25 * (prof_hueco - 0.3)))) + ((perimetro * 0.06) + (area_piso * 0.05))
cem_vaciado = round(vol_total_concreto * 8.5)
m3_lavada = round(vol_total_concreto * 0.55, 1)
m3_piedra = round(vol_total_concreto * 0.85, 1)
m3_mina = round((cem_pegar + cem_friso) * 0.1, 1)
n_laminas = round((area_piso * 1.15) / 3.6) if tipo_techo == "Acerolit / Zinc" else 0

# --- RESULTADOS ---
st.header("📋 Presupuesto Técnico")
col1, col2 = st.columns(2)

with col1:
    st.write(f"*Bloques:* {bloques_total} unid.")
    st.write(f"*Cemento Total:* {cem_pegar + cem_friso + cem_vaciado} sacos")
with col2:
    if tipo_soporte == "Tubo Estructural":
        st.write(f"*Tubos {medida_tubo}:* {total_tubos} unid.")
    st.write(f"*Cabillas:* {total_cabillas} unid.")

# Total
total_general = (bloques_total * p_bloque) + ((cem_pegar + cem_friso + cem_vaciado) * p_cemento) + \
                (total_cabillas * p_cabilla) + (total_tubos * p_tubo_est) + (n_laminas * p_lamina) + \
                (m3_mina * p_arena_mina) + (m3_lavada * p_arena_lavada) + (m3_piedra * p_piedra)

st.success(f"## 💰 INVERSIÓN TOTAL: ${total_general:.2f}")
