import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
import streamlit as st
import nbformat as nbf


df_vehicles = pd.read_csv('../vehicles.csv')

st.header('Veículos à venda')

hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
            # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
            # criar um histograma
    fig = px.histogram(df_vehicles, x="odometer")
        
            # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


hist_button = st.button('Criar gráfico de dispersão') # criar um botão
        
if hist_button: # se o botão for clicado
            # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
            
            # criar um histograma
    fig = px.histogram(df_vehicles, x="price")
        
            # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)