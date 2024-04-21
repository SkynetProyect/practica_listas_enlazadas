from juego.modelo.abs.Nodo import Nodo


class Alien(Nodo):
    def __init__(self, valor):
        super().__init__(valor)
        self.vida: int = 50

