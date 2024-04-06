from juego.modelo.abs import Nodo


class LinkedList:
    def __init__(self, inicial: Nodo):  # chequeado
        self.longitud: int = 1
        self.cabeza: Nodo = inicial
        self.cola: Nodo = inicial
        self.debug: bool = True  # uso personal para pruebas

    def __iter__(self):  # chequeado
        actual: Nodo = self.cabeza
        iteraciones = self.longitud

        while actual is not None and iteraciones > 0:
            if self.debug:
                print(f"retornando en iteracion")
                print(f" nodo {actual} valor {actual.valor}")
            yield actual
            actual = actual.siguiente
            iteraciones -= 1

    def agregar(self, nodo: Nodo):  # chequeado
        if self.debug:
            print(f"Agregando nodo{nodo} con valor {nodo.valor}")
        self.cola.siguiente = nodo
        _temporal = self.cola
        self.cola = nodo
        self.cola.siguiente = self.cabeza  # circular
        self.cola.previo = _temporal
        self.longitud += 1

    def agregarInicio(self, nodo: Nodo):  # chequeado
        if self.debug:
            print(f"Agregando en cabeza")
            print(f" Nodo actual en cabeza {self.cabeza} valor {self.cabeza.valor}")
            print(f" Nueva cabeza {nodo} valor {nodo.valor}")
        cabeza_temporal = self.cabeza
        self.cabeza.previo = nodo
        self.cabeza = nodo

        self.cabeza.siguiente = cabeza_temporal
        self.cola.siguiente = self.cabeza  # actualizar circularidad
        self.longitud += 1

    def buscarPos(self, posicion):  # para buscar por posicion #chequeado
        _iteraciones = self.longitud - (self.longitud - posicion)
        _nodo: Nodo = self.cabeza

        for _i in range(_iteraciones):
            _nodo = _nodo.siguiente
        if self.debug:
            print(f' BUSCANDO  -> Nodo: {_nodo} valor: {_nodo.valor}')
        return _nodo

    def buscar(self, valor):  # para buscar segun el valor del nodo #chequeado
        for _i in range(self.longitud):
            _valor_en_pos = self.buscarPos(_i)
            if valor == _valor_en_pos.valor:
                if self.debug:
                    print(f"Se encontro el valor {valor} en la posicion {_i}")
                return _i

    def insertarPos(self, nodo: Nodo, posicion):  # chequeado

        _objeto_actual: Nodo = self.buscarPos(posicion)

        if self.debug:
            print('insertando')
            print(f'encontrado {_objeto_actual} con valor {_objeto_actual.valor} en esa posicion')

        for i in self:
            if i == _objeto_actual:
                temporal_siguiente = i.siguiente

                i.siguiente.previo = nodo
                i.siguiente = nodo
                i.siguiente.previo = i

                i.siguiente.siguiente = temporal_siguiente
                print(f'insertando {nodo} en la posicion {posicion}')
                self.longitud += 1

    def modificar(self, valor_viejo, valor_nuevo):  # chequeado
        for i in self:
            if i.valor == valor_viejo:
                if self.debug:
                    print(f"Modificando {valor_viejo} a {valor_nuevo} en nodo {i}")
                i.valor = valor_nuevo

    def borrar(self, valor):  # chequeado
        for i in self:
            if i.valor == valor:
                if self.debug:
                    print(f'valor anterior {i.previo}')
                    print(f'valor siguiente {i.siguiente}')
                    print(f"Borrando nodo {i.valor} ")

                i.previo.siguiente = i.siguiente
                i.siguiente.previo = i.previo
                self.longitud -= 1
                break

    def limpiar(self):  # chequeado
        self.longitud = 0
        self.cabeza: Nodo
        self.cola: Nodo
