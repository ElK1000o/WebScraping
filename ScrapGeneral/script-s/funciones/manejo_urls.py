from os import system, makedirs, listdir, path
import pandas as pd
from .almacenamiento import urls

def agregar_url():
    system('cls')
    while True:
        url = input("Ingrese la URL (Enter para volver): ").strip()
        if url == '':
            return
        if url in urls:
            print("La URL ya existe. Intente con una nueva.")
            system("pause")
            system('cls')
        else:
            urls.append(url)

def generar_urls():
    from .menu import menu
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
    from .menu import menu
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
