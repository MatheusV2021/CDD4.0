nota1 = float(input("Insira sua nota 1: "))
nota2 = float(input("Insira sua nota 2: "))
nota3 = float(input("Insira sua nota 3: "))

media = (nota1+nota2+nota3)/3

if media >=7:
    print(f"Sua média foi: {media}. Você foi aprovado!")
elif media >=4:
    print(f"Sua média foi: {media}. Você está de recuperação!")
else:
    print(f"Sua média foi: {media}. Você foi reprovado!")