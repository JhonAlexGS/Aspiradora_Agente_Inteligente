class Aspiradora():
    def mover_texto(self, canvas, text_id, fila, columna, tamaño_casilla, lista_suciedades,delay=200):
        # Mover el texto a la siguiente casilla
        if columna < 8:
            # Calcular la nueva posición
            x = int(columna * tamaño_casilla + tamaño_casilla / 2)
            y = int(fila * tamaño_casilla + tamaño_casilla / 2)

            if (x,y) in lista_suciedades[0]:
                index = lista_suciedades[0].index((x,y))
                canvas.delete(lista_suciedades[1][index])
                lista_suciedades[0].pop(index)
                lista_suciedades[1].pop(index)
            
            # Mover el texto a la nueva posición
            canvas.coords(text_id, x, y)

            # Avanzar a la siguiente columna
            columna += 1

            # Programar la siguiente actualización
            canvas.after(delay, self.mover_texto, canvas, text_id, fila, columna, tamaño_casilla, lista_suciedades)
        elif fila < 7:
            # Mover a la siguiente fila
            fila += 1
            columna = 0
            self.mover_texto(canvas, text_id, fila, columna, tamaño_casilla, lista_suciedades)