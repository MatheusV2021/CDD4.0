att = int(input("Quantas atividades foram realizadas: "))
soma = 0

for x in range(att):
    nota = float(input("Insira sua nota: "))
    soma = soma + nota
media = soma/att

if media >= 7:
    print(f"Sua média foi {media}. Você foi aprovado!")
elif media >= 4:
    print(f"Sua média foi {media}. Você está de recuperação.")
else:
    print(f"Sua média foi {media}. Você foi reprovado.")

