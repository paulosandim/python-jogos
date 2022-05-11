import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print("Qual dificuldade vc quer?", numero_secreto)
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)
        
        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou     = numero_secreto == chute
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou):
            print("Acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(chute_maior):
                print("Você errou! O seu chute foi maior que o número secreto")
            elif(chute_menor):
                print("Você errou! O seu chute foi menor que o número secreto")
                
        pontos_perdidos = abs(numero_secreto - chute) 
        pontos = pontos - pontos_perdidos
                
        rodada = rodada + 1
            
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()