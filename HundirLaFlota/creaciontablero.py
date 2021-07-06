import numpy as np
import random


def crear_tablero():

    tablero = np.full((10, 10), ' ')
    t = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    counter = len(t)
    while counter > 0:
        orient = random.choice(['W', 'S', 'N', 'E'])
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        for i in t:
            if orient == 'W' and (i <= len(range(y, 0, -1))) and ('O' not in tablero[x, y:y - i:-1]):
                tablero[x, y:y - i:-1] = 'O'
                counter = counter - 1
                t.remove(i)
            elif orient == 'E' and (i <= len(range(y, 10))) and ('O' not in tablero[x, y:y + i]):
                tablero[x, y:y + i] = 'O'
                counter = counter - 1
                t.remove(i)
            elif orient == 'S' and (i <= len(range(x, 10))) and ('O' not in tablero[x:x + i, y]):
                tablero[x: x + i, y] = 'O'
                counter = counter - 1
                t.remove(i)
            elif orient == 'N' and (i <= len(range(x, 0, -1))) and ('O' not in tablero[x:x - i:-1, y]):
                tablero[x:x - i:-1, y] = 'O'
                counter = counter - 1
                t.remove(i)
    return tablero



