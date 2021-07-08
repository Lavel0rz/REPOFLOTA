import bienvenida as bienv
import creaciontablero
import finjuego
import player1
import player2
import tablerosnuevos

creaciontablero.crear_tablero()
tablero_disparos_maquina, tablero_disparos_jugador, tablero_vacio, tablero_vacio2 =tablerosnuevos.tableronuevo()
bienv.bienvenida(tablero_disparos_jugador,tablero_disparos_maquina,tablero_vacio, tablero_vacio2)
finjuego.fin_partida(tablero_disparos_maquina, tablero_disparos_jugador)