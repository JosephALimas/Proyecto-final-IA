import datetime
import pandas as pd
import csv


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
                self.ingresar_gastos()
            elif opcion == '2':
                self.ingresar_ingresos()
            elif opcion == '3':
                self.analizar_gastos()
            elif opcion == '4':
                self.predecir_gastos()
            elif opcion == '5':
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    buddy = FinancialBuddy()
    buddy.menu()
