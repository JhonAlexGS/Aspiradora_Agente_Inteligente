from Nodo import Casilla
import numpy as np

class Aspiradora():

    def __init__(self, laberinto, guardar_posicion) -> None:
        
        self.start = True
        self.laberinto = laberinto
        self.guardar_posicion_interfaz = guardar_posicion # Metodo usado para imprimir
        self.lista_Casillas = []
        self.lista_Casillas.append(Casilla.Nodo((1, 1)))
        

    def mover_aspiradora(self, canvas, text_id, y_cleaner=None, x_cleaner=None, tamaño_casilla=None, lista_suciedades=None, nodoAnterior= None, delay=2000):

        casilla_Nodo = Casilla.Nodo((x_cleaner,y_cleaner))
        direction = None

        if self.start==True:
            self.start=False
            x_cleaner = self.lista_Casillas[0].id_Casilla[0]
            y_cleaner = self.lista_Casillas[0].id_Casilla[1]
            x = int(x_cleaner * tamaño_casilla + tamaño_casilla / 2)
            y = int(y_cleaner * tamaño_casilla + tamaño_casilla / 2)
            canvas.coords(text_id, x, y)


        else:           

            while(True):

                flag = False
                direction = np.random.randint(1, 5)

                # Abajo
                if direction == 1:
                    if y_cleaner+1 < len(self.laberinto)-1:
                        y=y_cleaner+1
                        x=x_cleaner
                        flag = True
                # Arriba
                elif direction == 2:
                    if y_cleaner-1 > -1:
                        y=y_cleaner-1
                        x=x_cleaner
                        flag = True
                # Derecha
                elif direction == 3:
                    if x_cleaner+1 < len(self.laberinto[0])-1:
                        x=x_cleaner+1
                        y=y_cleaner
                        flag = True
                # Izquierda
                else:
                    if x_cleaner-1 > -1:
                        x=x_cleaner-1
                        y=y_cleaner
                        flag = True

                if flag:
                    if self.laberinto[y][x] == 1:
                        if direction == 1:
                            y_cleaner+=1
                        elif direction == 2:
                            y_cleaner-=1
                        elif direction == 3:
                            x_cleaner+=1
                        elif direction == 4:
                            x_cleaner-=1
                        break
                    else:
                        casilla_Nodo.camino[direction-1] = 0
                        self.guardar_posicion_interfaz(canvas, tamaño_casilla, x, y, 0)
                        

            x = int(x_cleaner * tamaño_casilla + tamaño_casilla / 2)
            y = int(y_cleaner * tamaño_casilla + tamaño_casilla / 2)

            # Algoritmo de decisión

            if (x,y) in lista_suciedades[0]:
                index = lista_suciedades[0].index((x,y))
                canvas.delete(lista_suciedades[1][index])
                lista_suciedades[0].pop(index)
                lista_suciedades[1].pop(index)

            self.guardar_posicion_interfaz(canvas, tamaño_casilla, x_cleaner, y_cleaner, 1)

            repetido = False

            index_casilla = 0

            # Busca si existen en la lista y si existe busca si encontro un muro o un obstaculo
            for casillas in self.lista_Casillas:
                if casillas.id_Casilla == casilla_Nodo.id_Casilla:
                    repetido = True
                    for direccion in range(4):
                        if casilla_Nodo.camino[direccion] == 0:
                            self.lista_Casillas[index_casilla].camino[direccion] = 0

                index_casilla+=1
            
            if not repetido:
                self.lista_Casillas.append(casilla_Nodo)


            # Guarda la posicion del nodo
            #################################################################################################
            nodoCasilla_Anterior_Actual = (nodoAnterior, casilla_Nodo)
            posicion_Lista_Anterior_Actual = []

            if nodoAnterior != None:

                for anterior_actual in nodoCasilla_Anterior_Actual:
                    index_casilla = 0
                    for casillas in self.lista_Casillas:
                        if self.lista_Casillas != 1:
                            if casillas.id_Casilla == nodoAnterior.id_Casilla:
                                posicion_Lista_Anterior_Actual.append(anterior_actual.id_Casilla)
                                break
                        index_casilla+=1
        
            #################################################################################################
            # Enlazar Nodo
            # print((x_cleaner,y_cleaner))
            # print(self.lista_Casillas)

            # Super poner
            canvas.tag_raise(text_id)
            canvas.coords(text_id, x, y)

        canvas.after(delay, self.mover_aspiradora, canvas, text_id, y_cleaner, x_cleaner, tamaño_casilla, lista_suciedades, casilla_Nodo)        

    def obtener_posicion(self, coordenadas):
        index = 0
        for casillas in self.lista_Casillas:
            if casillas.id_Casilla == coordenadas:
                return index
            index+=1
        return None