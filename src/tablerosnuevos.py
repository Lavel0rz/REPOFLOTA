import numpy as np

import creaciontablero


def tableronuevo():
    tablero1 = creaciontablero.crear_tablero()
    tablero2 = creaciontablero.crear_tablero()

    tablero_disparos_maquina = tablero1.copy()
    tablero_disparos_jugador = tablero2.copy()
    tablero_vacio = np.full((10, 10), ' ')
    tablero_vacio2 = np.full((10, 10), ' ')
    return (tablero_disparos_maquina, tablero_disparos_jugador, tablero_vacio, tablero_vacio2)

