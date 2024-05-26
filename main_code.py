import pandas as pd
import csv
import sys
import os
from datetime import datetime
<<<<<<< HEAD
# import requests
=======
#import requests
>>>>>>> 0cb990efd02519b656d5a18b7dc13c778fa16da4
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from PyQt6.QtWidgets import QApplication, QCheckBox, QFrame, QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout, QComboBox, QTableWidget, QTableWidgetItem
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
<<<<<<< HEAD
instr2_font.setBold(True)
=======
instr2_font.setBold(True)    

>>>>>>> 0cb990efd02519b656d5a18b7dc13c778fa16da4
################ GUI CLASES ##################
<<<<<<< HEAD


class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance UP")
        self.setMinimumSize(920, 1080)
=======
class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My budget buddy")
        self.setMinimumSize(950,1080)
        self.main_menu_widget = QWidget(self)
        self.main_menu_widget.setStyleSheet("background-color: #F5F5F5;")
        self.main_menu_layout = QVBoxLayout(self.main_menu_widget)
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
        title_label = QLabel("Bienvenido a ")
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #8B0000;")

        title_label2 = QLabel("My Budget Buddy")
        title_label2.setFont(title_font)
        title_label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label2.setStyleSheet("color: #8B0000;")
        
        instr1_label = QLabel("Selecciona una opción")
        instr1_label.setFont(instr_font)
        instr1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instr1_label.setStyleSheet("color: #191970;")

        # boton de opcion uno
        boton_opt_1 = QPushButton("1. Iniciar sesión")
        boton_opt_1.setFont(instr_font)
        boton_opt_1.setStyleSheet('border: 2px solid #4B4B4B')
        boton_opt_1.clicked.connect(self.open_opt_1_window)
        boton_opt_1.setFixedHeight(250)
        #boton de opcion dos
        boton_opt_2 = QPushButton("2. Registrarse")
        boton_opt_2.setFont(instr_font)
        boton_opt_2.setStyleSheet('border: 2px solid #4B4B4B')
        boton_opt_2.setFixedHeight(250)
        boton_opt_2.clicked.connect(self.open_opt_2_window)
        #agregamos los widgets a la pantalla
        self.main_menu_layout.addWidget(main_frame)
        main_frame.layout().addWidget(title_frame)
        title_frame.layout().addWidget(title_label)
        title_frame.layout().addWidget(title_label2)
        main_frame.layout().addWidget(instr1_label)
        main_frame.layout().addWidget(boton_opt_1)
        main_frame.layout().addWidget(boton_opt_2)
        self.setCentralWidget(self.main_menu_widget)

    def open_opt_1_window(self):
        self.opt1_window =  LogInWindow(self)
        self.opt1_window.show()
        self.hide()

    def open_opt_2_window(self):
        self.opt2_window = RegisterWindow(self)
        self.opt2_window.show()
        self.hide()

class LogInWindow(QWidget):
    def __init__(self,main_menu_window: startWindow):
        super().__init__()
        self.setWindowTitle("My budget buddy")
        self.setMinimumSize(920,1080)
        self.main_menu_window = main_menu_window
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
        instr1_label = QLabel("Ingresa la siguiente información")
        instr1_label.setFont(instr_font)
        instr1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instr1_label.setStyleSheet("color: #191970;")
        # header de cada dato requerido
        label_dato1 = QLabel("Ingresa tu nombre de Usuario")
        label_dato1.setFont(instr2_font)
        label_dato1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_dato1.setStyleSheet("color: #191970;")
        # espacio para añadir la información
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit1.setReadOnly(False)
        self.lineEdit1.textChanged.connect(self.on_text_changed)

        label_dato2 = QLabel("Ingresa tu contraseña")
        label_dato2.setFont(instr2_font)
        label_dato2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_dato2.setStyleSheet("color: #191970;")

        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit2.setReadOnly(False)
        self.lineEdit2.textChanged.connect(self.on_text_changed)

        self.confirm_button = QPushButton("Iniciar Sesión")
        self.confirm_button.clicked.connect(self.addUserProcess)
        self.confirm_button.setFont(instr2_font)
        self.confirm_button.setFixedWidth(880)


        #agregamos low widgets a los frames
        self.main_menu_layout.addWidget(main_frame)
        main_frame.layout().addWidget(title_frame)
        title_frame.layout().addWidget(title_label)
        main_frame.layout().addWidget(instr1_label)
        main_frame.layout().addWidget(label_dato1)    
        main_frame.layout().addWidget(self.lineEdit1)
        main_frame.layout().addWidget(label_dato2)
        main_frame.layout().addWidget(self.lineEdit2)
        main_frame.layout().addWidget(self.confirm_button)

    def on_text_changed(self):
        self.confirm_button.setEnabled(bool(self.lineEdit1.text()) and bool(self.lineEdit2.text()) and bool(self.lineEdit3.text()) and bool(self.lineEdit4.text()))
    
    def addUserProcess(self):
        return None
        
        
class RegisterWindow(QWidget):
    def __init__(self,main_menu_window: startWindow):
        super().__init__()
        self.setWindowTitle("My budget buddy")
        self.setMinimumSize(920,1080)
        self.main_menu_window = main_menu_window
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
        instr1_label = QLabel("Ingresa la información requerida")
        instr1_label.setFont(instr_font)
        instr1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instr1_label.setStyleSheet("color: #191970;")
        # header de cada dato requerido
        label_dato1 = QLabel("Ingresa tu nombre de Usuario")
        label_dato1.setFont(instr2_font)
        label_dato1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_dato1.setStyleSheet("color: #191970;")
        # espacio para añadir la información
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit1.setReadOnly(False)
        self.lineEdit1.textChanged.connect(self.on_text_changed)

        contr_label = QLabel("Ingresa una contraseña")
        contr_label.setFont(instr2_font)
        contr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        contr_label.setStyleSheet("color: #191970;")
        # espacio para añadir la información
        self.contrLine = QLineEdit()
        self.contrLine.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.contrLine.setReadOnly(False)
        self.contrLine.textChanged.connect(self.on_text_changed)

        label_dato2 = QLabel("Ingresa tu edad")
        label_dato2.setFont(instr2_font)
        label_dato2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_dato2.setStyleSheet("color: #191970;")

        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit2.setReadOnly(False)
        self.lineEdit2.textChanged.connect(self.on_text_changed)

        label_dato3 = QLabel("Ingresa tu fecha de nacimiento")
        label_dato3.setFont(instr2_font)
        label_dato3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_dato3.setStyleSheet("color: #191970;")

        self.lineEdit3 = QLineEdit()
        self.lineEdit3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit3.setReadOnly(False)
        self.lineEdit3.textChanged.connect(self.on_text_changed)

        label_dato4 = QLabel("¿Cuál es tu ingreso mensual?")
        label_dato4.setFont(instr2_font)
        label_dato4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_dato4.setStyleSheet("color: #191970;")

        self.lineEdit4 = QLineEdit()
        self.lineEdit4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit4.setReadOnly(False)
        self.lineEdit4.textChanged.connect(self.on_text_changed)

        self.confirm_button = QPushButton("Registrarse")
        self.confirm_button.clicked.connect(self.addUserProcess)
        self.confirm_button.setFont(instr2_font)
        self.confirm_button.setFixedWidth(880)


        #agregamos low widgets a los frames
        self.main_menu_layout.addWidget(main_frame)
        main_frame.layout().addWidget(title_frame)
        title_frame.layout().addWidget(title_label)
        main_frame.layout().addWidget(instr1_label)
        main_frame.layout().addWidget(label_dato1)  
        main_frame.layout().addWidget(self.lineEdit1)
        main_frame.layout().addWidget(contr_label)
        main_frame.layout().addWidget(self.contrLine) 
        main_frame.layout().addWidget(label_dato2)
        main_frame.layout().addWidget(self.lineEdit2)
        main_frame.layout().addWidget(label_dato3)
        main_frame.layout().addWidget(self.lineEdit3)
        main_frame.layout().addWidget(label_dato4)
        main_frame.layout().addWidget(self.lineEdit4)
        main_frame.layout().addWidget(self.confirm_button)

    def on_text_changed(self):
        self.confirm_button.setEnabled(bool(self.lineEdit1.text()) and bool(self.lineEdit2.text()) and bool(self.lineEdit3.text()) and bool(self.lineEdit4.text()))
    
    def addUserProcess(self):
        return None
        
        

class MainMenuWindow(QWidget):
    def __init__(self,main_menu_window: startWindow):
        super().__init__()
        self.setWindowTitle("My budget buddy")
        self.setMinimumSize(920,1080)
>>>>>>> emi
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
        # boton de opcion dos
        boton_opt_2 = QPushButton("2. Ver análisis de gastos")
        boton_opt_2.setFont(instr_font)
        boton_opt_2.setStyleSheet('border: 2px solid #4B4B4B')
        boton_opt_2.setFixedHeight(250)
        boton_opt_2.clicked.connect(self.open_opt_2_window)
        # boton de opcion tres
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
    def __init__(self, main_menu_window: startWindow):
        super().__init__()
        self.main_menu_window = main_menu_window
        self.setStyleSheet("background-color: #F5F5F5;")
        self.setWindowTitle("1. Ingresar gastos")
        self.setMinimumSize(920, 1080)
        menu1_layout = QVBoxLayout(self)

        # layout
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
<<<<<<< HEAD
    def __init__(self, main_menu_window: MainMenuWindow):
=======
    def __init__(self, main_menu_window:startWindow):
>>>>>>> emi
        super().__init__()
        self.main_menu_window = main_menu_window
        self.setStyleSheet("background-color: #F5F5F5;")
        self.setWindowTitle("1. Ingresar gastos")
        self.setMinimumSize(920, 1080)
        menu1_layout = QVBoxLayout(self)

        # layout
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

main_menu_window = startWindow()
main_menu_window.show()
deskTopApp.exec()
