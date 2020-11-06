contador_01 = 1
Ni_Cubo=lambda  N_inserido: N_inserido **3
Ni_Quadrado=lambda N_inserido: N_inserido **2

while contador_01 == 1:
    N_inserido= int(input("Digite o numero que sera utilizadado na função:"))
    opção_01= int(input("Para elevar o numero digitado no quadrado dele mesmo digite 1, e para elevar ao cubo digite 2: "))
    if opção_01 == 1:
        hm_Quadrado=Ni_Quadrado(N_inserido)
        print(hm_Quadrado)
    else:
       hm_Cubo=Ni_Cubo(N_inserido)
       print(hm_Cubo)
    contador_01= int(input("Voce deseja fazer outro calculo? 1 para sim, e 0 para não:"))

