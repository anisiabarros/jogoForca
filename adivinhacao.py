import random


def jogar():
    print("**********************************")
    print("Bem-vindo no jogo de Adivinhação!")
    print("**********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000
    # print(numero_secreto)

    print("Qual nivel de dificuldade você quer?")
    print("(1) Facil, (2) Médio, (3) Difícil")
    nivel = int(input("Defina o nível:  "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa: {} de {}".format(rodada, total_tentativas))
        chute = int(input("digite o numero: "))
        print("Você digitou", chute)

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        if chute < 1 or chute > 100:
            print("Você deve digitar um valor entre 1 e 100")
            continue

        if acertou:
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if maior:
                print("Você digitou um numero maior")
            elif menor:
                print("Você digitou um numero menor")
            pontos = abs(pontos - chute)

        rodada = rodada + 1
    print("Fim de jogo")


if __name__ == "__main__":
    jogar()
