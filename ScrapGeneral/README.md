# Herramienta para scraping

## Descripción

Este programa permite realizar scraping de datos desde sitios web en HTML o JSON. Puedes agregar URLs y definir secciones específicas de HTML y claves de JSON para extraer datos estructurados.

## Requisitos

- Python 3.x instalado.
- Librerías necesarias:
  - requests
  - BeautifulSoup
  - pandas
  - tqdm
  - beautifultable
  - pymysql
  - openpyxl

## Instrucciones de Uso

1. **Instalación de Librerías:**

```bash
pip install requests beautifulsoup4 pandas tqdm beautifultable pymysql openpyxl
python.exe -m pip install --upgrade pip
```

2. **Ejecución del Programa:**

- Clona o descarga el repositorio.
- Ejecuta el archivo `main.py` ubicado en la carpeta `script-s` (Descomenta la línea 4 si no tienes instaladas las librerías necesarias).

3. **Menú Principal:**

- Agregar (URL - Sección - Clave): Permite agregar URLs (individuales o listado) y definir secciones HTML o claves JSON para scraping.
- Listar URLs: Muestra las URLs agregadas.
- Eliminar (URL - Sección - Clave): Elimina URLs, secciones o claves agregadas.
- Iniciar Scraping: Realiza scraping de las URLs agregadas.
- Guardar Datos: Guarda los datos scrappeados en archivos CSV, Excel o ambos.
- Limpiar Programa: Reinicia el programa, eliminando URLs, secciones y claves.
- Salir: Cierra el programa.

4. **Scraping:**

- Selecciona el formato (HTML o JSON) y las secciones/claves específicas.
- Para HTML, ingresa selectores CSS en formato 'selector.de.clase' (punto como separador).
- Para JSON, ingresa las claves en formato 'nivel1.nivel2.nivel3' (punto como separador) según la estructura del JSON.

5. **Guardar Datos:**

Puedes guardar tus datos en una Base de Datos (SQL) o en un archivo:

- Base de Datos (SQL):

  - Debes tener creada de antemano la DB con su respectiva tabla y columnas.
  - Define las credenciales de inicio (host, usuario, contraseña y nombre de DB).
  - Indica el nombre de la tabla y columnas en que insertarás los datos (Considera que las columnas debes agregarlas en el mismo orden en que las buscaste al agregar sección HTML o clave JSON).

- Archivo:
  - Define un nombre para el archivo de salida.
  - Escoge el formato de archivo (CSV, Excel o ambos).
  - Opcionalmente, personaliza los encabezados de las columnas.

6. **Ejemplos:**

- HTML: 'a.product-card-name' para nombres de productos.
- JSON: 'MRData.RaceTable.Races.raceName' para nombres de carreras.

7. **Notas:**

- Asegúrate de tener una conexión a internet estable para realizar scraping correctamente.
- Al ejecutar el programa, se generarán automáticamente las carpetas `ListasURL` (Para agregar listado de URLs) y `output/data`.
- El programa guarda los archivos de salida en la carpeta `output/data`.
- Una vez cerrado el programa empiezas desde cero, asegúrate de guardar tus datos antes de salir.
- Para leer y agregar un listado de URLs desde un archivo debes considerar lo siguiente:

  - Para archivos de texto (.txt) el listado debe ir separado por un salto de línea (enter). Ejemplo:
    ```txt
    https://www.url1.com
    https://www.url2.com
    https://www.url3.com
    ```
  - Para archivos separados por comas (.csv) las URLs deben estar en una única columna. Ejemplo:
    ```csv
    URL
    https://www.url1.com
    https://www.url2.com
    https://www.url3.com
    ```
  - Para archivos excel (.xlsx) el listado debe ir (al igual que en CSV) en una única columna, cada url ocupa una celda (o fila) hacia abajo. Ejemplo:
    ```xlsx
    +-----+-----+-------------------+
    |     |  A  |        B          |
    +-----+-----+-------------------+
    |  1  | URL |                   |
    +-----+-----+-------------------+
    |  2  | https://www.url1.com    |
    +-----+-----+-------------------+
    |  3  | https://www.url2.com    |
    +-----+-----+-------------------+
    |  4  | https://www.url3.com    |
    +-----+-----+-------------------+
    ```
