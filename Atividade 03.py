# a linha 10 foi copiada do site https://pythonhelp.wordpress.com/2012/05/13/map-reduce-filter-e-lambda/
contador = 0
numeros = []
while contador<5:
    ns = int(input("Insira um número: "))
    numeros.append(ns)
    contador= contador +1
    print("Esses são os numeros colocados na lista",numeros)
numeros.sort()
Requisitados = [x for x in numeros if x > 10]
print("os numeros que são maior que 10:",Requisitados)
