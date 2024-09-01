import numpy as np

class Aspiradora():

    def __init__(self, laberinto) -> None:
        self.recorrido = [[],[]]
        self.laberinto = laberinto


    def mover_texto(self, canvas, text_id, y_cleaner, x_cleaner, tamaño_casilla, lista_suciedades,delay=200):

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


        x = int(x_cleaner * tamaño_casilla + tamaño_casilla / 2)
        y = int(y_cleaner * tamaño_casilla + tamaño_casilla / 2)

        # Algoritmo de decisión

        if (x,y) in lista_suciedades[0]:
            index = lista_suciedades[0].index((x,y))
            canvas.delete(lista_suciedades[1][index])
            lista_suciedades[0].pop(index)
            lista_suciedades[1].pop(index)

        # print(self.recorrido)
        self.guardar_posicion(canvas, tamaño_casilla, x_cleaner, y_cleaner)

        # Mover el texto a la nueva posición
        canvas.tag_raise(text_id)
        canvas.coords(text_id, x, y)

        canvas.after(delay, self.mover_texto, canvas, text_id, y_cleaner, x_cleaner, tamaño_casilla, lista_suciedades)
        


    def guardar_posicion(self, canvas, tamaño_casilla, x, y):
        self.recorrido[0].append((x,y))
        cuadrado = canvas.create_rectangle(
            tamaño_casilla*x, tamaño_casilla*y, (tamaño_casilla*x)+tamaño_casilla, (tamaño_casilla*y)+tamaño_casilla, 
            fill="orange", outline="black")
        self.recorrido[1].append(cuadrado)
        