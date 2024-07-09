import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from tqdm import tqdm
from os import system, makedirs, listdir, path

urls = []
secciones_html = []
claves_json = []
data = []

# Funciones tipo menú

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
        print("6. Limpiar Programa (Eliminar URLs y Secciones).")
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
                guardar_datos()
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
                return
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
                return
        except (ValueError, AssertionError):
            print("\nIngrese correctamente el valor.\n")
            system("pause")
        
def salir():
    system('cls')
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

# Funciones para manejo de URLs

def agregar_url():
    system('cls')
    while True:
        url = input("Ingrese la URL (Enter para volver al menú): ").strip()
        if url == '':
            menu()
        if url in urls:
            print("La URL ya existe. Intente con una nueva.")
            system("pause")
            system('cls')
        else:
            urls.append(url)

def generar_urls():
    while True:
        system('cls')
        try:
            paginas = input("\nIntroduce las páginas específicas o rangos (Enter para volver)\nLos rangos se separan por guión '-' y páginas únicas por comas ',' (por ejemplo: 1,5,7-10,15)\n\n-> ")
            if paginas == '':
                return
            system('cls')
            print(f'\nRango: ({paginas})\n')
            inicio = input("Introduce la URL base (sin el número de página) (Enter para volver)\nEjemplo -> https://www.jumbo.cl/lacteos?page= \033[9m{numero de pagina}\033[0m\n\n-> ")
            if inicio == '':
                return
            system('cls')
            print(f'\nRango: ({paginas})\nURL base: {inicio}\n')
            final = input("Introduce la continuación de la URL si es necesario\nSi no hay continuación presiona enter para dejar espacio vacío\n\n->")
            system('cls')
            print(f'\nRango: ({paginas})\nURL base: {inicio}\nContinuación URL: {final}\n\nURL ejemplo: {inicio}{paginas[0]}{final}\n')
            system('pause')

            final = final.strip()
            seleccion = paginas.split(',')

            url_gen = []

            for part in seleccion:
                if '-' in part:
                    start, end = map(int, part.split('-'))
                    assert start >= 0, "Las páginas deben ser mayores o iguales a 0."
                    for i in range(start, end + 1):
                        nueva_url = f"{inicio}{i}{final}"
                        if nueva_url not in urls:
                            url_gen.append(nueva_url)
                        else:
                            print(f'La URL {nueva_url} ya existe, se omitirá.')
                else:
                    page = int(part)
                    assert page >= 0, "Las páginas deben ser mayores o iguales a 0."
                    nueva_url = f"{inicio}{page}{final}"
                    if nueva_url not in urls:
                        url_gen.append(nueva_url)
                    else:
                        print(f'La URL {nueva_url} ya existe, se omitirá.')

            if not url_gen:
                print("Todas las URLs generadas ya existen. Intente con un nuevo rango o URL base.")
                system("pause")
                system('cls')
                continue

            system('cls')
            print(f"\n\nRango: ({paginas})\nURL base: {inicio}\nContinuación URL: {final}\n\nURLs generadas:\n")
            for url in url_gen:
                print(url)

            confirmacion = input("\n¿Desea autorizar estas URLs?\n\nPor favor, responda '1' para sí o '2' para no\n\n-> ")
            if confirmacion == '1':
                urls.extend(url_gen)
                system('cls')
                print('\nURLs agregadas exitosamente. Volviendo al menú principal.\n')
                system('pause')
                menu()
            elif confirmacion == '2':
                system('cls')
                print("\nProceso cancelado. Volviendo al menú principal.\n")
                system('pause')
                menu()
            else:
                print("Respuesta no válida. Por favor, responda '1' para sí o '2' para no.")

        except (ValueError, AssertionError, Exception) as e:
            print(f"\nError: {e}")
            print("Por favor, inténtalo de nuevo.\n")
            system('pause')

def leer_lista_urls():
    try:
        script_dir = path.dirname(path.abspath(__file__))
        directorio_listas = path.join(script_dir, "..", "..", "ListasURL")
        makedirs(directorio_listas, exist_ok=True)

        archivos = [arch for arch in listdir(directorio_listas) if arch.endswith(('.csv', '.txt', '.xlsx'))]

        while True:
            system('cls')
            if not archivos:
                print("No se encontraron archivos de URLs en la carpeta 'ListasURL'.\n")
                system('pause')
                return

            print("Archivos encontrados en 'ListasURL':\n")
            for i, archivo in enumerate(archivos, start=1):
                print(f"{i}. {archivo}")
            try:
                idx = input("\nIngrese el número del archivo de URLs que desea importar (Enter para volver): ")
                if idx == '':
                    system('cls')
                    print("\nOperación cancelada. Volviendo al menú principal.\n")
                    system('pause')
                    menu()

                idx = int(idx) - 1
                if 0 <= idx < len(archivos):
                    archivo_seleccionado = archivos[idx]
                    system('cls')

                    print(f"\nArchivo seleccionado: {archivo_seleccionado}\n")
                    
                    confirmacion = input("¿Desea importar este archivo?\n1 para SI\n2 para NO\n\n-> ")
                    if confirmacion == '1':
                        ruta_archivo = path.join(directorio_listas, archivo_seleccionado)
                        
                        if archivo_seleccionado.endswith('.csv'):
                            df = pd.read_csv(ruta_archivo, header=None)
                        elif archivo_seleccionado.endswith('.txt'):
                            df = pd.read_csv(ruta_archivo, header=None)
                        elif archivo_seleccionado.endswith('.xlsx'):
                            df = pd.read_excel(ruta_archivo, header=None)
                        else:
                            print("Formato de archivo no compatible.")
                            system('pause')
                            return

                        urls_mostrar = df[0].tolist()
                        if len(urls_mostrar) <= 10:
                            urls_mostrar_completo = [(i+1, url) for i, url in enumerate(urls_mostrar)]
                        else:
                            urls_mostrar_completo = [(i+1, url) for i, url in enumerate(urls_mostrar[:5])] + \
                                                    [(None, '...')] + \
                                                    [(len(urls_mostrar) - 4 + i, url) for i, url in enumerate(urls_mostrar[-5:])]

                        system('cls')

                        print(f"\nMostrando URLs del archivo '{archivo_seleccionado}':\n")
                        for num, url in urls_mostrar_completo:
                            if num is not None:
                                print(f"{num}. {url}")
                            else:
                                print(url)

                        considerar_headers = input("\n¿Desea considerar los headers (primer elemento) del archivo?\nPresione '1' para SI (de lo contrario, eliminará los headers)\n\n-> ")
                        if considerar_headers != '1':
                            df = df.iloc[1:]
                            system('cls')
                            print(f"\nMostrando URLs del archivo '{archivo_seleccionado}':\n")

                            urls_nuevas = df[0].tolist()

                            if len(urls_nuevas) <= 10:
                                urls_mostrar_completo = [(i+1, url) for i, url in enumerate(urls_nuevas)]
                            else:
                                urls_mostrar_completo = [(i+1, url) for i, url in enumerate(urls_nuevas[:5])] + \
                                                        [(None, '...')] + \
                                                        [(len(urls_nuevas) - 4 + i, url) for i, url in enumerate(urls_nuevas[-5:])]
                                
                            for num, url in urls_mostrar_completo:
                                if num is not None:
                                    print(f"{num}. {url}")
                                else:
                                    print(url)
                            
                            try:
                                conf = int(input('\n¿Confirma el cambio?\n1. Si\n2. No\n\n-> '))
                                assert 1 <= conf <= 2
                                if conf == 1:
                                    for url in urls_nuevas:
                                        if url not in urls:
                                            urls.append(url)
                                        else:
                                            print(f"La URL '{url}' ya existe en la lista y será omitida.")
                                    system('cls')
                                    print("\nURLs importadas exitosamente.\nVolviendo al menú principal.\n")
                                    system('pause')
                                    menu()
                                elif conf == 2:
                                    system('cls')
                                    print('\nProceso cancelado. Volviendo a agregar URLs\n')
                                    system('pause')
                                    return
                            except (AssertionError, ValueError):
                                system('cls')
                                print("\nDigite correctamente el número. '1' para si, '2' para no.\n")
                                system('pause')
                            except Exception as e:
                                system('cls')
                                print(f'\nError: {e}\n')
                                system('pause')
                        else:
                            urls_mostrar = df[0].tolist()
                            for url in urls_mostrar:
                                if url not in urls:
                                    urls.append(url)
                                else:
                                    print(f"La URL '{url}' ya existe en la lista y será omitida.")
                            system('cls')
                            print("\nURLs importadas exitosamente.\nVolviendo al menú principal.\n")
                            system('pause')
                            menu()
                    elif confirmacion == '2':
                        system('cls')
                        print("\nOperación cancelada. Volviendo al menú principal.\n")
                        system('pause')
                        menu()
                    else:
                        system('cls')
                        print("\nRespuesta no válida. Por favor, responda '1' para sí o '2' para no.\n")
                        system('pause')
                else:
                    system('cls')
                    print("\nNúmero de archivo no válido.\n")
                    system('pause')
            except ValueError:
                system('cls')
                print("\nIngrese un número válido.\n")
                system('pause')
    
    except Exception as e:
        print(f"\nError al procesar los archivos: {e}\n")
        system('pause')

def listar_urls():
    system("cls")
    if urls:
        print("URLs agregadas:\n")
        for i, url in enumerate(urls, start=1):
            print(f"{i}. {url}")
        print('')
    else:
        print("No hay URLs agregadas.\n")
    system("pause")

def listar_eliminar():
    system("cls")
    if urls:
        print("URLs agregadas:\n")
        for i, url in enumerate(urls, start=1):
            print(f"{i}. {url}")
        print('')
    else:
        print("\nNo hay URLs agregadas.\n")

def eliminar_url():
    while True:
        listar_eliminar()
        try:
            idx = int(input("Ingrese el número de la URL que desea eliminar (Enter para volver): ")) - 1
            if 0 <= idx < len(urls):
                urls.pop(idx)
                print('')
            elif idx == '':
                return
            else:
                print("\nNúmero inválido.")
                break
        except (ValueError, IndexError):
            print("\nEntrada inválida.")
            break

# Funciones para búsqueda en URLs

def mostrar_formato_respuesta(url, formato):
    try:
        resp = requests.get(url)
        if formato == "html":
            soup = BeautifulSoup(resp.text, 'html.parser')
            print(soup.prettify())
        elif formato == "json":
            json_data = resp.json()
            json_str = json.dumps(json_data, indent=2, ensure_ascii=False)
            print(json_str[:10000])
    except Exception as e:
        print(f"Error al obtener la respuesta de la URL: {e}")
    system("pause")

def agregar_seccion_html():
    system("cls")
    if not urls:
        print("\nNo hay URLs agregadas. Agregue una URL primero.\n")
        system("pause")
        agregar_urls()
    
    ver_formato = input("¿Desea ver el formato del resultado del request para elegir la sección?\nEscriba '1' para ver el formato (de lo contrario avanzará a agregar)\n\n-> ")
    if ver_formato == "1":
        url = urls[0]
        mostrar_formato_respuesta(url, "html")

    while True:
        system('cls')
        if len(secciones_html) > 0:
            print(f'Secciones agregadas: ')
            for sec in secciones_html:
                print(f'- {sec}')
        
        seccion = input("\nIngrese el selector de la sección HTML que desea scrapear (Enter para volver)\nEjemplo:\n- 'a.product-card-name'\n- 'span.prices-main-price'\n\n-> ")
        if seccion == '':
            return
        
        if seccion in secciones_html:
            print("La sección ya ha sido agregada. Por favor, ingrese una nueva sección.")
            system("pause")
            continue

        try:
            print('\nBuscando sección... \n\n')
            url = urls[0]
            resp = requests.get(url)
            soup = BeautifulSoup(resp.text, 'html.parser')
            elements = soup.select(seccion)
            
            if not elements:
                system('cls')
                print(f"\nNo se encontraron elementos con el selector '{seccion}'. Por favor, intente con otro selector.")
                system("pause")
                continue
            
            secciones_html.append(seccion)
            system('cls')

        except Exception as e:
            print(f"Error al verificar la sección: {e}")
            system("pause")
            continue

def eliminar_seccion_html():
    while True:
        system("cls")
        if not secciones_html:
            print("\nNo hay secciones HTML agregadas para eliminar.\n")
            system("pause")
            break
        
        print("Secciones HTML agregadas:\n")
        for i, sec in enumerate(secciones_html, start=1):
            print(f"{i}. {sec}")
        
        try:
            idx = input("\nIngrese el número de la sección HTML que desea eliminar\n\n *(Enter para volver al Menú Principal)*\n\n-> ")
            if idx == "":
                menu()
            idx = int(idx) - 1
            if 0 <= idx < len(secciones_html):
                secciones_html.pop(idx)
            else:
                print("\nNúmero de sección inválido.\n")
                system("pause")
        except ValueError:
            print("\nIngrese un valor numérico válido.\n")
            system("pause")

def agregar_clave_json():
    system("cls")
    if not urls:
        print("\nNo hay URLs agregadas. Agregue una URL primero.\n")
        system("pause")
        agregar_urls()
    
    ver_formato = input("¿Desea ver el formato del resultado del request para elegir la clave?\nEscriba '1' para ver el formato (de lo contrario avanzará a agregar)\n\n-> ").lower()
    if ver_formato == "1":
        url = urls[0]
        mostrar_formato_respuesta(url, "json")
        
    while True:
        system('cls')
        if len(claves_json) > 0:
            print(f'Claves agregadas: ')
            for sec in claves_json:
                print(f'- {sec}')
        
        clave = input("\nIngrese la clave de la sección JSON que desea scrapear (Enter para volver al menú)\nEjemplo:\n- 'MRData.RaceTable.Races.raceName'\n\n-> ").strip()
        if clave.lower() == '':
            menu()
        if clave in claves_json:
            print("La clave JSON ya existe. Intente con una nueva.")
            system("pause")
            system('cls')
        else:
            claves_json.append(clave)

def eliminar_clave_json():
    while True:
        system("cls")
        if not claves_json:
            print("\nNo hay claves JSON agregadas para eliminar.\n")
            system("pause")
            break
        
        print("Claves JSON agregadas:\n")
        for i, sec in enumerate(claves_json, start=1):
            print(f"{i}. {sec}")
        
        try:
            idx = input("\nIngrese el número de la clave JSON que desea eliminar\n\n *(Enter para volver al Menú Principal)*\n\n-> ")
            if idx == "":
                menu()
            idx = int(idx) - 1
            if 0 <= idx < len(claves_json):
                claves_json.pop(idx)
            else:
                print("\nNúmero de clave inválido.\n")
                system("pause")
        except ValueError:
            print("\nIngrese un valor numérico válido.\n")
            system("pause")

# Funciones para scraping

def iniciar_scraping():
    system("cls")
    global data
    data = []

    if not urls:
        print("\nNo hay URLs agregadas para scrapear.\n")
        system("pause")
        menu()
    
    try:
        formato = input("¿El sitio está en HTML o JSON?\nPor favor, digite el número\n1. html\n2. json\n *(Enter para volver)*\n\n-> ").lower()
        assert formato in ('1', '2', '')

        if formato == "1":
            if not secciones_html:
                print("\nNo hay secciones HTML agregadas para scrapear.\n")
                system("pause")
                menu()
            
            print('\nRealizando scraping... \n')

            with tqdm(total=len(urls), desc="Procesando URLs", ncols=80) as pbar:
                for url in urls:
                    resp = requests.get(url)
                    if resp.status_code == 200:
                        soup = BeautifulSoup(resp.text, 'html.parser')
                    
                        row = {seccion: [] for seccion in secciones_html}
                        for seccion in secciones_html:
                            items = soup.select(seccion)
                            for item in items:
                                row[seccion].append(item.get_text(strip=True))
                        data.append(row)
                        pbar.update(1)
                    else:
                        print(f"Error al acceder a la URL: {url}")

        elif formato == "2":
            if not claves_json:
                print("\nNo hay claves JSON agregadas para scrapear.")
                system("pause")
                menu()
            
            print('\nRealizando scraping... \n')

            with tqdm(total=len(urls), desc="Procesando URLs", ncols=80) as pbar:
                for url in urls:
                    resp = requests.get(url)
                    if resp.status_code == 200:
                        json_data = resp.json()

                        row = {clave: [] for clave in claves_json}
                        for clave in claves_json:
                            items = obtener_valores_json(json_data, clave)
                            if items:
                                row[clave].extend(items)
                            else:
                                print(f"La clave '{clave}' no se encontró en el JSON de {url}.")
                        data.append(row)
                        pbar.update(1)
                    else:
                        print(f"Error al acceder a la URL: {url}")

        elif formato == '':
            menu()
        system('cls')
        print("\nScraping completado.\n")
            
    except (ValueError, AssertionError, KeyError):
        print("Error en el scraping de las URLs. Por favor, revise la entrada.")
    except Exception as e:
        print(f"Error en el scraping de las URLs. Error: {e}")
    system("pause")

def obtener_valores_json(data, path):
    keys = path.split('.')
    for key in keys:
        if isinstance(data, list):
            data = [item.get(key, {}) if isinstance(item, dict) else {} for item in data]
        elif isinstance(data, dict):
            data = data.get(key, {})
        else:
            return []
    return data if isinstance(data, list) else [data]

# Funciones para manejo de datos

def guardar_datos():
    system("cls")
    if not data:
        print("\nNo hay datos para guardar.\n")
        system("pause")
        return
    
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

# PROGRAMA PRINCIPAL

menu()
