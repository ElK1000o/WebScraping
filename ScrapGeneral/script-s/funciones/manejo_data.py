import pandas as pd
from os import system, makedirs, path
from .almacenamiento import urls, secciones_html, claves_json, data

def guardar_datos():
    from .menu import menu
    system("cls")
    if not data:
        print("\nNo hay datos para guardar.\n")
        system("pause")
        menu()
    
    flat_data = []
    headers = list(data[0].keys())
    
    max_lengths = {key: max(len(row[key]) if isinstance(row[key], list) else 1 for row in data) for key in headers}
    
    for row in data:
        for i in range(max(max_lengths.values())):
            flat_row = {}
            for key in headers:
                if isinstance(row[key], list) and i < len(row[key]):
                    flat_row[key] = row[key][i]
                else:
                    flat_row[key] = None
            flat_data.append(flat_row)

    while True:
        nombre = input("\nIngrese el nombre del archivo (sin extensión)\nConsidere que si tiene un archivo con el mismo nombre y extensión se sobrescribirá y lo perderá.\n\n *(Enter para volver al menú)*\n\n-> ")
        if nombre == '':
            menu()
        system('cls')
        print(f'\nNombre del archivo: {nombre}\n')
        formato = input("\nIngrese el formato de archivo\nDigite el numero:\n1. csv\n2. xlsx\n3. ambos\n\n *(Enter para volver al menú)*\n\n-> ").lower()
        if formato == '':
            menu()
        system('cls')
        try:
            if formato in ["1", "2", "3"]:
                script_dir = path.dirname(path.abspath(__file__))
                output_dir = path.join(script_dir, "..", "output", "data")
                makedirs(output_dir, exist_ok=True)

                headers_modificados = headers[:]

                print(f'\nNombre del archivo: {nombre}\n')

                headers_custom = input("¿Desea agregar encabezados personalizados a las columnas?\n\nPor favor, responda '1' para sí o '2' para no.\n\n-> ")
                system('cls')
                if headers_custom == "1":
                    print('')
                    for idx, header in enumerate(headers_modificados):
                        nuevo_encabezado = input(f"Ingrese el encabezado para la columna '{header}': ")
                        headers_modificados[idx] = nuevo_encabezado
                    system('cls')
                elif headers_custom == "2":
                    system('cls')

                print('')

                df = pd.DataFrame(flat_data, columns=headers)
                df.columns = headers_modificados

                if formato == "1" or formato == "3":
                    csv_path = path.join(output_dir, f"{nombre}.csv")
                    df.to_csv(csv_path, index=False)
                    print(f"- Datos guardados en -> {csv_path}")
                
                if formato == "2" or formato == "3":
                    xlsx_path = path.join(output_dir, f"{nombre}.xlsx")
                    df.to_excel(xlsx_path, index=False)
                    print(f"- Datos guardados en -> {xlsx_path}")
                print('')
                system('pause')
                break
            else:
                print("Formato no válido. Intente de nuevo.")
                system("pause")
                system('cls')
        except Exception as e:
            print(f'Error al guardar los datos \nNúmero de error: {e}')
            system('pause')
            system('cls')

def limpiar_programa():
    system('cls')
    global urls, secciones_html, claves_json, data
    urls.clear()
    secciones_html.clear()
    claves_json.clear()
    data.clear()
    print("\nPrograma limpiado.\nSe han eliminado todas las URLs, secciones HTML y claves JSON.\nPuede realizar búsqueda nueva desde cero\n")
    system("pause")
