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