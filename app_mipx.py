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

st.set_page_config(layout="wide")

st.apptitle = 'MIPITA v1.0'

st.title('PROJETO IMPACTO O1-E7-IMPACTO')

st.markdown(""" 
            * APP MIPITA v 1.0
            * Data da versão: 2021.06.01   
            """)



st.write("Here's our first attempt at using data to create a table:")



df_mipita_all = pd.read_pickle("df_mipita_all.bz2")


df_mipita_all


fig = px.line(df_mipita_all, x="ano", y="eDN_produto", color="icao")

st.plotly_chart(fig)


