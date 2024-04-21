# aqui va la consola pa ver que hace el jugad
import random

from juego.controlador.logica.AsignarPredator import AsignarPredator
from juego.controlador.logica.Matriz import Matriz
from juego.controlador.logica.AsignacionVariables import MatrizConVariables
from juego.controlador.logica.Mover import Mover
from juego.modelo.Alien import Alien
from juego.modelo.Predator import Predator
from juego.modelo.abs.Nodo import Nodo


class Juego:

    def __init__(self):
        self.tablero: Matriz
        self.moverAlien: Mover
        self.moverPredator: Mover
        self.alien: Alien
        self.predator: Predator


    def menu(self):
        print(" BIENVENIDO A JUGADOR VS MAQUINA \n")
        iniciar = input("* Nuevo juego: pulse 1 ")
        if iniciar == "1":
            tamaño_tablero = int(input("* Escoja el tamaño del tablero "))
            self.tablero = Matriz(tamaño_tablero)
            print(self.tablero)
            dificultad = int(input("* Escoja la dificultad del juego de 10 a 100 "))
            tablero_con_variables = MatrizConVariables(self.tablero, dificultad)
            print(tablero_con_variables)

            coordenadas = input("Ingrese las coordenadas donde desea iniciar ")
            fila, columna = map(int, coordenadas.split(","))

            """ celda_fila = tablero.buscarPos(fila-1)
            fila_alien = celda_fila.valor    -------------------- Idea de violeta 
            columna_alien = fila_alien.buscarPos(columna-1)
            columna_alien.valor = Alien("👽")"""
            nodoAlien = Alien("👽")

            self.moverAlien = Mover(fila, columna, self.tablero, nodoAlien)
            self.tablero = self.moverAlien.colocar(Nodo(""))

            posicionPredator = AsignarPredator(fila, columna, self.tablero.large)
            posiciones = posicionPredator.posicionRandom()
            posicionFila = posiciones[0]
            posicionColumna = posiciones[1]
            nodoPredator = Predator("🤖")
            self. moverPredator = Mover(posicionFila, posicionColumna, self.tablero, nodoPredator)
            self.tablero = self.moverPredator.colocar(Nodo(""))

            print(self.tablero)
            print(f"Vida Alien: {self.moverAlien.nodo.vida} Vida Predator: {self.moverPredator.nodo.vida}")
            for i in range(100):
                self.jugar()
                if self.moverAlien.nodo.vida == 0:
                    print("El juego llega a su fin")
                    print("El alien ha muerto")
                    break
                if self.moverPredator.nodo.vida == 0:
                    print("El juego llega a su fin")
                    print("El Predator ha muerto")
                    break


    def jugar(self):
        print(" A para izquierda, W para arriba, D para derecha, S para abajo ")
        opciones = str(input("* Escoja movimiento "))
        movimientos: list = [self.moverPredator.movimientoIzquierda,
                             self.moverPredator.movimientoAbajo,
                             self.moverPredator.movimientoDerecha,
                             self.moverPredator.movimientoArriba]

        if opciones == "a":
            self.tablero = self.moverAlien.movimientoIzquierda()
            print(self.tablero)
            print(f"Vida Alien: {self.moverAlien.nodo.vida}")
            print(f"Vida Predator: {self.moverPredator.nodo.vida}")
            print(" El predator se mueve ")
            opcion = random.choice(movimientos)
            self.tablero = opcion()
            print(f"Vida Alien: {self.moverAlien.nodo.vida}")
            print(f"Vida Predator: {self.moverPredator.nodo.vida}")
            print(self.tablero)

        elif opciones == "d":
            self.tablero = self.moverAlien.movimientoDerecha()
            print(self.tablero)
            print(f"Vida Alien: {self.moverAlien.nodo.vida}")
            print(f"Vida Predator: {self.moverPredator.nodo.vida}")
            print(" El predator se mueve ")
            opcion = random.choice(movimientos)
            self.tablero = opcion()
            print(f"Vida Alien: {self.moverAlien.nodo.vida}")
            print(f"Vida Predator: {self.moverPredator.nodo.vida}")
            print(self.tablero)
        elif opciones == "w":
            self.tablero = self.moverAlien.movimientoArriba()
            print(self.tablero)
            print(f"Vida Alien: {self.moverAlien.nodo.vida}")
            print(f"Vida Predator: {self.moverPredator.nodo.vida}")
            print(" El predator se mueve ")
            opcion = random.choice(movimientos)
            self.tablero = opcion()
            print(f"Vida Alien: {self.moverAlien.nodo.vida}")
            print(f"Vida Predator: {self.moverPredator.nodo.vida}")
            print(self.tablero)
        elif opciones =="s":
            self.tablero = self.moverAlien.movimientoAbajo()
            print(self.tablero)
            print(f"Vida Alien: {self.moverAlien.nodo.vida}")
            print(f"Vida Predator: {self.moverPredator.nodo.vida}")
            print(" El predator se mueve ")
            opcion = random.choice(movimientos)
            self.tablero = opcion()
            print(f"Vida Alien: {self.moverAlien.nodo.vida}")
            print(f"Vida Predator: {self.moverPredator.nodo.vida}")
            print(self.tablero)
        else:
            print("fila no alcanzable")


J = Juego()
J.menu()
