# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 08:08:15 2021

@author: 08397697926
"""

from PySide6.QtWidgets import QFormLayout, QLabel, QPushButton, QApplication, QMainWindow, QDialog, QFileDialog, QMessageBox
from PySide6.QtGui import QTextCursor
from paredesexternas import Ui_ParedesExternas
from paredesinternas import Ui_ParedesInternas
from piso import Ui_PisoTeto
from menu import Ui_Menu
from database3 import Banco_Dados, SelectData
from outputs import ParedeExterna

import os
import pandas as pd
import xlsxwriter
from openpyxl import load_workbook
import sys

#listas parede externas
TAG = []
nome_da_sala = []
elevacao = []
area = []
pe_direito = []
espessura_pe = []
largura_pe = []
posicao_pe = []
material_pe = []
grupo_pe = []

class Manager:
    def __init__(self):
        
        self.menu = Menu()
        self.paredes_externas = ParedesExternas()
        self.paredes_internas = ParedesInternas()
        self.piso_teto = PisoTeto()
        
        #Parede Externa
        self.menu.pushButton.clicked.connect(self.paredes_externas.show)
        self.paredes_externas.pushButton.clicked.connect(self.menu.show)
        
        #Parede Interna
        self.menu.pushButton_2.clicked.connect(self.paredes_internas.show)
        self.paredes_internas.pushButton.clicked.connect(self.menu.show)
        
        #Piso-Teto-Telhado-Forro
        self.menu.pushButton_3.clicked.connect(self.piso_teto.show)
        self.piso_teto.pushButton.clicked.connect(self.menu.show)
        
        self.menu.show()
        
class Menu(QMainWindow, Ui_Menu,Banco_Dados, SelectData):    
    
    def __init__(self):
        
        super(Menu, self).__init__(parent=None)
       
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(self.hide)
        self.pushButton_3.clicked.connect(self.hide)
        # self.pushButton_4.clicked.connect(self.hide)
        # self.pushButton_5.clicked.connect(self.hide)
        # self.pushButton_6.clicked.connect(self.hide)
        self.pushButton_7.clicked.connect(self.inserir_dados)
        self.pushButton_8.clicked.connect(self.carregar_dados)

    def inserir_dados(self):
        
        self.extract_data()
        self.db_insert()
        
    def extract_data(self):
        
        self.TAG             = self.plainTextEdit.toPlainText()
        self.nome_da_sala    = self.plainTextEdit_2.toPlainText()      
        self.elevacao        = self.plainTextEdit_3.toPlainText() 
        self.area_da_sala    = self.plainTextEdit_4.toPlainText() 
        self.pe_direito      = self.plainTextEdit_5.toPlainText() 
        self.TBS             = self.plainTextEdit_6.toPlainText() 
        self.UR              = self.plainTextEdit_7.toPlainText() 
        self.pressao         = self.plainTextEdit_8.toPlainText() 

    def db_insert(self):
        
        db = Banco_Dados('db2')
        db.inserir_dados_menu(self.TAG, self.nome_da_sala, self.elevacao, self.area_da_sala, self.pe_direito, self.TBS, self.UR, self.pressao)
        
    def carregar_dados(self):
        i=self.tamanho_db()-1
        print (i)
        
        tag              = self.select_data('tag', 'Menu',i)
        nome_da_sala     = self.select_data('nome_da_sala', 'Menu',i)    
        elevacao         = self.select_data('elevacao', 'Menu',i) 
        area_da_sala     = self.select_data('area_da_sala', 'Menu',i) 
        pe_direito       = self.select_data('pe_direito', 'Menu',i) 
        TBS              = self.select_data('TBS', 'Menu',i) 
        UR               = self.select_data('UR', 'Menu',i) 
        pressao          = self.select_data('pressao', 'Menu',i) 
        
        self.plainTextEdit.setPlainText(str(tag))
        self.plainTextEdit_2.setPlainText(str(nome_da_sala))
        self.plainTextEdit_3.setPlainText(str(elevacao))
        self.plainTextEdit_4.setPlainText(str(area_da_sala))
        self.plainTextEdit_5.setPlainText(str(pe_direito))
        self.plainTextEdit_6.setPlainText(str(TBS))
        self.plainTextEdit_7.setPlainText(str(UR))
        self.plainTextEdit_8.setPlainText(str(pressao))

        # self.plainTextEdit.setPlainText(str(tag[i][0]))
        # self.plainTextEdit_2.setPlainText(str(nome_da_sala[i][0]))
        # self.plainTextEdit_3.setPlainText(str(elevacao[i][0]))
        # self.plainTextEdit_4.setPlainText(str(area_da_sala[i][0]))
        # self.plainTextEdit_5.setPlainText(str(pe_direito[i][0]))
        # self.plainTextEdit_6.setPlainText(str(TBS[i][0]))
        # self.plainTextEdit_7.setPlainText(str(UR[i][0]))
        # self.plainTextEdit_8.setPlainText(str(pressao[i][0]))

class ParedesExternas(QDialog, Ui_ParedesExternas, SelectData):
   
    def __init__(self):
        
        super(ParedesExternas, self).__init__(parent=None)
        
        lista_tag = self.lista_tag()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)
        # self.pushButton.clicked.connect(self.extract_data2)
        self.pushButton_2.clicked.connect(self.extract_data)
        self.pushButton_3.clicked.connect(self.calculo)
        self.pushButton_4.clicked.connect(self.carregar_dados_pe)
        self.comboBox_3.addItems(lista_tag)
        self.i = 0
        self.clear_data()
        
    def calculo(self):
        x = ParedeExterna()
        cs_pe = round(x.calcular(),3)
        self.db_insert_carga_termica(cs_pe)
        self.plainTextEdit_5.setPlainText("CS_pe= " + str(cs_pe) + "W")
        self.carregar_dados_pe()
        
    def carregar_dados_pe(self):
        i=self.tamanho_db()-1
        print (i)
        espessura = self.select_data('espessura_pe', 'ParedeExterna',i)
        largura = self.select_data('largura_pe', 'ParedeExterna',i)
        material = self.select_data('material_pe', 'ParedeExterna',i)
        grupo = self.select_data('grupo_pe', 'ParedeExterna',i)
        posicao = self.select_data('posicao_pe', 'ParedeExterna',i)
        ajanela = self.select_data('ajanela', 'ParedeExterna',i)
        self.plainTextEdit.setPlainText(str(espessura))
        self.plainTextEdit_2.setPlainText(str(largura))
        self.plainTextEdit_4.setPlainText(str(ajanela))
    
    def add_parede(self):# adicionar mais paredes
    
        print("Adicione a próxima parede")

        self.extract_data()
       
    # def extract_data2(self):
    #     print ('parede 2')
    #     self.i = 0
    #     print(len(self.espessura))
    #     if len(self.espessura)>0:
        
    #         for i in range(len(self.espessura)):
    #             self.espessura2[i] = self.espessura[i]
    #             self.largura2[i]   = self.largura[i]    
    #             self.material2[i]  = self.material[i]
    #             self.grupo2[i]     = self.grupo[i]
    #             self.posicao2[i]   = self.posicao[i]
    #             self.ajanela2[i]   = self.ajanela[i]
                
    #         self.db_insert(self.espessura2[0],  self.largura2[0],  self.material2[0],  self.grupo2[0],  self.posicao2[0], self.ajanela2[0],
    #                        self.espessura2[1],  self.largura2[1],  self.material2[1],  self.grupo2[1],  self.posicao2[1], self.ajanela2[1],
    #                        self.espessura2[2],  self.largura2[2],  self.material2[2],  self.grupo2[2],  self.posicao2[2], self.ajanela2[2],
    #                        self.espessura2[3],  self.largura2[3],  self.material2[3],  self.grupo2[3],  self.posicao2[3], self.ajanela2[3])

    #         self.clear_data()
        
    def extract_data(self):
        
        # print(self.i)      
        
        espessura = self.plainTextEdit.toPlainText()
        largura = self.plainTextEdit_2.toPlainText()    
        ajanela = self.plainTextEdit_4.toPlainText()
        material = self.comboBox.currentText()
        grupo = self.comboBox_2.currentText()
        
        # self.espessura.append(self.plainTextEdit.toPlainText())
        # self.largura.append(self.plainTextEdit_2.toPlainText())      
        # self.ajanela.append(self.plainTextEdit_4.toPlainText())  
        # self.material.append(self.comboBox.currentText())
        # self.grupo.append(self.comboBox_2.currentText())  
        
        
        if self.radioButton.isChecked():
            print('voce selecionou N')
            # self.posicao.append('N')'
            posicao = ('N')
        elif self.radioButton_2.isChecked():
            print('voce selecionou NNE')
            # self.posicao.append( 'NNE')
            posicao = ('NNE')
        elif self.radioButton_3.isChecked():
            print('voce selecionou NE')
            # self.posicao.append('NE')
            posicao = ('NE')
        elif self.radioButton_4.isChecked():
            print('voce selecionou ENE')
            # self.posicao.append('ENE')
            posicao = 'ENE'
        elif self.radioButton_5.isChecked():
            print('voce selecionou E')
            # self.posicao.append('E')
            posicao = 'E'
        elif self.radioButton_6.isChecked():
            print('voce selecionou ESE')
            # self.posicao.append('ESE')
            posicao = 'ESE'
        elif self.radioButton_7.isChecked():
            print('voce selecionou SE')
            # self.posicao.append('SE')
            posicao = 'SE'
        elif self.radioButton_8.isChecked():
            print('voce selecionou SSE')
            # self.posicao.append('SSE')
            posicao = 'SSE'
        elif self.radioButton_9.isChecked():
            print('voce selecionou S')
            # self.posicao.append('S')
            posicao = 'S'
        elif self.radioButton_10.isChecked():
            print('voce selecionou SSW')
            # self.posicao.append('SSW')
            posicao = 'SSW'
        elif self.radioButton_11.isChecked():
            print('voce selecionou SW')
            # self.posicao.append('SW')
            posicao = 'SW'
        elif self.radioButton_12.isChecked():
            print('voce selecionou WSW')
            # self.posicao.append('WSW')
            posicao = 'WSW'
        elif self.radioButton_13.isChecked():
            print('voce selecionou W')
            # self.posicao.append('W')
            posicao = 'W'
        elif self.radioButton_14.isChecked():
            print('voce selecionou WWW')         
            # self.posicao.append('WWW')
            posicao = 'WWW'
        elif self.radioButton_15.isChecked():
            print('voce selecionou NW')
            # self.posicao.append('NW')
            posicao = 'NW'
        elif self.radioButton_16.isChecked():
            print('voce selecionou NNW')
            # self.posicao.append('NNW')
            posicao = 'NNW'

        i=self.tamanho_db()-1
        print (i)
        tag = self.select_data('tag', 'Menu',i)

        print('Teste = ',espessura,  largura,  material,  grupo,  posicao, ajanela)
        self.db_insert(tag, espessura,  largura,  material,  grupo,  posicao, ajanela)
        
        self.calculo()

        # self.clear_data()
        
              
    # self.i = self.i+1     
            
            

        
        # if self.i == 3 :
        #     self.i = -1
        #     self.espessura_pe   = self.espessura
        #     self.largura_pe     = self.largura
        #     self.material_pe    = self.material
        #     self.grupo_pe       = self.grupo
        #     self.posicao_pe     = self.posicao
        #     self.ajanela_pe     = self.ajanela
            
            # self.db_insert(self.espessura_pe[0],  self.largura_pe[0],  self.material_pe[0],  self.grupo_pe[0],  self.posicao_pe[0], self.temp_viz[0], self.ajanela[0],
            #                self.espessura_pe[1],  self.largura_pe[1],  self.material_pe[1],  self.grupo_pe[1],  self.posicao_pe[1], self.temp_viz[1], self.ajanela[1],
            #                self.espessura_pe[2],  self.largura_pe[2],  self.material_pe[2],  self.grupo_pe[2],  self.posicao_pe[2], self.temp_viz[2], self.ajanela[2],
            #                self.espessura_pe[3],  self.largura_pe[3],  self.material_pe[3],  self.grupo_pe[3],  self.posicao_pe[3], self.temp_viz[3], self.ajanela[3])

            # self.db_insert(self.espessura_pe[0],  self.largura_pe[0],  self.material_pe[0],  self.grupo_pe[0],  self.posicao_pe[0], self.temp_viz[0], self.ajanela[0])

        
    def clear_data(self):

        self.espessura2  = ['']*4
        self.largura2    = ['']*4
        self.material2   = ['']*4
        self.grupo2      = ['']*4
        self.posicao2    = ['']*4
        self.ajanela2    = ['']*4
        
        self.espessura  = []
        self.largura    = []
        self.material   = []
        self.grupo      = []
        self.posicao    = []
        self.ajanela    = []

    # def db_insert(self, espessura_pe, largura_pe, material_pe, grupo_pe, posicao_pe, ajanela, 
    #                     espessura_pe2, largura_pe2, material_pe2, grupo_pe2, posicao_pe2, ajanela2,
    #                     espessura_pe3, largura_pe3, material_pe3, grupo_pe3, posicao_pe3, ajanela3,
    #                     espessura_pe4, largura_pe4, material_pe4, grupo_pe4, posicao_pe4, ajanela4):

    #     db = Banco_Dados()

    #     db.inserir_dados_parede_externa( espessura_pe,  largura_pe,  material_pe,  grupo_pe,  posicao_pe,   ajanela, 
    #                                      espessura_pe2, largura_pe2, material_pe2, grupo_pe2, posicao_pe2,  ajanela2,
    #                                      espessura_pe3, largura_pe3, material_pe3, grupo_pe3, posicao_pe3,  ajanela3,
    #                                      espessura_pe4, largura_pe4, material_pe4, grupo_pe4, posicao_pe4,  ajanela4) 

    def db_insert(self, tag, espessura_pe, largura_pe, material_pe, grupo_pe, posicao_pe, ajanela):
        
        db = Banco_Dados("db2")
    
        db.inserir_dados_parede_externa(tag, espessura_pe,  largura_pe,  material_pe,  grupo_pe,  posicao_pe,   ajanela)
        
    def db_insert_carga_termica(self, qt):
        db = Banco_Dados("db2")
        db.inserir_resultados(qt)
        
        
        
class ParedesInternas(QMainWindow,Ui_ParedesInternas):

    def __init__(self, parent=None):

        super(ParedesInternas, self).__init__(parent=None)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(self.add_paredes)

    def add_paredes(self):

        self.extract_data()
        self.db_insert_PI()
        self.clear_data()

    def extract_data(self):

        self.espessura_D1 = self.plainTextEdit.toPlainText()
        self.largura_D1 = self.plainTextEdit_2.toPlainText()
        self.t2_D1 = self.plainTextEdit_3.toPlainText()
        self.material_D1 = self.comboBox.currentText()

        self.espessura_D2 = self.plainTextEdit_4.toPlainText()
        self.largura_D2 = self.plainTextEdit_5.toPlainText()
        self.t2_D2 = self.plainTextEdit_6.toPlainText()
        self.material_D2 = self.comboBox_2.currentText()

        self.espessura_D3 = self.plainTextEdit_7.toPlainText()
        self.largura_D3 = self.plainTextEdit_8.toPlainText()
        self.t2_D3 = self.plainTextEdit_9.toPlainText()
        self.material_D3 = self.comboBox_3.currentText()

        self.espessura_D4 = self.plainTextEdit_10.toPlainText()
        self.largura_D4 = self.plainTextEdit_11.toPlainText()
        self.t2_D4 = self.plainTextEdit_12.toPlainText()
        self.material_D4 = self.comboBox_4.currentText()

    def db_insert_PI(self):

        db = Banco_Dados()
       
        db.inserir_dados_parede_interna(self.espessura_D1, self.largura_D1, self.t2_D1, self.material_D1, 
                                        self.espessura_D2, self.largura_D2, self.t2_D2, self.material_D2,
                                        self.espessura_D3, self.largura_D3, self.t2_D3, self.material_D3,
                                        self.espessura_D4, self.largura_D4, self.t2_D4, self.material_D4)

    def clear_data(self):
       
        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()
        self.plainTextEdit_3.clear()
        self.plainTextEdit_4.clear()
        self.plainTextEdit_5.clear()
        self.plainTextEdit_6.clear()
        self.plainTextEdit_7.clear()
        self.plainTextEdit_8.clear()
        self.plainTextEdit_9.clear()
        self.plainTextEdit_10.clear()
        self.plainTextEdit_11.clear()
        self.plainTextEdit_12.clear()
    
class PisoTeto(QDialog, Ui_PisoTeto):

    def __init__(self, parent=None):

        super(PisoTeto, self).__init__(parent=None)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.hide)
        self.pushButton_2.clicked.connect(self.add_data)

    def add_data(self):
        
       self.extract_data()
       self.db_insert_PT()
       # self.clear()     

    def extract_data(self):

        self.espessura_piso  = self.plainTextEdit.toPlainText()
        self.largura_piso    = self.plainTextEdit_2.toPlainText()
        self.t2_piso         = self.plainTextEdit_3.toPlainText()
        self.material_piso   = self.comboBox.currentText()
        
        self.espessura_teto  = self.plainTextEdit_4.toPlainText()
        self.largura_teto    = self.plainTextEdit_5.toPlainText()
        self.t2_teto         = self.plainTextEdit_6.toPlainText()
        self.material_teto   = self.comboBox_2.currentText()

        self.espessura_telhado  = self.plainTextEdit_7.toPlainText()
        self.largura_telhado    = self.plainTextEdit_8.toPlainText()
        self.material_telhado   = self.comboBox_3.currentText()
        self.grupo_telhado      = self.comboBox_4.currentText()

        self.espessura_forro  = self.plainTextEdit_9.toPlainText()
        self.largura_forro    = self.plainTextEdit_10.toPlainText()
        self.material_forro   = self.comboBox_5.currentText()
        self.grupo_forro      = self.comboBox_6.currentText()
    
    def db_insert_PT(self):
       
        db = Banco_Dados()
        
        db.inserir_dados_piso_teto(self.espessura_piso, self.largura_piso, self.t2_piso, self.material_piso, 
                                   self.espessura_teto, self.largura_teto, self.t2_teto, self.material_teto, 
                                   self.espessura_telhado, self.largura_telhado, self.material_telhado, self.grupo_telhado, 
                                   self.espessura_forro, self.largura_forro, self.material_forro, self.grupo_forro)
        
        # self.db_insert()
        # return espessura_piso,largura_piso, t2_piso, material_piso, espessura_teto, largura_teto, 
        # grupo_telhado, t2_teto, material_teto, espessura_telhado, largura_telhado, material_telhado, 
        # espessura_forro, largura_forro, material_forro, grupo_forro

def main():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    main = Manager()
    sys.exit(app.exec())
        
if __name__ == '__main__':
    main()
