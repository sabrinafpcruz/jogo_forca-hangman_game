import random
frutas=["laranja", "pera", "uva", "abacaxi", "amora", "acerola", "banana", "abacate", "cajá", "carambola","cereja", "coco"]
palavra = random.choice(frutas)
chances = 6
erros=0
letras_achadas=[]

letras_palavra = ["-"] * len(palavra)

opcao_palavra="Ss"

print("|---------Jogo da Forca---------|")
print("Dica a palavra tem",len(palavra), "letras")

while chances > erros:
    letra=input("\nDigite uma letra: ")
    letras_achadas.append(letra)

    if letra in palavra:
        for item in range(len(palavra)):
            if letra == palavra[item]:
                letras_palavra[item] = letra
        print(f'A letra está dentro de {letras_palavra}')
    else:
        print(f'A letra não está dentro de {letras_palavra}')
        chances -=1
    print(f'Você ainda tem {chances} chances')

    print("Você já digitou as letras: ")
    for item in letras_achadas:
        print(item, end=" ")
    print()

    while opcao_palavra in "Ss":
        opcao_palavra=input("\nDeseja falar qual é a palavra? (s/n)")
        if opcao_palavra == "Ss":
            tentativa_palavra=input("Qual é a palavra: ")
            if tentativa_palavra == palavra:
                print("\nParabêns! Você ganhou o jogo")
                break
        else:
            print("Ok, continuando....")


    if ''.join(letras_palavra) == palavra:
        print("\n \nParabêns! Você ganhou o jogo")

    elif erros == chances:
        print("Fim de jogo a palavra era",palavra)
