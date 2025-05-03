jornalA = 0
jornalB = 0
jornalC = 0
for i in range (20):
    jornal = input("qual jornal mais lido? A B OU C?").upper()
    if jornal == "A":
        jornalA += 1
    elif jornal == "B":
        jornalB += 1
    elif jornal == "C":
        jornalC += 1
porcentagemA = jornalA / 20 * 100
porcentagemB = jornalB / 20 * 100
porcentagemC = jornalC / 20 * 100
if porcentagemA <= porcentagemB and porcentagemA <= porcentagemC:
    print("A porcentagem de A é:", porcentagemA)
    if porcentagemB <= porcentagemC:
        print("A porcentagem de B é:", porcentagemB)
        print("A porcentagem de C é:", porcentagemC)
    else:
        print("A porcentagem de C é:", porcentagemC)
        print("A porcentagem de B é:", porcentagemB)
elif porcentagemB <= porcentagemA and porcentagemB <= porcentagemC:
    print("A porcentagem de B é:", porcentagemB)
    if porcentagemA <= porcentagemC:
        print("A porcentagem de A é:", porcentagemA)
        print("A porcentagem de C é:", porcentagemC)
    else:
        print("A porcentagem de C é:", porcentagemC)
        print("A porcentagem de A é:", porcentagemA)
else:
    print("A porcentagem de C é:", porcentagemC)
    if porcentagemA <= porcentagemB:
        print("A porcentagem de A é:", porcentagemA)
        print("A porcentagem de B é:", porcentagemB)
    else:
        print("A porcentagem de B é:", porcentagemB)
        print("A porcentagem de A é:", porcentagemA)
