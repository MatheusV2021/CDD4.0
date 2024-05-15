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

def estoque(produto, quantidade, valor):
    total = quantidade * valor
    return total

def soma(*numeros):
    soma = 0
    for x in range(len(numeros)):
        soma += numeros[x]
    print(soma)

def inverso(texto):
    letras = 0
    for x in range(len(texto)):
        if texto[x] not in " ,.!":
            letras += 1
    for y in range(len(texto)-1, -1, -1):
        if texto[y] not in " ,.!":
            print(texto[y], end=" ")
    print(f"\nQuantidade de letras: {letras}")

def lista_unica(*array):
    nova_lista = []
    for x in array:
        if x not in nova_lista:
            nova_lista.append(x)
    print(nova_lista)

def duplicados(*lista):
    nova=set(lista)
    print(f"A lista recebida foi: {lista}\nA lista sem repetição foi: {nova}")

