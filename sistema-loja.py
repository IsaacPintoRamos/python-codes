print('\n')
print('=' * 32)
print('{:=^40}'.format(' \033[34mNOME LOJA\033[m '))
print('=' * 32)

preço = float(input('\n\nPreço das compras: R$ '))

print('''\nFORMAS DE PAGAMENTO \n
[ 1 ] À VISTA: DINHEIRO / CHEQUE
[ 2 ] À VISTA CARTÃO
[ 3 ] 2x NO CARTÃO
[ 4 ] 3x OU MAIS NO CARTÃO \n\n''')

opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço - (preço * 10 / 100)
    print(f'\nSua compra de R$ {preço:.2f} vai custar R$ {total:.2f} no final.')

elif opção == 2:
    total = preço - (preço * 5 / 100)
    print(f'\nSua compra de R$ {preço:.2f} vai custar R$ {total:.2f} no final.')

elif opção == 3:
    total = preço
    parcela = preço / 2
    print(f'\nSua compra de R$ {total:.2f} será parcelada em 2x de R$ {parcela:.2f}.')

elif opção == 4:
    total = preço + (preço * 20 / 100)
    parcelas = int(input('Deseja parcelar em quantas vezes? '))
    parcela = preço / parcelas
    print(f'\nSua compra de R$ {preço:.2f} será parcelada em {parcelas}x de R$ {parcela:.2f}  e vai custar R$ {total:.2f} no final.')

else:
    print('\n\033[31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE!')
#OBS: A VISTA CONTEM DESCONTO, E PARCELADO EM 3X OU MAIS CONTEM JUROS.