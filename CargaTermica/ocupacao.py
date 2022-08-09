# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:16:12 2021

@author: 08397697926
"""

import pandas as pd        



class Ocupacao:
    
    def __init__(self):
        file_name = 'Dados.xlsx'
        sheet_name = 'Nivel de Atividade'
        self.dfs = pd.read_excel(file_name, sheet_name, index_col = 0)
    
    def tipo_de_ocupacao (self):
        tipo = self.dfs.index
        return tipo       
    


















