# app.py
import streamlit as st
from data_handler import DataHandler

st.title('Aplicación de Análisis de Datos')

# Cargar el archivo CSV
uploaded_file = st.file_uploader("Cargar archivo CSV", type="csv")

if uploaded_file is not None:
    # Guardar el archivo subido en una ruta temporal
    file_path = uploaded_file.name
    
    # Escribir el contenido del archivo subido en un archivo temporal
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Inicializar la clase DataHandler
    data_handler = DataHandler(file_path)
    data_handler.load_data()
    
    # Visualización de los datos
    st.header('Visualización de los Datos')
    st.write(data_handler.preview_data())
    
    # Estadísticas descriptivas
    st.header('Estadísticas Descriptivas')
    st.write(data_handler.calculate_statistics())
