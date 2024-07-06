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

## Instrucciones de Uso

1. **Instalación de Librerías:**

```bash
pip install requests beautifulsoup4 pandas tqdm
python.exe -m pip install --upgrade pip
```

2. **Ejecución del Programa:**

- Clona o descarga el repositorio.
- Ejecuta el archivo scraping.py ubicado en la carpeta py.

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

- Define un nombre para el archivo de salida.
- Escoge el formato de archivo (CSV, Excel o ambos).
- Opcionalmente, personaliza los encabezados de las columnas.

6. **Ejemplos:**

- HTML: 'a.product-card-name' para nombres de productos.
- JSON: 'MRData.RaceTable.Races.raceName' para nombres de carreras.

7. **Notas:**

- Asegúrate de tener una conexión a internet estable para realizar scraping correctamente.
- El programa guarda los archivos de salida en la carpeta `output/data`.
- Una vez cerrado el programa empiezas desde cero, asegúrate de guardar tus datos antes de salir.