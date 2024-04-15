from juego.controlador.logica.LinkedList import LinkedList
from juego.modelo.abs.Nodo import Nodo
from juego.modelo.Alien import Alien

class Matriz(LinkedList):
    def __init__(self, large):
        inicial: Nodo = Nodo(LinkedList(Nodo("**")))
        self.large: int = large
        super().__init__(inicial)

        for i in range(large - 1):
            self.agregar(Nodo(LinkedList(Nodo("**"))))

        for y in self:
            for x in range(large-1):
                y.valor.agregar(Nodo("**"))


        """            _lista: LinkedList = LinkedList(" ")
                    for y in range(large-1):
                        _lista.agregar(" ")
                    self.agregar(_lista)"""
 
    def __str__(self):
        result = []
        for i in self:
            fila =" "
            for y in i.valor:
                if isinstance(y.valor, Alien):
                    fila+=y.valor.valor
                else:
                    fila+= str(y.valor)
                fila+= " "
            result.append(fila)
        return "\n".join(result)



matris = Matriz(2)
print(matris)
