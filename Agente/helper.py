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


def status_batery(frame_batery, tamaño_casilla,current_energi,total_energia):
    total_casillas=10
    porcentaje_bateria=(total_casillas*current_energi)/total_energia
    for i in range(total_casillas):
        background="red"
        if i < porcentaje_bateria:
            background="green"
        label = tk.Label(frame_batery, bg=background, width=4)
        label.grid(row=0, column=i, padx=0, pady=1)