hora1 = int(input(f"Digite a hora: "))
minuto1 = int(input(f"Digite o minuto \n {hora1}:"))
hora2 = int(input(f"\nDigite a hora: "))
minuto2 = int(input(f"Digite o minuto \n {hora2}:"))

hora1_12 = hora1-12
hora2_12 = hora2-12
Hsoma1 = hora1+hora2
Hsoma1_12 = hora1_12+hora2_12
Msoma = minuto1+minuto2

if Msoma >60:
    Horario1 = Hsoma1 + 1
    Horario12 = Hsoma1_12 + 1
    Minutos = Msoma - 60

if hora1>12:
    print(f"entrada 1: {hora1_12}:{minuto1}")
else:
    print(f"entrada 2: {hora1}:{minuto1}")
if hora2>12:
    print(f"entrada 1: {hora2_12}:{minuto2}")
else:
    print(f"entrada 2: {hora2}:{minuto2}")

print(f"Saída: {Horario1}:{Minutos}")
print(f"Saída: {Horario12}:{Minutos}")