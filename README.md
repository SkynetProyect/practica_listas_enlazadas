● Simularán un juego básico de confrontación Jugador-Máquina. En este caso, el
jugador estará representado por el “Alien” y la máquina por el “Depredador”.

● Al iniciar el juego, se creará una matriz enlazada como tablero de juego de NxN
donde en N posiciones de la matriz, de manera aleatoria, habrá un “+” y N
posiciones habrá un “-”, sin solaparse. Adicionalmente, en una casilla que haya
quedado vacía, aparecerá el Depredador.

● El Alien tendrá la opción de iniciar la partida en la casilla que quiera. Una vez la elija,
 aparecerá en el tablero de juego:

● Tanto el Alien como el Depredador iniciarán con 50 de vida.

● El juego funcionará por turnos: un turno para el Alien, un turno para el Depredador,
un turno para el Alien, etc.

● El juego terminará cuando alguno de los dos personajes muera.

● Al final, muestre quién ganó.

● En su turno, el Alien tiene dos opciones:

    ○ Moverse: el alien se podrá mover horizontal y verticalmente a través de la
    matriz enlazada teniendo en cuenta:
        ■ Si se mueve a una posición con un “+” su vida aumenta 10 puntos.
        ■ Si se mueve a una posición con un “-” su vida disminuye 10 puntos.
        ■ Si se mueve a la casilla donde está el Depredador, su vida disminuye
        25 puntos.
    ○ Atacar: el alien podrá atacar al Depredador siempre y cuando esté adyacente
    horizontal o verticalmente al Depredador. En este caso, le quitará 10 puntos
    de vida al Depredador.

● En su turno, el Depredador se moverá de manera aleatoria a cualquier casilla
adyacente horizontal y verticalmente, teniendo en cuenta:

    ○ Si se mueve a una posición con un “+” su vida aumenta 10 puntos.
    ○ Si se mueve a una posición con un “-” su vida disminuye 10 puntos.
    ○ Si se mueve a la casilla donde está el Alien, la vida del Alien disminuye 25
    puntos.

● Podra escoger la dificultad del juego al inicio de este, siga las instrucciones que se indican en
la consola

Hecho por Lenin Ospina Lamprea y Violeta