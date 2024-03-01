A = int(input("Ingresar A: "))
while A < 0 or A >9:
    print("ingresar un valor de A entre 0 y 9: ")
    A = int(input("Ingresar A: "))
B = int(input("ingresar B: "))
while A == B:
    print("ingresar un valor de B distinto a A: ")
    B = int(input("ingresar B: "))
while B < 0 or B > 9:
    print("ingresar un valor de B entre 0 y 9: ")
    B = int(input("Ingresar B: "))
C = int(input("ingresar c: "))
while C == A or C == B:
    print("ingresar un valor de C distinto de A y B: ")
    C = int(input("ingresar c: "))
while C<0 or C>9:
    print("ingresar un valor de C entre 0 y 9: ")
    C = int(input("Ingresar C: "))
D = 0
if A > B and B > C:
    D = (A*100)+(B*10)+C
    print(D)
if B > A and A > C:
    D = (B*100)+(A*10)+C
    print(D)
if C > A and A > B:
    D = C*100+A*10+B
    print (D)
    