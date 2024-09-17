import os
from funciones.menu import menu
from funciones.gen_carpetas import GenerarCarpetas

# os.system('pip install -r requirements.txt')

if __name__ == "__main__":
    GenerarCarpetas()
    menu()
