class Nodo:
    def __init__(self, valor):
        self.previo: Nodo = None
        self.valor = valor
        self.siguiente: Nodo = None
        self.tipo: str

    def __str__(self):
        return self.valor

