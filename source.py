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
            writer.writerow(["id","articulo", "id_user","categoria","precio","importancia","fecha"]) # escribimos la primer linea del 
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
        writer.writerow([temp_user.id, temp_user.nombre, temp_user.contraseña, temp_user.edad, temp_user.fecha_nacimiento,temp_user.ingreso_mensual,temp_user.dinero_actual])

def csv_user_to_obj(users_list):
    userCSV = pd.read_csv('users.csv')
    for index in range(0,userCSV.shape[0],1):
        tempUser = cls.Usuario(userCSV['id'][index],userCSV['nombre'][index],userCSV['contrasena'][index],userCSV['edad'][index],userCSV['fecha_nacimiento'][index],userCSV['ingreso_mensual'][index],userCSV['dinero_actual'][index])
        users_list.append(tempUser)
    return users_list

def csv_gastos_to_obj(gastos_list):
    gastosCSV = pd.read_csv('gastos.csv')
    for index in range(0, gastosCSV.shape[0],1):
        tempGasto = cls.Gasto(gastosCSV['id'][index],gastosCSV['articulo'][index],gastosCSV['id_user'][index],
                              gastosCSV['categoria'][index],gastosCSV['precio'][index],gastosCSV['importancia'][index],
                              gastosCSV['fecha'][index])
        gastos_list.append(tempGasto)
    return gastos_list

def add_new_gasto_to_csv(temp_gasto = cls.Gasto):
    with open('gastos.csv', 'a', newline = "") as gastosCSV:
        writer = csv.writer(gastosCSV)
        writer.writerow([temp_gasto.id_gasto,temp_gasto.articulo,temp_gasto.id_user,temp_gasto.categoria,temp_gasto.precio,temp_gasto.importancia,temp_gasto.fecha])

