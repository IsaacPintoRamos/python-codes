larg = float(input("Largura da parede: "))
alt = float(input("ALtura da parede: "))
área = larg * alt
print(f"Sua parede tem a dimensão de {larg} x {alt} e sua área é de {área}m².")
tinta = área / 2 # COM UM LITRO DE TINTA PODEMOS PINTAR 2 METROS². OBS: VALORES APENAS ILUSTRATIVOS, QUE PODEM SER TROCADOS PELO USUARIO.
print(f"Para pintar essa parede, você precisará de {tinta}l de tinta.")
