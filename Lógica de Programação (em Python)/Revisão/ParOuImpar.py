resposta = 'sim'
while resposta == 'sim' or resposta == 'Sim':
    num = int(input("Insira um numero: "))
    if num % 2 != 0:
        print("Impar")
    else:
        print("Par")
    resposta = str(input("Deseja inserir outro numero? "))