peso = float(input('Qual é seu peso: (KG) '))
altura = float(input('Qual a sua altura: (M) '))

imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é de {imc:.1f} ', end='')

if imc < 18.5:
    print('Abaixo do peso')

elif imc >= 18.5 and imc < 25:
    print('Peso ideal')

elif imc >= 25 and imc < 30:
    print('Sobreso')

elif imc >= 30 and imc < 40:
    print('Obesidade')

elif imc >= 40:
    print('Obesidade mórbida')
