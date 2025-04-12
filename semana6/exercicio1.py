opcao = 0
contador = 0
somaaltura = 0
somaidade = 0
while opcao != 3:
    print("1 - Cadastrar pessoa")
    print("2 - Mostrar média parcial de altura e idade")
    print("3 - Sair")
    opcao = int(input("Digite a opçao:"))
    if opcao == 1:
        altura = int(input("Digite a altura:"))
        idade = int(input("Digite a idade:"))
        somaaltura += altura
        somaidade += idade
        contador += 1
        if contador >= 3:
            mediaaltura = somaaltura / contador
            mediaidade = somaidade / contador
            print("Media de altura:", mediaaltura, "Media de idade:", mediaidade)
    elif opcao == 2:
        mediaaltura = somaaltura / contador
        mediaidade = somaidade / contador
        print("Media de altura:", mediaaltura, "Media de idade:", mediaidade)
        
print("Voce saiu!, aqui está as medias:", "Media de altura:", mediaaltura, "Media de idade:", mediaidade)

