def main ():
    A, B, C = pesquisa()
    porcentagem = porcentagemjornal(A,B,C)
def pesquisa():
    A = 0
    B = 0
    C = 0
    for i in range (20):
        pesquisajornal = input("Qual seu jornal favorito?, A, B ou C?").upper()
        if pesquisajornal == "A":
            A += 1
        elif pesquisajornal == "B":
            B += 1
        elif pesquisajornal == "C":
            C += 1
        else:
            print("Jornal invalido!")
    return A, B, C

def porcentagemjornal(a, b, c):
    porcentagemA = a * 100 /20
    porcentagemB = b * 100 /20
    porcentagemC = c * 100 /20
    print("A porcentagem das pessoas que preferem o jornal A é:", porcentagemA)
    print("A porcentagem das pessoas que preferem o jornal B é:", porcentagemB)
    print("A porcentagem das pessoas que preferem o jornal C é:", porcentagemC)

main()
