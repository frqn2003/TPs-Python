vot1 = str(input("Ingresar el primer cantante: "))
vot2 = str(input("Ingresar el segundo cantante: "))
vot3 = str(input("Ingresar el tercer cantante: "))
vot4 = str(input("Ingresar el cuarto cantante: "))
vot5 = str(input("Ingresar el quinto cantante: "))
voto1 = 0
voto2= 0
voto3= 0
voto4 = 0
voto5 = 0
I = 1
while I != 0:
    voto = int(input("Ingresar el voto: (Si quiere votar al primer cantante ingresar 1, si cantante 2 ingresar 2, si cantante 3 ingresar 3, si cantante 4 ingresar 4, si cantante 5 ingresar 5)"))
    if voto == 1:
        voto1 = voto1+1
    elif voto == 2:
        voto2 = voto2+1
    elif voto == 3:
        voto3 = voto3 +1
    elif voto == 4:
        voto4 = voto4+1
    elif voto == 5:
        voto5 = voto5+1
    N = str(input("Desea seguir ingresando valores: ").upper())
    if N == "SI":
        I = 1
    if N == "NO":
        I = 0
print(voto1,voto2,voto3,voto4,voto5)
mayor1 = 0
cmv1 = 0
cmv2 =0
mayor2 = 0
if voto1 >mayor1:
    mayor2 = mayor1
    mayor1 = voto1
    cm1 = vot1
if voto2 > mayor1:
    mayor2 = mayor1
    mayor1 = voto2
    cm1 = vot2
if voto3 > mayor1:
    mayor2 = mayor1
    mayor1 = voto3
    cm1 = vot3
if voto4 > mayor1:
    mayor2 = mayor1
    mayor1 = voto4
    cm1 = vot4
if voto5 > mayor1:
    mayor2 = mayor1
    mayor1 = voto5
    cm1 = vot5
print (mayor1, mayor2, cm1)
