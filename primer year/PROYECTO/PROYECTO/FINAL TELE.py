vector = []
filas = 0
columnas = 2
while True:
    pregunta = int(input("Desea cargar un refran? (Si=1/No=0): "))
    if pregunta == 0:
        False
        break
    if pregunta == 1:
        refran = str(input("Ingrese el refran: "))
        filas += 1
        vector.append(refran)

Matriz = [[None for k in range (columnas)] for k in range (filas)]

for i in range (len(vector)):
    cantidad_palabras = 1
    for j in range (len(vector[i])):
        if vector[i][j] == " ":
            cantidad_palabras += 1
    Matriz[i][0] = cantidad_palabras

vector_vocales = ("a", "e", "i", "o", "u")

for i in range (len(vector)):
    vector_palabras = vector[i].split()
    mayor = " "
    c2 = 0
    for j in range (len(vector_palabras)):
        palabra = str(vector_palabras[j])
        cc = 0
        for t in range (len(palabra)):
            if palabra[t] != vector_vocales:
                cc += 1
        if cc > c2:
            mayor = palabra
    
    Matriz[i][1] = mayor

for fila in Matriz:
    print(fila)

MatrizGod = sorted(Matriz, key= lambda x: x[1].lower())

for fila in MatrizGod:
    print(fila)

