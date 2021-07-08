import time

import player1


def player2(tablero_disparos_jugador, tablero_disparos_maquina, tablero_vacio, tablero_vacio2):
    import random
    while 'O' in tablero_disparos_maquina and 'O' in tablero_disparos_jugador:
        try:

            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if tablero_disparos_maquina[x, y] == 'O':
                tablero_disparos_maquina[x, y] = 'X'
                tablero_vacio2[x, y] = 'X'
                print('Mi tablero\n', 'La máquina ha dado en el blanco!!\n', tablero_disparos_maquina)
                time.sleep(2)
                continue
            elif tablero_disparos_maquina[x, y] == ' ':
                tablero_disparos_maquina[x, y] = '-'
                tablero_vacio2[x, y] = '-'
                print('Mi tablero\n', 'La máquina ha hecho Agua!\n', tablero_disparos_maquina)
                time.sleep(2)
                player1.player1(tablero_disparos_jugador, tablero_disparos_maquina, tablero_vacio, tablero_vacio2)
            else:
                continue

        except:
            print("Error")
            continue
