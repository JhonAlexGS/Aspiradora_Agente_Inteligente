import tkinter as tk

class Intefaz:

    laberinto = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self):

        print("Creando Ventana")

        self.recorrido = [
            [], # Coordenadas
            [], # Elemento Canvas
            []] # Tipo de casilla (Bloque (0) o paso libre (1))
        # self.label = None
        # self.energia = 1000

    def centrar_ventana(self, ventana):

        # Obtener el tamaño de la pantalla
        pantalla_ancho = ventana.winfo_screenwidth()
        pantalla_alto = ventana.winfo_screenheight()

        # Obtener el tamaño de la ventana después de que se haya ajustado al contenido
        ventana.update_idletasks()
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()

        # Calcular las coordenadas de la ventana para que aparezca centrada
        x = (pantalla_ancho - ancho) // 2
        y = (pantalla_alto - alto) // 2

        # Configurar la geometría de la ventana
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

    def crear_tablero(self, frame, filas = 8, columnas = 0, tamaño_casilla = 60):

        

        # Crear el lienzo para dibujar el tablero
        canvas = tk.Canvas(frame, width=columnas * tamaño_casilla, height=filas * tamaño_casilla)
        canvas.pack()

        # Dibujar las casillas del tablero
        for fila in range(filas):
            for columna in range(columnas):
                # Alternar colores entre blanco y negro
                
                color = 'white' if self.laberinto[fila][columna] == 1 else 'black'
                
                x1 = columna * tamaño_casilla
                y1 = fila * tamaño_casilla
                x2 = x1 + tamaño_casilla 
                y2 = y1 + tamaño_casilla
                canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        
        return canvas
    
    def guardar_posicion(self, canvas, tamaño_casilla, x, y, bloqueo):

        color = "orange" if bloqueo == 1 else "blue"

        self.recorrido[0].append((x,y))
        cuadrado = canvas.create_rectangle(
            tamaño_casilla*x, tamaño_casilla*y, (tamaño_casilla*x)+tamaño_casilla, (tamaño_casilla*y)+tamaño_casilla, 
            fill=color, outline="black")
        self.recorrido[1].append(cuadrado)
        self.recorrido[2].append(bloqueo)

    def crear_botones(self, frame):
        # Crear un botón
        boton = tk.Button(frame, text="Presiona Aquí", command=lambda: print("¡Botón presionado!"))
        boton.pack(pady=10)


    def crear_energia(self, frame):
        label = tk.Label(frame, text="Segundos: 0", font=("Arial", 16))
        label.pack()
        return label

    #Creación por defecto
    def crear_fila(self, frame, tamaño_casilla):
        for i in range(int(tamaño_casilla*1.68)):
            label = tk.Label(frame, bg="green", width=0)
            label.grid(row=0, column=i, padx=0, pady=1)
        return frame