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

        posicion_alien = int(input("Ingrese la posicion donde desea iniciar "))
        alien = Alien(posicion_alien)


def main():
    while True:
        menu()
        break


if __name__ == "__main__":
    main()
