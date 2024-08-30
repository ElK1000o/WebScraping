from os import system
from .manejo_urls import agregar_url, generar_urls, leer_lista_urls, listar_urls, eliminar_url
from .scrap import iniciar_scraping
from .manejo_data import guardar_datos, limpiar_programa
from .buscar import agregar_clave_json, agregar_seccion_html, eliminar_clave_json, eliminar_seccion_html
from .cargar_db import guardar_datos_bbdd
from .almacenamiento import data

def menu():
    while True:
        system("cls")
        print("----------------------")
        print("    MENÚ PRINCIPAL   ")
        print("----------------------\n")
        print("1. Agregar (URL - Sección - Clave).")
        print("2. Listar URLs.")
        print("3. Eliminar (URL - Sección - Clave).")
        print("4. Iniciar Scraping.")
        print("5. Guardar Datos.")
        print("6. Limpiar Programa.")
        print("7. Salir.")
        
        try:
            op = int(input("\nIngrese numéricamente la opción del menú: "))
            assert 1 <= op <= 7
            
            if op == 1:
                agregar()
            elif op == 2:
                listar_urls()
            elif op == 3:
                eliminar()
            elif op == 4:
                iniciar_scraping()
            elif op == 5:
                guardar()
            elif op == 6:
                limpiar_programa()
            elif op == 7:
                salir()
        except (ValueError, AssertionError):
            print("Ingrese correctamente el valor.")
            system("pause")

def agregar():
    while True: 
        system("cls")
        print("---------------")
        print("    AGREGAR   ")
        print("---------------\n")
        print("1. Agregar URL / URLs")
        print("2. Agregar Sección HTML.")
        print("3. Agregar Clave JSON.")
        print("\n *(Enter para volver atrás)*")
        try:
            op = input("\nIngrese numéricamente la opción: ")
            assert op in ('1', '2', '3', '')
            if op == '1':
                agregar_urls()
            elif op == '2':
                agregar_seccion_html()
            elif op == '3':
                agregar_clave_json()
            elif op == '':
                menu()
        except (ValueError, AssertionError):
            print("\nIngrese correctamente el valor.\n")
            system("pause")

def eliminar():
    while True:
        system("cls")
        print("----------------")
        print("    ELIMINAR    ")
        print("----------------\n")
        print("1. Eliminar URL.")
        print("2. Eliminar Sección HTML.")
        print("3. Eliminar Clave JSON.")
        print("\n *(Enter para volver atrás)*")
        try:
            op = input("\nIngrese numéricamente la opción: ")
            assert op in ('1', '2', '3', '')
            if op == '1':
                eliminar_url()
            elif op == '2':
                eliminar_seccion_html()
            elif op == '3':
                eliminar_clave_json()
            elif op == '':
                return
        except (ValueError, AssertionError):
            print("\nIngrese correctamente el valor.\n")
            system("pause")

def agregar_urls():
    while True:
        system("cls")
        print("--------------------")
        print("    AGREGAR URLS    ")
        print("--------------------\n")
        print("1. Agregar URL única.")
        print("2. Agregar listado por páginas de URLs")
        print("3. Agregar lista de URLs de un archivo.")
        print("\n *(Enter para volver atrás)*")
        try:
            op = input("\nIngrese numéricamente la opción: ")
            assert op in ('1', '2', '3', '')
            if op == '1':
                agregar_url()
            elif op == '2':
                generar_urls()
            elif op == '3':
                leer_lista_urls()
            elif op == '':
                agregar()
        except (ValueError, AssertionError):
            print("\nIngrese correctamente el valor.\n")
            system("pause")

def guardar():
    while True:
        system('cls')
        
        if not data:
            print("\nNo hay datos para guardar.\n")
            system("pause")
            menu()

        try:
            op=input('¿De qué forma deseas guardar tus datos?\n1. En un archivo.\n2. En una Base de Datos (SQL).\n\n *(Enter para volver atrás)*\n\n-> ')
            assert op in ('1', '2', '')
            if op == '':
                menu()
            elif op == '1':
                guardar_datos()
            elif op == '2':
                guardar_datos_bbdd()
        except (ValueError, AssertionError):
            system('cls')
            print("\nIngrese correctamente el valor.\n")
            system('pause')

def salir():
    while True:
        system('cls')
        try:
            salir=input('¿Quieres salir del programa?\nTodos los datos no guardados se perderán.\n\nDigita 1 para salir. Enter para volver\n\n-> ')
            assert salir in ('1', '')
            if salir == '1':
                system('cls')
                exit()
            elif salir == '':
                system('cls')
                print("\n\nVolviendo al menú principal...\n")
                system('pause')
                return
        except (ValueError, AssertionError):
            system('cls')
            print("\nRespuesta no válida.\n")
            system('pause')
