

# Función para obtener la posicion de los lados vacíos de la  casilla
def neighbor_empty(casilla):
    position_none = []
    index=0
    for casillita in casilla:
        if casillita == None:
            position_none.append(index)
        index+=1
    if len(position_none) == 0:
        return False
    return position_none