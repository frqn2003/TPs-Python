#Ejercicio 19: Un empresa que vende seguros tiene 5 vendedores (María, Juan, Pedro,
#Julieta y Rosa). Mes a mes se desea saber los resultados de las ventas y el desempeño de los
#vendedores. La empresa cuenta a fin de mes con un listado con la siguiente información:
#código de vendedor (1: María, 2: Juan, 3: Pedro, 4: Julieta y 5:Rosa) y monto de la venta.
#Se desea obtener:
#a) Total de seguros vendidos.
#b) Promedio de ventas que debería haber vendido c/vendedor.
#c) Vendedor que mas vendió.
#d) Vendedor que menos vendió.
#e) Vendedores que están por debajo del promedio.
#f) Vendedores que están por encima del promedio.
menor = 0
mayor = 0 
Monto1 = int(input("Ingresar primer Monto: ")) #Maria
Monto2 = int(input("Ingresar segundo monto: ")) #Juan
Monto3 = int(input("Ingresar tercer monto: ")) #Pedro
Monto4 = int(input("Ingresar cuarto monto: ")) #Julieta
Monto5 = int(input("Ingresar quinto monto: ")) #Rosa

PrecioPorSeguro = int(input("Ingresar el precio por seguro: "))

Z1 = Monto1//PrecioPorSeguro
Z2 = Monto2//PrecioPorSeguro
Z3 = Monto3//PrecioPorSeguro
Z4 = Monto4//PrecioPorSeguro
Z5 = Monto5//PrecioPorSeguro

Z = Z1+Z2+Z3+Z4+Z5

#a
print("El total de seguros vendidos es de: ",Z)
#b
print("Cada vendedor debio de haber vendido: ",Z//5,"seguros")
#C y D
menor = Monto1

mayor = Monto1
if Monto2 > mayor:
    mayor = Monto2
if Monto3 > mayor:
    mayor = Monto3
if Monto4 > mayor:
    mayor = Monto4
if Monto5 > mayor:
    mayor = Monto5

if Monto2 < menor:
    menor = Monto2
if Monto3 < menor:
    menor = Monto3
if Monto4 < menor:
    menor = Monto4
if Monto5 < menor:
    menor = Monto5

if Monto1 == mayor:
    print("Quien vendio mas fue Maria")
if Monto2 == mayor:
    print("Quien vendio mas fue Juan")
if Monto3 == mayor:
    print("Quien vendio mas fue Pedro")
if Monto4 == mayor:
    print("Quien vendio mas fue Julieta")
if Monto5 == mayor:
    print("Quien vendio mas fue Rosa")

if Monto1 == menor:
    print("Quien vendio menos fue Maria")
if Monto2 == menor:
    print("Quien vendio menos fue Juan")
if Monto3 == menor:
    print("Quien vendio menos fue Pedro")
if Monto4 == menor:
    print("Quien vendio menos fue Julieta")
if Monto5 == menor:
    
    print("Quien vendio menos fue Rosa")

#E y F

PromedioTotalDeVentas = (Monto1+Monto2+Monto3+Monto4+Monto5)//5

if Monto1 > PromedioTotalDeVentas:
    print("Maria esta por encima del promedio total de las ventas")
else:
    print("Maria esta por debajo del promedio total de ventas")
        
if Monto2 > PromedioTotalDeVentas:
    print("Juan esta por encima del promedio total de las ventas")
else:
    print("Juan esta por debajo del promedio total de ventas")
    
if Monto3 > PromedioTotalDeVentas:
    print("Pedro esta por encima del promedio total de las ventas")
else:
    print("Pedro esta por debajo del promedio total de ventas")
    
if Monto4 > PromedioTotalDeVentas:
    print("Julieta esta por encima del promedio total de las ventas")
else:
    print("Julieta esta por debajo del promedio total de ventas")
    
if Monto5 > PromedioTotalDeVentas:
    print("Rosa esta por encima del promedio total de las ventas")
else:
    print("Rosa esta por debajo del promedio total de ventas")
#Vendedor_maximo = max(Monto1,Monto2,Monto3,Monto4,Monto5)1
#Vendedor_minimo = min(Monto1,Monto2,Monto3,Monto4,Monto5)22222222222