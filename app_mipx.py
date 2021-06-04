#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:40:48 2021

@author: guterres
"""

import pandas as pd
import streamlit as st
import plotly.express as px
import researchpy


#-----------------------------------------------------------------------------------

# Set page title and favicon.
st.set_page_config(page_title="Projeto Impacto", page_icon='ita-logo.png')


#-----------------------------------------------------------------------------------

df_mipita_all = pd.read_pickle("df_mipita_all.bz2")



list_templates =  ['presentation','ggplot2', 'seaborn', 'simple_white', 'plotly',
                   'plotly_white', 'plotly_dark', 'xgridoff','ygridoff', 'gridon', 'none']


list_mults = ['eDN_produto','eD_produto', 'eD_adicionado','eDN_adicionado', 
              'tD_adicionado', 'tDN_adicionado', 
              'eD_renda','eDN_renda', 'tD_renda', 'tDN_renda', 
              'eD_emprego', 'eDN_emprego','tD_emprego', 'tDN_emprego']


list_icao = ['ALL','ARP_SBCT', 'ARP_SBFL', 'ARP_SBJV', 'ARP_SBNF', 'MUN_SBGR',
             'MUN_SBKP', 'MUN_SBSP', 'ARP_SBGR', 'ARP_SBKP', 'ARP_SBSP']


#-----------------------------------------------------------------------------------

st.sidebar.info("🎈**VERSÃO:** 2021.06.03 - [ITA](https://www.ita.br)" )
input_template = st.sidebar.selectbox('Selecione o template?', list_templates)
input_mult_01  = st.sidebar.selectbox('Selecione o multiplicador 1?', list_mults)
input_mult_02  = st.sidebar.selectbox('Selecione o multiplicador 2?', list_mults)
input_icao     = st.sidebar.multiselect("Selecione um ou mais aeroportos:", list_icao,
                                        default=["ALL"])


if "ALL" in input_icao:
    input_icao = ['ARP_SBCT', 'ARP_SBFL', 'ARP_SBJV', 'ARP_SBNF', 
                  'MUN_SBGR', 'MUN_SBKP', 'MUN_SBSP', 
                  'ARP_SBGR', 'ARP_SBKP', 'ARP_SBSP']



df_mipita_filter = df_mipita_all.query('icao.isin(@input_icao)')


#-----------------------------------------------------------------------------------

st.image('ita-logo.png', width=200)


st.title('PROJETO IMPACTO O1-E7-IMPACTO')

st.markdown(""" 
            * APP MIPITA v 1.0;
            * Estudo de Caso: Região Litorânea de Santa Catarina;
            * Estudo de Caso: Região metropolitana de São Paulo.
            """)
    
  
st.subheader("Instruções") 

st.markdown(""" 
            * Use o menu à esquerda para selecionar os dados e definir os parâmetros do gráfico;
            * Seus gráficos aparecerão abaixo.
 """)
     
    
#-----------------------------------------------------------------------------------
st.subheader("Análise temporal") 
         
       
st.write("*Multiplicador selecionado*:", input_mult_01)

fig = px.line(df_mipita_filter,
              x="ano", 
              y= input_mult_01, 
              color="icao", 
              template=input_template)

st.write(fig)


#-----------------------------------------------------------------------------------

st.subheader("Análise da tendência geral") 

st.write(input_mult_02 , " x" , input_mult_01)

         
fig2 = px.scatter(df_mipita_filter, x=input_mult_02, y= input_mult_01, 
                  trendline="ols",
                  template=input_template)

st.write(fig2)


results_ols_all = px.get_trendline_results(fig2)

st.write(results_ols_all.px_fit_results.iloc[0].summary())


#-----------------------------------------------------------------------------------

st.subheader("Análise da tendência por aeroporto") 

fig3 = px.scatter(df_mipita_filter, x=input_mult_02, y= input_mult_01, 
                  trendline="ols",
                  color="icao",
                  template=input_template)


st.write(fig3)

#-----------------------------------------------------------------------------------

st.subheader("Intervalo de Confiança da Média") 

st.write("*Multiplicador selecionado*:", input_mult_01)

df_ic_95 = researchpy.summary_cont(df_mipita_filter[input_mult_01].groupby(df_mipita_filter['icao']))
df_ic_95.reset_index(inplace=True)

df_ic_95['margem_erro'] = df_ic_95['95% Conf.'] - df_ic_95["Mean"] 

st.write(df_ic_95)


fig4 = px.scatter(df_ic_95, 
                  x = 'icao', 
                  y = 'Mean',
                  color= 'icao',
                  error_y ='margem_erro',
                  error_y_minus = 'margem_erro',
                  template=input_template)


st.write(fig4)           

#-----------------------------------------------------------------------------------

st.subheader('Tabela geral') 

# -- Notes on whitening

with st.beta_expander("Veja nota informativa"):
    st.markdown("""
                * Os valores em amarelo correspondem aos máximos de cada coluna. 

""")

st.dataframe(df_mipita_filter.style.highlight_max(axis=0))


st.subheader("Sobre o app")
st.markdown("""
 * Este app foi construído pelo ITA para apresentar as ferramentas da metodologia IMPACTO desenvolvidas para SAC ;
 * O trabalho está em andamento;
 * ©2019-2021, Instituto Tecnológico de Aeronáutica (ITA), todos os direitos reservados.
""")
