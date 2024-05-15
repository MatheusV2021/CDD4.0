aprovados = []
recuperacao = []
reprovados = []

n = int(input("Numero de alunos que você deseja registrar: "))

for i in range(1,n+1):
    aluno = str(input("Insira seu nome: "))
    nota1 = float(input("Insira sua nota1: "))
    nota2 = float(input("Insira sua nota2: "))
    nota3 = float(input("Insira sua nota3: "))

    media = (nota1+nota2+nota3)/3

    if media >=7:
        aprovados.append(aluno)
    elif media>=4:
        recuperacao.append(aluno)
    else:
        reprovados.append(aluno)

print("\nAlunos aprovados: ")
for aluno in aprovados:
    print(aluno)

print("\nAlunos em Recuperação: ")
for aluno in recuperacao:
    print(aluno)

print("\nAlunos reprovados: ")
for aluno in reprovados:
    print(aluno)