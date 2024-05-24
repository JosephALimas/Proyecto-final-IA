import pandas as pd
import csv
import sys
import os
from datetime import datetime
import requests
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from PyQt6.QtWidgets import QApplication, QCheckBox, QFrame,QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout, QComboBox, QTableWidget , QTableWidgetItem
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import clases as cls
import source as src
################ FONTS ##################
title_font = QFont()
title_font.setFamily('Helvetica')
title_font.setPointSize(50)
title_font.setBold(True)

instr_font = QFont()
instr_font.setFamily('Helvetica')
instr_font.setPointSize(30)
instr_font.setBold(True)    

instr2_font = QFont()
instr2_font.setFamily('Helvetica')
instr2_font.setPointSize(15)
instr2_font.setBold(True)    
################ GUI CLASES ##################
class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance UP")
        self.setMinimumSize(920,1080)
        self.main_menu_widget = QWidget(self)
        self.main_menu_widget.setStyleSheet("background-color: #F5F5F5;")
        self.main_menu_layout = QVBoxLayout(self.main_menu_widget)
        # inicialización de widgets
        # frame principal
        main_frame = QFrame()
        main_frame.setFrameShape(QFrame.Shape.Box)
        main_frame.setLineWidth(4)
        main_frame.setLayout(QVBoxLayout())
        main_frame.setStyleSheet('color: #2F2F2F')
        # frame para el titulo
        title_frame = QFrame()
        title_frame.setFrameShape(QFrame.Shape.Box)
        title_frame.setLineWidth(4)
        title_frame.setLayout(QHBoxLayout())
        # label de titulo
        title_label = QLabel("My Budget Buddy")
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #8B0000;")
        # label de instrucciones
        instr1_label = QLabel("Selecciona una opción")
        instr1_label.setFont(instr_font)
        instr1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instr1_label.setStyleSheet("color: #191970;")
        # boton de opcion uno
        boton_opt_1 = QPushButton("1. Ingresar gastos")
        boton_opt_1.setFont(instr_font)
        boton_opt_1.setStyleSheet('border: 2px solid #4B4B4B')
        boton_opt_1.clicked.connect(self.open_opt_1_window)
        boton_opt_1.setFixedHeight(250)
        #boton de opcion dos
        boton_opt_2 = QPushButton("2. Ver análisis de gastos")
        boton_opt_2.setFont(instr_font)
        boton_opt_2.setStyleSheet('border: 2px solid #4B4B4B')
        boton_opt_2.setFixedHeight(250)
        boton_opt_2.clicked.connect(self.open_opt_2_window)
        #boton de opcion tres
        boton_opt_3 = QPushButton("3. Predecir gastos")
        boton_opt_3.setFont(instr_font)
        boton_opt_3.setStyleSheet('border: 2px solid #4B4B4B')
        boton_opt_3.setFixedHeight(250)
        boton_opt_3.clicked.connect(self.open_opt_3_window)
        # agregamos los widgets al layout
        self.main_menu_layout.addWidget(main_frame)
        main_frame.layout().addWidget(title_frame)
        title_frame.layout().addWidget(title_label)
        main_frame.layout().addWidget(instr1_label)
        main_frame.layout().addWidget(boton_opt_1)
        main_frame.layout().addWidget(boton_opt_2)
        main_frame.layout().addWidget(boton_opt_3)
        self.setCentralWidget(self.main_menu_widget)

    def open_opt_1_window(self):
        self.opt1_window = Opt1Window(self)
        self.opt1_window.show()
        self.hide()

    def open_opt_2_window(self):
        self.opt_2_window = Opt2Window(self)
        self.opt_2_window.show()
        self.hide()

    def open_opt_3_window(self):
        return None

class Opt1Window(QWidget):
    def __init__(self, main_menu_window: MainMenuWindow):
        super().__init__()
        self.main_menu_window = main_menu_window
        self.setStyleSheet("background-color: #F5F5F5;")
        self.setWindowTitle("1. Ingresar gastos")
        self.setMinimumSize(920,1080)
        menu1_layout = QVBoxLayout(self)

        #layout
        main_frame = QFrame()
        main_frame.setFrameShape(QFrame.Shape.Box)
        main_frame.setLineWidth(4)
        main_frame.setLayout(QVBoxLayout())
        main_frame.setStyleSheet('color: #3f2b17;')

        title_frame = QFrame()
        title_frame.setFrameShape(QFrame.Shape.Box) 
        title_frame.setLineWidth(4)
        title_frame.setLayout(QVBoxLayout())
        title_frame.setStyleSheet('color: #2F2F2F;')

        welcome1_label = QLabel('Selecciona una opción')
        welcome1_label.setStyleSheet('color: #191970;')
        welcome1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome1_label.setFont(title_font)


        # regresar al menu principal
        return_button = QPushButton("Regresar al menú principal")
        return_button.setStyleSheet('border: 10px solid #4B4B4B')
        return_button.clicked.connect(self.returnToMainMenu)
        return_button.setFont(instr_font)

        # adding widgets
        menu1_layout.addWidget(main_frame)
        main_frame.layout().addWidget(title_frame)
        title_frame.layout().addWidget(welcome1_label)
        main_frame.layout().addWidget(return_button)

    def returnToMainMenu(self):
        self.main_menu_window.show()
        self.hide()

class Opt2Window(QWidget):
    def __init__(self, main_menu_window:MainMenuWindow):
        super().__init__()
        self.main_menu_window = main_menu_window
        self.setStyleSheet("background-color: #F5F5F5;")
        self.setWindowTitle("1. Ingresar gastos")
        self.setMinimumSize(920,1080)
        menu1_layout = QVBoxLayout(self)

        #layout
        main_frame = QFrame()
        main_frame.setFrameShape(QFrame.Shape.Box)
        main_frame.setLineWidth(4)
        main_frame.setLayout(QVBoxLayout())
        main_frame.setStyleSheet('color: #3f2b17;')

        title_frame = QFrame()
        title_frame.setFrameShape(QFrame.Shape.Box) 
        title_frame.setLineWidth(4)
        title_frame.setLayout(QVBoxLayout())
        title_frame.setStyleSheet('color: #2F2F2F;')

        welcome1_label = QLabel('Selecciona una opción')
        welcome1_label.setStyleSheet('color: #191970;')
        welcome1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome1_label.setFont(title_font)


        # regresar al menu principal
        return_button = QPushButton("Regresar al menú principal")
        return_button.setStyleSheet('border: 10px solid #4B4B4B')
        return_button.clicked.connect(self.returnToMainMenu)
        return_button.setFont(instr_font)

        # adding widgets
        menu1_layout.addWidget(main_frame)
        main_frame.layout().addWidget(title_frame)
        title_frame.layout().addWidget(welcome1_label)
        main_frame.layout().addWidget(return_button)

        

    def returnToMainMenu(self):
        self.main_menu_window.show()
        self.hide()

############## VARIABLES PRINCIPALES ##################
deskTopApp = QApplication([])

################ MAIN ####################

main_menu_window = MainMenuWindow()
main_menu_window.show()
deskTopApp.exec()