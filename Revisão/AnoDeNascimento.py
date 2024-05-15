idade = int(input("Insira a sua idade: "))
ano = 2024

ano_nasc = ano - idade

aniv = str(input("Você já fez aniversario esse ano? "))

if aniv == 'Sim' or aniv == 'sim':
    print(ano_nasc)
else:
    ano_nasc = ano_nasc - 1
    print(f"Ano de nascimento: {ano_nasc}")
