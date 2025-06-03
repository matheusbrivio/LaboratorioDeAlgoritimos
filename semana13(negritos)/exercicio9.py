def leitura_dados():
    A = []
    B = []
    for i in range(5):
        valorA = int(input(f"Digite o valor {i} do vetor A: "))
        A.append(valorA)
    for i in range(5):
        valorB = int(input(f"Digite o valor {i} do vetor B: "))
        B.append(valorB)
    return A, B

def soma_dados(A, B):
    C = []
    for i in range(len(A)):
        C.append(A[i] + B[i])
    return C

def apresenta_valor_C(C):
    print("Valores do vetor C:")
    for i in range(len(C)):
        print(C[i])

def main():
    A, B = leitura_dados()
    C = soma_dados(A, B)
    apresenta_valor_C(C)

main()
