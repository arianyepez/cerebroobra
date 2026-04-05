
import streamlit as st
import math

# Configuración de la App
st.set_page_config(page_title="Cerebro de Obra Detallado", page_icon="🏗️")

st.title("🏗️ Cómputos Métricos Detallados PRO")
st.markdown("### Adrián Yépez - Experto en Construcción")
st.write("---")

# --- PANEL DE CONTROL ---
st.sidebar.header("📏 Dimensiones y Diseño")
largo = st.sidebar.number_input("Largo (m)", value=10.0)
ancho = st.sidebar.number_input("Ancho (m)", value=6.0)
alto = st.sidebar.number_input("Altura de Paredes (m)", value=2.7)

st.sidebar.header("🚪 Aberturas (Puntos Huecos)")
n_puertas = st.sidebar.number_input("Puertas", value=2)
n_ventanas = st.sidebar.number_input("Ventanas", value=3)

# --- LÓGICA DE CÁLCULO POR PARTIDAS ---
perimetro = (largo + ancho) * 2
area_piso = largo * ancho
num_columnas = math.ceil(perimetro / 3) + 1
area_huecos = (n_puertas * 2.1) + (n_ventanas * 1.5)
area_pared_neta = (perimetro * alto) - area_huecos

# 1. FUNDACIONES (Zapatas de 0.60x0.60x0.60)
vol_fundaciones = num_columnas * (0.6 * 0.6 * 0.6)
cem_fund = math.ceil(vol_fundaciones * 7) # 7 sacos por m3
arena_fund = round(vol_fundaciones * 0.5, 2)
piedra_fund = round(vol_fundaciones * 0.8, 2)
hierro_fund = num_columnas * 4.5 # Metros de cabilla 1/2 por zapata

# 2. COLUMNAS Y VIGAS (Riostra y Corona)
ml_vigas = perimetro * 2
ml_total_concreto = ml_vigas + (num_columnas * alto)
vol_concreto_estruc = ml_total_concreto * (0.15 * 0.20) # Sección 15x20
cem_estruc = math.ceil(vol_concreto_estruc * 8.5)
arena_estruc = round(vol_concreto_estruc * 0.5, 2)
piedra_estruc = round(vol_concreto_estruc * 0.8, 2)
hierro_12_estruc = ml_total_concreto * 4 # 4 pelos

# 3. ALBAÑILERÍA (Bloques y Pega)
bloques = math.ceil(area_pared_neta * 13)
cem_pega = math.ceil(bloques / 45) # 1 saco de cemento para pegar 45-50 bloques
arena_pega = round(area_pared_neta * 0.04, 2)

# 4. PISOS (Losa de 10cm y Sobrepiso)
vol_losa = area_piso * 0.10
cem_losa = math.ceil(vol_losa * 7)
arena_losa = round(vol_losa * 0.5, 2)
piedra_losa = round(vol_losa * 0.8, 2)

# --- INTERFAZ DE RESULTADOS ---
if st.button("🚀 GENERAR REPORTE DETALLADO"):
    
    st.subheader("📋 Detalle por Etapa")
    
    with st.expander("🛠️ 1. Fundaciones y Zapatas"):
        st.write(f"• *Cemento:* {cem_fund} sacos")
        st.write(f"• *Arena Lavada:* {arena_fund} m³")
        st.write(f"• *Piedra Picada:* {piedra_fund} m³")
        st.write(f"• *Cabilla 1/2:* {math.ceil(hierro_fund)} m")

    with st.expander("🏗️ 2. Columnas y Vigas (Riostra/Corona)"):
        st.write(f"• *Cemento:* {cem_estruc} sacos")
        st.write(f"• *Arena Lavada:* {arena_estruc} m³")
        st.write(f"• *Piedra Picada:* {piedra_estruc} m³")
        st.write(f"• *Cabilla 1/2:* {math.ceil(hierro_12_estruc)} m")

    with st.expander("🧱 3. Paredes (Albañilería)"):
        st.write(f"• *Bloques 15cm:* {bloques} unidades")
        st.write(f"• *Cemento (Pega):* {cem_pega} sacos")
        st.write(f"• *Arena:* {arena_pega} m³")

    with st.expander("👣 4. Losa de Piso"):
        st.write(f"• *Cemento:* {cem_losa} sacos")
        st.write(f"• *Arena Lavada:* {arena_losa} m³")
        st.write(f"• *Piedra Picada:* {piedra_losa} m³")

    # --- GRAN TOTAL TOTALIZADO ---
    st.markdown("---")
    st.header("🛒 LISTA DE COMPRA TOTAL")
    
    tot_cem = cem_fund + cem_estruc + cem_pega + cem_losa
    tot_arena = arena_fund + arena_estruc + arena_pega + arena_losa
    tot_piedra = piedra_fund + piedra_estruc + piedra_losa
    tot_hierro = math.ceil((hierro_fund + hierro_12_estruc) / 6) # En tubos de 6m
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Cemento", f"{tot_cem} Sacos")
    c2.metric("Arena Lavada", f"{tot_arena} m³")
    c3.metric("Piedra Picada", f"{tot_piedra} m³")
    
    st.info(f"💡 Necesitarás aproximadamente *{tot_hierro} cabillas de 1/2\"* (de 6 metros cada una).")
