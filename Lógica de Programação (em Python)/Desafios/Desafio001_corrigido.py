hora1 = int(input(f"Digite a hora: "))
minuto1 = int(input(f"Digite o minuto \n {hora1}:"))
hora2 = int(input(f"\nDigite a hora: "))
minuto2 = int(input(f"Digite o minuto \n {hora2}:"))

if hora1>12:
    hora1 = hora1-12
if hora2>12:
    hora2 = hora2-12
hora = hora1+hora2

if hora > 12:
    hora = hora - 12

minuto = minuto1+minuto2
if minuto >=60:
    minuto = minuto - 60
    hora = hora + 1

print(f"\nHorario: {hora :02d}:{minuto :02d}")