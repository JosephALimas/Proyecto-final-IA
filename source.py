import clases as cls
import os
import datetime
import csv
import pandas as pd

##### functions ########
def gastos_file_checkup():
    path = "gastos.csv" # la ruta relativa del archivo csv
    check_fie = os.path.isfile(path) # con la biblioteca OS buscamos que exista el archivo
    if check_fie: # comprobamos si ya está el archivo en nuestra computadora
        pass
    else: # en caso de que no esté el archivo lo creamos
        with open("gastos.csv", "w", newline = '') as inventario: # abrimos el archivo
            writer = csv.writer(inventario) # creaomos un objeto writer para poder escribir en el archivo
            writer.writerow(["id","articulo", "categoria","precio","importancia","fecha"]) # escribimos la primer linea del 
            # archivo que van a ser los encabezados de la tabla

def users_file_checkup():
    path = "users.csv" # la ruta relativa del archivo csv
    check_fie = os.path.isfile(path) # con la biblioteca OS buscamos que exista el archivo
    if check_fie: # comprobamos si ya está el archivo en nuestra computadora
        pass
    else: # en caso de que no esté el archivo lo creamos
        with open("users.csv", "w", newline = '') as inventario: # abrimos el archivo
            writer = csv.writer(inventario) # creaomos un objeto writer para poder escribir en el archivo
            writer.writerow(["id","nombre","edad","fecha_nacimiento","ingreso_mensual"]) # escribimos la primer linea del 
            # archivo que van a ser los encabezados de la tabla
#def csv_gastos_to_obj()