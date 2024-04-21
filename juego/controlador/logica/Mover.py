from juego.controlador.logica.Matriz import Matriz
from juego.modelo.Alien import Alien
from juego.modelo.Predator import Predator
from juego.modelo.abs.Nodo import Nodo


class Mover:
    def __init__(self, filaActual: int, columnaActual: int, tablero: Matriz, nodo):

        self.filaActual = filaActual - 1
        self.columnaActual = columnaActual - 1
        self.tablero = tablero
        self.nodo = nodo
        self.encuentro: bool = False

    def colocar(self, objeto: Nodo = None):
        celda_fila = self.tablero.buscarPos(self.filaActual).valor

        columna = celda_fila.buscarPos(self.columnaActual)
        print(f"recibo --{objeto.valor}--")
        if objeto.valor != " + " and objeto.valor != " - ":
            if objeto.valor != " ___ " and objeto.valor != "":
                columna.valor = "🤖/👽"
            else:
                columna.valor = self.nodo.valor
        else:
            columna.valor = self.nodo.valor
        return self.tablero

    def borrar(self, filaVieja: int, columnaVieja: int):
        celda_fila = self.tablero.buscarPos(filaVieja).valor
        columna = celda_fila.buscarPos(columnaVieja)
        columna.valor = " ___ "

    def revisar(self, fila: int, columna: int):
        celda_fila = self.tablero.buscarPos(fila).valor
        columna = celda_fila.buscarPos(columna)
        return columna

    def ajustarVida(self, nodo):
        print(f"action vida para -{nodo.valor}-")
        if nodo.valor == " ___ " or nodo.valor == " ___ " or nodo.valor == "___":
            print("Es una casilla")
            pass
        elif nodo.valor == " + ":

            self.nodo.vida += 10
        elif nodo.valor == " - ":

            self.nodo.vida -= 10
        else:
            self.nodo.vida -= 12

    def movimientoDerecha(self):
        filaVieja = self.filaActual
        columnaVieja = self.columnaActual
        self.borrar(filaVieja, columnaVieja)
        if self.columnaActual < self.tablero.large - 1:
            self.columnaActual += 1
            presente = self.revisar(self.filaActual, self.columnaActual)
            self.ajustarVida(presente)
            self.colocar(presente)
        else:
            self.movimientoIzquierda()
        return self.tablero

    def movimientoIzquierda(self):
        filaVieja = self.filaActual
        columnaVieja = self.columnaActual
        self.borrar(filaVieja, columnaVieja)
        if self.columnaActual > 0:
            self.columnaActual -= 1
            presente = self.revisar(self.filaActual, self.columnaActual)
            self.ajustarVida(presente)
            self.colocar(presente)
        else:
            self.movimientoDerecha()
        return self.tablero

    def movimientoAbajo(self):
        filaVieja = self.filaActual
        columnaVieja = self.columnaActual
        self.borrar(filaVieja, columnaVieja)
        if self.filaActual < self.tablero.large - 1:
            self.filaActual += 1
            presente = self.revisar(self.filaActual, self.columnaActual)
            self.ajustarVida(presente)
            self.colocar(presente)
        else:
            self.movimientoArriba()
        return self.tablero

    def movimientoArriba(self):
        filaVieja = self.filaActual
        columnaVieja = self.columnaActual
        self.borrar(filaVieja, columnaVieja)
        if self.filaActual > 0:
            self.filaActual -= 1
            presente = self.revisar(self.filaActual, self.columnaActual)
            self.ajustarVida(presente)
            self.colocar(presente)
        else:
            self.movimientoAbajo()
        return self.tablero
