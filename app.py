import streamlit as st

st.set_page_config(page_title="Cerebro de Obra MAESTRO - Adrián Yépez", layout="wide")

st.title("🏗️ Cerebro de Obra: Presupuesto Personalizado")
st.write("Configura el tipo de construcción, techado y acabados.")

# --- BARRA LATERAL: MEDIDAS Y OPCIONES ---
st.sidebar.header("📏 Medidas de la Obra")
largo = st.sidebar.number_input("Largo (m)", min_value=1.0, value=6.0)
ancho = st.sidebar.number_input("Ancho (m)", min_value=1.0, value=4.0)
alto = st.sidebar.number_input("Alto Pared (m)", min_value=1.0, value=2.6)

st.sidebar.header("🏗️ Opciones de Construcción")
tipo_estructura = st.sidebar.selectbox("Estructura (Vigas/Columnas)", ["Tubos Estructurales (Hierro)", "Vigas de Concreto Vaciado"])
tipo_techo = st.sidebar.selectbox("Tipo de Cobertura", ["Acerolit / Zinc", "Platabanda (Losa de Concreto)"])
n_banos = st.sidebar.number_input("Número de Baños", min_value=0, value=1)

st.sidebar.header("💰 Precios Actuales ($)")
p_cemento = st.sidebar.number_input("Saco Cemento", value=8.5)
p_bloque = st.sidebar.number_input("Bloque 15cm", value=0.65)
p_tubo = st.sidebar.number_input("Tubo Estructural (6m)", value=25.0)
p_techo_lam = st.sidebar.number_input("Lámina Techo / m2", value=18.0)
p_cabilla = st.sidebar.number_input("Cabilla 1/2\"", value=10.5)
p_bano_kit = st.sidebar.number_input("Kit Baño (Piezas/Tubos)", value=180.0)

# --- LÓGICA DE CÁLCULO ---
perimetro = (largo + ancho) * 2
area_piso = largo * ancho
area_paredes = (perimetro * alto) - 5 # Descuento estándar puertas/ventanas

# 1. Albañilería Base
total_bloques = round(area_paredes * 12.5)
cem_paredes = round(total_bloques / 45)

# 2. Estructura Seleccionada
cem_extra = 0
hierro_extra = 0
tubos_extra = 0

if tipo_estructura == "Vigas de Concreto Vaciado":
    # Cálculo para vigas de corona y riostras
    cem_extra += round(perimetro * 0.6) 
    hierro_extra += round(perimetro * 0.8) 
else:
    # Cálculo para correas de hierro
    tubos_extra += round(perimetro / 2) 

# 3. Techo Seleccionado
costo_techo_mat = 0
if tipo_techo == "Platabanda (Losa de Concreto)":
    cem_extra += round(area_piso * 0.8)
    hierro_extra += round(area_piso / 2)
    costo_techo_mat = area_piso * 15 # Malla truck, puntales, etc.
else:
    costo_techo_mat = area_piso * p_techo_lam

# --- PANTALLA PRINCIPAL ---
col1, col2 = st.columns(2)

with col1:
    st.header("📋 Lista de Materiales")
    st.info(f"🧱 *Bloques:* {total_bloques} unidades")
    st.info(f"🛒 *Cemento:* {cem_paredes + cem_extra} sacos totales")
    st.info(f"🏗️ *Hierro:* {hierro_extra} cabillas y {tubos_extra} tubos")
    st.info(f"🚿 *Baños:* {n_banos} kit(s) de plomería y piezas")

with col2:
    st.header("💵 Presupuesto Estimado ($)")
    c_bloque = total_bloques * p_bloque
    c_cemento = (cem_paredes + cem_extra) * p_cemento
    c_hierro = (hierro_extra * p_cabilla) + (tubos_extra * p_tubo)
    c_bano = n_banos * p_bano_kit
    
    total_gral = c_bloque + c_cemento + c_hierro + c_bano + costo_techo_mat
    
    st.write(f"Paredes y Bloques: *${c_bloque:.2f}*")
    st.write(f"Cemento Total: *${c_cemento:.2f}*")
    st.write(f"Estructura y Hierro: *${c_hierro:.2f}*")
    st.write(f"Techo Seleccionado: *${costo_techo_mat:.2f}*")
    st.write(f"Baños y Plomería: *${c_bano:.2f}*")
    
    st.success(f"### TOTAL ESTIMADO: ${total_gral:.2f}")

with st.expander("🔍 Detalle de la Configuración Seleccionada"):
    st.write(f"*Estructura:* Has seleccionado {tipo_estructura}. Esto ajusta la cantidad de cemento y acero.")
    st.write(f"*Techo:* El presupuesto para {tipo_techo} incluye materiales base para su instalación.")
    st.write(f"*Electricidad:* Se estima un kit básico de tubería y cableado para {area_piso} m2.")
