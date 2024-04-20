import time

a = 0

while a<4:
    num = int(input("Digite um numero: "))
    time.sleep(5)
    num2 = int(input("Digite outro numero: "))

    if num==num2:
        print("Os números são iguais. ")
    elif num>num2:
        print(num2, num)
    else:
        print(num, num2)
    a+=1