import clases as cls
import os
import datetime
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression


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
    path = "user.csv" # la ruta relativa del archivo csv
    check_fie = os.path.isfile(path) # con la biblioteca OS buscamos que exista el archivo
    if check_fie: # comprobamos si ya está el archivo en nuestra computadora
        pass
    else: # en caso de que no esté el archivo lo creamos
        with open("user.csv", "w", newline = '') as inventario: # abrimos el archivo
            writer = csv.writer(inventario) # creaomos un objeto writer para poder escribir en el archivo
            writer.writerow(["id","nombre","contrasena","edad","fecha_nacimiento","ingreso_mensual"]) # escribimos la primer linea del 
            # archivo que van a ser los encabezados de la tabla

def add_new_user_to_csv(temp_user = cls.Usuario):
    with open('user.csv','a', newline = "") as usersCSV:
        writer = csv.writer(usersCSV)
        writer.writerow([temp_user.id, temp_user.nombre, temp_user.contraseña, temp_user.edad, temp_user.fecha_nacimiento,temp_user.ingreso_mensual,temp_user.dinero_actual])

def csv_user_to_obj(users_list):
    userCSV = pd.read_csv('user.csv')
    for index in range(0,userCSV.shape[0],1):
        tempUser = cls.Usuario(userCSV['id'][index],userCSV['nombre'][index],userCSV['contrasena'][index],userCSV['edad'][index],userCSV['fecha_nacimiento'][index],userCSV['ingreso_mensual'][index],float(userCSV['dinero_actual'][index]))
        users_list.append(tempUser)
    return users_list

def csv_gastos_to_obj(gastos_list):
    gastosCSV = pd.read_csv('gastos.csv')
    for index in range(0, gastosCSV.shape[0],1):
        tempGasto = cls.Gasto(gastosCSV['id'][index],gastosCSV['id_user'][index],gastosCSV['articulo'][index],
                              float(gastosCSV['precio'][index]),int(gastosCSV['importancia'][index]),gastosCSV['categoria'][index],
                              gastosCSV['fecha'][index])
        gastos_list.append(tempGasto)
    return gastos_list

def add_new_gasto_to_csv(temp_gasto = cls.Gasto):
    with open('gastos.csv', 'a', newline = "") as gastosCSV:
        writer = csv.writer(gastosCSV)
        writer.writerow([temp_gasto.id_gasto,temp_gasto.articulo,temp_gasto.id_user,temp_gasto.categoria,temp_gasto.precio,temp_gasto.importancia,temp_gasto.fecha])

def analizarGastos(lista_gastos, user :cls.Usuario):
    if not lista_gastos:
        print("No hay gastos para analizar.") # se tiene que cambiar con la GUI
        return

    print("\nAnálisis de Gastos:")
    for gasto in lista_gastos:
        print(f"Nombre: {gasto.articulo}, Categoría: {gasto.categoria}, Importancia: {gasto.importancia}, Cantidad: {gasto.precio}, Fecha: {gasto.fecha}")

    categorias = [gasto.categoria for gasto in lista_gastos]
    categoria_mas_gastos = max(set(categorias), key=categorias.count)
    print(f"\nCategoría con más gastos: {categoria_mas_gastos}")

    mayor_gasto = max(lista_gastos, key=obtener_precio)
    menor_gasto = min(lista_gastos, key=obtener_precio)
    print(f"Mayor gasto: {mayor_gasto.articulo} - {mayor_gasto.precio}")
    print(f"Menor gasto: {menor_gasto.articulo} - {menor_gasto.precio}")

    total_ingresos = user.dinero_actual ##### A CAMBIAR LA SUMA DE INGRESOS
    total_gastos = sum(float(gasto.precio) for gasto in lista_gastos)
    balance = total_ingresos - total_gastos
    print(f"\nTotal de ingresos mensuales: {total_ingresos}")
    print(f"Total de gastos: {total_gastos}")
    print(f"Balance mensual: {balance}")
    print(f"Monto actual disponible: {user.dinero_actual}")

    #graficarGastos(lista_gastos,user)

def obtener_precio(gasto):
    return gasto.precio

def graficarGastos(lista_gastos, user):
    gastos_por_importancia = [0] * 6
    cantidad_por_categoria = {}

    for gasto in lista_gastos:
        # Por importancia
        if gasto.importancia >= 0 and gasto.importancia < 6:
            gastos_por_importancia[gasto.importancia] += gasto.precio
        # Por categoría
        if gasto.categoria in cantidad_por_categoria:
            cantidad_por_categoria[gasto.categoria] += gasto.precio
        else:
            cantidad_por_categoria[gasto.categoria] = gasto.precio

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('Análisis de Gastos', fontsize=16)

    # Graficar los gastos totales por importancia
    axs[0, 0].bar(range(6), gastos_por_importancia, color='darkred')
    axs[0, 0].set_xlabel('Importancia (0-5)')
    axs[0, 0].set_ylabel('Cantidad de Gasto')
    axs[0, 0].set_title('Gasto Total por Importancia')
    axs[0, 0].set_xticks(range(6))

    # Graficar los gastos totales por categoría
    axs[0, 1].bar(cantidad_por_categoria.keys(),
                    cantidad_por_categoria.values(), color='red')
    axs[0, 1].set_xlabel('Categoría')
    axs[0, 1].set_ylabel('Cantidad Total')
    axs[0, 1].set_title('Total de Gastos por Categoría')

    # Graficar la proporción de gastos por categoría
    axs[1, 0].pie(cantidad_por_categoria.values(),
                    labels=cantidad_por_categoria.keys(), autopct='%1.1f%%')
    axs[1, 0].set_title('Proporción de Gastos por Categoría')

    # Graficar los gastos a lo largo del tiempo
    fechas_precios_ordenados = sorted(zip([gasto.fecha for gasto in lista_gastos], [
                                        gasto.precio for gasto in lista_gastos]))
    fechas_ordenadas = [fecha for fecha, _ in fechas_precios_ordenados]
    precios_ordenados = [precio for _, precio in fechas_precios_ordenados]
    axs[1, 1].plot(fechas_ordenadas, precios_ordenados,
                    marker='o', color='#4169E1')
    axs[1, 1].set_xlabel('Fecha')
    axs[1, 1].set_ylabel('Cantidad de Gasto')
    axs[1, 1].set_title('Gastos a lo largo del tiempo')
    axs[1, 1].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()

def prediccion_de_gastos(lista_gastos,user : cls.Usuario):
    if len(lista_gastos) < 2:
        print("No hay suficientes datos para realizar la predicción.")
        return

    # Preparar los datos para la regresión
    fechas = [gasto.fecha for gasto in lista_gastos]
    precios = [gasto.precio for gasto in lista_gastos]

    # Convertir las fechas a un formato numérico para la regresión
    fechas_ordinal = np.array([fecha.toordinal()
                                for fecha in fechas]).reshape(-1, 1)
    precios = np.array(precios).reshape(-1, 1)

    # Inicializar y entrenar el modelo de regresión lineal
    model = LinearRegression()
    model.fit(fechas_ordinal, precios)

    # Solicitar la fecha para la predicción
    fecha_prediccion = input(
        "Ingrese la fecha para la predicción (dd-mm-yyyy): ")
    fecha_prediccion = datetime.strptime(
        fecha_prediccion, "%d-%m-%Y").toordinal()

    # Realizar predicción
    precio_predicho = model.predict([[fecha_prediccion]])[0][0]
    print(f"Para la fecha {datetime.fromordinal(fecha_prediccion).strftime('%d-%m-%Y')}, el gasto predicho es: ${precio_predicho:.2f}")

    # Recomendaciones y alertas
    total_ingresos = user.dinero_actual ##### SE TIENE QUE CAMBIAR
    if precio_predicho > total_ingresos:
        print("¡Alerta! Estás gastando más de lo que ingresas mensualmente.")
    elif precio_predicho > 0.5 * total_ingresos:
        print("Cuidado, has rebasado más del 50% de tus ingresos mensuales.")
    else:
        print("Vas bien, tu gasto predicho está dentro de un rango manejable.")

    # Graficar la regresión lineal
    plt.scatter(fechas_ordinal, precios,
                color='blue', label='Datos de Gastos')
    plt.plot(fechas_ordinal, model.predict(fechas_ordinal),
                color='red', label='Regresión Lineal')
    plt.scatter([fecha_prediccion], [precio_predicho],
                color='green', marker='x', s=100, label='Predicción')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad de Gasto')
    plt.title('Predicción de Gastos')
    plt.legend()
    plt.show()

def modify_precio_csv(user : cls.Usuario):
    df = pd.read_csv('user.csv')

    # Modificar el valor de dinero_actual para el usuario con el id dado
    df.loc[df['id'] == user.id, 'dinero_actual'] = user.dinero_actual

    # Guardar los cambios de vuelta en el archivo CSV
    df.to_csv('user.csv', index=False)
    print("prueba")

