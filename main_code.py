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
################ CLASES ##################
class MainMenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance UP")
        self.setMinimumSize(500,300)
        self.main_menu_widget = QWidget(self)
        self.main_menu_widget.setStyleSheet("background-color: #e0c49d;")
        self.main_menu_layout = QVBoxLayout(self.main_menu_widget)
        # inicialización de widgets
        # frame principal
        main_frame = QFrame()
        main_frame.setFrameShape(QFrame.Shape.Box)
        main_frame.setLineWidth(4)
        main_frame.setLayout(QVBoxLayout())
        main_frame.setStyleSheet('color: #3f2b17')
        # frame para el titulo
        title_frame = QFrame()
        title_frame.setFrameShape(QFrame.Shape.Box)
        title_frame.setLineWidth(4)
        title_frame.setLayout(QHBoxLayout())
        # label de titulo
        title_label = QLabel("Finance UP")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #804415;")
        # label de instrucciones
        instr1_label = QLabel("Selecciona una opción")
        instr1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        instr1_label.setStyleSheet("color: #804415;")

        # agregamos los widgets al layout
        self.main_menu_layout.addWidget(main_frame)
        main_frame.layout().addWidget(title_frame)
        title_frame.layout().addWidget(title_label)
        main_frame.layout().addWidget(instr1_label)

        self.setCentralWidget(self.main_menu_widget)





############## VARIABLES PRINCIPALES ##################
deskTopApp = QApplication([])

################ MAIN ####################

main_menu_window = MainMenuWindow()
main_menu_window.show()
deskTopApp.exec()