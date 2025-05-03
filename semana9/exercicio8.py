foraintervalo = 0
intervalo = 0
for i in range (10):
    numero = int(input("digite o numero:"))
    if numero > 10 and numero < 20:
        intervalo += 1
    else:
        foraintervalo += 1
print(intervalo, foraintervalo)
