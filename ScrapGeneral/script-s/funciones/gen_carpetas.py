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
    
    creado = False
    print('')

    if not path.exists(directorio_listas):
        try:
            makedirs(directorio_listas, exist_ok=True)
            print("-> Directorio 'ListasURL' creado.")
            creado = True
        except Exception as e:
            print(f"Error al crear el directorio 'ListasURL': {e}")
    
    if not path.exists(output_dir):
        try:
            makedirs(output_dir, exist_ok=True)
            print("-> Directorio 'output/data' creado.")
            creado = True
        except Exception as e:
            print(f"Error al crear el directorio 'output/data': {e}")
            
    if creado:
        print('')
        system('pause')
    else:
        print('\nCarpetas verificadas.\nComenzando programa.\n')
        system('pause')