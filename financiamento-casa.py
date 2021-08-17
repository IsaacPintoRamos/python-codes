valorCasa = float(input('Valor da casa: R$ '))
salario = float(input('Sálario do comprador: R$ '))
anosPagando = int(input('Anos de pagamento: '))

mensalidade = float(anosPagando * 12)
mensal = float(valorCasa / mensalidade)

print(f'Para pagar uma casa de R${valorCasa} em {anosPagando} anos a prestação será de R${mensal:.2f}')

if mensal <= salario*30/100:
    print('Emprestimo Aprovado')
else:
    print('Emprestimo Negado')
