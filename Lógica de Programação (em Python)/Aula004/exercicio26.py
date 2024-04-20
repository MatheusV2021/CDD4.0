senha = 191919
senha_usuario = int(input("Digite a sua senha: "))
contador = 0
while senha_usuario != senha:
    senha_usuario = int(input("Senha incorreta! \nDigite a sua senha novamente: "))
    contador = contador + 1
    if contador == 2 and senha_usuario != senha:
        print("Limite de tentativas! O sistema está bloqueado.")
        break
if senha_usuario == senha:
    print("Você está conectado no sistema.")