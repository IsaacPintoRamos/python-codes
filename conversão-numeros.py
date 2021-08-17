num = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opção = int(input('Sua opção: '))

if opção == 1:
    print(f'{num} convertido para BINÀRIO é igual a {bin(num)}')

elif opção == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)}')

elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)}')

else:
    print('Opção inválida. Tente novamente')
