#Ejercicio 18: Calcular cuantos días hay entre dos fechas de un mismo año no bisiesto
Dia1= int(input("ingresar el dia de la primera fecha: "))
Mes1= int(input("ingresar el mes de la primera fecha: "))
Dia2= int(input("ingresar el dia de la segunda fecha: "))
Mes2= int(input("ingresar el mes de la segunda fecha: "))
Fecha = Dia1-Dia2
if Mes1>Mes2:
    Z = Mes1-Mes2
else:
    Z = Mes2-Mes1
Y = Z * 30
X = Y+Fecha
print(X)