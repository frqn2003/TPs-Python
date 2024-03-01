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

n = int(input("Ingresar la dimensión del vector a: "))
a = [None] * n
i = 0
while i < n:
    a[i] = int(input("Ingrese los números de a: "))
    i = i + 1
i = 0
while i <n:
    for j in range (0,n-i-1):                               #BURBUJA
        if a[j] < a[j+1]:
            aux = a[j]
            a[j] = a[j+1]
            a[j+1] = aux
        print(a)
    i = i+1
    """

##Ejercicio N° 3: Dada una lista de N números ordenados, insertar M números en los lugares que corresponda 
##de tal manera que la lista preserve el orden.
"""
N = int(input("Ingresar lista ordenada: "))
i = 0
v = [None]*N
while i < N:
    v[i] = int(input("Ingresar numeros: "))
    i = i+1
tope = 0
M = int(input("Ingresar lista a reemplazar: "))
b = [None]*M
h = 0
while h <M:
    b[h]=int(input("Ingresar numeros de la segunda lista: "))
    h = h+1
l = []
i = 0
while i < N:
    l.append(v[i])
    i = i+1
h = 0
while h < M:
    l.append(b[h])  
    h = h+1
p = N+M
i = 0
while i < p:
    for j in range (0,p-i-1):
        if l[j] > l[j+1]:
            aux = l[j]
            l[j] = l[j+1]
            l[j+1] = aux
    i = i+1
print(l)"""
#Ejercicio N° 4: Dada una lista de palabras, contar cuantas vocales y consonantes tiene cada palabra. Mostrar 
#además de cada vocal encontrada la posición de esa vocal dentro de la palabra. Usar la función lenght.

N = int(input("Ingresar lista: "))
z = 0
l = []
while z < N:
    x= str(input("Ingresar una palabra: "))
    l.append(x)
    z = z+1
print (l)
z = 0
cV= 0
cC = 0
while z < N:
    if "a"in l[z]:
        cV = +1       
        print("la vocal encontrada es a y en la posicion: ",z)
    elif "i"in l[z]:
        cV = +1
        print("la vocal encontrada es i y en la posicion: ",z)
    elif "o"in l[z]:
        cV = +1
        print("la vocal encontrada es o y en la posicion: ",z)
    elif "u"in l[z]:
        cV = +1
        print("la vocal encontrada es u y en la posicion: ",z)
    elif "e" in l[z]:
        cV = +1
        print("la vocal encontrada es e")
    else:
        cC= +1
    z = z+1
print("La cantidad de vocales son: ",cV,"y la cantidad de consonantes son: ",cC)  