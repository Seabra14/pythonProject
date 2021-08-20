larg = float(input("Largura da parede: "))
alt = float(input("Altura da parede: "))
área = larg * alt
print("Sua parede tem uma dimensão de {}x{} e a sua área é de {}m2.".format(larg, alt, área))
tinta = área / 2
print ("Para pintar a parede, você precisará de {}l de tinta.".format(tinta))

