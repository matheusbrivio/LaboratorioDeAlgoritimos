contador = 0
somaidade = 0
maioridade = 0
parte = 0
while contador < 7:
    idade = int(input("Digite a idade:"))
    if idade >= 18:
        maioridade += 1
    if idade >= 10 and idade <= 30:
        parte += 1
    somaidade += idade
    contador += 1
media = somaidade / 7
porcentagem = parte / 7 * 100
print ("A media de idade é:", media,)
print ("A quantidade de pessoas maiores de idade é:", maioridade)
print ("A porcentagem de pessoas entre 10 e 30 anos é:", porcentagem)
