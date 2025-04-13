contador = 0
maior18 = 0
while contador < 10:
    idade = int(input("Digite a idade:"))
    if idade >=  18:
        maior18 += 1

    contador += 1
print("A quantidade de pessoas com mais de 18 é:", maior18)
