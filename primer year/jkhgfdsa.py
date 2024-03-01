#cuatro categorias: mi=2 veces, no=3 veces, av= 6 veces, su= mas de dos acividades
# avanzado y superior= 5000pe , minimo= 2000pe, normal=3000pe
#cantidad de socios total y cantidad por categoria, el monto total por categoria, mayor1 y mayor2 de monto, categoria por debajo del promedio
ban=0
i = 0
contmi=0
contno=0
contav=0
contsu=0
preciomi=0
preciono=0
precioav=0
preciosu=0
while ban==0:
    categorias = str(input("Ingresar categorias: si desea salir ingresar salir ").upper())
    if categorias=="SALIR":
        ban=1
    codigo=int(input("ingresar codigo de socio: "))
    if categorias=="MINIMO":
        contmi=contmi+1
        preciomi = preciomi + 2000
    if categorias=="NORMAL":
        contno=contno+1
        preciono = preciono + 3000
    if categorias=="AVANZADO":
        contav=contav+1
        precioav = +5000
    if categorias=="SUPERIOR":
        contsu=contsu+1
        preciosu = +5000
    if categorias=="SALIR":
        ban=1
    i = i+1
p=1
print(i)
print(preciomi,preciono,precioav,preciosu)
mayor = 0
m2 = 0
if mayor < preciomi:
    m2 = mayor
    mayor = preciomi

if mayor < preciono:
    m2 = mayor
    mayor = preciono
if mayor < precioav:
    m2 = mayor
    mayor = precioav
if mayor < preciosu:
    m2 = mayor
    mayor = preciosu

if mayor == preciomi:
    print("Categoria minima")
if mayor == preciono:
    print("Categoria normal")
if mayor == precioav:
    print("la mas que recaudo Categoria avanzada")
if mayor == preciosu:
    print("Categoria superior")
if m2 == preciomi:
    print("2Categoria minima")
if m2 == preciono:
    print("2Categoria normal")
if m2 == precioav:
    print("2Categoria avanzada")
if m2 == preciosu:
    print("2Categoria superior")
ptotal = (preciomi+preciono+precioav+preciosu)//i
if preciomi<ptotal:
    print("Categoria minima por debajo del promedio")
if preciono<ptotal:
    print("Categoria normal por debajo del promedio")
if precioav<ptotal:
    print("Categoria avanzada por debajo del promedio")
if preciosu<ptotal:
    print("Categoria superior por debajo del promedio")
