resposta = 's'
while resposta == 's' or resposta == 'S':
    n1 = float(input("Digite sua 1° nota: "))
    while n1 < 0 or n1 > 10:
        print("O valor tem que ser maior que 0 e menor que 10. Tente novamente.")
        n1 = float(input("Digite sua 1° nota mais uma vez: "))
    n2 = float(input("Digite sua 2° nota: "))
    while n2 < 0 or n2 > 10:
        print("O valor tem que ser maior que 0 e menor que 10. Tente novamente.")
        n2 = float(input("Digite sua 2° nota mais uma vez: "))
    media = (n1+n2)/2
    print(f"Sua média foi: {media}")

    resposta = str(input("Você quer fazer um novo calculo? \nPressione [S] para sim ou [N] para não: "))