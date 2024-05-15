escolha = 0
while escolha != 3:
    escolha = int(input("[1]- Calcular area do triangulo\n[2]-Calcular area do quadrado\nSelecione: "))
    if escolha == 1:
        base = float(input("Base do triangulo: "))
        altura = float(input("Altura do triangulo: "))
        areaT = (base * altura) / 2
        print(f"Area do Triângulo= {areaT}")
    elif escolha == 2:
        lado = float(input("Lado do quadrado: "))
        areaQ = lado ** 2
        print(f"Area do Quadrado: {areaQ} ")
    elif escolha == 3:
        print("Sistema desconectado.")
    else:
        print("\nOpção invalida! Selecione outra: ")