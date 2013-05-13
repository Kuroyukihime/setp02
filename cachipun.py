print("Juego de Cachipun")

import random    # La librería random es para escoger una opcion al azar en este programa. 

#Función que revisa los datos ingresados de los usuarios y escoge al ganador.
def ganador_cachipun(Cachipun, n):
    if n == 1:    # Si el valor es 1 quiere decir que se esta jugando con dos jugadores presenciales.
        if Cachipun[0][1] == Cachipun[1][1]:    # Se comprueba según la lista si fue un empate.
            print (Cachipun)    # Se muestra la lista común.
            print ("Jugador", Cachipun[0][0], "gana la partida.")    # En caso positivo se anuncia ganador al jugador1.
        elif (Cachipun[0][1] == "T" and Cachipun[1][1] == "P") or (Cachipun[0][1] == "P" and Cachipun[1][1] == "R") or (Cachipun[0][1] == "R" and Cachipun[1][1] == "T"):    # Se pregunta por si, en todos los casos posibles, el jugador1 es el ganador.
            print (Cachipun)    # Se muestra la lista antes de mostrar al ganador.
            print ("Jugador", Cachipun[0][0], "gana la partida.")    # Se muestra al ganador para terminar.
        else:    # Si no es ganador el jugador1, por defaul es el jugador2 el ganador.
            print (Cachipun)
            print ("Jugador", Cachipun[1][0], "gana la partida.")    # Se muestra el ganador.
    else:    # Si no es 1, se esta jugando una partida con el PC.
        if Cachipun[0][1] == Cachipun[1][1]:    # Se comprueba si no ha habido empate, en ese caso el jugador1 gana.
            print (Cachipun)    # Se muestra la lista con lo jugado por ambos.
            print ("Jugador", Cachipun[0][0], "gana la partida.")    # Se muestra finalmente al ganador.
        elif (Cachipun[0][1] == "T" and Cachipun[1][1] == "P") or (Cachipun[0][1] == "P" and Cachipun[1][1] == "R") or (Cachipun[0][1] == "R" and Cachipun[1][1] == "T"):    # Se comprueba si el ganador es el jugador1.
            print (Cachipun)    # se muestra la lista común.
            print ("Jugador", Cachipun[0][0], "gana la partida.")    # Se imprime el nombre del ganador.
        else:    # Si no es ninguna de las opciones el PC es el ganador.
            print (Cachipun)    # Se muestra lo jugado por cada jugador.
            print ("PC es el ganador. Pierdes la partida")    # Se imprime el resultado. 

cant = int(input("Ingrese cantidad de jugadores (1 = contra el PC): "))    #Se pide la cantidad de jugadores y se guarda en cant.

if (cant <= 0 or cant >= 3) :    # Si se escoge una opcion que no sea 1 o 2 se lanza una excepción.
    raise Exception("Cantidad incorrecta de jugadores.")
elif cant == 2 :    # Si la cantidad es correcta se entra al juego, en este caso, de dos.
    jugador1 = input("Nombre del primer jugador: ")    # se pide y guarda el nombre del primer jugador en jugador1.
    jugador2 = input("Nombre del segundo jugador: ")    # se pide y guarda el nombre del segundo jugador en jugador2 tambien.
    print ("Los lanzamientos pueden ser: T (Tijeras), P (Papel) y R (Piedra).")    # se da a conocer el tipo de opcion para jugar.
    jugada1 = input("Jugada 1: ")    # De lo anterior el jugador1 ingresa una opcion primero y se guarda en jugada1.
    jugada1 = jugada1.upper()    # Transforma el string jugada1 a mayúscula para evitar errores.
    if not (jugada1 == "T" or jugada1 == "P" or jugada1 == "R"):    # Si no es ninguna de las opciones se envía una excepción.
        raise Exception("Jugada no válida.")
    jugada2 = input("Jugada 2: ")    # Se pide, luego, la jugada del jugador2 si es que la anterior no fue erronea.
    jugada2 = jugada2.upper()    # Transforma el string jugada2 a mayúscula también.
    if not (jugada2 == "T" or jugada2 == "P" or jugada2 == "R"):    # si la opción del segundo jugador es incorrecta se envía una excepxión.
        raise Exception("Jugada no válida.")
    Cachipun = [[jugador1, jugada1], [jugador2, jugada2]]    # Se guardan dos listas con la infomación de cada jugador y ambas se pasan a una lista común.
    ganador_cachipun(Cachipun, 1)    # Llamada a la función que escoge el ganador según los datos enviados en la lista.
else:    # Si la cantidad es 1, se juega contra el PC.
    jugador1 = input("Nombre del jugador: ")    # Se ingresa el nombre del jugador a jugador1.
    jugador2 = "PC"    # El nombre del jugador2 es por defecto "PC".
    print ("Los lanzamientos pueden ser: T (Tijeras), P (Papel) y R (Piedra).")    # Se muestran las posibles opciones a escoger.
    jugada1 = input("Jugada: ")    # Se pide la opción del jugador y se guarda en jugada1.
    jugada1 = jugada1.upper()    # Transforma la palabra jugada a mayúscula.
    if jugada1 == "T" or jugada1 == "P" or jugada1 == "R":    # Si la jugada del jugador1 es correcta se ingresa al if.
        jugadaspos = ["T", "P", "R"]    # Se ingresan a una lista auxiliar las posibles opciones que el PC puede escoger.
        jugada2 = random.choice(jugadaspos)    # Se usa random para escoger una opcion de la lista anterior para jugar contra el jugador1.
        Cachipun = [[jugador1, jugada1], [jugador2, jugada2]]    # Se guardan las opciones en la lista común.
        ganador_cachipun(Cachipun, 2)    # Llamada a la función que escoge el ganador según los datos enviados en la lista.
    else:
        raise Exception("Jugada no válida.")    # Si la jugada del jugador no calza con las opciones se imprime una excepción.








