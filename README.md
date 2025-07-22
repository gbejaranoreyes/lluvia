# 🌦 Predicción de Lluvia con Machine Learning

Este proyecto utiliza un modelo de Machine Learning entrenado para predecir si **lloverá** o **no lloverá** en función de tres variables meteorológicas: **temperatura (°C), humedad (%) y presión atmosférica (hPa)**.

## 📌 Descripción

El modelo fue desarrollado en Python y desplegado como aplicación web utilizando **Gradio** y **Streamlit Cloud**. El objetivo es mostrar de forma práctica cómo un modelo de aprendizaje supervisado puede ser aplicado a un caso real con una interfaz sencilla para el usuario.

---

## 🧠 Modelo de Machine Learning

- Algoritmos explorados: Árbol de Decisión, Regresión Logística, SVC.
- Algoritmo final: (especifica aquí cuál fue el seleccionado, por ejemplo, `RandomForestClassifier`).
- Entrenado con datos históricos simulados.
- Guardado usando `joblib` como `modelo_lluvias.joblib`.

---

## 🚀 Cómo usar esta aplicación

1. Ve a la app desplegada en Streamlit:  
   👉 [[https://lluvia-<tudominio>.streamlit.app](https://lluvia-<tudominio>.streamlit.app)](https://lluvia-gdbvplqfqbeusoujp5y5ao.streamlit.app/)

2. Ajusta los valores de:
   - Temperatura (°C)
   - Humedad (%)
   - Presión (hPa)

3. Haz clic en **Predecir** y la app te dirá si **🌧️ lloverá** o **☀️ no lloverá**.

---

## 🗂 Archivos del repositorio

- `app.py`: Código principal de la aplicación.
- `modelo_lluvias.joblib`: Modelo entrenado y guardado con joblib.
- `requirements.txt`: Lista de dependencias necesarias para correr la app.

---

## 📦 Requisitos

Instala las dependencias con:

```bash
pip install -r requirements.txt

## 🧪 Ejecución local

Para probar la app en tu entorno local:

```bash
streamlit run app.py

🛠 Tecnologías utilizadas
Python

Scikit-learn

Joblib

Gradio

Streamlit

GitHub
