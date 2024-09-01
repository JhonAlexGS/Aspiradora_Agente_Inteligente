import tkinter as tk

def centrar_ventana(ventana):

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

def crear_tablero(frame, filas = 8, columnas = 0, tamaño_casilla = 60):

    # Crear el lienzo para dibujar el tablero
    canvas = tk.Canvas(frame, width=columnas * tamaño_casilla, height=filas * tamaño_casilla)
    canvas.pack()

    # Dibujar las casillas del tablero
    for fila in range(filas):
        for columna in range(columnas):
            # Alternar colores entre blanco y negro
            color = 'white' if (fila + columna) % 2 == 0 else 'white'
            x1 = columna * tamaño_casilla
            y1 = fila * tamaño_casilla
            x2 = x1 + tamaño_casilla
            y2 = y1 + tamaño_casilla
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)
    
    return canvas

def crear_botones(frame):
    # Crear un botón
    boton = tk.Button(frame, text="Presiona Aquí", command=lambda: print("¡Botón presionado!"))
    boton.pack(pady=10)