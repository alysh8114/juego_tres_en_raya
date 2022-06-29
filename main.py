import random
def inicio_juego():
    print("~~~~~~BIENVENIDO AL JUEGO TRES EN RAYA~~~~~~")
    while True:
        ficha = input("Seleccione ficha: X - 0\n")
        ficha = ficha.upper()
        if ficha=="X":
            persona = "X"
            computadora = "O"
            break
        if ficha =="0":
            persona = "0"
            computadora = "X"
            break
        else:
            print("Por favor, introduce una ficha posible.")
    return (persona, computadora)

def tablero():
    print("**************TRES EN RAYA**************")
    print()
    print("1            |2            |3              ")
    print("      {}      |      {}      |      {}        ".format(matriz[0], matriz[1], matriz[2]))
    print("             |             |             ")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print("4            |5            |6              ")
    print("      {}      |      {}      |      {}        ".format(matriz[3], matriz[4], matriz[5]))
    print("             |             |             ")
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print("7            |8            |9              ")
    print("      {}      |      {}      |      {}        ".format(matriz[6], matriz[7], matriz[8]))
    print("             |             |             ")

def empate(matriz):
    empate =True
    i = 0
    while(empate==True and i<9):
        if matriz[i] == " ":
            empate = False
        i = i+1

    return empate

def victoria(matriz):
    if(matriz[0]==matriz[1]==matriz[2]!=" "or matriz[3]==matriz[4]==matriz[5]!=" "or matriz[6]==matriz[7]==matriz[8]!=" "or
    matriz[0]==matriz[3]==matriz[6]!=" "or matriz[1]==matriz[4]==matriz[7]!=" "or matriz[2]==matriz[5]==matriz[8]!=" "or
    matriz[0]==matriz[4]==matriz[8]!=" "or matriz[2]==matriz[4]==matriz[6]!=" "):
        return True
    else:
        return False

def movimiento_jugador():
    while True:
        posiciones=[0,1,2,3,4,5,6,7,8,9]
        casilla=int(input("Seleccione casilla: "))
        if casilla not in posiciones:
            print("Casilla no disponible")

        else:
            if matriz[casilla-1] == " ":
                matriz[casilla-1] = persona
                break
            else:
                print("Casilla no disponible")

def movimiento_ordenador():
    posiciones = [0,1,2,3,4,5,6,7,8]
    casilla = 9
    parar = False

    for i in posiciones:
        copia = list(matriz)
        if copia[i] == " ":
            copia[i] = computadora
            if victoria(copia) == True:
                casilla = i
    if casilla == 9:
        for j in posiciones:
            copia = list(matriz)
            if copia[j] == " ":
                copia[j] = persona
            if victoria(copia) == True:
                casilla = j
    if casilla == 9:
        while(not parar):
            casilla = random.randint(0,8)
            if matriz[casilla] == " ":
                parar = True
    matriz[casilla] = computadora

while True:
    matriz = [" "]*9
    persona,computadora = inicio_juego()
    partida = True
    ganador = 0

    while partida:
        ganador = ganador+1
        tablero()

        if victoria(matriz):
            if ganador%2 == 0:
                print("**Gana el jugador**")
                print("**Fin del juego TRES EN RAYA**")
                partida = False
            else:
                print("**Gana el ordenador**")
                print("**Fin del juego TRES EN RAYA**")
                partida=False
        elif empate(matriz):
            print("**Empate**")
            print("**Fin del juego TRES EN RAYA**")
            partida = False

        elif ganador%2 == 0:
            print("El ordenador está pensando")
            movimiento_ordenador()

        else:
            movimiento_jugador()
