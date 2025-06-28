def inserir_faturamento(faturamento):
    for i in range(4):
        valor = float(input("Digite o faturamento da semana " + str(i + 1) + ": "))
        faturamento[i] = valor

def exibir_faturamento(faturamento):
    for i in range(4):
        print("Semana " + str(i + 1) + ":", faturamento[i], "reais")

def calcular_relatorio(faturamento):
    soma = 0
    for i in range(4):
        soma = soma + faturamento[i]

    media = soma / 4
    print("Média mensal de faturamento:", media, "reais")

    maior = faturamento[0]
    semana_maior = 1
    for i in range(1, 4):
        if faturamento[i] > maior:
            maior = faturamento[i]
            semana_maior = i + 1

    print("Semana com maior faturamento: Semana " + str(semana_maior) + " com " + str(maior) + " reais")

    for i in range(3):
        diferenca = faturamento[i + 1] - faturamento[i]
        porcentagem = (diferenca / faturamento[i]) * 100
        if porcentagem >= 0:
            print("Crescimento da semana " + str(i + 1) + " para semana " + str(i + 2) + ":", round(porcentagem, 2), "%")
        else:
            print("Queda da semana " + str(i + 1) + " para semana " + str(i + 2) + ":", round(porcentagem, 2), "%")

def alterar_faturamento(faturamento):
    semana = int(input("Digite o número da semana que deseja alterar (1 a 4): "))
    if semana >= 1 and semana <= 4:
        novo_valor = float(input("Digite o novo valor para a semana " + str(semana) + ": "))
        faturamento[semana - 1] = novo_valor
    else:
        print("Semana inválida.")

def main():
    faturamento = [0, 0, 0, 0]
    cadastrado = 0
    sair = 0

    while sair == 0:
        print("")
        print("1 - Inserir faturamento semanal")
        print("2 - Exibir faturamento")
        print("3 - Calcular e exibir relatórios")
        print("4 - Alterar faturamento de uma semana")
        print("5 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            inserir_faturamento(faturamento)
            cadastrado = 1

        elif opcao == 2:
            if cadastrado == 1:
                exibir_faturamento(faturamento)
            else:
                print("Nenhum faturamento cadastrado ainda.")

        elif opcao == 3:
            if cadastrado == 1:
                calcular_relatorio(faturamento)
            else:
                print("Nenhum faturamento cadastrado ainda.")

        elif opcao == 4:
            if cadastrado == 1:
                alterar_faturamento(faturamento)
            else:
                print("Nenhum faturamento cadastrado ainda.")

        elif opcao == 5:
            sair = 1

        else:
            print("Opção inválida.")
