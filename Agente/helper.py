import tkinter as tk

# Función para obtener la posicion de los lados vacíos de la  casilla
def neighbor_empty(casilla, target=None):
    position_none = []
    index=0
    for casillita in casilla:
        if casillita == target:
            position_none.append(index)
        index+=1
    if len(position_none) == 0:
        return False
    return position_none


def status_batery(frame, tamaño_casilla):
    for i in range(int(tamaño_casilla*1.68)):
        label = tk.Label(frame, bg="green", width=0)
        label.grid(row=0, column=i, padx=0, pady=1)
    return frame