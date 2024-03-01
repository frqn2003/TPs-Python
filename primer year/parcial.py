Usuario = str(input("Ingresar usuario: "))
DNI = int(input("ingresar dni: "))
Z = DNI
I = 1
a = 0
c = 0
while DNI > 0:
    D = DNI%10
    I = 1
    c = 0
    while I <= D:
        if D%I == 0:
            c = c+1
        I = I+1
    if c == 2:
        a = a+1
    DNI = DNI//10
print(a)
A = a
print(A)
B = Z//10000000
A = A*10+B
B = Z//100000
H = B%10
A = A*10+H
B = Z//1000
H = B%10
A = A*10+H
B = Z//10
H = B%10
A = A*10+H
print(A)