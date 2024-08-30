from os import system, makedirs, path

def GenerarCarpetas():
    system('cls') 
    script_dir = path.dirname(path.abspath(__file__))
    
    # Carpeta ListasURL
    directorio_listas = path.join(script_dir, "..", "..", "ListasURL")
    directorio_listas = path.abspath(directorio_listas)
    
    # Carpeta 'output/data'
    output_dir = path.join(script_dir, "..", "..", "output", "data")
    output_dir = path.abspath(output_dir)
    
    no_creado = False
    creado = False
    print('')

    if not path.exists(directorio_listas):
        try:
            makedirs(directorio_listas, exist_ok=True)
            print("-> Directorio 'ListasURL' creado.")
            creado = True
        except Exception as e:
            no_creado = True
            print(f"Error al crear el directorio 'ListasURL': {e}")
            print('''\n
                                **NOTA**
                  Sin esta carpeta no podrás leer archivos 
                  con las listas de URLs que necesites utilizar. 
                  Verifica el error y vuelve a intentarlo.\n 
                  ''')
        
    if not path.exists(output_dir):
        try:
            makedirs(output_dir, exist_ok=True)
            print("-> Directorio 'output/data' creado.")
            creado = True
        except Exception as e:
            no_creado = True
            print(f"Error al crear el directorio 'output/data': {e}")
            print('''\n
                                **NOTA**
                  Sin esta carpeta no podrás guardar un archivo 
                  con los datos obtenidos del sitio web, 
                  pero aún podrás guardarlo en una bbdd en la nube.
                  Verifica el error y vuelve a intentarlo.\n 
                  ''')

    while no_creado:
        try:
            salir = input('''
                          ¿Desea continuar sin estas carpetas?
                          Considere las notas mencionadas. 
                          Presione 1 para salir o enter para continuar. 
                          
                          -> ''')
            assert salir in ['1', '']

        except (ValueError, AssertionError):
            print('Digite correctamente la opción solicitada. ')
        except Exception as e:
            print(f'Error: {e}')
            

        if salir == '1':
            system('cls')
            exit()
        elif salir == '':
            break

    if creado:
        print('')
        system('pause')
    else:
        print('\nCarpetas verificadas.\nComenzando programa.\n')
        system('pause')
        