negativo = 0
for x in range(10):
    a = int(input("Digite um numero: "))
    if a < 0:
        negativo = negativo + 1
print(negativo)