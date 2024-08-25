from os import system
from funciones.menu import menu
from funciones.gen_carpetas import GenerarCarpetas

# system('pip install requests beautifulsoup4 pandas tqdm beautifultable pymysql openpyxl')

if __name__ == "__main__":
    GenerarCarpetas()
    menu()
