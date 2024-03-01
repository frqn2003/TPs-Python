filas = int(input("Ingresar cantidad de filas: "))
Matriz = [[" " for _ in range(filas)] for _ in range(filas)]
for i in range(filas):
    for j in range(filas):
        Matriz[i][j] = int(input("Ingresar el elemento de la posicion {}{}: ".format(i,j)))
for fila in Matriz:
    print(fila)
suma_diagonal = 0
diagonal = []
for i in range(1, filas):
    S = 0
    n = 0
    for j in range(filas-i):
        S += Matriz[j+i][n]
        n += 1
    diagonal.append(S)
print(diagonal)