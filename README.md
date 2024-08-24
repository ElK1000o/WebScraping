# WebScraping

## Descripción

Este repositorio contiene herramientas para realizar scraping de datos desde sitios web en HTML o JSON. Incluye un caso específico para el scraping de productos lácteos del supermercado Jumbo y una herramienta general para scraping de HTML y JSON.

## Estructura del Repositorio

El repositorio está organizado en las siguientes carpetas:

- **ScrapGeneral/**: Herramienta general para scraping de HTML y JSON.

  - **script-s**: Carpeta que contiene el script principal.
  - **README.md**: Instrucciones específicas para esta herramienta.
  - **output/**: Carpeta para los datos generados por la herramienta general.
    - **data/**: Datos en formato CSV o XLSX.

- **jumbo_scraping/**: Scripts específicos para scraping de productos lácteos de Jumbo.
  - **py**: Carpeta que contiene script en Python.
  - **ipynb**: Carpeta que contiene notebook de Jupyter.
  - **README.md**: Instrucciones específicas para este caso de uso.
  - **output/**: Carpeta para los datos generados por los scripts de Jumbo.
    - **data/**: Datos en formato CSV o XLSX.

## Requisitos

- Python 3.x instalado.
- Librerías necesarias:
  - requests
  - beautifulsoup4
  - pandas
  - jupyter
  - tqdm
  - beautifultable
  - pymysql

## Instalación de Librerías

Para instalar las librerías necesarias, ejecuta el siguiente comando:

```bash
pip install requests beautifulsoup4 pandas jupyter tqdm beautifultable pymysql
python.exe -m pip install --upgrade pip
```

## Uso

Dentro de cada carpeta 'ScrapGeneral' o 'ScrapJumbo' encontrarás un archivo README.md con el contenido, uso y detalles específicos del cada herramienta.

## Notas

- Asegúrate de tener una conexión a internet estable para realizar scraping correctamente.
- Los programas guardan los archivos de salida en las carpetas `output/data` correspondientes dentro de cada subcarpeta (`ScrapGeneral/output/data` y `ScrapJumbo/output/data`).
