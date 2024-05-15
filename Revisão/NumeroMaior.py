n1 = int(input("Insira um numero: "))
n2 = int(input("Insira um numero: "))
n3 = int(input("Insira um numero: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior.")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior.")
else:
    print(f"{n3} é maior")

