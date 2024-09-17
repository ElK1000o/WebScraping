import pymysql
from tqdm import tqdm
from os import system
from .manejo_data import aplanarData

class DAO:
    def __init__(self, host, user, password, db):
        try:
            self.connection = pymysql.connect(host=host,
                                              user=user,
                                              password=password,
                                              db=db)
            self.cursor = self.connection.cursor()
            system('cls')
            print('\n\nConexión establecida\n') 
            system('pause')
            system('cls')
        except Exception as e:
            print(f"\n\nError al conectar con la base de datos: {e}\n")
            system('pause')
            raise

    def CargarDatos(self, lista, nombre_tabla, columnas):
        sep = ', '.join(['%s'] * len(columnas))
        col_str = ', '.join(columnas)
        sql = f'INSERT INTO {nombre_tabla} ({col_str}) VALUES ({sep})'

        try:
            for dato in tqdm(lista, desc="Insertando datos", unit="registro"):
                try:
                    val = tuple(dato[col] for col in dato)
                    self.cursor.execute(sql, val)
                    self.connection.commit()
                except Exception as e:
                    print(f"\nError al insertar dato: {e}\n")
            print('\nDatos ingresados correctamente.\n')
            system('pause')
        except Exception as e:
            print(f"\nError al ingresar dato: {e}\n")
            system('pause')

    def cerrar_conexion(self):
        self.connection.close()

def solicitar_datos_conexion():
    from .menu import menu
    while True:
        system('cls')
        host = input("Ingrese el host de la base de datos: ")
        system('cls')
        print(f"host='{host}'")
        user = input("Ingrese el usuario de la base de datos: ")
        system('cls')
        print(f"host='{host}'\nuser='{user}'")
        password = input("Ingrese la contraseña de la base de datos: ")
        system('cls')
        print(f"host='{host}'\nuser='{user}'\npassword='{password}'")
        db = input("Ingrese el nombre de la base de datos: ")
        system('cls')
        print(f"host='{host}'\nuser='{user}'\npassword='{password}'\ndb='{db}'\n")
        op = input('\n¿Está de acuerdo con los datos ingresados?\nDigite 1 para confirmar o 2 para volver al menú princpal \n(de lo contrario volverá a ingresar)\n\n-> ')
        if op == '1':
            return host, user, password, db
        elif op == '2':
            menu()
        else:
            system('cls')
            print('\nVolverá a ingresar los datos.\n')
            system('pause')

def solicitar_datos_tabla():
    from .menu import menu
    while True:
        system('cls')
        nombre_tabla = input("\nIngrese el nombre de la tabla\n\n-> ")
        system('cls')
        print(f"Tabla -> {nombre_tabla}")
        columnas = input("\nIngrese los nombres de las columnas separándolos por comas\nEjemplo: columna1, columna2, ..., columnaN\n\n*NOTA: Debes escribirlas en el mismo orden que las agregaste para su búsqueda, ya sea en sección HTML o clave JSON*\n\n-> ").split(',')
        columnas = [col.strip() for col in columnas]
        system('cls')
        print(f"Tabla -> {nombre_tabla}\nColumnas -> {columnas}")
        op = input('\n¿Está de acuerdo con los datos ingresados?\nDigite 1 para confirmar o 2 para volver al menú princpal \n(de lo contrario volverá a ingresar)\n\n-> ')
        if op == '1':
            return nombre_tabla, columnas
        elif op == '2':
            menu()
        else:
            system('cls')
            print('Volverá a ingresar los datos.')
            system('pause')

def guardar_datos_bbdd():
    from .almacenamiento import data
    system('cls')

    print('''
    Para guardar los datos descargados en una Base de Datos SQL
    debes tener de antemano creada la base y tabla (con sus respectivas columnas)
    de no ser así, el programa no funcionará correctamente. Si aun no
    tienes creada tu tabla y sus columnas, debes crearla ahora.
    Si ya está creada, continua.
    ''')
    
    system('pause')

    host, user, password, db = solicitar_datos_conexion()
    nombre_tabla, columnas = solicitar_datos_tabla()

    flat_data = aplanarData(data)

    dao = DAO(host, user, password, db)
    dao.CargarDatos(flat_data, nombre_tabla, columnas)
    dao.cerrar_conexion()
