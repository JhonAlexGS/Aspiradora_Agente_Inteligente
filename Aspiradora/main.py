import tkinter as tk
from Vista import ventana, agente, suciedad

if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Tablero de Ajedrez con Texto en Movimiento")

    n_columas = 8
    n_filas = 8
    tamaño_casilla = 60

    # Crear un Frame principal para el tablero
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    ventana.crear_botones(frame)

    # Crear el tablero de ajedrez
    canvas = ventana.crear_tablero(frame, filas=n_filas, columnas=n_columas, tamaño_casilla=tamaño_casilla)

    aspiradora = canvas.create_text(
        tamaño_casilla / 2, tamaño_casilla / 2, text="🧿", font=('Arial', 32), fill='red'
        )

    susi = suciedad.suciedad(filas=n_filas, columnas=n_columas)

    lista_suciedades = [[],[]]

    for suciedades in susi.list_suciedad:

        x = int(suciedades[1] * tamaño_casilla + tamaño_casilla / 2)
        y = int(suciedades[0] * tamaño_casilla + tamaño_casilla / 2)

        canvas_suciedades = canvas.create_text(x, y, text="💩", font=('Arial', 32), fill='brown')
        lista_suciedades[0].append((x,y))
        lista_suciedades[1].append(canvas_suciedades)

    agente_aspiradora = agente.Aspiradora()

    # Mover el texto a través del tablero
    agente_aspiradora.mover_texto(canvas, aspiradora, fila=0, columna=0, tamaño_casilla=tamaño_casilla, lista_suciedades=lista_suciedades)

    # Ajustar el tamaño de la ventana al contenido
    root.update_idletasks()
    ventana.centrar_ventana(root)

    # Ejecutar el bucle principal de Tkinter
    root.mainloop()
