#Ejercicio 1: Sumar N números mayores a un numero x
N = int(input("Ingresar N numeros: "))
X = int(input("Ingresar X: "))
I = 1
Suma = 0
B=0
while I<=N and B==0:
    Y = int(input("Ingresar un numero de N: "))
    if Y>=X:
        Suma = Suma+Y
    else:
        B = 1
        print("Ingresar numeros mayores a X")
    I = I+1
print("La suma de numeros mayores a: ",X,"es: ",Suma)