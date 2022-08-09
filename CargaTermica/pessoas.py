# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pessoas.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Pessoas(object):
    def setupUi(self, Pessoas):
        if not Pessoas.objectName():
            Pessoas.setObjectName(u"Pessoas")
        Pessoas.resize(643, 384)
        self.textBrowser = QTextBrowser(Pessoas)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(60, 20, 241, 41))
        self.textBrowser_2 = QTextBrowser(Pessoas)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(60, 90, 121, 31))
        self.textBrowser_2.setFrameShape(QFrame.WinPanel)
        self.textBrowser_2.setLineWidth(4)
        self.comboBox = QComboBox(Pessoas)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(210, 90, 141, 31))
        self.comboBox.setEditable(False)
        self.comboBox_2 = QComboBox(Pessoas)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(210, 130, 291, 31))
        self.comboBox_2.setEditable(False)
        self.textBrowser_3 = QTextBrowser(Pessoas)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(60, 130, 121, 31))
        self.textBrowser_3.setFrameShape(QFrame.WinPanel)
        self.textBrowser_3.setLineWidth(4)
        self.pushButton = QPushButton(Pessoas)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(160, 280, 171, 24))
        self.textBrowser_4 = QTextBrowser(Pessoas)
        self.textBrowser_4.setObjectName(u"textBrowser_4")
        self.textBrowser_4.setGeometry(QRect(60, 180, 121, 41))
        self.textBrowser_4.setFrameShape(QFrame.WinPanel)
        self.textBrowser_4.setLineWidth(4)
        self.plainTextEdit = QPlainTextEdit(Pessoas)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(210, 180, 111, 41))
        self.plainTextEdit_11 = QPlainTextEdit(Pessoas)
        self.plainTextEdit_11.setObjectName(u"plainTextEdit_11")
        self.plainTextEdit_11.setGeometry(QRect(400, 230, 231, 141))
        self.pushButton_2 = QPushButton(Pessoas)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 250, 171, 24))
        self.pushButton_3 = QPushButton(Pessoas)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(160, 310, 171, 24))

        self.retranslateUi(Pessoas)

        QMetaObject.connectSlotsByName(Pessoas)
    # setupUi

    def retranslateUi(self, Pessoas):
        Pessoas.setWindowTitle(QCoreApplication.translate("Pessoas", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Pessoas", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700;\">Ocupa\u00e7\u00e3o</span></p></body></html>", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Pessoas", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">TAG</span></p></body></html>", None))
        self.textBrowser_3.setHtml(QCoreApplication.translate("Pessoas", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">Tipo de Ocupa\u00e7\u00e3o</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Pessoas", u"Voltar para o Menu", None))
        self.textBrowser_4.setHtml(QCoreApplication.translate("Pessoas", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt;\">Quantidade de Pessoas</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("Pessoas", u"Adicionar ", None))
        self.pushButton_3.setText(QCoreApplication.translate("Pessoas", u"Carregar Dados Anteriores", None))
    # retranslateUi

