horasTrabalhadas = float(input("digite as horas trabalhadas:"))
valorhora = 35
salario = horasTrabalhadas * valorhora
if salario < 1000:
    salariofinal = salario + 300
    print ("Salario final:", salariofinal)
else:
    print("Salario final:", salario)
