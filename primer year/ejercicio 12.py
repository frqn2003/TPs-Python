#Ejercicio 12: Determinar hasta que numero natural consecutivo es necesario sumar para llegar a un valor K. (partir del número 1)
k = int(input("ingresar el valor K: "))
I = 1
S = 0
while I <= k:
    S = S+I
    I = I+1
    if S==k:
        print(I)
if S != k:
    print("No existe numero consecutivo que sume para llegar a un valor ",k)