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


list_mults = ["eDN_produto", "eD_adicionado", "eDN_adicionado", "tDN_adicionado",
              "eD_renda", "eDN_renda", "tDN_renda",	"eD_emprego",	"eDN_emprego",
              "tDN_emprego"]


df_mipita_all = pd.read_pickle("df_mipita_all.bz2")



option = st.sidebar.selectbox('Select the multiplier?', list_mults)

st.apptitle = 'MIPITA v1.0'

st.title('PROJETO IMPACTO O1-E7-IMPACTO')

st.markdown(""" 
            * APP MIPITA v 1.0
            * Data da versão: 2021.06.01
            * Estudo de Caso: Região Litorânea de Santa Catarina
            * Estudo de Caso: Região metropolitana de São Paulo
            """)
            
            

st.write(df_mipita_all)

st.write('You selected:', option)


fig = px.line(df_mipita_all, x="ano", y= option, color="icao")

st.write(fig)


