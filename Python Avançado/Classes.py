# Dessa linha para baixo são assuntos de Programação Orientada a Objetos (POO)

# Classe
# Pascal Case: Cada primeira letra da palavra maiuscula

# metodo
# camelCase: primeira letra da primeira palavra minuscula, primeira letra da segunda palavra maiuscula

class Pessoa():
    def __init__(self, nomeAluno, pesoAluno, idadeAluno, comendo= False, dormindo = False, falando = False ):
        self.nome = nomeAluno
        self.peso = pesoAluno
        self.idade = idadeAluno
        self.comendo = comendo
        self.dormindo = dormindo
        self.falando = falando

    def comer(self, alimento):
        print(f"{self.nome} está comendo {alimento}.")
        self.comendo = True


    def parardecomer(self):
        print(f"{self.nome} parou de comer.")
        self.comendo = False

    def falar(self, frase):
        print(f"{self.nome} está falando {frase}.")
        self.falando = True

    def parardefalar(self):
        print(f"{self.nome} parou de falar.")
        self.falando = False

    def dormir(self):
        print(f"{self.nome} está dormindo.")
        self.dormindo = True

    def acordar(self):
        print(f"{self.nome} acordou.")
        self.dormindo = False

class Conta():
    def __init__(self, numeroConta, nomeConta, tipoConta):
        self.numero = numeroConta
        self.saldo = 0.0
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
        if self.status == True:
            if valor < 0:
                print(f"Valor invalido!")
            else:
                print(f"Você depositou R${valor}")
                self.saldo += valor
        else:
            print("Movimentação bloqueada! Conta inativa.")
    def sacar(self, valorsaque):
        if self.status == True:
            if self.saldo >= valorsaque:
                print(f"Você sacou R${valorsaque}")
                self.saldo -= valorsaque
            else:
                print("Saldo insuficiente.")
        else:
            print("Movimentação bloqueada! Conta inativa.")
    def verificar(self):
        print(f"\nOlá, {self.nome}!\nNúmero da conta: {self.numero}\nVocê possui R${self.saldo} na sua conta {self.tipo}.")

class Animal():
    def __init__(self,nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print(f"O {self.nome} foi comer...")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def miar(self):
        print(f"O {self.nome} miou...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def latir(self):
        print(f"O {self.nome} latiu...")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def mugir(self):
        print(f"O {self.nome} mugiu...")

class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()
    def calcularArea(self, base, altura):
        self.area = base * altura
        print(f"A area é {self.area}")
    def calcularPerimetro(self, base, altura):
        self.perimetro = 2 * (base+altura)
        print(f"O perimetro é {self.perimetro}")

class Ingresso():
    def __init__(self, valor):
        self.valor = valor
    def imprimir(self):
        print(f"Valor do ingresso comum: {self.valor}")

class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprimirVIP(self):
        vip = self.valor+50
        print(f"Valor do ingresso VIP é: {vip}")

class Atleta():
    def __init__(self, peso):
        self.peso = peso
        self.aposentado = False
        self.aquecendo = False


    def aposentar(self):
        if self.aposentado == False:
            print("O Atleta está se aposentando...")
            self.aposentado = True
        else:
            print("O Atleta já está aposentado.")
    def aquecer(self):
        if self.aposentado == False:
            if self.aquecendo == False:
                print("O Atleta está aquecendo...")
                self.aquecendo = True
            else:
                print("O Atleta já está aquecido.")
        else:
            print("O Atleta está aposentado.")

class Corredor(Atleta):
    def __init__(self, peso):
        super().__init__(peso)
        self.correndo = False
    def correr(self):
        if self.aquecendo == True:
            if self.correndo == False:
                print("O Corredor começou a correr.")
                self.correndo = True
            else:
                print("O Corredor já está correndo.")
        else:
            print("O Corredor não pode correr, pois não aqueceu.")
    def parardecorrer(self):
        if self.correndo == True:
            print("O Corredor parou de correr.")
            self.correndo = False
        else:
            print("O Corredor não está correndo.")
