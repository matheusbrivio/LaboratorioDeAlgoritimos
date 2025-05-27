#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
#O sistema deve receber um valor de hora entre 0 e 23 e de minutos entre 0 e 59.


def convertor(horas, minutos):
    if horas > 12 and horas < 25:
        horafinal = horas - 12
        horacomminutos = str(horafinal) + ":" + str(minutos)
        return horacomminutos
    print("O horario ja está convertido!")



def main():
    horas = int(input("digite a hora a ser convertida:"))
    minutos = int(input("digite os minutos a ser convertido:"))
    horafinal = convertor(horas, minutos)
    print("O horario convertido é:", horafinal)

main()
