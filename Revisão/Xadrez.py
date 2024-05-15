hora1 = int(input(f"Digite a hora de inicio: "))
hora2 = int(input(f"Digite a hora de encerramento: "))
if hora2>hora1:
    diff = hora2 - hora1
elif hora1>hora2:
    diff = 24-hora1+hora2
else:
    diff = 24
print(f"A duração é de {diff} horas.")