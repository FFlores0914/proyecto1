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


