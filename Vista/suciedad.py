import numpy as np

class suciedad():

    def __init__(self, filas, columnas, laberinto) -> None:

        self.list_suciedad = []

        # Generando la cantidad de basuras
        a, b = 1, 5
        numero_aleatorio = int(np.random.uniform(a, b))
        
        for i in range(numero_aleatorio):

            while(True):

                a, b = 0, filas
                fila = int(np.random.uniform(a, b))
                c, d = 0, columnas
                columna = int(np.random.uniform(c, d))

                if laberinto[fila][columna] == 1:
                    break

            self.list_suciedad.append([fila,columna])