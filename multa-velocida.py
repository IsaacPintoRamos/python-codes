v = int(input("Qual a velocidade do veículo? "))
placa = str(input("Placa do veículo: "))
if v >80:
    print(f'O veículo de placa {placa} foi multado por exesso de velocidade.')
    print('Será aplicado R$ 7 a cada km ultrapassado.')
    multa = (v-80)*7
    print(f'O valor da sua multa é de R$ {multa} por exesso de velocidade.')
else:
    print(f'O veículo de placa {placa} esta dirrigindo corretamente, Continue assim!')
