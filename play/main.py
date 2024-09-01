import tkinter as tk
import numpy as np

num_trash = []

def centrar_ventana(ventana):
    # Obtener el tamaño de la pantalla
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    # Obtener el tamaño de la ventana después de que se haya ajustado al contenido
    ventana.update_idletasks()
    ancho = ventana.winfo_width()
    alto = ventana.winfo_height()

    # Calcular las coordenadas de la ventana para que aparezca centrada
    x = (pantalla_ancho - ancho) // 2;  y = (pantalla_alto - alto) // 2

    # Configurar la geometría de la ventana
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

def crear_tablero(frame, posicion):

    # Dimensiones del tablero
    filas, columnas = 8, 8
    tamaño_casilla = 65  # Tamaño de cada casilla en píxeles

    # Generando la cantidad de basuras
    a, b = 1, 5
    numero_aleatorio = int(np.random.uniform(a, b))
    
    for i in range(numero_aleatorio):
        a, b = 0, filas
        fila_trash = int(np.random.uniform(a, b))
        c, d = 0, columnas
        columna_trash = int(np.random.uniform(c, d))
        num_trash.append([fila_trash,columna_trash])

    # Crear el lienzo para dibujar el tablero
    canvas = tk.Canvas(frame, width=columnas * tamaño_casilla, height=filas * tamaño_casilla)
    canvas.pack()

    # Dibujar las casillas del tablero
    for fila in range(filas):
        for columna in range(columnas):
            # Alternar colores entre blanco y negro
            color = 'white' if (fila + columna) % 2 == 0 else 'black'
            x1 = columna * tamaño_casilla
            y1 = fila * tamaño_casilla
            x2 = x1 + tamaño_casilla
            y2 = y1 + tamaño_casilla
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

            if fila == 0 and columna == 0:
                # Añadir aspiradora a las casillas
                texto = f"🧿"  # Ejemplo de texto: A1, B2, etc.
                canvas.create_text(x1 + tamaño_casilla / 2, y1 + tamaño_casilla / 2,
                                text=texto, font=('Arial', 50), fill='dark green')

            if ([fila, columna] in num_trash):

                # Añadir texto a las casillas
                texto = f"💩"  # Ejemplo de texto: A1, B2, etc.
                canvas.create_text(x1 + tamaño_casilla / 2, y1 + tamaño_casilla / 2,
                                text=texto, font=('Arial', 19), fill='brown')

    canvas.after(delay, mover_texto, canvas, text_id, fila, columna, tamaño_casilla)

def crear_botones(frame):
    # Crear un botón
    boton = tk.Button(frame, text="Presiona Aquí", command=lambda: print("¡Botón presionado!"))
    boton.pack(pady=10)

def ejecutar(n_trash=1):

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Robot aspiradora")

    # Crear un Frame principal para el tablero y el botón
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Crear el tablero de ajedrez
    crear_tablero(frame, posicion=(0,0))

    # Crear el botón debajo del tablero
    crear_botones(frame)

    # Ajustar el tamaño de la ventana al contenido
    root.update_idletasks()
    centrar_ventana(root)

    # Ejecutar el bucle principal de Tkinter
    root.mainloop()

    