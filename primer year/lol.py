M = 0
H = 0
N = int(input("Cantidad de hombres: "))
A = int(input("Cantidad de mujeres: "))
B = N+A
I = 1
S = 0
Mujer = 0
Hombre = 0
while I <= N:
    Nombre = input("Ingresar nombre: ")
    Sexo = input("ingresar sexo del hombre: ")
    Edad = int(input("ingresar edad del hombre: "))
    Pregunta = int(input("Enfermo?" "1 tos 2 fiebre 3 dolor de pecho 0 ninguno"))
    telefono = int(input("Ingresar telefono: "))
    if Pregunta !=0:
        Edad1 = Edad1+Edad
        P = P+1
        H = H+1
    else:
        Edad2 = Edad2+Edad
        Z = Z+1
    if telefono > 38800000 and telefono < 38700000:
        F = F+1
    I = I+1
I=1
while I <= A:
    Nombre = input("Ingresar nombre: ")
    Sexo = input("ingresar sexo de la mujer: ")
    Edad = int(input("ingresar edad de la mujer: "))
    Pregunta = int(input("Enfermo?" "1 tos 2 fiebre 3 dolor de pecho 0 ninguno"))
    telefono = int(input("Ingresar telefono: "))
    if Pregunta !=0:
        Edad1 = Edad1+Edad
        P = P+1
        M = M+1
    else:
        Edad2 = Edad2+Edad
        G = G+1
    if telefono > 38800000 and telefono < 38700000:
        F = F+1
    I = I+1
Promedioedad = Edad1//P
Promedioedadsin = Edad2//G
PTelefono = (F*100)//B
PromedioMujer = (M*100)//Mujer

PromedioHombre = (H*100)//Hombre    