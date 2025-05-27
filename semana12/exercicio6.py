#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaInposto(taxaimposto, custo):
    taxa = custo * (taxaimposto / 100)
    valorfinal = custo + taxa
    return valorfinal

def main():
    valor = float(input("Digite o valor do produto:"))
    taxa = int(input("Digite o valor da taxa do produto:"))
    valorfinal = somaInposto(taxa, valor)
    print("O valor final é:", valorfinal)

main()
