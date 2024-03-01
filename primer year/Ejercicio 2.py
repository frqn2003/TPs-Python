#Ejercicio 2: De una lista de N números determinar el promedio de los positivos y el de los negativos.
N = int(input("ingresar la longitud de la lista: "))
prompositivo = 0
ContadorPositivo = 0
promnegativo = 0
ContadorNegativo = 0
I = 1
while I<=N:
    X = int(input("Ingresar un numero: "))
    if X > 0:
        ContadorPositivo = ContadorPositivo+1
        prompositivo = prompositivo + X
    else:
        ContadorNegativo = ContadorNegativo + 1
        promnegativo = promnegativo + X
    I = I + 1
prompositivo = prompositivo//ContadorPositivo
promnegativo = promnegativo//ContadorNegativo
print("El promedio de los numeros positivos es de: ",prompositivo,"y el de los negativos es: ",promnegativo)