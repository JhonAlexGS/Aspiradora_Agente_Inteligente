import tkinter as tk

class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Fila de 100 columnas")

        # Crear una fila con 100 columnas de Labels
        self.crear_fila()

    def crear_fila(self):
        for i in range(30):
            # Crear un Label para cada columna
            label = tk.Label(self.root, bg="red", width=1)
            # Colocar cada Label en la fila 0, columna i
            label.grid(row=0, column=i, padx=1, pady=1)

# Crear la ventana principal de Tkinter
root = tk.Tk()
app = Aplicacion(root)
root.mainloop()
