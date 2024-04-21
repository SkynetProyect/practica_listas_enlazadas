import random


class AsignarPredator:
    def __init__(self, filaJugador:int, columnaJugador: int, matrizlongitud: int):

        self.columnaJugador = columnaJugador
        self.filaJugador = filaJugador
        self.matrizlongitud = matrizlongitud


    def posicionRandom(self):
        filaPredator = random.randint(1, self.matrizlongitud)
        columnaPredator = random.randint(1, self.matrizlongitud)
        if (filaPredator == self.filaJugador) or (columnaPredator == self.columnaJugador):
            self.posicionRandom()

        return [filaPredator,columnaPredator]
