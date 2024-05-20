class Pessoa():
    def __init__(self, nomeAluno, pesoAluno, idadeAluno, comendo= False, dormindo = False, falando = False ):
        self.nome = nomeAluno
        self.peso = pesoAluno
        self.idade = idadeAluno
        self.comendo = comendo
        self.dormindo = dormindo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f"{self.nome} já está comendo.")
        elif self.dormindo:
            print (f"{self.nome} não pode comer enquanto está dormindo")
        elif self.falando:
            print(f"{self.nome} não pode comer enquanto está falando")
        else:
            print (f"{self.nome} foi comer {alimento}")
            self.comendo = True
        

    def parardecomer(self):
        if not self.comendo:
            print (f"{self.nome} não está comendo")
        else:
            print(f"{self.nome} parou de comer.")
            self.comendo = False

    def falar(self, frase):
        if self.falando:
            print(f"{self.nome} já está falando.")
        elif self.dormindo:
            print (f"{self.nome} não pode falar enquanto está dormindo")
        elif self.comendo:
            print (f"{self.nome} não pode falar enquanto está comendo")
        else:
            print (f"{self.nome} está falando {frase}")
            self.falando = True
        

    def parardefalar(self):
        if not self.falando:
            print (f"{self.nome} não está falando")
        else:
            print(f"{self.nome} parou de falar.")
            self.comendo = False

    def dormir(self):
        if self.dormindo:
            print(f"{self.nome} já está dormindo.")
        elif self.falando:
            print (f"{self.nome} não pode dormir enquanto está falando")
        elif self.comendo:
            print (f"{self.nome} não pode dormir enquanto está comendo")
        else:
            print (f"{self.nome} está dormindo")
            self.dormindo = True

    def acordar(self):
        if not self.dormindo:
            print (f"{self.nome} está acordado")
        else:
            print(f"{self.nome} acordou.")
            self.dormindo = False
        
    