from juego.controlador.logica.Matriz import Matriz
import random

class MatrizConVariables():
    def __init__(self, matriz, n):
        self.matriz = matriz
        self.n = n
        self.GenerarVariables(n)
    def __str__(self):
        result = []
        for i in self.matriz:
            row =" ".join(str(x.valor) for x in i.valor)
            result.append(row)
        return"\n".join(result)

    def GenerarVariables(self, n):
        for i in self.matriz:
                for y in i.valor:
                    if random.random() < n/100:
                        y.valor = random.choice(["+ ", "- "])
                    else:
                        y.valor = "** "



#matriz = Matriz(2)
#n = 80
#matriznueva = MatrizConVariables(matriz, n)
#print(matriz)
