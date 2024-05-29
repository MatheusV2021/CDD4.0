def desenhaTabuleiro(tabuleiro):
    if len(tabuleiro) > 0:
        if len(tabuleiro[0]) > 0:
            print(tabuleiro[0][0], end="")
            if len(tabuleiro[0]) > 1:
                print("|" + tabuleiro[0][1], end="")
                if len(tabuleiro[0]) > 2:
                    print("|" + tabuleiro[0][2])
        print("-----")
        if len(tabuleiro) > 1:
            if len(tabuleiro[1]) > 0:
                print(tabuleiro[1][0], end="")
                if len(tabuleiro[1]) > 1:
                    print("|" + tabuleiro[1][1], end="")
                    if len(tabuleiro[1]) > 2:
                        print("|" + tabuleiro[1][2])
            print("-----")
            if len(tabuleiro) > 2:
                if len(tabuleiro[2]) > 0:
                    print(tabuleiro[2][0], end="")
                    if len(tabuleiro[2]) > 1:
                        print("|" + tabuleiro[2][1], end="")
                        if len(tabuleiro[2]) > 2:
                            print("|" + tabuleiro[2][2])
                print("-----")

def verificaVitoria(tabuleiro, jogador):
    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == jogador:
        return True
    else:
        if tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == jogador:
            return True
        else:
            if tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == jogador:
                return True
            else:
                if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == jogador:
                    return True
                else:
                    if tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == jogador:
                        return True
                    else:
                        if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == jogador:
                            return True
                        else:
                            if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
                                return True
                            else:
                                if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
                                    return True
                                else:
                                    return False

def verificaEmpate(tabuleiro):
    if tabuleiro[0][0] != " " and tabuleiro[0][1] != " " and tabuleiro[0][2] != " ":
        if tabuleiro[1][0] != " " and tabuleiro[1][1] != " " and tabuleiro[1][2] != " ":
            if tabuleiro[2][0] != " " and tabuleiro[2][1] != " " and tabuleiro[2][2] != " ":
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def jogar():
    vitoriasX = 0
    vitoriasO = 0
    partida = 1

    while vitoriasX < 2 and vitoriasO < 2 and partida <= 3:
        tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        jogadorAtual = "X"

        while True:
            print(f"Partida {partida}")
            desenhaTabuleiro(tabuleiro)
            entrada = input(f"Jogador {jogadorAtual} escolha a linha e a coluna (1 2 3): ")
            if entrada:
                if len(entrada) == 3:
                    if entrada[0] in "123" and entrada[2] in "123":
                        linha = int(entrada[0]) - 1
                        coluna = int(entrada[2]) - 1
                        if tabuleiro[linha][coluna] == " ":
                            tabuleiro[linha][coluna] = jogadorAtual
                            if verificaVitoria(tabuleiro, jogadorAtual):
                                desenhaTabuleiro(tabuleiro)
                                print(f"Jogador {jogadorAtual} venceu!")
                                if jogadorAtual == "X":
                                    vitoriasX += 1
                                else:
                                    vitoriasO += 1
                                partida += 1
                                break
                            else:
                                if verificaEmpate(tabuleiro):
                                    desenhaTabuleiro(tabuleiro)
                                    print("Empate!")
                                    partida += 1
                                    break
                                else:
                                    if jogadorAtual == "X":
                                        jogadorAtual = "O"
                                    else:
                                        jogadorAtual = "X"
                        else:
                            print("Movimento inválido. Tente novamente.")
                    else:
                        print("Entrada inválida. Tente novamente.")
                else:
                    print("Entrada inválida. Tente novamente.")
            else:
                print("Entrada inválida. Tente novamente.")

    print(f"Resultado final: Jogador X: {vitoriasX}\nJogador O: {vitoriasO}")
    if vitoriasX > vitoriasO:
        print("Jogador X é o campeão!")
    else:
        print("Jogador O é o campeão!")

jogar()
