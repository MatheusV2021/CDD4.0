dia_nascimento = int(input("Digite o dia do seu nascimento: "))
mes_nascimento = int(input("Digite o mês do seu nascimento: "))
ano_nascimento = int(input("Digite o ano do seu nascimento: "))

dia_atual = int(input("Digite o dia atual: "))
mes_atual = int(input("Digite o mês atual: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento

if (mes_nascimento, dia_nascimento) > (mes_atual, dia_atual):
  idade = idade - 1

mes2 = 12 - mes_nascimento + mes_atual
dia2 = 30 - dia_nascimento + dia_atual
dias_totais = idade*365 + mes2*30 + dia2
dias_meses = dias_totais//30
dias_horas = dias_totais*24

if mes2<0:
  mes2 = mes2* -1

print(f"\nVocê tem {idade} anos, {mes2} meses e {dia2} dias. \nDias de vida: {dias_totais} \nMeses de vida: {dias_meses}\nHoras de vida: {dias_horas}")