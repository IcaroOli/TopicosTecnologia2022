leituras = []
media = 0
acima = 0

num_moradores = int(input('Quantos moradores moram nesse condominio? '))

for i in range(0, num_moradores):
    leitura = int(input(f'Qual é a leitura para o morador {i+1}? '))

    leituras.append(leitura)
    media += leitura
media = media/len(leituras)

for morador, leitura in enumerate(leituras):
    if leitura > media:
        acima += 1
print(f'Media: {media}\nAcima: {acima}')