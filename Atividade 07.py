contador = 0
notas_finais = []
notas_letras = []
while contador<10:
    nota_01= float(input("Digite a primeria nota do aluno:"))
    nota_02= float(input("Digite a segunda nota do aluno:"))


    calculo=lambda x,y: (nota_01+nota_02)/2
    nota_media =calculo(nota_01,nota_02)


    if(nota_media<5):
        print("A nota foi D")
        notas_letras.append("D")
    elif(nota_media>5 and nota_media<7):
        print("A nota foi C")
        notas_letras.append("C")
    elif(nota_media>7 and nota_media<9):
        print("A nota foi B")
        notas_letras.append("B")
    elif(nota_media>9 and nota_media<=10):
        print("A nota foi A")
        notas_letras.append("A")
    notas_finais.append(nota_media)
    contador = contador +1
print("Essa foram as notas finais dos 10 alunos numeros foi", notas_finais)
print("Essa foram as notas finais dos 10 alunos em letras foi", notas_letras)