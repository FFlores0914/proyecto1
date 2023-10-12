import os

def borrar_terminal():
    # Esta función borra la terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    numero = 0

    while numero <= 50:
        borrar_terminal()
        print(f"Número actual: {numero}")
        input("Presiona 'n' y Enter para continuar...")
        numero += 1
if __name__ == "__main__": 
    main()