Nome = input("Digite o nome do funcionario:")
Salario = float(input("Digite o valor do salário:"))
TempoServiço = int (input ("Digite o tempo de trabalho:"))
if TempoServiço >= 5 and Salario <= 2000:
    ValorFinal = Salario * 1.10
    print("O funcionario:", Nome, "Tem como sálario:", ValorFinal)
else:
    ValorFinal = Salario * 1.05
    print ("O funcionario:", Nome, "Tem como sálario:", ValorFinal)
