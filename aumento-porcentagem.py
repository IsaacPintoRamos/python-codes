s = float(input("Quando é o salário do Funcionário? "))
p = float(input("Qual a porcentagem do aumento? "))
n = s + (s * p / 100)
print(f"Um funcionário que ganhava R${s}, com {p}% de aumento, passa a receber R${n:0.2f}.")
