selecao = str(input("Selecione o tipo de combustivel: [G]-Gasolina ou [E]-Etanol: "))
litros = float(input("Insira quantos litros você deseja: "))
gasolina = 5.80
etanol = 4.90
if selecao == 'G' or selecao == 'g':
    print(f"Você abasteceu {litros} litros de gasolina. Pague R${litros*gasolina}")
elif selecao == 'E' or selecao == 'e':
    print(f"Você abasteceu {litros} litros de etanol. Pague R${litros*etanol}")
else:
    print("O tipo de combustivel selecionado não existe.")