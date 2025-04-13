contador = 0 
idade = 0
contadorM = 0
contadorF = 0
salarioF = 0
salarioM = 0
idadeF = 0
idadeM = 0
salario10000 = 0
maior_idadeF = 0
menor_idadeF = 200
maior_idadeM = 0
menor_idadeM = 200
while contador < 10:
    print("PESSOA:", contador + 1)
    sexo = input("Digite o sexo(F/M):").upper()
    if sexo == "F":
        idade = int(input("Digite a idade:"))
        idadeF += idade
        if idade > maior_idadeF:
            maior_idadeF = idade
        if idade < menor_idadeF:
            menor_idadeF = idade
        salario = float(input("Digite o salario:"))
        salarioF += salario
        if salario <= 10000:
            salario10000 += 1
        contadorF += 1
        contador += 1
    elif sexo == "M":
        idade = int(input("Digite a idade:"))
        idadeM += idade
        if idade > maior_idadeM:
            maior_idadeM = idade
        if idade < menor_idadeM:
            menor_idadeM = idade
        salarioM += float(input("Digite o salario:"))
        contadorM += 1
        contador += 1
    else:
        print("Sexo invalido!")
    
    

mediasalarioM = salarioM / contadorM
mediasalarioF = salarioF / contadorF

print("A média de salario masculina é:", mediasalarioM)
print("A maior idade do grupo masculino é:", maior_idadeM, "E a menor:", menor_idadeM)

print("A média de salario feminina é:", mediasalarioF)
print("A maior idade do grupo feminino é:", maior_idadeF, "E a menor:", menor_idadeF)
print("A quantidade de mulheres com salario ate R$ 10000 é:", salario10000)
