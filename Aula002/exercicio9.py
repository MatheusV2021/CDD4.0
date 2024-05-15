time1 = str(input("Escolha um time: "))
gol1 = int(input(f"Quantidade de gols  {time1}: "))

time2 = str(input("Escolha um time: "))
gol2 = int(input(f"Quantidade de gols marcados pelo {time2}: "))

if gol1==gol2:
    print("Empate")
elif gol1>gol2:
    print(f"{time1} venceu o {time2} por {gol1}x{gol2}")
else:
    print(f"{time2} venceu o {time1} por {gol2}x{gol1}")