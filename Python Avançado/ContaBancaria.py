class Conta():
    def __init__(self, numeroConta, nomeConta, tipoConta):
        self.numero = numeroConta
        self.saldo = 0
        self.status = False
        self.nome = nomeConta
        self.tipo = tipoConta

    def ativar(self):
        if self.status == False:
            print("Sua conta foi ativada.")
            self.status = True
        else:
            print(f"Sua conta já está ativa.")

    def desativar(self):
        if self.status == True and self.saldo == 0:
            print(f"Sua conta foi desativada.")
            self.status = False
        elif self.status == False:
            print(f"Sua conta já está desativada.")
        else:
            print(f"Não foi possível desativar sua conta.")

    def deposito(self, valor):
        if valor < 0:
            print(f"Valor invalido!")
        else:
            print(f"Você depositou R${valor}")
            self.saldo += valor

    def sacar(self, valor):
        print(f"Você sacou R${valor}")
        self.saldo -= valor

    def verificar(self):
        print(f"\nOlá, {self.nome}!\nNúmero da conta: {self.numero}\nVocê possui R${self.saldo} na sua conta {self.tipo}.")
