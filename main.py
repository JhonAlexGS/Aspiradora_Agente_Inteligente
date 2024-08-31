import tkinter as tk
from PIL import Image, ImageTk

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

def cargar_imagen(path, tamaño):
    # Cargar la imagen y redimensionarla
    imagen = Image.open(path)
    imagen = imagen.resize(tamaño, Image.ANTIALIAS)
    return ImageTk.PhotoImage(imagen)

def crear_tablero(frame):
    # Dimensiones del tablero
    filas, columnas = 8, 8
    tamaño_casilla = 80  # Tamaño de cada casilla en píxeles

    # Crear un marco para cada casilla
    for fila in range(filas):
        for columna in range(columnas):
            color = 'white' if (fila + columna) % 2 == 0 else 'black'
            x1 = columna * tamaño_casilla
            y1 = fila * tamaño_casilla

            # Crear un marco para la casilla
            casilla = tk.Frame(frame, width=tamaño_casilla, height=tamaño_casilla, bg=color)
            casilla.grid(row=fila, column=columna)

            # Opcional: Añadir un ícono en una casilla específica
            if fila == 0 and columna == 0:  # Ejemplo: Colocar un ícono en la casilla (0, 0)
                icono = cargar_imagen("ruta/a/tu/icono.png", (tamaño_casilla, tamaño_casilla))
                etiqueta_icono = tk.Label(casilla, image=icono)
                etiqueta_icono.image = icono  # Mantener una referencia para evitar que se recoja por el recolector de basura
                etiqueta_icono.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def crear_botones(frame):
    # Crear un botón
    boton = tk.Button(frame, text="Presiona Aquí", command=lambda: print("¡Botón presionado!"))
    boton.pack(pady=10)

if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Tablero de Ajedrez con Ícono y Botón")

    # Crear un Frame principal para el tablero y el botón
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Crear el tablero de ajedrez
    crear_tablero(frame)

    # Crear el botón debajo del tablero
    crear_botones(frame)

    # Ajustar el tamaño de la ventana al contenido
    root.update_idletasks()
    centrar_ventana(root)

    # Ejecutar el bucle principal de Tkinter
    root.mainloop()
