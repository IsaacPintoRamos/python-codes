import random
n = random.randint(1, 10)
computador = n
contJogadas = 0
print('FOI SORTEADO UM NÚMERO DE 1 Á 10. TENTE ACERTAR\n')

jogada = int(input('Qual sua jogada? '))

if jogada == computador:
    contJogadas = contJogadas + 1
    tentativas = contJogadas
elif jogada > computador:
    print('MENOS... TENTE NOVAMENTE!\n')
elif jogada < computador:
    print('MAIS...TENTE NOVAMENTE!\n')

while jogada != computador:
    jogada = int(input('VOCÊ ERROU. TENTE NOVAMENTE. DIGITE SUA JOGADA: '))
    if jogada > computador:
        print('MENOS... TENTE NOVAMENTE!\n')
    elif jogada < computador:
        print('MAIS...TENTE NOVAMENTE!\n')
    contJogadas = (contJogadas + 1)
    tentativas = contJogadas + 1 # COLOQUEI ESSA TENTATIVA, POIS TODA VEZ O CALCULO SEMPRE DAVA UM NÚMERO A MENOS (SE NÃO ACERTASSE DE PRIMEIRA)

print('PARABÉNS VOCÊ ACERTOU')
print(f'NÚMEROS DE TENTATIVAS: {tentativas}')
