import streamlit as st

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
p_tubo_est = st.sidebar.number_input(f"Precio Tubo {medida_tubo} (6m)", value=35.0)
p_lamina = st.sidebar.number_input("Lámina de Zinc/Acerolit", value=18.0)
p_arena_mina = st.sidebar.number_input("M3 Arena Mina", value=25.0)
p_arena_lavada = st.sidebar.number_input("M3 Arena Lavada", value=30.0)
p_piedra = st.sidebar.number_input("M3 Piedra Picada", value=35.0)

# --- CÁLCULOS LÓGICOS ---
perimetro = (largo + ancho) * 2
area_piso = largo * ancho
n_col = round(perimetro / dist_col) + 1
largo_guia = prof_hueco + alto_pared + 0.50 

# Acero (Cabillas o Tubos)
if tipo_soporte == "Concreto Vaciado":
    total_cabillas = round((n_col * n_guias * largo_guia + (perimetro * 8)) / 6)
    total_tubos = 0
else:
    total_tubos = round(((n_col * alto_pared) + perimetro) / 6)
    total_cabillas = round(n_col * 2)

# Bloques y Cemento (Pega y Friso)
bloques_total = round(((perimetro * alto_pared) - 4) * 12.5)
cem_pegar = round(bloques_total / 80)
cem_friso = round((perimetro * alto_pared * 2) * 0.12)

# Concreto de Fundaciones y Vigas
vol_fundaciones = n_col * ((0.6 * 0.6 * 0.3) + (0.25 * 0.25 * (prof_hueco - 0.3)))
vol_vigas_sobrepiso = (perimetro * 0.20 * 0.20) + (area_piso * 0.05)
vol_total_concreto = vol_fundaciones + vol_vigas_sobrepiso

cem_vaciado = round(vol_total_concreto * 8.5)
m3_lavada = round(vol_total_concreto * 0.55, 1)
m3_piedra = round(vol_total_concreto * 0.85, 1)
m3_mina = round((cem_pegar + cem_friso) * 0.1, 1)
n_laminas = round((area_piso * 1.15) / 3.6) if tipo_techo == "Acerolit / Zinc" else 0

# --- RESULTADOS EN PANTALLA ---
st.header("📋 Presupuesto Técnico Detallado")
col1, col2 = st.columns(2)

with col1:
    st.info("🧱 *Albañilería*")
    st.write(f"- *Bloques:* {bloques_total} piezas")
    st.write(f"- *Arena de Mina:* {m3_mina} m3")
    st.write(f"- *Sacos Cemento (Pega/Friso):* {cem_pegar + cem_friso} sacos")

with col2:
    st.info("🏗️ *Estructura*")
    if tipo_soporte == "Tubo Estructural":
        st.write(f"- *Tubos {medida_tubo}:* {total_tubos} piezas")
    st.write(f"- *Cabillas de 1/2:* {total_cabillas} piezas")
    st.write(f"- *Sacos Cemento (Vaciado):* {cem_vaciado} sacos")

# TOTAL GENERAL
total_general = (bloques_total * p_bloque) + ((cem_pegar + cem_friso + cem_vaciado) * p_cemento) + \
                (total_cabillas * p_cabilla) + (total_tubos * p_tubo_est) + (n_laminas * p_lamina) + \
                (m3_mina * p_arena_mina) + (m3_lavada * p_arena_lavada) + (m3_piedra * p_piedra)

st.divider()
st.success(f"## 💰 INVERSIÓN TOTAL ESTIMADA: ${total_general:.2f}")

# Métricas para el resumen de carga
m1, m2, m3, m4 = st.columns(4)
m1.metric("Cemento Total", f"{cem_pegar + cem_friso + cem_vaciado} sacos")
m2.metric(
