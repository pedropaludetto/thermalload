# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:11:19 2021

@author: 08397697926
"""
import pandas as pd


# file_name = 'CARGA TÉRMICA N02 18-03-21.xlsx'
# sheet_name = 'Materiais (Dados de Entrada)'
# dfs = pd.read_excel(file_name, sheet_name, index_col = 0)'

class SelectMaterial(): 
   
    def select_material(self, material):
        file_name = 'Dados.xlsx'
        sheet_name = 'Materiais'
        dfs = pd.read_excel(file_name, index_col = 0)
        # print("column = ", dfs.columns)
        # print("index = ", dfs.index)    
        [camada_1, C, camada_2, R_2, camada_3, R_3, camada_4, R_4, R_total, hi, he] = dfs.loc[material,['Camada 1','C','Camada 2','R','Camada 3','R','Camada 4','R','RTOTAL','hi','he']]

        return camada_1, C, camada_2, R_2, camada_3, R_3, camada_4, R_4, R_total, hi, he
        # return dfs

    def select_tipo_ocupacao(self, tipo_de_ocupacao):  
        file_name = 'Dados.xlsx'
        sheet_name = 'Nivel de Atividade'
        dfs = pd.read_excel(file_name, index_col = 0, sheet_name = sheet_name)
        # print(dfs.index)
        [Cs, Cl] = dfs.loc[tipo_de_ocupacao,["Calor Sensível [W/pessoa]", "Calor Latente [W/pessoa]"]]
        return Cs, Cl
        # return dfs
        
X = SelectMaterial()
[Cs, Cl] = X.select_tipo_ocupacao("Atividade Moderada em Trabalhos de Escritório")
# # dfs = X.select_tipo_ocupacao()

# print(Cs, Cl)