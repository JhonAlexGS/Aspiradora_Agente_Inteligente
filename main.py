import tkinter as tk
from Vista import ventana, suciedad
from Agente import agenteInteligente

if __name__ == "__main__":
    # Crear la ventana principal
    root = tk.Tk()
    root.title("agenteInteligente Aspiradora")

    n_columas = 10
    n_filas = 10
    tamaño_casilla = 40
    posicion_origin = (1,1)

    interfaz = ventana.Intefaz()

    # Crear un Frame principal para el tablero
    frame = tk.Frame(root)
    frame.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)
    # interfaz.crear_botones(frame)
    energia_label = interfaz.crear_energia(frame)

    frame_batery = tk.Frame(frame, bd=15)
    interfaz.crear_fila(frame_batery, tamaño_casilla)
    frame_batery.pack()

    # Crear el tablero de ajedrez
    canvas = interfaz.crear_tablero(frame, filas=n_filas, columnas=n_columas, tamaño_casilla=tamaño_casilla)

    aspiradora = canvas.create_text(
        tamaño_casilla / 2, tamaño_casilla / 2, text="🧿", font=('Arial', tamaño_casilla-13), fill='red')

    susi = suciedad.suciedad(filas=n_filas, columnas=n_columas, laberinto=interfaz.laberinto)

    lista_suciedades = [[],[]]

    for suciedades in susi.list_suciedad:

        x = int(suciedades[1] * tamaño_casilla + tamaño_casilla / 2)
        y = int(suciedades[0] * tamaño_casilla + tamaño_casilla / 2)
            
        canvas_suciedades = canvas.create_text(x, y, text="💩", font=('Arial', tamaño_casilla-13), fill='brown')
        lista_suciedades[0].append((x,y))
        lista_suciedades[1].append(canvas_suciedades)

    agenteInteligente_aspiradora = agenteInteligente.Aspiradora(laberinto=interfaz.laberinto, 
        guardar_posicion=interfaz.guardar_posicion,tamaño_casilla=tamaño_casilla, posicion_origin=posicion_origin, 
        energia_label=energia_label, frame_batery=frame_batery)

    # Mover el texto a través del tablero
    agenteInteligente_aspiradora.mover_aspiradora(canvas, aspiradora, lista_suciedades=lista_suciedades)

    # Ajustar el tamaño de la ventana al contenido
    root.update_idletasks()
    interfaz.centrar_ventana(root)

    # Ejecutar el bucle principal de Tkinter
    root.mainloop()
