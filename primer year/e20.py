"""Ejercicio 20: Un cajero automático necesita entregar dinero con la menor cantidad de
billetes posibles. Realizar un algoritmo de tal manera entregar al usuario de acuerdo al
monto de la extracción la menor de cantidad de billetes. (Considerar billetes de $100, $50,
$20, $10, $5)"""
X = int(input("Ingresar cantidad de billetes a sacar: "))
B100 = 0
B50 = 0
B20 = 0
B10 = 0
B5= 0
D = X%10
if D == 5:
        B5 = B5+1
X = X//10
C = X%10
if C == 9:
        B50 = 1
        B20 = 2
if C == 8:
        B50 = 1
        B20 = 1
        B10 = 1
if C == 7:
        B50 = 1
        B20 = 1
if C == 6:
        B50 = 1
        B10 = 1
if C == 5:
        B50 = 1
if C == 4:
        B20 = 2
if C == 3:
        B20 = 1
        B10 = 1
if C == 2:
        B20 = 1
if C == 1:
        B10 = 1
X = X//10
print(X)
P = X
I = 1
while I <=P:
        B100 = B100 + 1
        I = I+1
if C == 0 and D == 0:
        print("Para llegar al numero ",X,"con la menor cantidad de billetes se necesitan ",B100,"de 100")
else:
    if C == 0 and D != 0:
        print("Para llegar al numero ",X,"con la menor cantidad de billetes se necesitan: ",B5,"de 5 ",B100,"de 100")   
    if C != 0 and D != 0:
        print("Para llegar al numero ",X,"con la menor cantidad de billetes se necesitan: ",B5,"de 5 ", B10," de 10", B20,"de 20 ", B50,"de 50 ",B100,"de 100")