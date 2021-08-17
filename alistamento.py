nascimento = int(input('Ano de nascimento: '))

anoAtual = 2021 #ANO ATUAL
idade = 2021 - nascimento
idadeAlistamento = idade - 18
anoAlistamento = nascimento + 18

if idade == 18:
    print(f'''Quem nasceu em {nascimento} tem {idade} anos em {anoAtual}.
Você tem que se alistar IMEDIATAMENTE. ''')

elif idade > 18:
    print(f'''Quem nasceu em {nascimento} tem {idade} anos em {anoAtual}.
Você já deveria ter se alistado há {idadeAlistamento} anos.
Seu alistamento foi em {anoAlistamento}.''')

elif idade < 18:
    print(f'''Quem nasceu em {nascimento} tem {idade} anos em {anoAtual}.
Ainda faltam {abs(idadeAlistamento)} anos para o alistamento
Seu alistamento será em {anoAlistamento}.''')
