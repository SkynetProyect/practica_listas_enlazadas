from juego.controlador.logica.Matriz import Matriz
import random

class MatrizConVariables(Matriz):
    def __init__(self, large):
        super().__init__(large)

    def GenerarVariables(self, n):
        for i in range(n):
            fila = random.randint(0, self.large-1)
            columna = random.randint(0, self.large-1)
            nodo = self.buscarPos(fila).valor.buscarPos(columna)
            nodo.valor = random.choice(["+", "-"])



n = 2
matriz = MatrizConVariables(n)
matriz.GenerarVariables(n)
print(matriz)
