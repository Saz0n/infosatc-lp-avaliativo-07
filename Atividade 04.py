contador = 0
numeros = []
while contador<10:
    numero = int(input("Digite um número: "))
    numeros.append(numero)
    contador= contador +1
    print("Esses são os numeros colocados na lista",numeros)
    numeros.sort()
par = [x for x in numeros if x%2==0]
impar = [x for x in numeros if x%2!=0]
print("Os numeros impares são ", impar)
print("Os pares são",par)

