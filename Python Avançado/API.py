import requests

resposta = "sim"

while resposta == "sim" or resposta == "Sim":
    print("Verificando o endereço...")
    cep = str(input("Digite o CEP: "))

    if len(cep) != 8:
        print("CEP Inválido!")
        exit()
    consulta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    print(consulta.json())
    resposta = str(input("Deseja inserir outro CEP: [Sim ou Não]"))