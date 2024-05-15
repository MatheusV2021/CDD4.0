notas = ["","","","",""]
soma = 0
cont = 0

for x in range(5):
    notas[x] = float(input("Digite sua nota: "))

for i in range(5):
    soma = soma + notas[i]

media = soma / 5

for z in range(5):
    if notas[z]>=media:
        cont = cont + 1
print(f"A média da sala foi {media}, e tivemos {cont} acima da média.")