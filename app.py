import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
import streamlit as st
import nbformat as nbf


df_vehicles = pd.read_csv('./vehicles.csv')

st.header('Veículos à venda')

hist_button = st.button('Histograma') # criar um botão
        
if hist_button: # se o botão for clicado
            # escrever uma mensagem
    st.write('Conjunto de dados de anúncios de vendas de carros')
            
            # criar um histograma
    fig = px.histogram(df_vehicles, x="odometer")
        
            # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


hist_check = st.checkbox('Gráfico de dispersão') 
        
if hist_check: # se o botão for clicado
            # escrever uma mensagem
    st.write('Gráfico de dispersão preço por ano')
            
            # criar um histograma
    fig = px.scatter(df_vehicles, x="model_year", y="price", title="Preço dos veículos por ano")
        
            # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)