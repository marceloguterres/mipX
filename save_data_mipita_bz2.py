#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 13:45:57 2021

@author: guterres
"""
import pandas as pd


def save_data_mipita_bz2():
    
    df_mipita_all = pd.read_excel('data_mipita_all_02.xls')  
    path = 'df_mipita_all.bz2'
    df_mipita_all.to_pickle(path, protocol=2)
    return()

