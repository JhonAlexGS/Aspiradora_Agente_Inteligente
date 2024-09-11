from Nodo import Casilla
from Agente.helper import neighbor_empty
import numpy as np

class Aspiradora():

    def __init__(self, laberinto, guardar_posicion, tamaño_casilla) -> None:
        
        self.start = True
        self.laberinto = laberinto
        self.guardar_posicion_interfaz = guardar_posicion # Metodo usado para imprimir
        self.lista_Casillas = []
        self.lista_Casillas.append(Casilla.Nodo((4, 4)))
        self.tamaño_casilla = tamaño_casilla

    def mover_aspiradora(self, canvas, text_id, lista_suciedades=None, nodoAnterior= None, re_tour=[], delay=50):

        # for i in self.lista_Casillas:
        #     print(str(i.id_Casilla) + " -> " + str(i.camino))

        if self.start==True:

            self.start=False
            x_cleaner = self.lista_Casillas[0].id_Casilla[0]
            y_cleaner = self.lista_Casillas[0].id_Casilla[1]
            x = int(x_cleaner * self.tamaño_casilla + self.tamaño_casilla / 2)
            y = int(y_cleaner * self.tamaño_casilla + self.tamaño_casilla / 2)
            self.guardar_posicion_interfaz(canvas, self.tamaño_casilla, x_cleaner, y_cleaner, 1)
            canvas.coords(text_id, x, y)
            canvas.tag_raise(text_id)
            canvas.after(delay, self.mover_aspiradora, canvas, text_id, lista_suciedades, self.lista_Casillas[0]) 

        else: 

            # self.imprimir_lista()
            new_x, new_y, direction, re_tour= self.next_move(nodoAnterior, re_tour)
            index = self.obtener_posicion((new_x,new_y))

            if self.laberinto[new_y][new_x] == 1:
                # Agregando nuevo nodo
                if index == None:
                    self.lista_Casillas.append(Casilla.Nodo((new_x,new_y)))
                nuevo_Nodo = Casilla.Nodo((new_x,new_y))
                self.link(nodoAnterior, nuevo_Nodo)
                x_table = int(new_x * self.tamaño_casilla + self.tamaño_casilla / 2)
                y_table = int(new_y * self.tamaño_casilla + self.tamaño_casilla / 2)
                lista_suciedades = self.clean(canvas, x_table, y_table, lista_suciedades)
                self.guardar_posicion_interfaz(canvas, self.tamaño_casilla, new_x, new_y, 1)
                canvas.tag_raise(text_id)
                canvas.coords(text_id, x_table, y_table)
                canvas.after(delay, self.mover_aspiradora, canvas, text_id, lista_suciedades, nuevo_Nodo, re_tour) 
            else:
                index = self.obtener_posicion((nodoAnterior.id_Casilla[0],nodoAnterior.id_Casilla[1]))
                self.lista_Casillas[index].camino[direction] = 0
                self.guardar_posicion_interfaz(canvas, self.tamaño_casilla, new_x, new_y, 0)
                canvas.after(delay, self.mover_aspiradora, canvas, text_id, lista_suciedades, nodoAnterior, re_tour) 

    def imprimir_lista(self):
        print("")
        for casillas in self.lista_Casillas:
            print((casillas.id_Casilla, casillas.camino))
        print("")    

    def obtener_posicion(self, coordenadas):
        index = 0
        for casillas in self.lista_Casillas:
            if casillas.id_Casilla == coordenadas:
                return index
            index+=1
        return None

    def clean(self, canvas, x_table, y_table, lista_suciedades):
        if (x_table,y_table) in lista_suciedades[0]:
                index = lista_suciedades[0].index((x_table,y_table))
                canvas.delete(lista_suciedades[1][index])
                lista_suciedades[0].pop(index)
                lista_suciedades[1].pop(index)
        return lista_suciedades

    def next_move(self, casilla, mandatory_address=[]):

        x_cleaner=casilla.id_Casilla[0]
        y_cleaner=casilla.id_Casilla[1]

        # mandatory_address = []
        if len(mandatory_address)==0:
            neighbor_empty_near=self.search_empty((x_cleaner, y_cleaner))
            if neighbor_empty_near != False:
                index_direction = np.random.randint(0, len(neighbor_empty_near))
                direction=neighbor_empty_near[index_direction]
            else:
                mandatory_address = self.new_tour_list(casilla)
                # print(mandatory_address)
                # direction=np.random.randint(0, 4)
                mandatory_address.pop(0)
                direction=mandatory_address.pop(0)
        else:
            direction=mandatory_address.pop(0)

        x = x_cleaner
        y = y_cleaner

        # Abajo 
        if direction == 0:
            if y_cleaner+1 < len(self.laberinto):
                y=y_cleaner+1
                x=x_cleaner
                
        # Arriba
        elif direction == 1:
            if y_cleaner-1 > -1:
                y=y_cleaner-1
                x=x_cleaner
                
        # Derecha
        elif direction == 2:
            if x_cleaner+1 < len(self.laberinto[0]):
                x=x_cleaner+1
                y=y_cleaner
                
        # Izquierda
        else:
            if x_cleaner-1 > -1:
                x=x_cleaner-1
                y=y_cleaner

        return (x, y, direction, mandatory_address)
    
    def link(self, nodoAnterior, nodoActual):
        
        #################################################################################################
        # Enlazar Nodo (Anterior, Actual)  # [Abajo, # Arriba, # Derecha, # Izquierda]

        index_anterior = self.obtener_posicion(nodoAnterior.id_Casilla)
        index_actual = self.obtener_posicion(nodoActual.id_Casilla)

        # Abajo - Arriba
        if nodoAnterior.id_Casilla[0] == nodoActual.id_Casilla[0]:

            if (nodoAnterior.id_Casilla[1]+1) == (nodoActual.id_Casilla[1]):
                self.lista_Casillas[index_anterior].camino[0] = nodoActual.id_Casilla
                self.lista_Casillas[index_actual].camino[1] = nodoAnterior.id_Casilla
            elif (nodoAnterior.id_Casilla[1]) == (nodoActual.id_Casilla[1]+1):
                self.lista_Casillas[index_anterior].camino[1] = nodoActual.id_Casilla
                self.lista_Casillas[index_actual].camino[0] = nodoAnterior.id_Casilla

        # Derecha - Izquierda
        else:

            if (nodoAnterior.id_Casilla[0]+1) == (nodoActual.id_Casilla[0]):
                self.lista_Casillas[index_anterior].camino[2] = nodoActual.id_Casilla
                self.lista_Casillas[index_actual].camino[3] = nodoAnterior.id_Casilla
            elif (nodoAnterior.id_Casilla[0]) == (nodoActual.id_Casilla[0]+1):
                self.lista_Casillas[index_anterior].camino[3] = nodoActual.id_Casilla
                self.lista_Casillas[index_actual].camino[2] = nodoAnterior.id_Casilla

    def search_empty(self, nodo):
        casilla = self.obtener_posicion(nodo)
        return neighbor_empty(self.lista_Casillas[casilla].camino)
    
    def search_square(self, list_square, squares_traveled = [], memory_square = []):
        
        new_traveled= []
        new_list_square=[]

        repeat_method = True

        # print("\n")
        # for i in list_square:
        #     print(i.id_Casilla)

        if len(list_square)==0:
            return squares_traveled
        
        for square in list_square:
            # Agregar a la lista si no se a recorrido

            if not (square.id_Casilla in memory_square):
                memory_square.append(square.id_Casilla)
                new_traveled.append(square.id_Casilla)
            
                for squa in square.camino:
                    
                    if squa == None:
                        squares_traveled.append(new_traveled)
                        return squares_traveled
                    else:
                        if squa != 0:
                            index = self.obtener_posicion(squa)
                            new_list_square.append(self.lista_Casillas[index])
                        
        
        if len(self.lista_Casillas) == len(memory_square):
            return squares_traveled

        if len(new_traveled) != 0:
            squares_traveled.append(new_traveled)

        if repeat_method:
            return self.search_square(list_square=new_list_square, squares_traveled=squares_traveled, memory_square=memory_square)
        else:
            return squares_traveled

    def new_tour_list(self, casilla):

        index=self.obtener_posicion(casilla.id_Casilla)
        list_tour = self.search_square(list_square=[self.lista_Casillas[index]], squares_traveled=[], memory_square = [])
        # print(list_tour)
        len_tour = len(list_tour)-1
        if len(list_tour)<=1:
            return [np.random.randint(0, 4)]
        target=None
        re_tour = []
        for n_tour in range(len(list_tour)):
            for squar in list_tour[len_tour-n_tour]:
                index=self.obtener_posicion(squar)
                casilla = self.lista_Casillas[index]
                if target in casilla.camino:
                    new_index =casilla.camino.index(target)
                    target= squar
                    if new_index == 0:
                        re_tour.append(0)
                    elif new_index == 1:
                        re_tour.append(1)
                    elif new_index == 2:
                        re_tour.append(2)
                    elif new_index == 3:
                        re_tour.append(3)
                    break
        
        return re_tour