import requests
from bs4 import BeautifulSoup
from os import system
import json
from .almacenamiento import secciones_html, claves_json, urls

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
    from .menu import agregar_urls
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
    from .menu import menu
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
    from .menu import agregar_urls
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
        
        clave = input("\nIngrese la clave de la sección JSON que desea scrapear (Enter para volver)\nEjemplo:\n- 'MRData.RaceTable.Races.raceName'\n\n-> ").strip()
        if clave.lower() == '':
            return
        if clave in claves_json:
            print("La clave JSON ya existe. Intente con una nueva.")
            system("pause")
            system('cls')
        else:
            claves_json.append(clave)

def eliminar_clave_json():
    from .menu import menu
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
