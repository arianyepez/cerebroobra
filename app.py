import streamlit as st

st.set_page_config(page_title="Cerebro de Obra TOTAL - Adrián Yépez", layout="wide")

st.title("🏗️ Cerebro de Obra: Presupuesto Global Maestro")
st.write("Cálculos desde fundaciones hasta acabados, plomería y electricidad.")

# --- BARRA LATERAL: MEDIDAS, PUNTOS Y PRECIOS ---
st.sidebar.header("📏 Medidas y Puntos")
largo = st.sidebar.number_input("Largo (m)", min_value=1.0, value=6.0)
ancho = st.sidebar.number_input("Ancho (m)", min_value=1.0, value=4.0)
alto = st.sidebar.number_input("Alto Pared (m)", min_value=1.0, value=2.6)
n_puertas = st.sidebar.number_input("Puertas", min_value=0, value=1)
n_ventanas = st.sidebar.number_input("Ventanas", min_value=0, value=2)
n_banos = st.sidebar.number_input("Número de Baños", min_value=0, value=1)
n_puntos_elec = st.sidebar.number_input("Puntos Eléctricos", min_value=1, value=10)

st.sidebar.header("💰 Precios Actuales ($)")
p_cemento = st.sidebar.number_input("Saco Cemento", value=8.0)
p_bloque = st.sidebar.number_input("Bloque 15cm", value=0.60)
p_cabilla = st.sidebar.number_input("Cabilla 1/2\"", value=10.5)
p_tubo_est = st.sidebar.number_input("Tubo Estructural (6m)", value=25.0)
p_techo = st.sidebar.number_input("Lámina Techo (3.6m)", value=18.0)
p_combo_bano = st.sidebar.number_input("Combo Poceta/Lavamanos", value=120.0)
p_tuberia_plom = st.sidebar.number_input("Kit Tubería por Baño", value=60.0)

# --- CÁLCULOS TÉCNICOS ---
area_piso = largo * ancho
perimetro = (largo + ancho) * 2
# Descuento exacto de vanos
area_paredes = (perimetro * alto) - (n_puertas * 1.89) - (n_ventanas * 1.20)

# 1. Albañilería y Fundaciones
total_bloques = round(area_paredes * 12.5)
# Detalle de cemento: Pegar bloques + Fundaciones + Riostras + Piso base
cem_asentado = round(total_bloques / 45)
n_columnas = round(perimetro / 3) + 1
cem_fundaciones = round(n_columnas * 1.2)
cem_riostras = round(perimetro * 0.4)
cem_total = cem_asentado + cem_fundaciones + cem_riostras + round(area_piso * 0.15)

# 2. Estructura y Techo
hierro_fundaciones = round(n_columnas * 1.5) # Cabillas para zapatas y pedestales
area_techo = (largo + 0.5) * (ancho + 0.5)
n_laminas = round(area_techo / 3)
n_tubos = round((largo / 1.0) * (ancho / 6) + (ancho * 2 / 6))

# 3. Plomería y Electricidad
costo_piezas = n_banos * p_combo_bano
costo_tuberia_bano = n_banos * p_tuberia_plom
costo_elec = n_puntos_elec * 12.0 # Promedio de material por punto (tubo/caja/cable)

# --- PANTALLA PRINCIPAL ---
col1, col2 = st.columns(2)

with col1:
    st.header("📋 Lista de Materiales")
    st.info(f"🧱 *Albañilería:* {total_bloques} bloques, {cem_total} sacos cemento (incluye riostras).")
    st.info(f"🏗️ *Hierro Base:* {hierro_fundaciones} cabillas para fundaciones y columnas.")
    st.info(f"🏠 *Techo:* {n_laminas} láminas, {n_tubos} tubos estructurales.")
    st.info(f"🚿 *Plomería:* {n_banos} Kit(s) de piezas sanitarias y tuberías.")
    st.info(f"⚡ *Electricidad:* {n_puntos_elec} puntos con tubería y cableado.")

with col2:
    st.header("💵 Presupuesto Estimado ($)")
    c_gris = (total_bloques * p_bloque) + (cem_total * p_cemento) + (hierro_fundaciones * p_cabilla)
    c_techo = (n_laminas * p_techo) + (n_tubos * p_tubo_est)
    c_plomeria = costo_piezas + costo_tuberia_bano
    
    st.write(f"Obra Gris y Hierro: *${c_gris:.2f}*")
    st.write(f"Techo y Estructura: *${c_techo:.2f}*")
    st.write(f"Baños y Plomería: *${c_plomeria:.2f}*")
    st.write(f"Instalación Eléctrica: *${costo_elec:.2f}*")
    
    total = c_gris + c_techo + c_plomeria + costo_elec + 100 # 100 para imprevistos
    st.success(f"### TOTAL ESTIMADO: ${total:.2f}")

# --- DESGLOSE FINAL ---
with st.expander("🔍 Detalle Técnico de la Obra"):
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("*Desglose de Cemento:*")
        st.write(f"- Pegar bloques: {cem_asentado} sacos")
        st.write(f"- Fundaciones/Zapatas: {cem_fundaciones} sacos")
        st.write(f"- Vigas de Riostra: {cem_riostras} sacos")
        st.write(f"- Piso base: {round(area_piso * 0.15)
