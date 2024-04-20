dentro = 0
fora = 0

for x in range(10):
    a = int(input("Digite um numero: "))
    if a >= 10 and a <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1

print(f"Numeros dentro do intervalo entre 10 e 20: {dentro} \n Numeros fora do intervalo entre 10 e 20: {fora}")
