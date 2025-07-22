import streamlit as st
import joblib

# Cargar el modelo
modelo = joblib.load("modelo_lluvias.joblib")

# Título y descripción
st.title("🌧️ Predicción de Lluvia")
st.write("Esta aplicación predice si lloverá en función de tres variables meteorológicas.")

# Entradas del usuario
temp = st.slider("Temperatura (°C)", 0, 40, 25)
humedad = st.slider("Humedad (%)", 0, 100, 50)
presion = st.slider("Presión (hPa)", 900, 1100, 1013)

# Botón de predicción
if st.button("Predecir"):
    pred = modelo.predict([[temp, humedad, presion]])
    if pred[0] == 1:
        st.success("🌧️ Sí lloverá")
    else:
        st.info("🌤️ No lloverá")
