t = float(input("Digite o tempo gasto na viagem, (em horas): "))
vm = float(input("Digite sua velocidade média durante a viagem, (em km/h): "))
d = t * vm
lu = d / 12
print("O tempo gasto na viagem foi:", t, "horas")
print("Sua velocidade média durante a viagem foi de:", vm, "km/h")
print("A distância percorrida durante a viagem foi:", d, "Km")
print('Foram usados {:.2f}'.format(lu) ,'litros durante sua viagem')
