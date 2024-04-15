from juego.controlador.logica.Matriz import Matriz
import random

class MatrizConVariables:
    def __init__(self, matriz, n):
        self.matriz = matriz
        self.n = n
        self.GenerarVariables(n)
    def __str__(self):
        result = ""
        for i in self:
            row = ""
            for y in i.valor:
                row += str(y.valor)+" "
        result += row.strip() + "\n"
        return result

    def GenerarVariables(self, n):
        for i in self.matriz:
                for y in i.valor:
                    if random.random() < n/100:
                        y.valor = random.choice(["+", "-"])
                    else:
                        y.valor = "**"



matriz= Matriz(2)
n = 50
matriznueva = MatrizConVariables(matriz, n )
print(matriz)
