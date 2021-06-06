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
import seaborn as sns


#-----------------------------------------------------------------------------------
# Set page title and favicon.
st.set_page_config(page_title="Projeto Impacto", page_icon='ita-logo.png')


#----------------------------------------------------------------------------------

df_def_mults  = pd.read_excel('data_mipita_def_mults.xls') 

dic_def_mults = df_def_mults.set_index('name_mult')['definicao'].to_dict()

df_mipita_all = pd.read_pickle("df_mipita_all.bz2")


list_templates =  ['presentation','ggplot2', 'seaborn', 'simple_white', 'plotly',
                   'plotly_white', 'plotly_dark', 'xgridoff','ygridoff', 'gridon', 'none']


list_mults_01 = ['eDN_produto','eD_produto', 'eD_adicionado','eDN_adicionado', 
                  'tD_adicionado', 'tDN_adicionado', 
                  'eD_renda','eDN_renda', 'tD_renda', 'tDN_renda', 
                  'eD_emprego', 'eDN_emprego','tD_emprego', 'tDN_emprego']


list_mults_02 = ['eD_renda','eDN_produto','eD_produto', 'eD_adicionado','eDN_adicionado', 
                 'tD_adicionado', 'tDN_adicionado', 
                 'tD_renda', 'tDN_renda', 
                 'eD_emprego', 'eDN_emprego','tD_emprego', 'tDN_emprego']


list_mults_03 = ['eD_emprego', 'eD_renda','eDN_produto','eD_produto', 'eD_adicionado','eDN_adicionado', 
                 'tD_adicionado', 'tDN_adicionado', 
                 'tD_renda', 'tDN_renda', 
                  'eDN_emprego','tD_emprego', 'tDN_emprego']




list_icao = ['ALL','ARP_SBCT', 'ARP_SBFL', 'ARP_SBJV', 'ARP_SBNF', 'MUN_SBGR',
             'MUN_SBKP', 'MUN_SBSP', 'ARP_SBGR', 'ARP_SBKP', 'ARP_SBSP']



#-----------------------------------------------------------------------------------

with st.sidebar:
    
    st.title('Navegação')
    
    st.info("🎈**VERSÃO:** 2021.06.03 - [ITA](https://www.ita.br)" )
    
    input_template = st.selectbox('Selecione o template?', list_templates)
    
    input_mult_01  = st.selectbox('Selecione o multiplicador 1?', list_mults_01)
    
    input_mult_02  = st.selectbox('Selecione o multiplicador 2?', list_mults_02)
    
    input_mult_03  = st.selectbox('Selecione o multiplicador 3?', list_mults_03)
    
    input_icao     = st.multiselect("Selecione um ou mais aeroportos:", list_icao,
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
   


st.markdown('***')
  
#-----------------------------------------------------------------------------------
st.subheader("Descrição dos Multiplicadores") 


st.write("- ", input_mult_01, ": " ,  dic_def_mults[input_mult_01])
st.write("- ", input_mult_02, ": "  , dic_def_mults[input_mult_02])
st.write("- ", input_mult_03, ": "  , dic_def_mults[input_mult_03])

st.markdown('***')
    
#-----------------------------------------------------------------------------------
st.subheader("Análise temporal") 
         
       
st.write("*Multiplicador selecionado*:", input_mult_01)

fig = px.line(df_mipita_filter,
              x="ano", 
              y= input_mult_01, 
              color="icao", 
              template=input_template)

st.write(fig)

st.markdown('***')
#-----------------------------------------------------------------------------------

st.subheader("Análise da tendência geral") 

st.write(input_mult_01 , " x" , input_mult_02)

         
fig2 = px.scatter(df_mipita_filter, x=input_mult_01, y= input_mult_02, 
                  trendline="ols",
                  template=input_template)

st.write(fig2)


results_ols_all = px.get_trendline_results(fig2)

st.write(results_ols_all.px_fit_results.iloc[0].summary())

st.markdown('***')
#-----------------------------------------------------------------------------------

st.subheader("Análise da tendência por aeroporto") 

st.write(input_mult_01 , " x" , input_mult_02)

fig3 = px.scatter(df_mipita_filter, x=input_mult_01, y= input_mult_02, 
                  trendline="ols",
                  color="icao",
                  template=input_template)


st.write(fig3)
st.markdown('***')

#-----------------------------------------------------------------------------------

st.subheader("Pairplots") 


fig_hist_01 = sns.pairplot(df_mipita_filter[['icao', input_mult_01, input_mult_02, input_mult_03]],
                           hue="icao")


st.pyplot(fig_hist_01)
    

st.markdown('***')
#-----------------------------------------------------------------------------------

st.subheader("Box Plots") 
st.write("*Multiplicador selecionado*:", input_mult_01)


fig_bp = px.box(df_mipita_filter, 
                x = 'icao', 
                y= input_mult_01,
                color= 'icao',
                points="all",
                template=input_template)
st.write(fig_bp)   

st.markdown('***')

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
st.markdown('***')

#-----------------------------------------------------------------------------------

st.subheader('Tabela geral') 

# -- Notes on whitening

with st.beta_expander("Veja nota informativa:"):
    st.markdown("""* Os valores em amarelo correspondem aos máximos de cada coluna. """)

st.dataframe(df_mipita_filter.style.highlight_max(axis=0))

st.markdown('***')
st.subheader("Sobre o app")
st.markdown("""
 * Este app foi construído pelo ITA para apresentar as ferramentas da metodologia IMPACTO desenvolvidas para SAC ;
 * O trabalho está em andamento;
 * ©2019-2021, Instituto Tecnológico de Aeronáutica (ITA), todos os direitos reservados.
""")
