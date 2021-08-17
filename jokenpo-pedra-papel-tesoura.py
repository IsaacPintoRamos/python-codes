from random import randint
from time import sleep
itens = ('Pedra' , 'Papel' , 'Tesoura')
computador = randint(0 , 2)

print('''Suas opções:\n
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\n''')

jogador = int(input('Qual é a sua jogada? '))
print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

if computador == 0: # PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU!')
    elif jogador == 2:
        print('COMPUTADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE!')

elif computador == 1: # PAPEL
    if jogador == 0:
        print('COMPUTADOR GANHOU!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOAGADOR GANHOU!')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE!')

elif computador == 2: # TESOURA
    if jogador == 0:
        print('JOGADOR GANHOU!')
    elif jogador == 1:
        print('COMPUTADOR GANHOU!')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA. TENTE NOVAMENTE!')

else:
    print('JOGADA INVÁLIDA. TENTE NOVAMENTE!')
