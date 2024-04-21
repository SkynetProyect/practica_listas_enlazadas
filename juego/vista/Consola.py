from juego.controlador.logica.Matriz import Matriz
from juego.controlador.logica.AsignacionVariables import MatrizConVariables
from juego.modelo.Alien import Alien
from juego.modelo.Predator import Predator
import random


def menu():
    print(" BIENVENIDO A JUGADOR VS MAQUINA \n")
    iniciar = input("* Nuevo juego: pulse 1 ")
    if iniciar == "1":
        tamaño_tablero = int(input("* Escoja el tamaño del tablero "))
        tablero = Matriz(tamaño_tablero)

        dificultad = int(input("* Escoja la dificultad del juego de 10 a 100 "))
        tablero_con_variables = MatrizConVariables(tablero, dificultad)
        print(tablero_con_variables)

        coordenadas = input("Ingrese las coordenadas donde desea iniciar ")
        fila, columna = map(int, coordenadas.split(","))

        celda_fila = tablero.buscarPos(fila-1)
        fila_alien = celda_fila.valor
        columna_alien = fila_alien.buscarPos(columna-1)
        columna_alien.valor = Alien("👽")

        fila2 = random.randint(1, 10)
        columna2 = random.randint(1, 10)

        celda_fila = tablero.buscarPos(fila2-1)
        fila_maquina = celda_fila.valor
        columna_predator = fila_maquina.buscarPos(columna2-1)
        columna_predator.valor = Predator("🤖")



        print(tablero)




def main():
    while True:
        menu()
        break


if __name__ == "__main__":
    main()
