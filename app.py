import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Venta de vehículos usados en EEUU 2018 - 2019')

build_histogram = st.checkbox('Construir un histograma') # crear casilla de verificación
     
if build_histogram: # al hacer clic en el botón

    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de vehiculos')  # escribir un mensaje
            
    fig = px.histogram(car_data, x="odometer") # crear un histograma
        
    st.plotly_chart(fig, use_container_width=True)  # mostrar un gráfico Plotly interactivo


build_scatter = st.checkbox('Construir gráfico de dispersión') # crear casilla de verificación
        
if build_scatter: # al hacer clic en el botón

    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de vehiculos')  # escribir un mensaje
            
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
        
    st.plotly_chart(fig, use_container_width=True)  # mostrar un gráfico Plotly interactivo
