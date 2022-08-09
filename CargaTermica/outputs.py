# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 07:36:35 2021

@author: 08397697926
"""
import sqlite3
from memorialdecalculo2 import CargaTermica
from dados import SelectMaterial
from database3 import SelectData
from cltd import SGHF
   
class ParedeExterna(SelectData, SelectMaterial):
    
    def calcular(self):
        tag =  self.select_data('tag', "ParedeExterna")
        nome = self.select_data_2('nome_da_sala', "Menu", tag)
        Ta = self.select_data_2('TBS', "Menu", tag)
        area = self.select_data_2('area_da_sala', "Menu",tag)
        UR = self.select_data_2('UR', 'Menu', tag)
        PD = self.select_data_2("pe_direito", "Menu", tag)
        elevacao = self.select_data('elevacao', "Menu")
        TBS = self.select_data_2('TBS', 'Menu',tag)
        pressao = self.select_data_2('pressao', "Menu", tag)
        espessura = self.select_data('espessura_pe', 'ParedeExterna')
        largura = self.select_data('largura_pe', 'ParedeExterna')
        material = self.select_data('material_pe', 'ParedeExterna')
        grupo = self.select_data('grupo_pe', 'ParedeExterna')
        posicao = self.select_data('posicao_pe', 'ParedeExterna')
        ajanela = self.select_data('ajanela', 'ParedeExterna')
        # Tv = self.select_data('temp_viz', 'ParedeExterna  ')
        hora = 'maximo'
        Tamb = 34.3
        # TBS = 34.3
        latitude = 24
        mes = 'Dec'
        [camada_1, k, camada_2, R_2, camada_3, R_3, camada_4, R_4, R_total, hi, he] = self.select_material(material)
        X = CargaTermica(tag, nome, PD, area, Ta, UR, pressao)
        Cs_pe = X.q_paredes_externas(material, grupo, espessura, largura, posicao, R_total, k, hi, he, ajanela, latitude, hora, mes, Tamb, TBS)
        print("Tag = ", tag)
        print('Nome da Sala = ', nome)
        print("Orientação", posicao)
        print("Espessura = ", espessura)
        print("Posição = ", posicao)
        print("Área = ", area)
        print("TBS", TBS)
        print("k = ", k)
        print("R total = ", R_total)
        print("hi = ", hi)
        print("he = ", he)
        print('Pé Direito = ', PD)
        print('Cs_pe = ', round(Cs_pe,3), ' W')
        
        return Cs_pe
        
class ParedeInterna(SelectData, SelectMaterial):
    
    def calcular(self):
        nome = self.select_data('nome_da_sala', "Menu")
        area = self.select_data('area_da_sala', "Menu")
        UR = self.select_data('UR', 'Menu')
        elevacao = self.select_data('elevacao', "Menu")
        TBS = self.select_data('TBS', 'Menu')
        pressao = self.select_data('pressao', "Menu")
        tag         = self.select_data("tag", "ParedeInterna")
        espessura   = self.select_data("espessura_pi", "ParedeInterna")
        largura     = self.select_data("largura_pi", "ParedeInterna")
        material    = self.select_data("material_pi", "ParedeInterna") 
        t_viz       = self.select_data("tviz", "ParedeInterna")
        PD = self.select_data_2('pe_direito', "Menu", tag)
        [camada_1, k, camada_2, R_2, camada_3, R_3, camada_4, R_4, R_total, hi, he] = self.select_material(material)
        X = CargaTermica(tag, nome, PD, area, TBS, UR, pressao)
        Cs_pi = X.q_paredes_internas(t_viz, R_total, espessura, largura, k, hi, he, material, TBS)
        print("Cs_pi = " , Cs_pi, "W")
        print('Pé Direito = ', PD)
        print("Largura = ", largura)
        
        return Cs_pi
        
class Janelas(SelectData, SelectMaterial):
            
    def calcular(self):
        tag =  self.select_data('tag', "ParedeExterna")
        nome = self.select_data_2('nome_da_sala', "Menu", tag)
        TBS = self.select_data_2('TBS', 'Menu', tag)
        area = self.select_data_2('area_da_sala', "Menu",tag)
        UR = self.select_data_2('UR', 'Menu', tag)
        pressao = self.select_data_2('pressao', "Menu", tag)
        PD = self.select_data_2("pe_direito", "Menu", tag)
        elevacao = self.select_data_2('elevacao', "Menu", tag)
        ajanela = self.select_data_2('ajanela', 'ParedeExterna', tag)
        posicao = self.select_data_2('posicao_pe', 'ParedeExterna', tag)
        # material = self.select_data('material_pe', 'ParedeExterna')
        material = "V03"
        espessura = self.select_data_2('espessura_pe', 'ParedeExterna', tag)
        largura = self.select_data_2('largura_pe', 'ParedeExterna', tag)
        Tamb = 34.3
        FS = 1
        # SHGF_max = 1
        dt = Tamb - TBS 
        [camada_1, k, camada_2, R_2, camada_3, R_3, camada_4, R_4, R_total, hi, he] = self.select_material(material)
        Y = SGHF()
        SGHF_max = Y.sghf('maximo', posicao)
        X = CargaTermica(tag, nome, PD, area, TBS, UR, pressao)
        [Cs_jan_cond, Cs_jan_trans] = X.q_janelas(R_total, espessura, largura, k, hi, he, material, TBS, dt, ajanela, FS, SGHF_max)
        print("Cs_jan_cond", Cs_jan_cond)
        print("Cs_jan_trans", Cs_jan_trans)
                
        return Cs_jan_cond, Cs_jan_trans

    
class PisoTeto2(SelectData, SelectMaterial):
    
    def __init__(self):
        self.tag =  self.select_data('tag', "Piso")
        self.nome = self.select_data_2('nome_da_sala', "Menu", self.tag)
        self.TBS = self.select_data('TBS', 'Menu')
        self.area = self.select_data_2('area_da_sala', "Menu",self.tag)
        self.UR = self.select_data_2('UR', 'Menu', self.tag)
        self.pressao = self.select_data_2('pressao', "Menu", self.tag)
        self.PD = self.select_data_2("pe_direito", "Menu", self.tag)
        self.elevacao = self.select_data_2('elevacao', "Menu", self.tag)  
        self.latitude = 24
        
    def calcular_piso(self):
        espessura   = self.select_data('espessura_piso', "Piso")
        largura     = self.select_data('largura_piso', 'Piso')
        Tamb          = self.select_data('t2_piso', 'Piso')
        material    = self.select_data('material_piso', 'Piso')
        [camada_1, k, camada_2, R_2, camada_3, R_3, camada_4, R_4, R_total, hi, he] = self.select_material(material)
        X = CargaTermica(self.tag, self.nome, self.PD, self.area, self.TBS, self.UR, self.pressao)
        dt = Tamb - self.TBS
        Cs_piso = X.q_piso(R_total, espessura, largura, k, hi, he, dt)
        
        return Cs_piso
        
    def calcular_teto(self):
        espessura   = self.select_data('espessura_teto', "Teto")
        largura     = self.select_data('largura_teto', 'Teto')
        Tamb          = self.select_data('t2_teto', 'Teto')
        material    = self.select_data('material_teto', 'Teto')
        [camada_1, k, camada_2, R_2, camada_3, R_3, camada_4, R_4, R_total, hi, he] = self.select_material(material)
        X = CargaTermica(self.tag, self.nome, self.PD, self.area, self.TBS, self.UR, self.pressao)
        dt = Tamb - self.TBS
        Cs_teto = X.q_teto(R_total, espessura, largura, k, hi, he, dt)
                
        return Cs_teto  
                
    def calcular_telhado(self):
        espessura   = self.select_data_2('espessura_telhado', "Telhado", self.tag)
        largura     = self.select_data_2('largura_telhado', 'Telhado', self.tag)
        grupo          = self.select_data_2('grupo_telhado', 'Telhado', self.tag)
        material    = self.select_data_2('material_telhado', 'Telhado', self.tag)
        [camada_1, k, camada_2, R_2, camada_3, R_3, camada_4, R_4, R_total, hi, he] = self.select_material(material)
        X = CargaTermica(self.tag, self.nome, self.PD, self.area, self.TBS, self.UR, self.pressao)                          
        Cs_telhado = X.q_telhado(R_total, espessura, largura, k, hi, he, self.latitude, grupo, self.TBS)
        return Cs_telhado         
            
    def calcular_forro(self):
        espessura   = self.select_data_2('espessura_forro', "Forro", self.tag)
        largura     = self.select_data_2('largura_forro', 'Forro', self.tag)
        grupo          = self.select_data_2('grupo_forro', 'Forro', self.tag)
        material    = self.select_data_2('material_forro', 'Forro', self.tag)
        [camada_1, k, camada_2, R_2, camada_3, R_3, camada_4, R_4, R_total, hi, he] = self.select_material(material)
        X = CargaTermica(self.tag, self.nome, self.PD, self.area, self.TBS, self.UR, self.pressao)          
        Cs_forro = X.q_forro(R_total, espessura, largura, k, hi, he, self.latitude, grupo, self.TBS)
        
        return Cs_forro  

        
class Pessoas2(SelectData, SelectMaterial):
    
    def calcular_carga_ocupacao(self):
        self.tag =  self.select_data('tag', "Pessoas" )
        area = self.select_data_2("area_da_sala", "Menu", self.tag)
        tipo_de_ocupacao = self.select_data('tipo_de_ocupacao', "Pessoas")
        qtd_de_pessoas     = self.select_data('qtd_pessoas', 'Pessoas')
        [Cs, Cl] = self.select_tipo_ocupacao(tipo_de_ocupacao)
        Carga_sensivel_ocupacao = qtd_de_pessoas * Cs        
        Carga_latente_ocupacao = qtd_de_pessoas * Cl 
        return Carga_sensivel_ocupacao, Carga_latente_ocupacao 
        
# X = PisoTeto2()        
# Cs_teto = X.calcular_telhado()        
        
# X = Pessoas2()
# X.calcular_carga_ocupacao()        
        
    


# X = ParedeInterna()       
# Cs_pi = X.calcular()

# print("Cs_pi = ", Cs_pi, "W")


    