anos = int(input("Quantos anos você tem: "))
mes = int(input("Quantos meses você tem: "))
dias = int(input("Quantos dias você tem: "))

anos_dias = anos*365
mes_dias = mes*30

diastotais = anos_dias+mes_dias+dias

print(f"Você possui {diastotais} dias de vida.")
