"""Dado un vector con N números, determinar la cantidad de pares y sumarlos, también contar la cantidad 
de impares y multiplicarlos, mostrar los resultados
n = int(input("Ingresar la cantidad de espacios del vector: "))
v = [None]*n
i = 0
cp = 0
ci = 0
s = 0
m = 1
while i < n:
    v[i] = int(input("Ingresar un numero del vector: "))
    if v[i]%2 == 0:
        cp =cp+1
        s = s+v[i]
    else:
        ci = ci+1
        m = m*v[i]
    i = i+1
print (v)
print (cp,ci,m,s)"""

"""2) Dado un vector con N dígitos, invertir sus elementos considerando lo siguiente:
a. Usando un vector auxiliar
b. Sin usar un vector auxiliar."""
"""n = int(input("Ingresar la cantidad de espacios del vector: "))
v = [None]*n
i = 0
while i < n:
    v[i] = int(input("Ingresar un numero del vector: "))
    i = i+1
z = [None]*n
i = n-1
l = 0
while l < n:
    z[l] = v[i]
    l = l+1
    i = i-1
print (z)"""
"""3) Dada una lista de N números, generar un vector con los números que sean capicúas.
n = int(input("Ingresar la cantidad de espacios del vector: "))
v = [None]*n
i = 0
while i < n:
    x = int(input("Ingresar un numero de la lista: "))
    num = x
    d = x%10
    c = (d*10)+d
    x = x//10
    if num == c:
        v[i] = c
    i = i+1
print (v)"""
"""4) Obtener los k primeros términos de la sucesión de Fibonacci, definida por:
FIB(1) = 1
FIB(2) = 1
FIB(3) = FIB(2)+FIB(1)
FIB (4) = FIB (3)+FIB (2)
……..
Y almacenarlos en un vector
k = int(input("Ingresar los k primeros terminos: "))
v = [None]*k
i = 0
FIB1 = 0
FIB2 = 0
while i < k:
    if i == 0:
        v[i] = 1
        FIB1 = 1
    elif i == 1:
        v[i] = 1
        FIB2 = 1
    else:
        FIB = FIB2+FIB1
        v[i] = FIB
    i = i+1
    FIB1 = FIB2
    FIB2 = v[i-1]
print (v)"""

"""5)Dado dos vectores A y B que contienen cada uno un número natural positivo, se pide componer un 
nuevo numero
Z = int(input("Ingresar la lista A: "))
J = int(input("Ingresar la lista B: "))
A = [None]*Z
B = [None]*J
i = 0
while i < Z:
    A[i] = int(input("A: "))
    i = i+1
k = 0
while k < J:
    B[k] = int(input("B: "))
    k=k+1
C = 0
i = Z-1
k = 0
while k < B:
    aux1 = B[k]
    aux2 = A[i]
    D = (D*10)+aux1
    D = (D*10)+aux2
    i = i-1
    k =k+1
print(D)"""
"""ejercicico 6
n=int(input("ingrese la dimension del vector"))
v=[None]*n
x=int(input("ingrese numero x: "))
i=0
while i<n:
    v[i]=int(input("ingrese un numero del vector: "))
    y=v[i]*(x**i)
    i=i+1
print (y)"""

""" EJERCICIO 7 A)
vector=int(input("ingrese la dimension del vector"))
v=[None]*vector
i=0
while i<vector:
    v[i]=int(input("ingrese un numero del vector: "))
    i=i+1
vector_aux = []
i = 0
while i < vector:
    bandera = 0
    j = vector-1
    while j != i:
        if v[i] == v[j]:
            bandera = 1
            break
        j = j-1
    if bandera == 0:
        vector_aux.append(v[i])
    i = i+1
print (vector_aux)"""
"""b)
vector=int(input("ingrese la dimension del vector"))
v=[None]*vector
i=0
while i<vector:
    v[i]=int(input("ingrese un numero del vector: "))
    i=i+1
i = 0
while i < vector:
    bandera = 0
    j = i+1
    while j != vector:
        if v[i] == v[j]:
            del(v[j])
            vector=vector-1
        j = j+1
    i = i+1
print (v)"""
"""ejercicio 8 a) 1)
vector=int(input("ingrese la dimension del vector"))
v=[None]*vector
i=0
while i<vector:
    v[i]=int(input("ingrese un numero del vector: "))
    i=i+1
i = 0
x = int(input("Ingresar el numero que se desea buscar: "))
while i < vector:
    bandera = 0
    if x == v[i]:
        bandera = 1
        print("El numero",x,"se encuentra en el vector.") 
        break
    i = i+1
if bandera == 0:
    print("El numero",x,"no se encuentra en el vector.")"""
"""2
vector=int(input("ingrese la dimension del vector"))
v=[None]*vector
tope = 0
i=0
while i<vector:
    x=int(input("ingrese un numero del vector: "))
    j = 0
    while j<tope and v[j]<x:
        j = j+1
    if j != tope:
        k = tope-1
        while k>=j:
            v[k+1]=v[k]
            k = k-1
    v[j] = x
    i = i+1
    tope = tope+1
print(v)
inicio = 0
fin = vector-1
bandera = 0
buscado=int(input("ingresar numero buscado: "))
while inicio<=fin:
    i=(inicio+fin) // 2
    if v[i] == buscado:
        print("el numero",buscado,"esta en el vector")
        bandera = 1
        break
    else:
        if v[i] < buscado:
            inicio = i + 1
        else:
            fin = i-1
if bandera == 0:
        print("el numero",buscado,"no esta en el vector")    """

                        ####ORDENAMIENTO POR SELECCION####
"""
vector=int(input("ingrese la dimension del vector"))
v=[None]*vector
i=0
while i<vector:
    v[i]=int(input("ingrese un numero del vector: "))
    i=i+1
for i in range(0, vector-1):
    for j in range(i+1,vector):
        if v[i]>v[j]:
            aux = v[i]
            v[i]=v[j]
            v[j]=aux
print(v)  """

            #####ORDENAMIENTO POR INSERCION#####
"""
n = int(input(":"))
v = [None]*n
tope = 0
i = 0
while i < n:
    x = int(input("x:"))
    j = 0
    while j<tope and v[j]<x:
        j = j+1
    if j != tope:
        k = tope-1
        while k>=j:
            v[k+1]=v[k]
            k = k-1
    v[j] = x
    i = i+1
    tope = tope+1
print(v)"""

                ####ORDENAMIENTO POR BURBUJA:####
"""
vector=int(input("ingrese la dimension del vector"))
v=[None]*vector
i=0
while i<vector:
    v[i]=int(input("ingrese un numero del vector: "))
    i=i+1
print (v)
i = 0
while i <vector:
    for j in range (0,vector-i-1):
        if v[j] > v[j+1]:
            aux = v[j]
            v[j] = v[j+1]
            v[j+1] = aux
    i = i+1
print (v)"""

"""#9: Dados dos vectores de números A y B, indicar si el mayor de A se encuentra en B.
n=int(input("ingrese la dimension del vector a: "))
a=[None]*n
i=0
mayora=0
while i<n:
    a[i]=int(input("ingrese los numeros del vector a: "))
    if mayora<=a[i]:
        mayora=a[i]
    i=i+1
n=int(input("ingrese la dimension del vector b: "))
b=[None]*n
i=0
bandera=0
while i<n:
    b[i]=int(input("ingrese los numeros del vector b: "))
    if mayora==b[i]:
        bandera=1
    i=i+1
if bandera==1:
    print("el mayor de a esta en el vector b")
else:
    print("el mayor de a no esta en b")"""
#10:Dados los conjuntos A y B almacenados en 2 vectores respectivamente, realizar las siguientes operaciones:
#a)union 
"""
n=int(input("ingresar la dimension del vector a: "))
a=[None]*n
i=0
while i<n:
    a[i]=int(input("ingrese los numeros de a: "))
    i=i+1
print (a)
m=int(input("ingresar la dimension del vector b: "))
b=[None]*m
j=0
while j<m:
    b[j]=int(input("ingrese los numeros de b: "))
    j = j+1
print (b)
c=[]
i=0
while i<n:
    c.append(a[i])
    i=i+1
i = n
v = 0
while v < m:
    j = 0
    bandera = 0
    while j < n and bandera == 0:
        if b[v] == a[j]:
            bandera = 1
            break 
        j = j+1
    if bandera == 0:
        c.append(b[v])
print(c)
"""
####INTERSECCION.####
"""
n=int(input("ingresar la dimension del vector a: "))
a=[None]*n
i=0
while i<n:
    a[i]=int(input("ingrese los numeros de a: "))
    i=i+1
m=int(input("ingresar la dimension del vector b: "))
b=[None]*m
j=0
while j<m:
    b[j]=int(input("ingrese los numeros de b: "))
    j = j+1
c = []
i = 0
while i < m:
    j = 0
    while j < n:
        if b[i] == a[j]:
            c.append(b[i])
            break
        j = j+1
    i = i+1
print(c)    
"""
"""
###################            A-B                ##########
n = int(input("Ingresar la dimensión del vector a: "))
a = [None] * n
i = 0

while i < n:
    a[i] = int(input("Ingrese los números de a: "))
    i = i + 1

m = int(input("Ingresar la dimensión del vector b: "))
b = [None] * m
j = 0
c = []

while j < m:
    b[j] = int(input("Ingrese los números de b: "))
    j = j + 1

i = 0

while i < n:
    j = 0
    bandera = 0
    while j < m:
        if a[i] == b[j]:
            bandera = 1
            break
        j = j + 1
    if bandera == 0:
        c.append(a[i])
    i = i + 1

print("Diferencia entre a y b:", c)
"""
"""
###################            B-A                ##########
n = int(input("Ingresar la dimensión del vector a: "))
a = [None] * n
i = 0

while i < n:
    a[i] = int(input("Ingrese los números de a: "))
    i = i + 1

m = int(input("Ingresar la dimensión del vector b: "))
b = [None] * m
j = 0
c = []

while j < m:
    b[j] = int(input("Ingrese los números de b: "))
    j = j + 1

i = 0

while i < m:
    j = 0
    bandera = 0
    while j < n:
        if b[i] == a[j]:
            bandera = 1
            break
        j = j + 1
    if bandera == 0:
        c.append(b[j])
    i = i + 1

print("Diferencia entre a y b:", c)
"""
#Ejercicio N° 2: Se tiene una lista de números enteros, ordenar la misma de mayor a menor. Mostrar en cada 
#paso como va quedando el vector. Aplicar el método de Selección y el de la Burbuja
"""
n = int(input("Ingresar longitud de la lista: "))
v = [None]*n
i = 0
tope = 0
while i < n:
    x = int(input("x:"))
    j = 0
    while j<tope and v[j]>x:
        j = j+1
    if j != tope:
        k = tope-1              ######SELECCION.
        while k>=j:
            v[k+1]=v[k]
            k = k-1
    v[j] = x
    i = i+1
    tope = tope+1
    print(v)
"""
n = int(input("Ingresar la dimensión del vector a: "))
a = [None] * n
i = 0
while i < n:
    a[i] = int(input("Ingrese los números de a: "))
    i = i + 1
i = 0
while i <n:
    for j in range (0,n-i-1):
        if a[j] < a[j+1]:
            aux = a[j]
            a[j] = a[j+1]
            a[j+1] = aux
        print(a)
    i = i+1
    

