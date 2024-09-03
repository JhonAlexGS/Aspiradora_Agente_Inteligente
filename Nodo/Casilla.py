class Nodo:
    

    def __init__(self, id_Casilla):
        
        self.id_Casilla = id_Casilla # El identificador es la posición del elementos
        self.camino = [
            None, # Arriba
            None, # Abajo
            None, # Derecha
            None  # Izquierda
            ]