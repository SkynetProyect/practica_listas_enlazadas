from juego.modelo.abs.Nodo import Nodo


class Variable(Nodo):
    def __init__(self, valor: object):
        super().__init__(valor)
        self.vida: int
        if valor == " + ":
            self.vida = 10
        else:
            self.vida = -10
        self.tipo = "V"