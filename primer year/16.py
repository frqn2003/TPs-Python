#Ejercicio 16: Dada una lista de N números enteros, mostrar todos aquellos que no sean capicúas.
N = int(input("ingresar longitud de lista: "))
I = 1
while I<=N:
    X = int(input("Ingresar un numero de la lista: "))
    S = X
    Z = 0
    while X>0:
        D = X%10
        Z = (Z*10)+D
        X = X//10
    if Z != S:
        print("El numero:",S,"no es capicua")
    I = I+1