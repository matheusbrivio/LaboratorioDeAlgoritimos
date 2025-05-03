numero1 = int(input("digite o primeiro numero:"))  
numero2 = int(input("digite o segundo numero:"))
while numero2 <= numero1:
    print("O numero 2 deve ser maior que o primeiro!")
    numero2 = int(input("digite o segundo numero:"))
for i in range (numero1 + 1, numero2):
    if i % 2 == 0:
        print(i)
