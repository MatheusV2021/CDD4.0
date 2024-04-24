eleitores = int(input("Digite o numero de eleitores: "))
validos = 0
nulos = 0
brancos = 0

for x in range(eleitores):
    voto = int(input("Vote: [1]- Cleitão, bom de guerra, [2]- Peter Porker, [3]- Nulo\n Selecione: "))
    if voto == 1 or voto == 2:
        validos += 1

    elif voto == 3:
        nulos += 1

    else:
        brancos += 1

porcentagemV = (validos/eleitores)*100
porcentagemN = (nulos/eleitores)*100
porcentagemB = (brancos/eleitores)*100
print(f"Votos válidos: {porcentagemV}%\nVotos nulos: {porcentagemN}%\nVotos brancos: {porcentagemB}%")
