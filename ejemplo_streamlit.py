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

    st.subheader("Filtrar datos")
    column = st.selectbox("Selecciona una columna para filtrar", df.columns)
    unique_values = df[column].unique()
    selected_value = st.selectbox("Selecciona un valor", unique_values)
    filtered_df = df[df[column] == selected_value]
    st.write("Datos filtrados:")
    st.write(filtered_df)
    st.subheader("Gráfico de dispersión")
    x_axis = st.selectbox("Selecciona la columna para el eje X", df.columns)
    y_axis = st.selectbox("Selecciona la columna para el eje Y", df.columns)
    if st.button("Mostrar gráfico"):
        plt.figure(figsize=(10, 6))
        plt.scatter(filtered_df[x_axis], filtered_df[y_axis])
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title(f"Gráfico de dispersión de {x_axis} vs {y_axis}")
        st.pyplot(plt)

else: 
    st.write("Por favor, sube un archivo CSV para continuar.")