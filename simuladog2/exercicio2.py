def ler_tamanho_array():
    tamanho = int(input("Digite o tamanho do array: "))
    return tamanho

def preencher_array(tamanho):
    array = []
    i = 0
    while i < tamanho:
        valor = int(input("Digite o elemento " + str(i) + ": "))
        array.append(valor)
        i = i + 1
    return array

def mostrar_array(array):
    print("")
    print("1 - Mostrar todos os valores")
    print("2 - Mostrar valores ímpares e múltiplos de 3")
    print("3 - Mostrar valores nas posições ímpares e múltiplos de 5")
    print("4 - Mostrar os valores invertidos")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        i = 0
        while i < len(array):
            print(array[i])
            i = i + 1

    elif opcao == 2:
        i = 0
        while i < len(array):
            if array[i] % 2 != 0 and array[i] % 3 == 0:
                print(array[i])
            i = i + 1

    elif opcao == 3:
        i = 0
        while i < len(array):
            if i % 2 != 0 and array[i] % 5 == 0:
                print(array[i])
            i = i + 1

    elif opcao == 4:
        i = len(array) - 1
        while i >= 0:
            print(array[i])
            i = i - 1

    else:
        print("Opção inválida")

def main():
    array = []
    tem_tamanho = 0
    tem_array = 0
    sair = 0

    while sair == 0:
        print("")
        print("1 - Definir tamanho do array")
        print("2 - Preencher array")
        print("3 - Mostrar array")
        print("4 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            tamanho = ler_tamanho_array()
            tem_tamanho = 1

        elif opcao == 2:
            if tem_tamanho == 1:
                array = preencher_array(tamanho)
                tem_array = 1
            else:
                print("Primeiro defina o tamanho do array.")

        elif opcao == 3:
            if tem_array == 1:
                mostrar_array(array)
            else:
                print("O array não foi preenchido ainda.")

        elif opcao == 4:
            sair = 1

        else:
            print("Opção inválida")

