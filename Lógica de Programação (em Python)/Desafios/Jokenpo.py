import random

opcoes = ["Pedra", "Papel", "Tesoura"]
escolha = random.choice(opcoes)
resposta = 'sim' or 'Sim'

while resposta == 'sim' or resposta == 'Sim':
    jogador = str(input("Escolha entre Pedra, Papel ou Tesoura: "))

    if jogador == escolha:
        print(f"Jogador: {jogador} \n Maquina: {escolha} \n Empate!")

    elif jogador == "Pedra" and escolha == "Tesoura":
        print(f"Jogador: {jogador} \n Maquina: {escolha} \n Jogador Venceu!")
    elif escolha == "Pedra" and jogador == "Tesoura":
        print(f"Jogador: {jogador} \n Maquina: {escolha} \n Maquina Venceu!")

    elif jogador == "Tesoura" and escolha == "Papel":
        print(f"Jogador: {jogador} \n Maquina: {escolha} \n Jogador Venceu!")
    elif escolha == "Tesoura" and jogador == "Papel":
        print(f"Jogador: {jogador} \n Maquina: {escolha} \n Maquina Venceu!")

    elif jogador == "Papel" and escolha == "Pedra":
        print(f"Jogador: {jogador} \n Maquina: {escolha} \n Jogador Venceu!")
    elif escolha == "Papel" and jogador == "Pedra":
        print(f"Jogador: {jogador} \n Maquina: {escolha} \n Maquina Venceu!")

    resposta = str(input("Deseja jogar novamente? "))
