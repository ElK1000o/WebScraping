import urllib.request
import urllib.robotparser
import io
import gzip
from os import system
import time
from .almacenamiento import urls

def VerificarRobots(user_agent='*'):
    system('cls')
    try:
        print("\nSe procederá a revisar el archivo 'robots.txt' \npara evaluar autorización de las URLs agregadas. \n")
        url_sitio = input('Ingresa la URL general del sitio web (por ejemplo: https://www.urlweb.com)\n-> ')
        
        system('cls')

        print(f"Revisando 'robots.txt' desde {url_sitio}/robots.txt ...")
        time.sleep(3)

        with urllib.request.urlopen(f'{url_sitio}/robots.txt') as response:
            content_encoding = response.info().get('Content-Encoding')

            if content_encoding == 'gzip':
                buf = io.BytesIO(response.read())
                with gzip.GzipFile(fileobj=buf) as f:
                    robots_txt = f.read().decode('utf-8', errors='replace')
            else:
                robots_txt = response.read().decode('utf-8', errors='replace')

        # Analizar robots.txt
        rp = urllib.robotparser.RobotFileParser()
        rp.parse(robots_txt.splitlines())

        # Verificar cada URL de la lista urls
        no_permitidos = []
        for url_scrap in urls:
            permitido = rp.can_fetch(user_agent, url_scrap)

            if not permitido:
                no_permitidos.append(url_scrap)

        system('cls')

        if no_permitidos:
            print(f'Las siguientes URLs no pueden ser scrapeadas: {no_permitidos}\n\nDeberías eliminarlas de tu lista.')
        else:
            print('Todas las URLs pueden ser scrapeadas.')

    except urllib.error.URLError as e:
        print(f'Error de URL: {e.reason}')
    except UnicodeDecodeError:
        print('Error de codificación del archivo robots.txt')
    except Exception as e:
        print(f'Error inesperado: {e}')
    print('')
    system('pause')
    system('cls')
