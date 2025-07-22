import gradio as gr
import joblib

modelo = joblib.load("modelo_lluvias.joblib")

def predecir_lluvia(temp, humedad, presion):
    pred = modelo.predict([[temp, humedad, presion]])
    return "☔ Sí lloverá" if pred[0] == 1 else "🌤️ No lloverá"

app = gr.Interface(
    fn=predecir_lluvia,
    inputs=[
        gr.Slider(0, 40, label="Temperatura (°C)"),
        gr.Slider(0, 100, label="Humedad (%)"),
        gr.Slider(900, 1100, label="Presión (hPa)")
    ],
    outputs="text",
    title="Predicción de Lluvia",
    description="App simple de Machine Learning que predice si lloverá"
)

app.launch()
