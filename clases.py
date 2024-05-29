import datetime
import pandas as pd
import csv

class Usuario:
    def __init__(self,id = 0,nombre = "",contraseña = "",edad = 0,fecha_nacimiento = datetime, ingreso_mensual = "", dinero_actual = 0.0):
        self.id = id
        self.nombre = nombre
        self.contraseña = contraseña
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.ingreso_mensual = ingreso_mensual
        self.dinero_actual = dinero_actual

class Gasto:
    def __init__(self, id = 0,id_user = 0,articulo = "", precio = 0.0, importancia = 0, categoria = "" ,fecha = datetime):
        self.id_gasto = id
        self.articulo = articulo
        self.id_user = id_user
        self.categoria = categoria
        self.precio = precio
        self.importancia = importancia
        self.fecha = fecha
