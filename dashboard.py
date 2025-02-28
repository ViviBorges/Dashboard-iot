import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1020@localhost:5432/postgres')

def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

st.title('Dashboard de Temperaturas IoT')

st.header('Média de Temperatura por Dispositivo')
df_avg_temp = load_data('avg_temp_por_dispositivo')
fig1 = px.bar(df_avg_temp, x='device_id', y='avg_temp')
st.plotly_chart(fig1)

st.header('Leituras por Hora do Dia')
df_leituras_hora = load_data('leituras_por_hora')
fig2 = px.line(df_leituras_hora, x='hora', y='contagem')
st.plotly_chart(fig2)

st.header('Temperaturas Máximas e Mínimas por Dia')
df_temp_max_min = load_data('temp_max_min_por_dia')
fig3 = px.line(df_temp_max_min, x='data', y=['temp_max', 'temp_min'])
st.plotly_chart(fig3)
