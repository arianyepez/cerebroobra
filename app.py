import streamlit as st

st.set_page_config(page_title="Cerebro de Obra TOTAL - Adrián Yépez", layout="wide")

st.title("🏗️ Cerebro de Obra: Presupuesto Global con Plomería")
st.write("Desde la fundación hasta las piezas sanitarias y acabados.")

# --- BARRA LATERAL: MEDIDAS, PUNTOS Y PRECIOS ---
st.sidebar.header("📏 Medidas y Puntos")
largo = st.sidebar.number_input("Largo (m)", min_value=1.0, value=6.0)
ancho = st.sidebar.number_input("Ancho (m)", min_value=1.0, value=4.0)
alto = st.sidebar.number_input("Alto Pared (m)", min_value=1.0, value=2.6)
n_puertas = st.sidebar.number_input("Puertas", min_value=0, value=1)
n_ventanas = st.sidebar.number_input("Ventanas", min_value=0, value=2)
n_banos = st.sidebar.number_input("Número de Baños", min_value=0, value=1)

st.sidebar.header("💰 Precios Actuales ($)")
p_cemento = st.sidebar.number_input("Saco Cemento", value=8.0)
p_bloque = st.sidebar.number_input("Bloque 15cm", value=0.60)
p_tubo_est = st.sidebar.number_input("Tubo Estructural (6m)", value=25.0)
p_techo = st.sidebar.number_input("Lámina Techo (3.6m)", value=18.0)
p_combo_bano = st.sidebar.number_input("Combo Poceta/Lavamanos", value=120.0)
p_tuberia_plom = st.sidebar.number_input("Kit Tubería por Baño", value=60.0)

# --- CÁLCULOS TÉCNICOS ---
area_piso = largo * ancho
perimetro = (largo + ancho) * 2
area_paredes = (perimetro * alto) - (n_puertas * 2.1) - (n_ventanas * 1.5)

# 1. Albañilería
total_bloques = round(area_paredes * 12.5)
cem_total = round((perimetro * 0.8) + (total_bloques / 45) + (area_piso * 0.15))

# 2. Techo
area_techo = (largo + 0.5) * (ancho + 0.5)
n_laminas = round(area_techo / 3)
n_tubos = round((largo / 1.0) * (ancho / 6) + (ancho * 2 / 6))

# 3. Plomería y Piezas Sanitarias
costo_piezas = n_banos * p_combo_bano
costo_tuberia_bano = n_banos * p_tuberia_plom

# --- PANTALLA PRINCIPAL ---
col1, col2 = st.columns(2)

with col1:
    st.header("📋 Lista de Materiales")
    st.info(f"🧱 *Albañilería:* {total_bloques} bloques, {cem_total} sacos cemento.")
    st.info(f"🏠 *Techo:* {n_laminas} láminas, {n_tubos} tubos estructurales.")
    st.info(f"🚿 *Plomería:* {n_banos} Kit(s) de piezas sanitarias y tuberías.")
    st.info(f"⚡ *Electricidad:* Incluye cableado y mangueras para {area_piso} m2.")

with col2:
    st.header("💵 Presupuesto Estimado ($)")
    c_gris = (total_bloques * p_bloque) + (cem_total * p_cemento)
    c_techo = (n_laminas * p_techo) + (n_tubos * p_tubo_est)
    c_plomeria = costo_piezas + costo_tuberia_bano
    
    st.write(f"Materiales Base: *${c_gris:.2f}*")
    st.write(f"Techo y Estructura: *${c_techo:.2f}*")
    st.write(f"Baños y Plomería: *${c_plomeria:.2f}*")
    
    total = c_gris + c_techo + c_plomeria + 150 # 150 de extras (pintura/elec base)
    st.success(f"### TOTAL ESTIMADO: ${total:.2f}")

with st.expander("🔍 Detalle de Aguas Blancas y Negras"):
    st.write(f"*Aguas Negras:* Incluye tubería de 4\" para descarga de poceta y 2\" para desagües.")
    st.write(f"*Aguas Blancas:* Tubería de 1/2\" termofusión o PVC con sus llaves de paso.")
    st.write(f"*Piezas:* {n_banos} Poceta(s), {n_banos} Lavamanos y {n_banos} Kit(s) de ducha.")
    [attachment_0](attachment)
