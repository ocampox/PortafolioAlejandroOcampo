import streamlit as st
from PIL import Image

st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
    st.subheader("Aplicaciones de portafolio - Alejandro Ocampo")
    parrafo = (
        "Las aplicaciones mostradas en esta página corresponden a las desarrolladas "
        "durante el transcurso del semestre en Programación Avanzada, las cuales "
        "corresponden al portafolio de Alejandro Ocampo."
    )
    st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

col1, col2, col3 = st.columns(3)

# --- COLUMNA 1 ---
with col1:
    # Fila 1 (Original)
    st.subheader("Analizador de frutas")
    image = Image.open('frutas.png')
    st.image(image, width=190)
    st.write("En el siguiente enlace encontraremos una App diseñada para identificar frutas de acuerdo a su peso, diámetro y dulzor.") 
    url = "https://fruits-b3sbauefe9bawca4xffvnf.streamlit.app/"
    st.write(f"Medidor de frutas: [Enlace]({url})")

    # Fila 2 (Nuevo)
    st.subheader("Nivel de ríos y quebradas")
    image = Image.open('rios.png') 
    st.image(image, width=190)
    st.write("Aplicación que monitorea e integra datos en tiempo real de la API de CORNARE sobre los niveles de agua (como en la Quebrada Bodegas de El Santuario).") 
    url = "https://cornare-owrerbnunwkd27cmnzbcld.streamlit.app/"
    st.write(f"Niveles CORNARE: [Enlace]({url})")

    # Fila 3 (Nuevo)
    st.subheader("Series de Tiempo IoT")
    image = Image.open('series_tiempo.png') 
    st.image(image, width=190)
    st.write("Análisis interactivo de series de tiempo basado en datos generados por sensores IoT para visualizar tendencias y patrones.") 
    url = "https://timeseriesalejandro.streamlit.app/"
    st.write(f"Series de Tiempo: [Enlace]({url})")

# --- COLUMNA 2 ---
with col2: 
    # Fila 1 (Original)
    st.subheader("Descenso de Gradiente Interactivo")
    image = Image.open('gradiante.png')
    st.image(image, width=200)
    st.write("En el siguiente enlace veremos una aplicación que ayuda a simular la tasa de aprendizaje y el punto inicial que afectan la convergencia del descenso de gradiente.") 
    url = "https://gradiante.streamlit.app/"
    st.write(f"Gradiente: [Enlace]({url})")

    # Fila 2 (Nuevo)
    st.subheader("KNN con datos de AGROSAVIA")
    image = Image.open('suelos.png') 
    st.image(image, width=200)
    st.write("Modelo de clasificación K-Nearest Neighbors (KNN) aplicado a un conjunto de datos agrícolas de suelos proporcionado por AGROSAVIA.") 
    url = "https://knnsuelos-1.streamlit.app/"
    st.write(f"KNN Suelos: [Enlace]({url})")

    # Fila 3 (Nuevo)
    st.subheader("Detector de Anomalías")
    image = Image.open('anomalias.png') 
    st.image(image, width=200)
    st.write("Implementación algorítmica optimizada con NumPy enfocada en la detección de anomalías evaluando la complejidad computacional (Big-O).") 
    url = "https://logicabig.streamlit.app/"
    st.write(f"Anomalías: [Enlace]({url})")

# --- COLUMNA 3 ---
with col3: 
    # Fila 1 (Original)
    st.subheader("Regresión Logística interactiva")
    image = Image.open('clima.png')
    st.image(image, width=190)
    st.write("En la siguiente aplicación veremos la probabilidad de que llueva basado en la humedad, temperatura y viento") 
    url = "https://regresionlogisticaa.streamlit.app/"
    st.write(f"Clima: [Enlace]({url})")

    # Fila 2 (Nuevo)
    st.subheader("Dataset sintético de sensores IoT")
    image = Image.open('iot_dataset.png') 
    st.image(image, width=190)
    st.write("Herramienta para la generación, limpieza y preparación de un conjunto de datos sintéticos simulando lecturas de sensores IoT.") 
    url = "https://preparaciondedatos.streamlit.app/"
    st.write(f"Dataset IoT: [Enlace]({url})")
