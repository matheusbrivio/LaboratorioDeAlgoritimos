lado1 = float(input("Insira o lado 1 do triangulo:"))
lado2 = float(input("Insira o lado 2 do triangulo:"))
lado3 = float(input("Insira o lado 3 do triangulo:"))

if lado1 and lado2 == lado3:
    print("O triangulo é equilátero.")
elif lado2 == lado1 or lado1 == lado3 or lado3 == lado2:
    print ("O triangulo é Isósceles")
else:
    print ("O triangulo é escaleno")
