import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Ejemplo de Streamlit")
st.write("Este es un ejemplo de una aplicación Streamlit que muestra un gráfico de dispersión.")

upload_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.subheader("Datos del archivo CSV")
    st.write(df.head())

else: 
    st.write("Por favor, sube un archivo CSV para continuar.")