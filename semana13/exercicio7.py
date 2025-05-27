#Crie um método que converta graus Celsius para Fahrenheit.
#Função: def celsius_para_fahrenheit(celsius):
#Fórmula: Fahrenheit = (Celsius * 9/5) + 32


def main():
    celsius = float(input("Digite os graus em celsius:"))
    convertor = celsius_para_fahrenheit(celsius)
    print("O valor convertido para Fahrenheit:", convertor)

def celsius_para_fahrenheit(celsius):
    Fahrenheit = (celsius * 9/5) + 32
    print("Convertendo...")
    return Fahrenheit

main()
