contador = 0
elevadorA = 0
elevadorB = 0
elevadorC = 0
while contador < 10:
    elevador = input("Qual seu elevador de preferencia?").upper()
    if elevador == "A":
        elevadorA += 1
        contador += 1
    elif elevador == "B":
        elevadorB += 1
        contador += 1
    elif elevador == "C":
        elevadorC += 1
        contador += 1
    else:
        print("Elevador invalido")
porcentagemA = elevadorA / 10 * 100
porcentagemB = elevadorB / 10 * 100
porcentagemC = elevadorC / 10 * 100

print("A quantidade de pessoas que usam o elevador A é:", elevadorA, "E a porcentagem é de:", porcentagemA)
print("A quantidade de pessoas que usam o elevador B é:", elevadorB, "E a porcentagem é de:", porcentagemB)
print("A quantidade de pessoas que usam o elevador C é:", elevadorC, "E a porcentagem é de:", porcentagemC)
