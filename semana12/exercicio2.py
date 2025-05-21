def main():
    valor = pegarvalor()
    resultadodobro = calcdobro(valor)
    resultadotriplo = calctriplo(valor)
    print(resultadodobro)
    print(resultadotriplo)

def pegarvalor():
    valor = int(input("Digite um valor:"))
    return valor
def calcdobro(numero):
    return numero *2
    
def calctriplo(numero):
    return numero *3
   
main()
