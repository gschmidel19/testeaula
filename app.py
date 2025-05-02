import streamlit as st
import pandas as pd
import plotly.express as px

# Lendo o arquivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Cabeçalho do aplicativo
st.header('Análise de Anúncios de Carros Usados')

# Caixa de seleção para histograma
build_histogram = st.checkbox('Criar um histograma')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Caixa de seleção para gráfico de dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_scatter:
    st.write('Criando gráfico de dispersão: preço vs. odômetro')
    fig = px.scatter(car_data, x='odometer', y='price', title='Preço x Quilometragem')
    st.plotly_chart(fig, use_container_width=True)
