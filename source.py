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
            writer.writerow(["id","nombre","contrasena","edad","fecha_nacimiento","ingreso_mensual"]) # escribimos la primer linea del 
            # archivo que van a ser los encabezados de la tabla

def add_new_user_to_csv(temp_user = cls.Usuario):
    with open('users.csv','a', newline = "") as usersCSV:
        writer = csv.writer(usersCSV)
        writer.writerow([temp_user.id, temp_user.nombre, temp_user.contraseña, temp_user.edad, temp_user.fecha_nacimiento,temp_user.ingreso_mensual])

def csv_user_to_obj(users_list):
    userCSV = pd.read_csv('users.csv')
    for index in range(0,userCSV.shape[0],1):
        tempUser = cls.Usuario(userCSV['id'][index],userCSV['nombre'][index],userCSV['contrasena'][index],userCSV['edad'][index],userCSV['fecha_nacimiento'][index],userCSV['ingreso_mensual'][index])
        users_list.append(tempUser)
    return users_list

#def csv_gastos_to_obj()