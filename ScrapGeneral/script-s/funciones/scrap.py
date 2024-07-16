from bs4 import BeautifulSoup
import requests
from tqdm import tqdm
from os import system
from .almacenamiento import data, secciones_html, claves_json, urls

def iniciar_scraping():
    from .menu import menu
    system("cls")
    global data

    if not urls:
        print("\nNo hay URLs agregadas para scrapear.\n")
        system("pause")
        menu()
    
    try:
        formato = input("¿El sitio está en HTML o JSON?\n\nPor favor, digite el número\n1. html\n2. json\n\n *(Enter para volver)*\n\n-> ").lower()
        assert formato in ('1', '2', '')

        if formato == "1":
            if not secciones_html:
                print("\nNo hay secciones HTML agregadas para scrapear.\n")
                system("pause")
                menu()
            
            system('cls')
            print('\n\nRealizando scraping... \n')

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

            system('cls')
            print('\n\nRealizando scraping... \n')

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
        print("\nScraping completado.\nVolviendo al menú principal.\n")
            
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
