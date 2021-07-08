# HUNDIR LA FLOTA

## Descripción del proyecto
Programa del juego Hundir la flota desarrollado en siete scripts: main.py, bienvenida.py, creaciontablero.py, tablerosnuevos.py, player1.py, player2.py y finjuego.py.  

**Inicio del juego**

* El programa se ejecuta con main.py.
* Primero se inicializan los tableros de 10x10 desde la función `crear_tablero()` del script creaciontablero.py. Se generan aleatoriamente cuatro barcos de eslora 1, tres barcos de eslora 2, dos barcos de eslora 3 y un barco de eslora 4. Los barcos no pueden superponerse ni salirse del tablero, aunque no dejan espacio entre ellos.  
Con la función `tableronuevo()` recogida en el script tablerosnuevos.py, creamos cuatro tableros: tablero_disparos_maquina, tablero_disparos_jugador, tablero_vacio y tablero_vacio2.
  * El `tablero_vacio` es el tablero que se muestra al jugador y en el que juega. Se le va mostrando "X" para tocado y "-" para agua.
  * El `tablero_disparos_jugador` es donde están todos los barcos de la máquina y donde se van comprobando los disparos del jugador, si es agua o tocado, y donde se van cambiando "O" (barco) por "X" (tocado) y por "-" (agua). Este tablero no se muestra.
  * El `tablero_vacio2` es el tablero que se le muestra a la máquina y donde juega.
  * El `tablero_disparos_maquina` es donde están todos los barcos del jugador y se van comprobando los disparos de la máquina. Este tablero no se muestra. 

* La función `bienvenida()` del script bienvenida.py, da la bienvenida al juego, lo explica, y le pide al jugador (J1) que introduzca las primeras coordenas, y llama a la función `player1()`.  

**Dinámica del juego**

* El primero en jugar es el jugador (J1). Los cambios en los tableros los realiza la función `player1()` del script player1.py. La función recoge las coordenadas del jugador y comprueba si es agua o tocado. Si es tocado, realiza los cambios en los tableros y el jugador continua jugando. Si es agua, pasa el turno a la máquina llamando a la función `player2()` del script player2.py. (Están excepcionadas entradas de coordenadas distintas al rango del 1 al 9).

* La función `player2()` gestiona el turno de la máquina. En este caso no hay entrada de coordenadas, sino que se generan aleatoriamente. Hechas las comprobaciones del disparo y las anotaciones en los tableros tablero_disparos_maquina y tablero_vacio2, la función llama a la función `player1()` cuando acaba su turno al hacer agua.

* Las funciones `player1()` y `player2()` se van llamando mientras hay algún barco en los tableros `tablero_disparos_jugador` y `tablero_disparos_maquina`, es decir, mientras contengan "O".  

**Fin del juego**

* Cuando no quedan barcos en alguno de los tableros, se acaba el juego y gana quien haya hundido primero los barcos del contrincante. 
  * La función `finpartida()` del script finjuego.py imprime "Enhorabuena J1, has ganado" si gana el jugador (es decir, si aún quedan "O" en el tablero_disparos_maquina y no quedan "O" en el tablero_disparos_jugador).
  * La función imprime "La maquina te derrotó" en caso contrario.

## Autores 

Julio Bravo-Ferrer Acosta  
Nieves Noha Pascual

## Librerías y recursos utilizados
Las librerías que hemos utilizado son: Numpy, Random y Time.

