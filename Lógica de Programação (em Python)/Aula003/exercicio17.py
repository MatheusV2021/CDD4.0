soma = 0
for x in range(10):
    n = int(input("Digite um numero: "))
    if n % 2 != 0:
        soma = soma + n
print(f"a soma total dos numeros impares é: {soma}")