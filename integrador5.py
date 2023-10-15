import os
import random

class Juego:
    def __init__(self, mapa, inicio, final):
        self.mapa = mapa
        self.inicio = inicio
        self.final = final

    def mover(self, direccion):
        
        pass

    def mostrar_mapa(self):
        
        pass

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        archivos = os.listdir(path_a_mapas)
        if not archivos:
            raise FileNotFoundError("No se encontraron archivos de mapas en el directorio.")

        nombre_archivo = random.choice(archivos)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            lines = archivo.readlines()
        
        
        coordenadas = list(map(int, lines[0].split()))
        inicio = (coordenadas[0], coordenadas[1])
        final = (coordenadas[2], coordenadas[3])

        mapa = ''.join(lines[1:])  

        super().__init__(mapa, inicio, final)


if __name__ == "__main__":
    path_a_mapas = "mapas"  
    juego = JuegoArchivo(path_a_mapas)

    
    juego.mostrar_mapa()



