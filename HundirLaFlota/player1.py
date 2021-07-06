import player2


def player1(tablero_disparos_jugador, tablero_disparos_maquina, tablero_vacio, tablero_vacio2):
    while 'O' in tablero_disparos_jugador and 'O' in tablero_disparos_maquina:
        try:

            x = int(input('J1, Introduce coordenada X'))
            if x < 0 or x > 9:
                print('Num. no valido, tira otra vez')
                continue
            y = int(input('J1, Introduce coordenada Y'))
            if y < 0 or y > 9:
                print('Num. no valido, tira otra vez')
                continue

            if tablero_disparos_jugador[x, y] == 'O':
                tablero_disparos_jugador[x, y] = 'X'
                tablero_vacio[x, y] = 'X'
                print("Tablero de la maquina\n", 'Has dado en el blanco!\n', tablero_vacio)
                continue
            elif tablero_disparos_jugador[x, y] == ' ':
                tablero_disparos_jugador[x, y] = '-'
                tablero_vacio[x, y] = '-'
                print("Tablero de la maquina\n", 'Has hecho Agua!\n', tablero_vacio)
                player2.player2(tablero_disparos_jugador, tablero_disparos_maquina, tablero_vacio, tablero_vacio2)


            else:
                print('No valido, tira otra vez')
                continue
        except:
            print("error")
            continue
