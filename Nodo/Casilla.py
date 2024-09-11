class Nodo:
    

    def __init__(self, id_Casilla):
        
        self.id_Casilla = id_Casilla # El identificador es la posición del elementos
        self.camino = [
            None, # Abajo
            None, # Arriba
            None, # Derecha
            None  # Izquierda
            ]