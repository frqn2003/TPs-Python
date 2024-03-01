#Ejercicio 14: Dado un numero entero, determinar la cantidad de dígitos que tiene.
X = int(input("Ingresar un numero: "))
C = 0
while X>0:
    X=X//10
    print(X)
    C = C+1
print("Cantidad de digitos es: ",C)