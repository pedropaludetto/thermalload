# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 09:06:32 2021

@author: 08397697926
"""
import pandas as pd

class CLTD: 
   
    def cltd(self, posicao, grupo, TBS, mes , latitude , hora ):
    # def cltd(self): 
        # posicao = 'SSE'
        # grupo = 'A'
        # TBS = 34.3
        K = 0.83
        Tviz = 9.8/2
        # mes = 'Dec'
        # latitude = 24
        # hora = 'maximo'
        file_name = 'CLTD.xlsx'
        sheet_name = 'group_' + grupo
        LM = self.cltd_corrigido(mes,posicao, latitude)
        dfs = pd.read_excel(file_name, sheet_name, index_col = 0)
        [CLTD] = dfs.loc[posicao, [hora]]
        LM = self.cltd_corrigido(mes, posicao, latitude)
        CLTD_corr = (CLTD + LM) * K +(25.5-Tviz) + (TBS-29.4)
        print("LM = ", LM)
        print("CLTD = ", CLTD)
        print("CLTD corrigido = ", CLTD_corr)
        return CLTD_corr
    
    def cltd_corrigido(self, mes, posicao, latitude):
        file_name = 'CLTD.xlsx'
        sheet_name = 'cltd_corrigido_lat' + str(latitude)
        df = pd.read_excel(file_name, sheet_name, index_col = 0)
        [LM] = df.loc[mes,[posicao]]
        return LM
            
class SGHF:
    def sghf(self, hora, posicao):
        file_name = 'CLTD.xlsx'
        sheet_name = 'SGHF' 
        df = pd.read_excel(file_name, sheet_name, index_col = 0)
        # if hora == 'máximo':
        [X] = df.loc[posicao, [hora]]
            
        return X
    
    
# X = SGHF()
# # sghf = X.sghf

    
 