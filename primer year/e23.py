"""Ejercicio 23: Se debe generar los primeros k números de la serie de Fibonacci. En la serie
los dos primeros números son el 0 y el 1. El resto se calcula como la suma de los dos
números que lo preceden. Además debe contar cuantos números primos existen en la serie
generada.
Ejemplo:
Si k = 10, entonces la serie sería: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 y la cantidad de primos es 6"""
K = int(input("ingresar los primeros numeros de la serie de Fibonacci: "))
a=0
i = 1
b = 1
if K <= 1:
    print(a)
    if K==1:
        print (b)
else:
    i = 2
    print(a,b)
    while i <=K:
        c =a+b
        print(c)
        a == b
        b == c
        i = i+1