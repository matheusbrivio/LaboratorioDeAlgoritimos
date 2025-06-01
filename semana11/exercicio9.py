def main():
    A, B = leituradedados()
    C = somadosdados(A, B)
    apresentavalorC(C)


def leituradedados():
    A = []
    B = []
    print("Preenchendo o vetor A:")
    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número para A: "))
        A.append(numero)
        print("O número:", numero, "foi adicionado com sucesso!")
    
    print("\nPreenchendo o vetor B:")
    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número para B: "))
        B.append(numero)
        print("O número:", numero, "foi adicionado com sucesso!")
    
    return A, B


def somadosdados(A, B):
    C = []
    for i in range(len(A)):
        soma = A[i] + B[i]
        C.append(soma)
    return C


def apresentavalorC(C):
    print("\nValores do vetor C (somas):")
    for i in range (5):
        print(C[i])


main()
