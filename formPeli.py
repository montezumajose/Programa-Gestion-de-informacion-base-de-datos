# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formPeli.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

class Ui_formPeli(object):

    def setupUi(self, formPeli):
        formPeli.setObjectName("formPeli")
        formPeli.resize(577, 361)
        self.label = QtWidgets.QLabel(formPeli)
        self.label.setGeometry(QtCore.QRect(30, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(formPeli)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(formPeli)
        self.label_3.setGeometry(QtCore.QRect(300, 140, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(formPeli)
        self.label_4.setGeometry(QtCore.QRect(290, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(formPeli)
        self.label_5.setGeometry(QtCore.QRect(30, 200, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(formPeli)
        self.label_6.setGeometry(QtCore.QRect(20, 300, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(formPeli)
        self.label_7.setGeometry(QtCore.QRect(170, 20, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tituloPeli = QtWidgets.QLineEdit(formPeli)
        self.tituloPeli.setGeometry(QtCore.QRect(100, 80, 141, 21))
        self.tituloPeli.setObjectName("tituloPeli")
        self.duracionPeli = QtWidgets.QLineEdit(formPeli)
        self.duracionPeli.setGeometry(QtCore.QRect(380, 80, 121, 21))
        self.duracionPeli.setObjectName("duracionPeli")
        self.generoPeli = QtWidgets.QLineEdit(formPeli)
        self.generoPeli.setGeometry(QtCore.QRect(380, 139, 131, 21))
        self.generoPeli.setObjectName("generoPeli")
        self.directorPeli = QtWidgets.QLineEdit(formPeli)
        self.directorPeli.setGeometry(QtCore.QRect(110, 139, 131, 21))
        self.directorPeli.setObjectName("directorPeli")
        self.sinopsisPeli = QtWidgets.QPlainTextEdit(formPeli)
        self.sinopsisPeli.setGeometry(QtCore.QRect(110, 200, 261, 71))
        self.sinopsisPeli.setObjectName("sinopsisPeli")
        self.fechaPeli = QtWidgets.QLineEdit(formPeli)
        self.fechaPeli.setGeometry(QtCore.QRect(210, 300, 161, 21))
        self.fechaPeli.setObjectName("fechaPeli")
        self.enviarPeli = QtWidgets.QPushButton(formPeli)
        self.enviarPeli.setGeometry(QtCore.QRect(440, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.enviarPeli.setFont(font)
        self.enviarPeli.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enviarPeli.setInputMethodHints(QtCore.Qt.ImhNone)
        self.enviarPeli.setCheckable(False)
        self.enviarPeli.setAutoExclusive(False)
        self.enviarPeli.setObjectName("enviarPeli")

        self.retranslateUi(formPeli)
        QtCore.QMetaObject.connectSlotsByName(formPeli)

    def retranslateUi(self, formPeli):
        _translate = QtCore.QCoreApplication.translate
        formPeli.setWindowTitle(_translate("formPeli", "Form"))
        self.label.setText(_translate("formPeli", "Título:"))
        self.label_2.setText(_translate("formPeli", "Director:"))
        self.label_3.setText(_translate("formPeli", "Género:"))
        self.label_4.setText(_translate("formPeli", "Duración:"))
        self.label_5.setText(_translate("formPeli", "Sinopsis:"))
        self.label_6.setText(_translate("formPeli", "Fecha de lanzamiento:"))
        self.label_7.setText(_translate("formPeli", "Formulario de Películas"))
        self.enviarPeli.setText(_translate("formPeli", "Enviar"))