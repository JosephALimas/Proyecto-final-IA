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
################ MAIN ####################

main_menu_window = MainMenuWindow()
main_menu_window.show()
deskTopApp.exec()