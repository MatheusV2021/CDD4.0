import random

opcoes = ["Pedra", "Papel", "Tesoura"]
pj1 = 0
mpj2 = 0

while pj1 < 2 and mpj2< 2:
    escolha = random.choice(opcoes)
    jogador = str(input("Escolha entre Pedra, Papel ou Tesoura: "))

    if jogador not in opcoes:
        print("Escolha inválida. Tente novamente.")
        continue  

    if jogador == escolha:
        print("Empate")

    elif jogador == "Pedra" and escolha == "Tesoura":
        print(f"Jogador: {jogador} \n Maquina: {escolha} \n Jogador Venceu!")
        pj1 += 1
    elif escolha == "Pedra" and jogador == "Tesoura":
        print(f"Jogador: {jogador} \n Maquina: {escolha} \n Maquina Venceu!")
        mpj2 += 1

    elif jogador == "Tesoura" and escolha == "Papel":
        print(f"Jogador: {jogador} \n Maquina: {escolha} \n Jogador Venceu!")
        pj1 += 1
    elif escolha == "Tesoura" and jogador == "Papel":
        print(f"Jogador: {jogador} \n Maquina: {escolha} \n Maquina Venceu!")
        mpj2 += 1

    elif jogador == "Papel" and escolha == "Pedra":
        print(f"Jogador: {jogador} \n Maquina: {escolha} \n Jogador Venceu!")
        pj1 += 1
    elif escolha == "Papel" and jogador == "Pedra":
        print(f"Jogador: {jogador} \n Maquina: {escolha} \n Maquina Venceu!")
        mpj2 += 1

    print(f"Placar - Jogador: {pj1} x Maquina: {mpj2}")

if pj1 == 2:
    print("Jogador venceu a melhor de 3!")
else:
    print("Maquina venceu a melhor de 3!")
