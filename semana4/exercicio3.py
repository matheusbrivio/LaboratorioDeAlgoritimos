Nota1 = float(input("Insira a primeira nota do aluno:"))
Nota2 = float(input("Insira a segunda nota do aluno:"))
frequencia = int(input("Insira a frequencia do aluno:"))
Notafinal = Nota1 + Nota2 /2
if Notafinal >= 7 and frequencia >= 75:
    print("Aluno aprovado")
elif Notafinal >= 4 and Notafinal < 7 and frequencia >= 75:
    print("Aluno está de exame")
else:
    print("Aluno reprovado")
