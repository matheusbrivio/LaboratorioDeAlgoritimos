classificaçao = 0

resposta = input("Voce telefonou para vítima?:").upper()
resposta2 = input("Esteve no local do crime?:").upper()
resposta3 = input("Mora perto da vítima?:").upper()
resposta4 = input("Devia para vítima?:").upper()
resposta5 = input("Ja trabalhou com a vítima?:").upper()

if resposta == "SIM":
    classificaçao += 1
if resposta2 == "SIM":
    classificaçao += 1
if resposta3 == "SIM":
    classificaçao += 1
if resposta4 == "SIM":
    classificaçao += 1
if resposta5 == "SIM":
    classificaçao += 1

if classificaçao == 2:
    print("Voce é considerado Suspeito!")
elif classificaçao == 3 or classificaçao == 4:
    print("Voce é considerado Cúmplice!")
elif classificaçao == 5:
    print("Voce é considerado Assassino!")
else:
    print("Voce é considerado Inocente!")
