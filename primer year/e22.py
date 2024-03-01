"""Ejercicio 22: Dada una lista de N números naturales y un dígito D, realizar lo siguiente:
1) Mostrar el segundo menor y el segundo mayor, número de la lista.
2) Mostrar los números que contengan al dígito D.
3) Buscar y mostrar el número que contenga más veces al dígito D (se supone uno
solo)"""
n = int(input("Ingresar longitud de la lista: "))
d = int(input("Ingresar digito: "))
I = 1
X = int(input("Ingresar el primer numero: "))
MC = 0
NM = 0
Z = X
while Z > 0:
    if Z%10 == d:
        MC = MC+1
        NM = X
        print("el digito ",d,"esta en el numero: ",X)
    Z = Z//10
menor = X
menor1 = 1000000000
mayor1 = 0
mayor = X
while I<n:
    x = int(input("Ingresar un numero: "))
    B = x
    CD = 0
    while B > 0:
        if B%10 == d:
            print("El digito" ,d,"esta en el numero: ",x)
            CD = CD+1
        B = B//10
    if CD > MC:
        MC = CD
        NM = x   
    if x < X:
        menor1 = X 
        menor = x
    else:
        if x>X:
            mayor1 = X
            mayor = x
    Z = x
    X = x
    I = I + 1
print ("el segundo numero mayor de la lista es: ",mayor1,"el segundo numero menor de la lista es: ", menor1)
print ("El numero que mas contiene al digito ",d,"es: ",NM,"y lo contiene una cantidad de veces :" ,MC)