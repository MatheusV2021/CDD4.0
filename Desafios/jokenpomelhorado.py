import random

pj1 = 0
pj2 = 0

opcoes = ["Pedra", "Papel", "Tesoura"]
escolha = random.choice(opcoes)
jogador = str(input("Escolha entre Pedra, Papel ou Tesoura: "))

if jogador == escolha:
    print("Empate")

if jogador == "Pedra" and escolha == "Tesoura":
    print(f"Jogador: {jogador} \n Maquina: {escolha} \n Jogador Venceu!")
    pj1 += 1

if escolha == "Pedra" and jogador == "Tesoura":
    print(f"Jogador: {jogador} \n Maquina: {escolha} \n Maquina Venceu!")
    pj2 += 1

if jogador == "Tesoura" and escolha == "Papel":
    print(f"Jogador: {jogador} \n Maquina: {escolha} \n Jogador Venceu!")
    pj1 += 1