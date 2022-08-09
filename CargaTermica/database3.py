# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 10:37:20 2021

@author: 08397697926
"""
import numpy as np
import sqlite3



class SelectData():
    
    def select_data(self, name, table):
        X = []
        con = sqlite3.connect('db2.db')
        cur = con.cursor()
        for row in cur.execute('SELECT '+ name +' FROM ' + table ):
            X.append(row)
        i = len(X)-1
        # print("Dados = ", X)
        return X[i][0]
    
    def select_data_2(self, name, table, tag):
        searchstr = str(tag)
        tg  = []
        Y   = []
        con = sqlite3.connect('db2.db')
        cur = con.cursor()
        tg  = self.lista('tag', table)
        Y   = self.lista(name, table)
        i   = tg.index(tag)        
        x   = Y[i]
        return x
                 
    def tamanho_db(self, table, column):
        X = []
        con = sqlite3.connect('db2.db')
        cur = con.cursor()
        for row in cur.execute('SELECT '+ column + ' FROM ' + table ):
            X.append(row)
        n = len(X)
        return n
    
    def lista(self, name, table):
        X = []
        con = sqlite3.connect('db2.db')
        cur = con.cursor()
        for row in cur.execute('SELECT '+ name+ ' FROM ' + table ):
            X.append(row)
        L = []
        for i in range(len(X)):
            L.append(X[:][i][0])              
        return L
    
    def lista_tag(self):
        X = []
        con = sqlite3.connect('db2.db')
        cur = con.cursor()
        for row in cur.execute('SELECT tag FROM Menu' ):
            X.append(row)
        L = []
        for i in range(len(X)):
            L.append(X[:][i][0])              
        return L

class Banco_Dados():    
   
    def __init__(self, nome_db):
        super (Banco_Dados,self).__init__()
        self.nome_db = nome_db + ".db"
        self.conn = sqlite3.connect(self.nome_db) 
        self.cursor = self.conn.cursor()
                 
    def newtable(self):
        conn = sqlite3.connect(self.nome_db) 
        # conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS Menu(
        Sequencial INTEGER PRIMARY KEY,
        tag VARCHAR,
        nome_da_sala STRING,
        elevacao FLOAT,
        area_da_sala FLOAT,
        pe_direito FLOAT,
        TBS FLOAT,
        UR FLOAT,
        pressao FLOAT
        )""")
        
        cursor.execute(""" CREATE TABLE IF NOT EXISTS ParedeExterna
        (Sequencial INTEGER PRIMARY KEY,
        tag VARCHAR,
        espessura_pe FLOAT,
        largura_pe FLOAT,
        material_pe VARCHAR,
        grupo_pe VARCHAR,
        posicao_pe STRING,
        ajanela FLOAT,   
        carga_termica_pe,
        carga_termica_jan_cond,
        carga_termica_jan_trans
        )""")
        
        cursor.execute(""" CREATE TABLE IF NOT EXISTS ParedeInterna
        (Sequencial INTEGER PRIMARY KEY,
        tag VARCHAR,
        espessura_pi FLOAT,
        largura_pi FLOAT,
        material_pi VARCHAR,
        tviz FLOAT,   
        carga_termica
        )""")
        conn.commit()
        
        # cursor.execute(""" CREATE TABLE IF NOT EXISTS PisoTeto
        # (Sequencial INTEGER PRIMARY KEY,
        # espessura_piso FLOAT,
        # largura_piso FLOAT,
        # t2_piso FLOAT,        
        # material_piso VARCHAR,        
        # espessura_teto FLOAT,
        # largura_teto FLOAT,
        # t2_teto FLOAT,
        # material_teto VARCHAR,        
        # espessura_telhado FLOAT,
        # largura_telhado FLOAT,
        # material_telhado VARCHAR,    
        # grupo_telhado VARCHAR,        
        # espessura_forro FLOAT,
        # largura_forro FLOAT,
        # material_forro VARCHAR,    
        # grupo_forro VARCHAR
        # )""")
        # conn.commit()
        
    def newtable_piso(self):
        conn = sqlite3.connect(self.nome_db) 
        # conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS Piso
        (Sequencial INTEGER PRIMARY KEY,
        tag VARCHAR,
        espessura_piso FLOAT,
        largura_piso FLOAT,
        t2_piso FLOAT,        
        material_piso VARCHAR,
        carga_termica_piso FLOAT        
        )""")
        conn.commit()

        cursor.execute(""" CREATE TABLE IF NOT EXISTS Teto
        (Sequencial INTEGER PRIMARY KEY,
         tag VARCHAR,
         espessura_teto FLOAT,
         largura_teto FLOAT,
         t2_teto FLOAT,
         material_teto VARCHAR,
         carga_termica_teto FLOAT)""")
        conn.commit()

        cursor.execute(""" CREATE TABLE IF NOT EXISTS Telhado
        (Sequencial INTEGER PRIMARY KEY,
        tag VARCHAR,
        espessura_telhado FLOAT,
        largura_telhado FLOAT,
        material_telhado VARCHAR,    
        grupo_telhado VARCHAR,
        carga_termica_telhado FLOAT)""")
        conn.commit()

        cursor.execute(""" CREATE TABLE IF NOT EXISTS Forro
        (Sequencial INTEGER PRIMARY KEY,
         tag VARCHAR,
         espessura_forro FLOAT,
         largura_forro FLOAT,
         material_forro VARCHAR,    
         grupo_forro VARCHAR, 
         carga_termica_forro FLOAT)""")        
        conn.commit()

    def newtable_equip(self):
        conn = sqlite3.connect(self.nome_db) 
        # conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS Equipamentos
        (Sequencial INTEGER PRIMARY KEY,
        tag VARCHAR,
        carga_equipamento_eletrica FLOAT,
        carga_equipamento_mecanica FLOAT,
        carga_equipamento_telecomunicacao FLOAT,        
        carga_equipamento_incendio FLOAT,
        carga_equipamento_outros FLOAT        
        )""")
        conn.commit()
        
    def newtable_pessoas(self):
        conn = sqlite3.connect(self.nome_db) 
        # conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS Pessoas
        (Sequencial INTEGER PRIMARY KEY,
        tag VARCHAR,
        tipo_de_ocupacao VARCHAR,
        qtd_pessoas FLOAT,
        carga_latente_pessoas FLOAT,        
        carga_sensível_pkkkessoas FLOAT        
        )""")
        conn.commit()
        
        
        

    def inserir_dados_menu(self,TAG,nome_da_sala, elevacao, area_da_sala, pe_direito, TBS, UR, pressao):
    
        self.conn = sqlite3.connect(self.nome_db ) 
        self.cursor = self.conn.cursor()
        self.conn.commit()
        self.TAG = TAG
        self.nome_da_sala = nome_da_sala
        self.elevacao = elevacao
        self.area_da_sala = area_da_sala
        self.pe_direito = pe_direito
        self.TBS = TBS
        self.UR = UR
        self.pressao = pressao
                
        self.cursor.execute("""INSERT INTO Menu (tag, nome_da_sala, elevacao, area_da_sala,
                            pe_direito,TBS, UR, pressao) VALUES (?,?,?,?,?,?,?,?)""", 
                            (self.TAG,
                             self.nome_da_sala,
                             self.elevacao,
                             self.area_da_sala,
                             self.pe_direito,
                             self.TBS,
                             self.UR,
                             self.pressao))

        self.conn.commit()
        self.conn.close()
        
        
    def inserir_dados_parede_externa(self,tag, espessura_pe, largura_pe, material_pe, grupo_pe, posicao_pe,  ajanela):
        
        self.conn = sqlite3.connect(self.nome_db ) 
        self.cursor = self.conn.cursor()
        self.conn.commit()
        self.cursor.execute("""INSERT INTO ParedeExterna (tag, espessura_pe, largura_pe, material_pe, grupo_pe, posicao_pe, ajanela) 
                                                          VALUES (?,?,?,?,?,?,?)""", 
                              (tag, espessura_pe, largura_pe, material_pe, grupo_pe, posicao_pe,  ajanela))  
        self.conn.commit()
        self.conn.close()   
                

        
    def inserir_dados_parede_interna(self,tag, espessura_pi, largura_pi, material_pi, tviz):
        
        self.conn = sqlite3.connect(self.nome_db ) 
        self.cursor = self.conn.cursor()
        self.conn.commit()
        self.cursor.execute("""INSERT INTO ParedeInterna (tag, espessura_pi, largura_pi, material_pi, tviz) 
                                                          VALUES (?,?,?,?,?)""", (tag, espessura_pi, largura_pi, material_pi, tviz))  
                                               
        self.conn.commit()
        self.conn.close()    
      
    def inserir_dados_piso(self,tag,   espessura_piso,largura_piso, t2_piso, material_piso):
         
         self.conn = sqlite3.connect(self.nome_db) 
         self.cursor = self.conn.cursor()
         self.conn.commit()    

         self.cursor.execute("""INSERT INTO Piso ( tag, espessura_piso,largura_piso, t2_piso, material_piso) 
                             VALUES (?,?,?,?,?)""", 
                             ( tag,
                              espessura_piso,
                              largura_piso,
                              t2_piso,
                              material_piso))
         
         self.conn.commit()
         self.conn.close()  
         
    def inserir_dados_teto(self, tag, espessura_teto,largura_teto, t2_teto, material_teto):
         
         self.conn = sqlite3.connect(self.nome_db) 
         self.cursor = self.conn.cursor()
         self.conn.commit()    

         self.cursor.execute("""INSERT INTO Teto (tag, espessura_teto,largura_teto, t2_teto, material_teto) 
                             VALUES (?,?,?,?,?)""", 
                             (tag,
                              espessura_teto,
                              largura_teto,
                              t2_teto,
                              material_teto))
         
         self.conn.commit()
         self.conn.close()  
  
    def inserir_dados_telhado(self, tag, espessura_telhado,largura_telhado, material_telhado, grupo_telhado):
         
         self.conn = sqlite3.connect(self.nome_db) 
         self.cursor = self.conn.cursor()
         self.conn.commit()    

         self.cursor.execute("""INSERT INTO Telhado ( tag, espessura_telhado,largura_telhado, material_telhado, grupo_telhado) 
                             VALUES (?,?,?,?,?)""", 
                             (tag,
                              espessura_telhado,
                              largura_telhado,
                              material_telhado,
                              grupo_telhado))
         
         self.conn.commit()
         self.conn.close()  
    
    def inserir_dados_forro(self, tag, espessura_forro,largura_forro, material_forro, grupo_forro):
           
         self.conn = sqlite3.connect(self.nome_db) 
         self.cursor = self.conn.cursor()
         self.conn.commit()    

         self.cursor.execute("""INSERT INTO Forro (tag, espessura_forro,largura_forro, material_forro, grupo_forro) 
                            VALUES (?,?,?,?,?)""", 
                            (tag,
                             espessura_forro,
                             largura_forro,
                             material_forro,
                             grupo_forro))
           
         self.conn.commit()
         self.conn.close()              

    def inserir_dados_equipamentos(self, tag, carga_equipamento_eletrica, carga_equipamento_mecanica, carga_equipamento_telecomunicacao, carga_equipamento_incendio, carga_equipamento_outros):
          
          self.conn = sqlite3.connect(self.nome_db) 
          self.cursor = self.conn.cursor()
          self.conn.commit()    

          self.cursor.execute("""INSERT INTO Equipamentos (tag, carga_equipamento_eletrica, carga_equipamento_mecanica, carga_equipamento_telecomunicacao, carga_equipamento_incendio, carga_equipamento_outros) 
                              VALUES (?,?,?,?,?,?)""", 
                              (tag,
                              carga_equipamento_eletrica,
                              carga_equipamento_mecanica, 
                              carga_equipamento_telecomunicacao,
                              carga_equipamento_incendio,
                              carga_equipamento_outros))
          
          self.conn.commit()
          self.conn.close()  
          
    def inserir_dados_pessoas(self, tag, tipo_de_ocupacao, qtd_pessoas):
        self.conn = sqlite3.connect(self.nome_db) 
        self.cursor = self.conn.cursor()
        self.conn.commit()    

        self.cursor.execute("""INSERT INTO Pessoas (tag, tipo_de_ocupacao, qtd_pessoas) 
                            VALUES (?,?,?)""", 
                            (tag,
                             tipo_de_ocupacao,
                             qtd_pessoas))
        
        self.conn.commit()
        self.conn.close()  
         
         
    def inserir_resultados(self,qt, n, table, carga):
        self.conn = sqlite3.connect(self.nome_db ) 
        self.cursor = self.conn.cursor()
        self.conn.commit()
        self.cursor.execute("""UPDATE """ + table + """ SET """ + carga + """ = (?) WHERE Sequencial = (?) """, (qt, n))
        self.conn.commit()
        self.conn.close()      
         
        
# X = SelectData()
# x = X.select_data_2("pe_direito", "Menu", "A01")       
# print(x)
        
        
        