Altura = float(input("Insira a altura:"))
Sexo = input("insira o sexo:").upper()
if Sexo == "MASCULINO":
    pesoideal = 72.7 * Altura - 58
    print ("Seu peso ideal é:", pesoideal)
else:
    pesoideal = 61.1 * Altura - 44.7
    print ("Seu peso ideal é:", pesoideal)
