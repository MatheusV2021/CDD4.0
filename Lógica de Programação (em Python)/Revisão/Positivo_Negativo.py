resposta = 'sim'

while resposta == 'sim' or resposta == 'Sim':
    num = int(input("Digite um numero: "))

    if num > 0:
        print("Numero positivo!")
    elif num == 0:
        print("Neutro")
    else:
        print("Numero negativo")

    resposta = str(input("Deseja refazer? "))