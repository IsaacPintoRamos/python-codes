preco = float(input('Qual o preço do produto? R$ '))
porcento = float(input('Qual o valor da porcentagem? '))
desconto = preco - (preco*porcento/100)
print(f'O produto que custava R$ {preco}, na promoção com desconto de {porcento}% vai custar R${desconto:.2f}.')
