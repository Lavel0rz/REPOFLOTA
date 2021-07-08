import player1


def bienvenida(tablero_disparos_jugador, tablero_disparos_maquina, tablero_vacio, tablero_vacio2):
    print('¡Bienvenido a hundir la flota!\n'
          'El juego consiste en hundir los barcos de tu oponente.\n'
          'El primero que hunda los barcos del otro gana la partida.')
    player1.player1(tablero_disparos_jugador, tablero_disparos_maquina, tablero_vacio, tablero_vacio2)
