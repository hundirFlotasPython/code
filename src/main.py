from partida import *


partida = Partida(solicitar_datos_jugador(),"Skynet", solicitar_nivel_dificultad())

print(f'Empezamos {partida.jugadorA.nombre} !\nLucharás contra Skynet!!\n\n\n')
temp = input("Pulsar enter para continuar")
clearConsole()

exportar_flotas(partida.jugadorA.dict_flota_propia, partida.jugadorB.dict_flota_propia)

while True:
    temp = ''
    if partida.jugadorA.realizar_disparo(partida.jugadorB.flota_propia, partida.nivel_dificultad) == 'OK':
        if partida.jugadorA.humano:
            temp = input("Has ganado {}!\n\nPulsa ENTER para finalizar.\n".format(partida.jugadorA.nombre))
        else:
            print("Has ganado {}!\n\n".format(partida.jugadorA.nombre))
        break
    else:
        if partida.jugadorA.humano:
            temp = input("Pulsar enter para continuar")
        clearConsole()

    if partida.jugadorB.realizar_disparo(partida.jugadorA.flota_propia, partida.nivel_dificultad) == 'OK':
        if partida.jugadorB.humano:
            temp = input("Has ganado {}!\n\nPulsa ENTER para finalizar.\n".format(partida.jugadorB.nombre))
        else:
            print("Has ganado {}!\n\n".format(partida.jugadorB.nombre))
        break
    else:
        if partida.jugadorB.humano:
            temp = input("Pulsar enter para continuar")
        clearConsole()

clearConsole()
partida.generar_estadisticas()
sys.exit("\n\nHasta luego {}!!".format(partida.jugadorA.nombre))

