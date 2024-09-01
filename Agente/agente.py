import numpy as np

class Aspiradora():

    def __init__(self, laberinto, guardar_posicion) -> None:
        
        self.laberinto = laberinto
        self.guardar_posicion_interfaz = guardar_posicion


    def mover_aspiradora(self, canvas, text_id, y_cleaner, x_cleaner, tamaño_casilla, lista_suciedades,delay=200):

        while(True):

            flag = False

            ramdon_direction = np.random.randint(1, 5)

            # Abajo
            if ramdon_direction == 1:
                if y_cleaner+1 < len(self.laberinto)-1:
                    y=y_cleaner+1
                    x=x_cleaner
                    flag = True
            # Arriba
            elif ramdon_direction == 2:
                if y_cleaner-1 > -1:
                    y=y_cleaner-1
                    x=x_cleaner
                    flag = True
            # Derecha
            elif ramdon_direction == 3:
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
                    if ramdon_direction == 1:
                        y_cleaner+=1
                    elif ramdon_direction == 2:
                        y_cleaner-=1
                    elif ramdon_direction == 3:
                        x_cleaner+=1
                    elif ramdon_direction == 4:
                        x_cleaner-=1
                    break
                else:
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

        canvas.tag_raise(text_id)
        canvas.coords(text_id, x, y)

        canvas.after(delay, self.mover_aspiradora, canvas, text_id, y_cleaner, x_cleaner, tamaño_casilla, lista_suciedades)