class Nodo:
    def __init__(self, valor: object):
        self.previo: Nodo = None
        self.valor: object = valor
        self.siguiente: Nodo = None