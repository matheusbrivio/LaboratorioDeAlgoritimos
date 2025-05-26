#Faça um algoritmo que leia cinco notas e faça a média das notas, após isso informe a situação do aluno: 
#>= 7 			Aprovado 
#4 <= e < 7 	Recuperação 
#< 4 			Reprovado 
#Utilize três funções para apresentar a situação do aluno.

def main():
    notas = []
    pegarnotas(notas)
    media(notas)

def pegarnotas(lista):
    for i in range (5):
        while True:
            try:
                nota = float(input("Digite a nota:"))
                break
            except ValueError:
                print("Tente uma nota válida!")
        lista.append(nota)
        


def media(lista):
    soma = 0
    for i in range (5):
        soma += lista [i]

    media = soma / 5
    print("A sua média é:",media)


main()
