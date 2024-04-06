from juego.modelo.abs.Nodo import Nodo


class Predator(Nodo):
    def __init__(self, valor: object):
        super().__init__("🤖")
        self.vida: int = 50