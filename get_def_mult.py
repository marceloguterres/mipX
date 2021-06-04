#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 15:00:23 2021

@author: guterres
"""

import pandas as pd

def def_mult(input_mult):
    df_def_mults  = pd.read_excel('data_mipita_def_mults.xls') 
    dic_def_mults = df_def_mults.set_index('name_mult')['definicao'].to_dict()
    output_mult = dic_def_mults[input_mult]    
    return(output_mult)



