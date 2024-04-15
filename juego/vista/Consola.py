from juego.controlador.logica.Matriz import Matriz
from juego.controlador.logica.AsignacionVariables import MatrizConVariables
from juego.modelo.Alien import Alien


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
        fila_alien, columna_alien = map(int, coordenadas.split(","))
        celda_alien = tablero.buscarPos(fila_alien-1)
        fila_alien = celda_alien.valor
        nodo_alien = fila_alien.buscarPos(columna_alien-1)
        nodo_alien.valor = Alien("👽")

        print(tablero)



def main():
    while True:
        menu()
        break


if __name__ == "__main__":
    main()
