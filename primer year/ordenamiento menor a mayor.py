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
        if v[j] < v[j+1]:
            aux = v[j]
            v[j] = v[j+1]
            v[j+1] = aux
    i = i+1
print (v)"""
