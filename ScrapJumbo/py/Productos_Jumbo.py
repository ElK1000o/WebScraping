import requests
from bs4 import BeautifulSoup
import pandas as pd
from os import system

system('cls')
print('\nCargando...\n')

webs = [
    'https://www.jumbo.cl/lacteos?page=1',
    'https://www.jumbo.cl/lacteos?page=2',
    'https://www.jumbo.cl/lacteos?page=3',
    'https://www.jumbo.cl/lacteos?page=4',
    'https://www.jumbo.cl/lacteos?page=5',
    'https://www.jumbo.cl/lacteos?page=6',
    'https://www.jumbo.cl/lacteos?page=7',
    'https://www.jumbo.cl/lacteos?page=8',
    'https://www.jumbo.cl/lacteos?page=9',
    'https://www.jumbo.cl/lacteos?page=10',
    'https://www.jumbo.cl/lacteos?page=11',
    'https://www.jumbo.cl/lacteos?page=12',
    'https://www.jumbo.cl/lacteos?page=13',
    'https://www.jumbo.cl/lacteos?page=14',
    'https://www.jumbo.cl/lacteos?page=15',
    'https://www.jumbo.cl/lacteos?page=16',
    'https://www.jumbo.cl/lacteos?page=17',
    'https://www.jumbo.cl/lacteos?page=18',
    'https://www.jumbo.cl/lacteos?page=19',
    'https://www.jumbo.cl/lacteos?page=20',
]

lista = []

for web in webs:
    resp = requests.get(web)
    soup = BeautifulSoup(resp.text, 'html.parser')
    
    productos = soup.find_all('a', class_='product-card-name')
    precios = soup.find_all('span', class_='prices-main-price')
    
    for prod, prec in zip(productos, precios):
        nombre = prod.get_text(strip=True)
        precio = prec.get_text(strip=True)
        lista.append({'Producto': nombre, 'Precio': precio})

df = pd.DataFrame(lista)

system('cls')

print(f'\nRevisión de DataFrame obtenido:\n\n{df}')

while True:
    try:
        print('\n\nQuieres guardar los datos?')
        guardar = int(input('\nPresiona 1 para SI.\nPresiona 2 para NO.\n\n- '))
        assert guardar == 1 or guardar == 2
        
        if guardar == 1:
            system('cls')
            nom = input('\nIngresa el nombre que quieres para tu archivo.\nNota: Si el nombre ya existe, el archivo se sobrescribirá.\n\n- ')
            while True:
                try:
                    system('cls')
                    print(f'El nombre de tu achivo será: {nom}')
                    print('\nEn qué formato lo quieres guardar?\n')
                    tipo = int(input('\nPresiona 1 para CSV.\nPresiona 2 para XLSX.\nPresiona 3 para ambos.\nPresiona 4 para cancelar.\n- '))
                    assert tipo >= 1 and tipo <= 4
                    
                    if tipo == 1:
                        system('cls')
                        df.to_csv(f'output/data/{nom}.csv', index=False)
                        print(f'\nLos datos han sido guardados en\n\n- output/data/{nom}.csv\n\nPrograma terminado.')
                        system('pause')
                        system('cls')
                    elif tipo == 2:
                        system('cls')
                        df.to_excel(f'output/data/{nom}.xlsx', index=False)
                        print(f'\nLos datos han sido guardados en\n\n- output/data/{nom}.xlsx\n\nPrograma terminado.')
                        system('pause')
                        system('cls')
                    elif tipo == 3:
                        system('cls')
                        df.to_csv(f'output/data/{nom}.csv', index=False)
                        df.to_excel(f'output/data/{nom}.xlsx', index=False)
                        print(f'\nLos datos han sido guardados en\n\n- output/data/{nom}.csv\n- output/data/{nom}.xlsx\n\nPrograma terminado.')
                        system('pause')
                        system('cls')
                    elif tipo == 4:
                        system('cls')
                        print('Has cancelado el proceso.\n\nPrograma Terminado.')
                        system('pause')
                        break
                    break
                except AssertionError:
                    system('cls')
                    print('\nNúmero mal ingresado.')
                    system('pause')
                    system('cls')
                except ValueError:
                    system('cls')
                    print('\nEl espacio no puede quedar en blanco/valor debe ser numérico.')
                    system('pause')
                    system('cls')
            break
        else:
            print('\nLos datos no han sido guardados.\n\nPrograma terminado.')
            system('pause')
            system('cls')
            break 
    except AssertionError:
        system('cls')
        print('\nNúmero mal ingresado.')
        system('pause')
        system('cls')
    except ValueError:
        system('cls')
        print('\nEl espacio no puede quedar en blanco/valor debe ser numérico.')
        system('pause')
        system('cls')
