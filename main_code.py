import pandas as pd
import csv
import sys
import os
from datetime import datetime
#import requests
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from PyQt6.QtWidgets import QApplication, QCheckBox, QFrame,QMainWindow, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QLabel, QHBoxLayout, QComboBox, QTableWidget , QTableWidgetItem,QDateEdit,QProgressBar
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import clases as cls
import source as src
import string

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
class startWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My budget buddy")
        self.setMinimumSize(920,1080)
        self.main_menu_widget = QWidget(self)
        self.main_menu_widget.setStyleSheet("background-color: #F5F5F5;")
        self.main_menu_layout = QVBoxLayout(self.main_menu_widget)
        
        ############## SE CORREN LAS FUNCIONES INICIALES
        src.gastos_file_checkup() #crea el archivo para guardar los gastos
        src.users_file_checkup() #crea el archivo de los usuarios
        self.users_list = []
        self.users_list = src.csv_user_to_obj(users_list)
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
        title_label = QLabel("Bienvenido a My Budget Buddy")
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet(title_style)

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
        boton_opt_1.setStyleSheet(back_button_style)  

        #boton de opcion dos
        boton_opt_2 = QPushButton("2. Registrarse")
        boton_opt_2.setFont(instr_font)
        boton_opt_2.setStyleSheet('border: 2px solid #4B4B4B')
        boton_opt_2.setFixedHeight(250)
        boton_opt_2.clicked.connect(self.open_opt_2_window)
        boton_opt_2.setStyleSheet(button_style)
        #agregamos los widgets a la pantalla
        self.main_menu_layout.addWidget(main_frame)
        main_frame.layout().addWidget(title_frame)
        title_frame.layout().addWidget(title_label)
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
        self.lineEdit1.setStyleSheet(border_style)
        self.lineEdit1.setReadOnly(False)
        self.lineEdit1.textChanged.connect(self.on_text_changed)

        label_dato2 = QLabel("Ingresa tu contraseña")
        label_dato2.setFont(instr2_font)
        label_dato2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_dato2.setStyleSheet("color: #191970;")

        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit2.setStyleSheet(border_style)
        self.lineEdit2.setEchoMode(QLineEdit.EchoMode.Password)
        self.lineEdit2.setReadOnly(False)
        self.lineEdit2.textChanged.connect(self.on_text_changed)

        self.confirm_button = QPushButton("Iniciar Sesión")
        self.confirm_button.clicked.connect(self.logInProcess)
        self.confirm_button.setFont(instr2_font)
        self.confirm_button.setStyleSheet(button_style)
        self.confirm_button.setFixedWidth(880)
        

        # regresar al menu principal
        return_button = QPushButton("Regresar al menú principal")
        return_button.setStyleSheet(back_button_style)
        return_button.clicked.connect(self.returnToMainMenu)
        return_button.setFont(instr_font)

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
        main_frame.layout().addWidget(return_button)

    def on_text_changed(self):
        self.confirm_button.setEnabled(bool(self.lineEdit1.text()) and bool(self.lineEdit2.text())) 
    
    def logInProcess(self):
        for user in users_list:
            if user.nombre == self.lineEdit1.text():
                if str(user.contraseña) == str(self.lineEdit2.text()):
                    self.newWindow = MainMenuWindow(self,user) #mandamos a la siguiente pantalla
                    #el usuario identificado para poder operar con sus datos
                    src.csv_gastos_to_obj(gastos_list)
                    self.newWindow.show()
                    self.hide()

    
    def returnToMainMenu(self):
        self.main_menu_window.show()
        self.hide()
              
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
        self.lineEdit1.setStyleSheet(border_style)
        self.lineEdit1.setReadOnly(False)
        self.lineEdit1.textChanged.connect(self.on_text_changed)

        contr_label = QLabel("Ingresa una contraseña")
        contr_label.setFont(instr2_font)
        contr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        contr_label.setStyleSheet("color: #191970;")
        # espacio para añadir la información
        self.contrLine = QLineEdit()
        self.contrLine.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.contrLine.setStyleSheet(border_style)
        self.contrLine.setEchoMode(QLineEdit.EchoMode.Password)

        self.contrLine.setReadOnly(False)
        self.contrLine.textChanged.connect(self.on_text_changed)

        label_dato2 = QLabel("Ingresa tu edad")
        label_dato2.setFont(instr2_font)
        label_dato2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_dato2.setStyleSheet("color: #191970;")

        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit2.setStyleSheet(border_style)
        self.lineEdit2.setReadOnly(False)
        self.lineEdit2.textChanged.connect(self.on_text_changed)

        label_dato3 = QLabel("Ingresa tu fecha de nacimiento")
        label_dato3.setFont(instr2_font)
        label_dato3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_dato3.setStyleSheet(date_edit_style)
        label_dato3.setStyleSheet("color: #191970;")

        self.lineEdit3 = QDateEdit()
        self.lineEdit3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit3.setStyleSheet(date_edit_style)
        self.lineEdit3.setCalendarPopup(True)  
        self.lineEdit3.setDisplayFormat("dd-MM-yyyy")
        self.lineEdit3.setReadOnly(False)
        self.lineEdit3.timeChanged.connect(self.on_text_changed)

        label_dato4 = QLabel("¿Cuál es tu ingreso mensual?")
        label_dato4.setFont(instr2_font)
        label_dato4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_dato4.setStyleSheet("color: #191970;")

        self.lineEdit4 = QLineEdit()
        self.lineEdit4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit4.setStyleSheet(border_style)
        self.lineEdit4.setReadOnly(False)
        self.lineEdit4.textChanged.connect(self.on_text_changed)

        label_dato_dinero = QLabel("Ingresa tu dinero actual: ")
        label_dato_dinero.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_dato_dinero.setFont(instr2_font)
        label_dato_dinero.setStyleSheet("color: #191970;")

        self.lineEdit_dinero = QLineEdit()
        self.lineEdit_dinero.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_dinero.setStyleSheet(border_style)
        self.lineEdit_dinero.setReadOnly(False)
        self.lineEdit_dinero.textChanged.connect(self.on_text_changed)

        self.confirm_button = QPushButton("Registrarse")
        self.confirm_button.clicked.connect(self.addUserProcess)
        self.confirm_button.setFont(instr2_font)
        self.confirm_button.setStyleSheet(button_style)
        self.confirm_button.setFixedWidth(880)

        # regresar al menu principal
        return_button = QPushButton("Regresar al menú principal")
        return_button.setStyleSheet(back_button_style)
        return_button.clicked.connect(self.returnToMainMenu)
        return_button.setFont(instr_font)

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
        main_frame.layout().addWidget(label_dato_dinero)
        main_frame.layout().addWidget(self.lineEdit_dinero)
        main_frame.layout().addWidget(self.confirm_button)
        main_frame.layout().addWidget(return_button)

    def on_text_changed(self):
        self.confirm_button.setEnabled(bool(self.lineEdit1.text()) and bool(self.lineEdit2.text()) and bool(self.lineEdit3.text()) and bool(self.lineEdit4.text()) and bool(self.lineEdit_dinero.text()))
    
    def addUserProcess(self):
        nombre = self.lineEdit1.text()
        contraseña = str(self.contrLine.text())
        edad = self.lineEdit2.text()
        fecha_nacimiento = self.lineEdit3.text()
        ingreso_mensual = self.lineEdit4.text()
        id = len(users_list)
        dinero_actual = self.lineEdit_dinero.text()
        #isntanciamos un usuario con los datos ingresados
        temp_user = cls.Usuario(id,nombre,contraseña,edad,fecha_nacimiento,ingreso_mensual,dinero_actual)
        # lo agregamos a la lista de usuarios 
        users_list.append(temp_user)
        # lo agregamos al csv
        src.add_new_user_to_csv(temp_user)
        # en el momento en que se registra el nuevo usuario, regresamos al menu principal
        self.returnToMainMenu()

    def returnToMainMenu(self):
        self.main_menu_window.show()
        self.hide()
               
class MainMenuWindow(QWidget):
    def __init__(self,main_menu_window: startWindow,user:cls.Usuario):
        super().__init__()
        self.setWindowTitle("My budget buddy")
        self.setMinimumSize(920,1080)
        self.main_menu_window = main_menu_window
        self.user = user
        print(user.id)
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
        #inicio frame
        inicio_frame = QFrame()
        inicio_frame.setFrameShape(QFrame.Shape.Box)
        inicio_frame.setLineWidth(4)
        inicio_frame.setLayout(QHBoxLayout())
        # saludos label
        saludos_label = QLabel(f"Bienvenido {self.user.nombre}")
        saludos_label.setFont(instr_font)
        saludos_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        saludos_label.setStyleSheet(title_style)
        # fecha 
        fecha_actual = datetime.now()
        fecha_formateada = fecha_actual.strftime("%d-%m-%Y")
        fecha_label = QLabel(fecha_formateada)
        fecha_label.setFont(instr_font)
        fecha_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        fecha_label.setStyleSheet(title_style)

        # label de titulo
        title_label = QLabel("My Budget Buddy")
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #8B0000;")
        
        # frame para el gasto
        dinero_frame = QFrame()
        dinero_frame.setFrameShape(QFrame.Shape.Box)
        dinero_frame.setLineWidth(4)
        dinero_frame.setLayout(QHBoxLayout())
        #label de ingresos
        ingreso_label = QLabel("Ingresos")
        ingreso_label.setFont(instr2_font)
        ingreso_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        ingreso_label.setStyleSheet("color: #8B0000;")
        # label de dinero actual
        dinero_label = QLabel(f"${self.user.dinero_actual}")
        dinero_label.setFont(instr2_font)
        dinero_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        dinero_label.setStyleSheet("color: #8B0000;")
        #barra
        barra = QProgressBar()
        barra.setMinimum(0)
        barra.setMaximum(self.user.dinero_actual)
        barra.setValue(self.user.dinero_actual)
        barra.setStyleSheet(progressBar_style)
        # widgets para barra de gasto
        gasto_frame = QFrame()
        gasto_frame.setFrameShape(QFrame.Shape.Box)
        gasto_frame.setLineWidth(4)
        gasto_frame.setLayout(QHBoxLayout())
        #label de ingresos
        gasto_label = QLabel("Gastos")
        gasto_label.setFont(instr2_font)
        gasto_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        gasto_label.setStyleSheet("color: #8B0000;")
        # label de dinero actual
        dinero2_label = QLabel(f"$0") #agregar la cantidad total de gastos
        dinero2_label.setFont(instr2_font)
        dinero2_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        dinero2_label.setStyleSheet("color: #8B0000;")
        #barra
        barra2 = QProgressBar()
        barra2.setMinimum(0)
        barra2.setMaximum(self.user.dinero_actual)
        barra2.setValue(0) #agregar el total de los gastos
        barra2.setStyleSheet(progressBar_style)
        # label de instrucciones
        instr1_label = QLabel("Selecciona una opción")
        instr1_label.setFont(instr_font)
        instr1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instr1_label.setStyleSheet("color: #191970;")
        # boton de opcion uno
        boton_opt_1 = QPushButton("1. Ingresar gastos")
        boton_opt_1.setFont(instr_font)
        boton_opt_1.setMinimumWidth(875)
        boton_opt_1.setStyleSheet(back_button_style)
        boton_opt_1.clicked.connect(self.open_opt_1_window)
        boton_opt_1.setFixedHeight(250)
        #boton de opcion dos
        boton_opt_2 = QPushButton("2. Ver análisis de gastos")
        boton_opt_2.setFont(instr_font)
        boton_opt_2.setStyleSheet(back_button_style)
        boton_opt_2.setFixedHeight(250)
        boton_opt_2.clicked.connect(self.open_opt_2_window)
        #boton de opcion tres
        boton_opt_3 = QPushButton("3. Predecir gastos")
        boton_opt_3.setFont(instr_font)
        boton_opt_3.setStyleSheet(back_button_style)
        boton_opt_3.setFixedHeight(250)
        boton_opt_3.clicked.connect(self.open_opt_3_window)
        # agregamos los widgets al layout
        self.main_menu_layout.addWidget(main_frame)
        main_frame.layout().addWidget(inicio_frame)
        inicio_frame.layout().addWidget(saludos_label)
        inicio_frame.layout().addWidget(fecha_label)
        main_frame.layout().addWidget(title_frame)
        title_frame.layout().addWidget(title_label)
        main_frame.layout().addWidget(dinero_frame)
        dinero_frame.layout().addWidget(ingreso_label)
        dinero_frame.layout().addWidget(dinero_label)
        main_frame.layout().addWidget(barra)
        main_frame.layout().addWidget(gasto_frame)
        gasto_frame.layout().addWidget(gasto_label)
        gasto_frame.layout().addWidget(dinero2_label)
        main_frame.layout().addWidget(barra2)
        main_frame.layout().addWidget(instr1_label)
        main_frame.layout().addWidget(boton_opt_1)
        main_frame.layout().addWidget(boton_opt_2)
        main_frame.layout().addWidget(boton_opt_3)
        #self.setCentralWidget(self.main_menu_widget)

    def open_opt_1_window(self):
        self.opt1_window = Opt1Window(self,self.user)
        self.opt1_window.show()
        self.hide()

    def open_opt_2_window(self):
        self.opt_2_window = Opt2Window(self)
        self.opt_2_window.show()
        self.hide()

    def open_opt_3_window(self):
        self.opt_3_window = Opt3Window(self)
        self.opt_3_window.show()
        self.hide()

class Opt1Window(QWidget):
    def __init__(self, main_menu_window: startWindow,user:cls.Usuario):
        super().__init__()
        self.main_menu_window = main_menu_window
        self.user = user
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

        welcome1_label = QLabel('Ingresa los siguientes datos')
        welcome1_label.setStyleSheet('color: #191970;')
        welcome1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome1_label.setFont(title_font)

        arti_label = QLabel("Nombre de la compra: ")
        arti_label.setStyleSheet('color: #191970;')
        arti_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        arti_label.setFont(instr2_font)

        self.lineEdit_nombre = QLineEdit()
        self.lineEdit_nombre.setFixedHeight(60)
        self.lineEdit_nombre.setStyleSheet(border_style)
        self.lineEdit_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_nombre.setReadOnly(False)

        second_frame = QFrame()
        second_frame.setFrameShape(QFrame.Shape.Box) 
        second_frame.setLineWidth(1)
        second_frame.setLayout(QHBoxLayout())
        second_frame.setStyleSheet('color: #2F2F2F;')

        third_frame = QFrame()
        third_frame.setFrameShape(QFrame.Shape.Box) 
        third_frame.setLineWidth(1)
        third_frame.setLayout(QVBoxLayout())
        third_frame.setStyleSheet('color: #2F2F2F;')

        fourth_frame = QFrame()
        fourth_frame.setFrameShape(QFrame.Shape.Box) 
        fourth_frame.setLineWidth(1)
        fourth_frame.setLayout(QVBoxLayout())
        fourth_frame.setStyleSheet('color: #2F2F2F;')

        categ_label = QLabel("Selecciona una categoría: ")
        categ_label.setStyleSheet('color: #191970;')
        categ_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        categ_label.setFont(instr2_font)

        self.categ_options = QComboBox(self)
        self.categ_options.setFont(instr2_font)
        self.categ_options.setStyleSheet('border: 2px solid #7e562e')
        self.categ_options.addItem('-- Selecciona --')
        self.categ_options.addItem('Comida')
        self.categ_options.addItem('Ropa')
        self.categ_options.addItem('Transporte')
        self.categ_options.addItem('Salud')
        self.categ_options.addItem('Entretenimiento')
        self.categ_options.addItem('Desarrollo Personal')
        self.categ_options.addItem('Otro')
        self.categ_options.setStyleSheet(qcomboBox_style)
        
        import_label = QLabel("Selecciona un nivel de importancia: ")
        import_label.setStyleSheet('color: #191970;')
        import_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        import_label.setFont(instr2_font)

        self.import_options = QComboBox(self)
        self.import_options.setFont(instr2_font)
        self.import_options.setStyleSheet('border: 2px solid #7e562e')
        self.import_options.addItem('0')
        self.import_options.addItem('1')
        self.import_options.addItem('2')
        self.import_options.addItem('3')
        self.import_options.addItem('4')
        self.import_options.addItem('5')
        self.import_options.setStyleSheet(qcomboBox_style)
        
        precio_label = QLabel("Ingresa el precio pagado: ")
        precio_label.setStyleSheet('color: #191970;')
        precio_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        precio_label.setFont(instr2_font)

        self.lineEdit_precio = QLineEdit()
        self.lineEdit_precio.setStyleSheet(border_style)
        self.lineEdit_precio.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_precio.setReadOnly(False)

        finish_button = QPushButton("Registrar")
        finish_button.setStyleSheet('border: 10px solid #4B4B4B')
        finish_button.setStyleSheet(button_style)
        finish_button.clicked.connect(self.addGastoProcess)
        finish_button.setFont(instr_font)

        restart_button = QPushButton("Borrar selecciones")
        restart_button.setStyleSheet(button_style)
        restart_button.clicked.connect(self.restartSelection)
        restart_button.setFont(instr_font)

        # regresar al menu principal
        return_button = QPushButton("Regresar al menú principal")
        return_button.setStyleSheet(back_button_style)
        return_button.clicked.connect(self.returnToMainMenu)
        return_button.setFont(instr_font)

        # adding widgets
        menu1_layout.addWidget(main_frame)
        main_frame.layout().addWidget(title_frame)
        title_frame.layout().addWidget(welcome1_label)
        main_frame.layout().addWidget(arti_label)
        main_frame.layout().addWidget(self.lineEdit_nombre)
        main_frame.layout().addWidget(second_frame)
        second_frame.layout().addWidget(third_frame)
        third_frame.layout().addWidget(categ_label)
        third_frame.layout().addWidget(self.categ_options)
        second_frame.layout().addWidget(fourth_frame)
        fourth_frame.layout().addWidget(import_label)
        fourth_frame.layout().addWidget(self.import_options)
        main_frame.layout().addWidget(precio_label)
        main_frame.layout().addWidget(self.lineEdit_precio)
        main_frame.layout().addWidget(finish_button)
        main_frame.layout().addWidget(restart_button)
        main_frame.layout().addWidget(return_button)

    def addGastoProcess(self):
        id_gasto = len(gastos_list)
        articulo = self.lineEdit_nombre.text()
        id_user = self.user.id
        categoria = self.categ_options.currentText()
        precio = self.lineEdit_precio.text()
        importancia = self.categ_options.currentText()
        fecha_default = datetime.now()
        fecha_formateada = fecha_default.strftime("%d-%m-%Y")
        temp_gasto = cls.Gasto(id_gasto,id_user,articulo,precio,importancia,categoria,fecha_formateada)
        gastos_list.append(temp_gasto)
        src.add_new_gasto_to_csv(temp_gasto)

    def restartSelection(self):
        self.lineEdit_nombre.clear()
        self.categ_options.setCurrentIndex(0)
        self.import_options.setCurrentIndex(0)
        self.lineEdit_precio.clear()

    def returnToMainMenu(self):
        self.main_menu_window.show()
        self.hide()

class Opt2Window(QWidget):
    def __init__(self, main_menu_window:startWindow):
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
        return_button.setStyleSheet(back_button_style)
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

class Opt3Window(QWidget):
    def __init__(self,main_menu_window : startWindow):
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
        return_button.setStyleSheet(back_button_style)
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
################ VARIABLES IMPORTANTES #################
user_cont = 0
gastos_cont = 0
users_list = []
gastos_list = []
border_style = """
QLineEdit {
    border: 2px solid #4B4B4B; /* Color del borde */
    border-radius: 5px;       /* Esquinas redondeadas */
    padding: 10px;            /* Espacio interno */
    font-size: 16px;          /* Tamaño de la fuente */
}
"""

button_style = """
QPushButton {
    background-color: #8B0000; /* Color de fondo */
    color: white;              /* Color del texto */
    border: 2px solid #4B4B4B; /* Borde del botón */
    border-radius: 10px;       /* Bordes redondeados */
    padding: 10px;             /* Espacio interno */
    font-size: 16px;           /* Tamaño de la fuente */
    font-weight: bold;         /* Negrita */
    text-align: center;        /* Alinear el texto al centro */
    text-decoration: none;     /* Sin subrayado */
}
QPushButton:hover {
    background-color: #A52A2A; /* Color de fondo al pasar el ratón por encima */
    border: 2px solid #191970; /* Cambiar borde al color #191970 */
    color: #FFD700;            /* Cambiar el color del texto al color dorado */
}
QPushButton:pressed {
    background-color: #5C0000; /* Color de fondo al presionar */
    border: 2px solid #191970; /* Cambiar borde al color #191970 */
}
"""

back_button_style = """
QPushButton {
    background-color: #191970; /* Color de fondo */
    color: white;              /* Color del texto */
    border: 2px solid #4B4B4B; /* Borde del botón */
    border-radius: 10px;       /* Bordes redondeados */
    padding: 10px;             /* Espacio interno */
    font-size: 16px;           /* Tamaño de la fuente */
    font-weight: bold;         /* Negrita */
    text-align: center;        /* Alinear el texto al centro */
    text-decoration: none;     /* Sin subrayado */
}
QPushButton:hover {
    background-color: #1E90FF; /* Color de fondo al pasar el ratón por encima */
    border: 2px solid #8B0000; /* Cambiar borde al color #8B0000 */
    color: #FFD700;            /* Cambiar el color del texto al color dorado */
}
QPushButton:pressed {
    background-color: #000080; /* Color de fondo al presionar */
    border: 2px solid #8B0000; /* Cambiar borde al color #8B0000 */
}
"""

date_edit_style = """
    QDateEdit {
        font-size: 20px;  /* Tamaño de letra */
        color: #333333;  /* Color del texto */
        background-color: #f2f2f2;  /* Color de fondo */
        border: 1px solid #cccccc;  /* Borde */
        padding: 5px;  /* Espaciado interno */
        border-radius: 10px;  /* Bordes redondeados */
    }
    QDateEdit::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 20px;  /* Ancho del botón desplegable */
        border-left-width: 1px;
        border-left-color: darkgray;
        border-left-style: solid;  /* Estilo del borde del botón desplegable */
        border-top-right-radius: 3px;  /* Bordes redondeados */
        border-bottom-right-radius: 3px;  /* Bordes redondeados */
    }
    QDateEdit::down-arrow {
        width: 10px;
        height: 10px;
    }
    QDateEdit QAbstractItemView {
        font-size: 18px;  /* Tamaño de letra de la vista del calendario */
        color: #333333;  /* Color del texto de la vista del calendario */
        background-color: #ffffff;  /* Color de fondo de la vista del calendario */
        selection-background-color: #009688;  /* Color de fondo de la selección */
        selection-color: #ffffff;  /* Color del texto de la selección */
    }
"""

qcomboBox_style = """
    QComboBox {
        font-size: 20px;  /* Tamaño de letra */
        color: #333333;  /* Color del texto */
        background-color: #f2f2f2;  /* Color de fondo */
        border: 1px solid #cccccc;  /* Borde */
        padding: 5px;  /* Espaciado interno */
        border-radius: 10px;  /* Bordes redondeados */
    }
    QComboBox::drop-down {
        subcontrol-origin: padding;
        subcontrol-position: top right;
        width: 20px;  /* Ancho del botón desplegable */
        border-left-width: 1px;
        border-left-color: darkgray;
        border-left-style: solid;  /* Estilo del borde del botón desplegable */
        border-top-right-radius: 3px;  /* Bordes redondeados */
        border-bottom-right-radius: 3px;  /* Bordes redondeados */
    }
    QComboBox::down-arrow {
        width: 10px;
        height: 10px;
    }
    QComboBox QAbstractItemView {
        font-size: 18px;  /* Tamaño de letra de la vista desplegable */
        color: #333333;  /* Color del texto de la vista desplegable */
        background-color: #ffffff;  /* Color de fondo de la vista desplegable */
        selection-background-color: #009688;  /* Color de fondo de la selección */
        selection-color: #ffffff;  /* Color del texto de la selección */
    }
"""

title_style = """
    QLabel {
        font-size: 36px;  /* Tamaño de letra grande */
        font-weight: bold;  /* Negrita */
        color: #8B0000;  /* Color del texto rojo */
        padding: 20px;  /* Espaciado interno */
        background-color: #ffffff;  /* Color de fondo blanco */
        border-radius: 15px;  /* Bordes redondeados */
        border: 3px solid #8B0000;  /* Borde rojo */
        text-align: center;  /* Alinear al centro */
    }
    QLabel:hover {
        background-color: #f0f0f0;  /* Color de fondo al pasar el mouse */
    }
"""

progressBar_style = """
QProgressBar {
    border: 2px solid #4B4B4B;
    border-radius: 10px;
    text-align: center;
    font-size: 16px;
    color: #8B0000;
}
QProgressBar::chunk {
    background-color: #8B0000;
    width: 20px;
}
"""

################ MAIN ####################

main_menu_window = startWindow()
main_menu_window.show()
deskTopApp.exec()       