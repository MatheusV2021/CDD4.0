def cadastro():
    nomes = ["","",""]
    senhas = ["","",""]
    cont = 0

    for x in range(3):
        nomes[x] = str(input("Crie um nome de usuario: "))
        senhas[x] = str(input("Crie sua senha: "))

def imprime_nome(x):
    print(f"Nome: {x}")

def piramide_numerica(n):
    for y in range(n):
        for x in range(y+1):
            print(y+1, end=" ")
        print()

def piramide_numerica_inversa(n):
    for y in range(n):
        for x in range(y+1):
            print(x+1, end=" ")
        print()

def contador_count(texto):
    a = texto.count("a")
    e = texto.count("e")
    i = texto.count("i")
    o = texto.count("o")
    u = texto.count("u")
    espaco = texto.count(" ")

    soma = a+e+i+o+u
    print(f"A soma das vogais é: {soma}\nE possui {espaco} espaços.")

def contador_len(texto):
    vogais = 0
    for x in range (len(texto)):
        if texto[x] == "a" or texto[x] == "e" or texto[x] == "i" or texto[x] == "o" or texto[x] == "u":
            vogais += 1
    print(f"O texto possui: {vogais}")

