a = [0,0,0,0,0,0,0,0,0,0]
m = [0,0,0,0,0,0,0,0,0,0]

for i in range(10):
    a[i] = int(input("Digite um numero: "))

x = int(input("Digite um multiplicador: "))

for z in range(10):
    m[z]=a[z]*x

print(f"Numeros: {a}")
print(f"Numeros multiplicados por {x}: {m}")


