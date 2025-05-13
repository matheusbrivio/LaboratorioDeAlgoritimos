import random
guardioes = 0
invasores = 0

guardiao = []
for i in range (5):
    forca = int(input("digite o valor da força do guardião:"))
    while forca > 100 or forca < 0:
        print("Digite força de 0 a 100!")
        forca = int(input("digite o valor da força do guardião ", (i + 1)))
    guardiao.append(forca)

invasor = []
for i in range (5):
    forca = random.randint(0, 100)
    invasor.append(forca)

for i in range (5):
    if guardiao[i] > invasor[i]:
        guardioes += 1
        print("o resultado da batalha", i + 1, "foi vitoria dos guardioes!")
    elif guardiao[i] <= invasor[i]:
        invasores += 1
        print("o resultado da batalha", i + 1, "foi vitoria dos invasores!")
    

print("a força dos guardioes é:", guardiao)
print("a força dos invasores é:", invasor)
print("o placar final foi: guardioes:", guardioes, "X invasores:", invasores)
