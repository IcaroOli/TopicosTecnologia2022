import random

w_player = 0
w_cpu = 0

def reset(w1, w2):
    w1 = 0
    w2 = 0


def getInput(msg):
    choice = input(msg + "\n>>> ")
    return choice


def game(w1, w2):
    while w1 < 3 and w2 < 3:

        par_impar = 0
        while par_impar not in [1, 2]:
            par_impar = int(getInput("Escolha:\n1 - Par\n2 - Impar"))

        num = -1
        while num not in range(0, 5):
            num = int(getInput("Escolha um número de 0 à 5"))

        random.seed()
        cpu_num = random.randint(0, 5)
        print("Seu oponente escolheu", cpu_num)

        if (num + cpu_num) % 2 == 0:
            print("Par ganhou.\n")
            ganhador = 1
        else:
            ganhador = 2
            print("Impar ganhou.\n")

        if par_impar == ganhador:
            w1 += 1
        else:
            w2 += 1

    novo = 0
    while novo not in [1, 2]:
        novo = int(getInput("Você gostaria de continuar o jogo?\n1 - Sim\n2 - Não"))
    if novo == 1:
        reset(w1, w2)
        game(w1, w2)
    else:
        print("Fim")


if __name__ == '__main__':
    game(w_player, w_cpu)
