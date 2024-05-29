import datetime
import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime


class Usuario:
    def __init__(self, id=0, nombre="", contraseña="", edad=0, fecha_nacimiento=datetime, ingreso_mensual=""):
        self.id = id
        self.nombre = nombre
        self.contraseña = contraseña
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.ingreso_mensual = ingreso_mensual


class Gasto:
    def __init__(self, id=0, id_user=0, articulo="", precio=0.0, importancia=0, categoria="", fecha=datetime):
        self.id_gasto = id
        self.articulo = articulo
        self.id_user = id_user
        self.categoria = categoria
        self.precio = precio
        self.importancia = importancia
        self.fecha = fecha


class FinancialBuddy:
    def __init__(self):
        self.gastos = []
        self.ingresos = []
        self.monto_actual = 0.0

    def obtener_precio(self, gasto):
        return gasto.precio

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Ingresar Gastos")
            print("2. Ingresos")
            print("3. Analizar Gastos")
            print("4. Predecir Gastos")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.ingresarGastos()
            elif opcion == '2':
                self.ingresarIngresos()
            elif opcion == '3':
                self.analizarGastos()
            elif opcion == '4':
                self.predecirGastos()
            elif opcion == '5':
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    def ingresarGastos(self):
        nombre = input("Nombre del gasto: ")
        categoria = input(
            "Categoría (comida, ropa, transporte, salud, entretenimiento, desarrollo personal, otro): ")
        importancia = int(input("Importancia (0-5): "))
        cantidad = float(input("Cantidad: "))
        fecha = input("Fecha (dd-mm-yyyy): ")
        fecha = datetime.strptime(fecha, "%d-%m-%Y")

        nuevo_gasto = Gasto(articulo=nombre, categoria=categoria,
                            importancia=importancia, precio=cantidad, fecha=fecha)
        self.gastos.append(nuevo_gasto)

        print("Gasto ingresado exitosamente.")

    def ingresarIngresos(self):
        while True:
            tipo_ingreso = input(
                "Ingrese el tipo de ingreso (mensual/actual): ").strip().lower()
            if tipo_ingreso not in ["mensual", "actual"]:
                print("Tipo de ingreso no válido. Por favor, intente de nuevo.")
                continue

            ingreso = float(input("Ingrese el monto: "))
            if tipo_ingreso == "mensual":
                self.ingresos.append(ingreso)
            elif tipo_ingreso == "actual":
                self.monto_actual += ingreso

            print("Ingreso ingresado exitosamente.")
            break

    def analizar_gastos(self):
        if not self.gastos:
            print("No hay gastos para analizar.")
            return

        print("\nAnálisis de Gastos:")
        for gasto in self.gastos:
            print(f"Nombre: {gasto.articulo}, Categoría: {gasto.categoria}, Importancia: {
                  gasto.importancia}, Cantidad: {gasto.precio}, Fecha: {gasto.fecha}")

        categorias = [gasto.categoria for gasto in self.gastos]
        categoria_mas_gastos = max(set(categorias), key=categorias.count)
        print(f"\nCategoría con más gastos: {categoria_mas_gastos}")

        mayor_gasto = max(self.gastos, key=self.obtener_precio)
        menor_gasto = min(self.gastos, key=self.obtener_precio)
        print(f"Mayor gasto: {mayor_gasto.articulo} - {mayor_gasto.precio}")
        print(f"Menor gasto: {menor_gasto.articulo} - {menor_gasto.precio}")

        total_ingresos = sum(self.ingresos)
        total_gastos = sum(gasto.precio for gasto in self.gastos)
        balance = total_ingresos - total_gastos
        print(f"\nTotal de ingresos mensuales: {total_ingresos}")
        print(f"Total de gastos: {total_gastos}")
        print(f"Balance mensual: {balance}")
        print(f"Monto actual disponible: {self.monto_actual}")

        self.graficar_gastos()

    def graficarGastos(self):
        categorias = [gasto.categoria for gasto in self.gastos]
        precios = [gasto.precio for gasto in self.gastos]

        fig, axs = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle('Análisis de Gastos', fontsize=16)

        # Gráfico de barras
        axs[0, 0].barh(categorias, precios, color='#4169E1')  # Azul claro
        axs[0, 0].set_xlabel('Cantidad de Gasto')
        axs[0, 0].set_ylabel('Categoría')
        axs[0, 0].set_title('Distribución de Gastos por Categoría')

        # Gráfico de barras
        cantidad_por_categoria = {}
        for gasto in self.gastos:
            if gasto.categoria in cantidad_por_categoria:
                cantidad_por_categoria[gasto.categoria] += gasto.precio
            else:
                cantidad_por_categoria[gasto.categoria] = gasto.precio

        axs[0, 1].bar(cantidad_por_categoria.keys(),
                      cantidad_por_categoria.values(), color='red')  # Rojo
        axs[0, 1].set_xlabel('Categoría')
        axs[0, 1].set_ylabel('Cantidad Total')
        axs[0, 1].set_title('Total de Gastos por Categoría')

        # Gráfico de pastel
        axs[1, 0].pie(cantidad_por_categoria.values(), labels=cantidad_por_categoria.keys(
        ), autopct='%1.1f%%', colors=['blue', 'gray', 'blue', 'red'])
        axs[1, 0].set_title('Proporción de Gastos por Categoría')

        # Gráfico de líneas por orden de fecha
        fechas_precios_ordenados = sorted(
            zip([gasto.fecha for gasto in self.gastos], precios))
        fechas_ordenadas = [fecha for fecha, _ in fechas_precios_ordenados]
        precios_ordenados = [precio for _, precio in fechas_precios_ordenados]

        axs[1, 1].plot(fechas_ordenadas, precios_ordenados,
                       marker='o', color='#4169E1')  # Azul claro
        axs[1, 1].set_xlabel('Fecha')
        axs[1, 1].set_ylabel('Cantidad de Gasto')
        axs[1, 1].set_title('Gastos a lo largo del tiempo')
        axs[1, 1].tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    buddy = FinancialBuddy()
    buddy.menu()
