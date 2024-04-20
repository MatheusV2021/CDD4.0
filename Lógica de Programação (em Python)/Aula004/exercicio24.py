soma = 0
c = 0
alunos = int(input("Numero de alunos na sala: "))
while alunos > c:
    a = float(input("Digite sua nota: "))
    soma = soma + a
    c = c + 1
media = soma / alunos
print(media)
