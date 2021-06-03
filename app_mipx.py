#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:40:48 2021

@author: guterres
"""

import pandas as pd
import streamlit as st
import plotly.express as px



# -- Set page config

list_templates =  ['ggplot2', 'seaborn', 'simple_white', 'plotly',
                   'plotly_white', 'plotly_dark', 'presentation', 'xgridoff',
                   'ygridoff', 'gridon', 'none']




list_mults = ["eDN_produto", "eD_adicionado", "eDN_adicionado", "tDN_adicionado",
              "eD_renda", "eDN_renda", "tDN_renda",	"eD_emprego",	"eDN_emprego",
              "tDN_emprego"]


df_mipita_all = pd.read_pickle("df_mipita_all.bz2")




input_template = st.sidebar.selectbox('Selecione o template?', list_templates)
input_mult_01  = st.sidebar.selectbox('Selecione o multiplicador 1?', list_mults)
input_mult_02  = st.sidebar.selectbox('Selecione o multiplicador 2?', list_mults)



st.apptitle = 'MIPITA v1.0'


st.title('PROJETO IMPACTO O1-E7-IMPACTO')

st.markdown(""" 
            * APP MIPITA v 1.0;
            * Data da versão: 2021.06.02;
            * Estudo de Caso: Região Litorânea de Santa Catarina;
            * Estudo de Caso: Região metropolitana de São Paulo.
            """)
    
            
st.subheader("Instruções:") 

st.markdown(""" 
            * Use o menu à esquerda para selecionar os dados e definir os parâmetros do gráfico;
            * Seus gráficos aparecerão abaixo.
 """)
     
    
st.subheader("Gráfico da série temporal") 
         
       
st.write("*Multiplicador selecionado*:", input_mult_01)

fig = px.line(df_mipita_all,
              x="ano", 
              y= input_mult_01, 
              color="icao", 
              template=input_template)

st.write(fig)


st.subheader("Gráfico de dispersão") 

st.write( input_mult_02 , " x" , input_mult_01)

         
fig2 = px.scatter(df_mipita_all, x=input_mult_02, y= input_mult_01, template=input_template)


st.write(fig2)



st.subheader('Tabela gera:') 

# -- Notes on whitening

with st.beta_expander("Veja nota informativa"):
    st.markdown("""
                * Os valores em amarelo correspondem aos máximos de cada coluna. 

""")

st.dataframe(df_mipita_all.style.highlight_max(axis=0))


st.subheader("Sobre o app")
st.markdown("""
 * Este app foi construído pelo ITA para apresentar as ferramentas da metodologia IMPACTO desenvolvidas para SAC ;
 * O trabalho está em andamento;
 * ©2019-2021, Instituto Tecnológico de Aeronáutica (ITA), todos os direitos reservados.
""")
