#Ejercicio 20: Simular el juego del tatetí.
def ganador(A, jugador):
    for i in range(3):
        if all(A[i][j] == jugador for j in range(3)) or all(A[j][i] == jugador for j in range(3)):
            return True
    if all(A[i][i] == jugador for i in range(3)) or all(A[i][2 - i] == jugador for i in range(3)):
        return True
    return False

def tateti():
    jugador= ["X", "O"]
    filas = 3
    columnas = 3
    A = [[" " for _ in range(columnas)]for _ in range (filas)]
    jugador_actual = 0
    jugando = True
    
    while jugando:
        for fila in (A):
            print (fila)
        f = int(input("Jugador {} - Elije una fila (0, 1, 2): ".format(jugador[jugador_actual])))
        c = int(input("Jugador {} - Elije una columna (0, 1, 2): ".format(jugador[jugador_actual])))
        if A[f][c] == " ":
            A[f][c] = jugador[jugador_actual]
            if ganador(A, jugador[jugador_actual]):
                for fila in (A):
                    print(fila)
                print("¡Jugador {} ha ganado!".format(jugador[jugador_actual]))
                jugando = False
            elif all(A[i][j] != " " for i in range(3) for j in range(3)):
                print("Empate")
                jugando = False
            else:
                jugador_actual = 1-jugador_actual
        else:
            print("Casilla ya ocupada")
    print("Fin del juego")
tateti()