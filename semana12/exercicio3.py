def main():
    laranjas = qtdlaranjas()
    precofinal = laranjamultiplicacao(laranjas)
    print(precofinal)

def laranjamultiplicacao(laranjas):
    if laranjas > 12:
        valorlaranjas = laranjas * 0.25
        return valorlaranjas
    else:
        valorlaranjas = laranjas * 0.40
        return valorlaranjas

    

def qtdlaranjas():
    laranjas = int(input("Digite a quantidade de laranjas:"))
    return laranjas

main()
