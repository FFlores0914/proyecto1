nombre=input("Ingrese su nombre de usuario: ")
print ("Bienvenido a este laberinto ", nombre)

import readchar #Contiene funciones relacionadas con la lectura de caracteres y teclas desde el teclado.

print("Presiona cualquier tecla y Presiona ↑ para salir.")

while True:
    tecla = readchar.readkey() #La función readkey() es para leer una tecla presionada desde el teclado.
    if tecla == readchar.key.UP:
        print("¡Presionaste la tecla ↑! Saliendo del programa.")
        break

    print(f"Presionaste la tecla: {tecla}")

import os

def borrar_terminal():
    # Esta función borra la terminal según el sistema operativo
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

