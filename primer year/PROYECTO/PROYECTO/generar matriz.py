
#Ejercicio 1: Dada una matriz de MxN elementos, calcular el promedio de cada fila y de 
#cada columna. Mostrar en pantalla la matriz cargada y los promedios correspondientes.
"""
filas=int(input(":"))
columnas=int(input(":"))
promedio_filas = 0
promedio_columnas = 0
a=[[0 for k in range(columnas)] for k in range(filas)]
for i in range(filas):
    for j in range(columnas):
        a[i][j]=int(input(""))

        #Carga de la matriz

for i in range(filas):
    print()
    for j in range(columnas):
        print(a[i][j],"",end="")

        #Muestra de la matriz

for i in range(filas):
    promedio_filas = (sum(a[i])) / columnas                         #promedio de la filas
    print("promedio de las filas es: ",promedio_filas)
for j in range(columnas):
    suma_columna = sum(a[i][j] for i in range(filas))
    promedio_columnas = suma_columna / filas                        #promedio de las columnas
    print("promedio de columnas es: ",promedio_columnas)"""

"""
filas=int(input(":"))
columnas=int(input(":"))
a=[[0 for k in range(columnas)] for k in range(filas)]
for i in range(filas):
    for j in range(columnas):
        a[i][j]=str(input(""))

        #Carga de la matriz

print("Matriz 1")
for i in range(filas):
    print()
    for j in range(columnas):
        print(a[i][j],"",end="")

        #Muestra de la matriz

for j in range(columnas):
    columna = [a[i][j] for i in range(filas)]
    columna.sort()
    for i in range(filas):
        a[i][j] = columna[i]

print("Matriz 2")

for i in range(filas):
    print()
    for j in range(columnas):
        print(a[i][j],"",end="")
"""
    
"""filas=int(input(":"))
a=[[0 for k in range(filas)] for k in range(filas)]
for i in range(filas):
    for j in range(filas):
        a[i][j]=int(input(""))

suma_diagonal = 0
for i in range(filas):
    suma_diagonal += a[i][i]
print(suma_diagonal)

v = []
for i in range(filas):
    for j in range(filas):
        factorial = 1
        for k in range(1, (a[i][j])+1):
            factorial = factorial * k
        if factorial >= suma_diagonal:
            v.append(a[i][j])
print(v)

v = list(set(v))

for i in range(v):
    j = i+1
    while j < len(v):
        if v[i] == v[j]:
            del v[j]
        else:
            j = j+1

print("Matriz 1")
for i in range(filas):
    print()
    for j in range(filas):
        print(a[i][j],"",end="")
"""

"""k = int(input("Ingresar cantidad de matrices: "))
a = 0
while a < k:
    filas = int(input("Ingresar cantidad de filas: "))
    columnas = int(input("Ingresar cantidad de columnas: "))
    matriz = [[0 for q in range(filas)] for q in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = int(input(f"ingresar el elemento de la posicion ({i},{j}) :"))
    suma_diagonal = 0
    for i in range(filas):
        suma_diagonal =+ matriz[i][i]
    print(suma_diagonal)
    if suma_diagonal == 0:
        for i in range(filas):
            print()
            for j in range(filas):
                print(matriz[i][j], "",end="")
    a = a+1
""""""
filas = int(input("Ingresar cantidad de filas: "))
columnas = int(input("Ingresar cantidad de columnas: "))
A = [[0 for k in range(filas)] for k in range(filas)]
B = [[0 for _ in range(filas)] for _ in range(filas)]
for i in range(filas):
    for j in range(columnas):
        A[i][j] = int(input(f"ingresar el elemento de la posicion ({i},{j}) :"))
        B[i][j] = int(input(f"Ingresar el elemento de la posicion ({i},{j}) :"))
contador_repetidos = 0

matriz_repetidos = []
for i in range(filas):
    contador_repetidos = 0
    for j in range(columnas):
        if A[i][j] == B[i][j]:
            contador_repetidos = contador_repetidos+1
    if contador_repetidos > 0:
        matriz_repetidos.append((i, contador_repetidos))
print("Matriz de elementos repetidos")
print (matriz_repetidos)"""



"""filas = int(input("Ingresar cantidad de filas: "))
columnas = int(input("Ingresar cantidad de columnas: "))
A = [[0 for k in range(columnas)] for k in range(filas)]
B = [[0 for _ in range(columnas)] for _ in range(filas)]
for i in range(filas):
    for j in range(columnas):
        A[i][j] = int(input(f"ingresar el elemento de la posicion ({i},{j}) :"))
        B[i][j] = int(input(f"Ingresar el elemento de la posicion ({i},{j}) :"))
v = []
for i in range(filas):
    for j in range(columnas):
        octal = oct(A[i][j])[2:]
        octalb = str(B[i][j])
        if octal == octalb:
            v.append(A[i][j])
print(v)
"""
contador_dni = 0
matriz = []
v = []
while True:
    print("Desea el usuario ingresar mas dnis?")
    pregunta = str(input("Si o no: ")).upper()
    if pregunta == "NO":
        False
        break
    if pregunta == "SI":
        DNI = int(input("Ingresar el DNI: "))
        v.append(DNI)
        digito = [int(digito) for digito in str(DNI)]
        matriz.append(digito)
        contador_dni = contador_dni+1
filas = contador_dni
columnas = 8
b = []
A = [0 for k in range(columnas) for k in range(filas)]
for i in range (filas):
    contador = 0
    for j in range(columnas):
        if matriz[i][j] % 2 != 0:
            contador = contador + 1
    if contador == 8:
        digito2 = [int(digito) for digito in str(v[i])]
        b.append(digito2)
for fila in b:
    print(fila)