#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 13 09:40:48 2021

@author: guterres
"""

import pandas as pd
import streamlit as st
import pickle    


# -- Set page config

st.apptitle = 'MIPITA v1.0'

st.title('PROJETO IMPACTO O1-E7-IMPACTO')

st.markdown(""" 
            * APP MIPITA v 1.0: versão de desenvolvimento: 2021.05.145
            * Use the menu at left to select data and set plot parameters
            * Your plots will appear below
            """)



st.write("Here's our first attempt at using data to create a table:")


f = open('df_mipita_all.pkl', 'rb')   # 'rb' for reading binary file
df_mipita_all = pickle.load(f)     
f.close()    
df_mipita_all
