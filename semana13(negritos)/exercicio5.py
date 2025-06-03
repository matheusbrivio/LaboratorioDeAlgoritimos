#Uma Empresa deseja efetuar uma pesquisa de ibope sobre a aceitação de um certo produto lançado por ela no mercado. Para isto encomendou uma pesquisa a ser realizada sobre o produto aplicada a 20 pessoas, onde cada pessoa responderá sim ou não. Ao final da pesquisa deverá ser mostrado o resultado dos seguintes cálculos:
#Total de pessoas que responderam sim;
#Total de pessoas que responderam não;

def main():
    quantidadesim, quantidadenao = perguntas()
    print("A quantidade de sim foi:",quantidadesim,"A quantidade de não foi:", quantidadenao)

def perguntas():
    variavel = 0
    variavel2 = 0
    for i in range (20):
        perguntasimounao = input("Digite sim ou nao para a aceitação do produto:").upper()
        if perguntasimounao == "SIM":
            variavel += 1
        elif perguntasimounao == "NAO":
            variavel2 += 1
    return variavel, variavel2

