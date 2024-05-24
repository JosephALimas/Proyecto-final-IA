import datetime
import pandas as pd
import csv

class Gasto:
    def __init__(self, articulo = "", precio = 0.0, importancia = 0, categoria = ""):
        self.arituclo = articulo
        self.precio = precio
        self.importancia = importancia
        self.categoria = categoria


