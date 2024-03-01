"""Ejercicio 21: Dada una lista de número naturales, determinar si está ordenada en forma
ascendente o descendente. De lo contrario informar que no se encuentra ordenada"""
N = int(input("Ingresar longitud de la lista: "))
I = 2
X1 = int(input("Ingresar el primer numero de la lista: "))
menor = 10000000000000000000000000000000000000000000000000000000000
mayor = 0
menor = X1
b = 1
C = 1
while I<=N:
    X2 = int(input("Ingresar un numero de la lista: "))
    if X2 > X1:
        b = b+1
    I = I+1
    C = C+1
    X1 = X2
if b == C:
    print("lista ordenada ascendentemente")
if b == 1:
    print("lista ordenada descendentemente")
if b!=1 and C!=b:
    print("lista desordenada")