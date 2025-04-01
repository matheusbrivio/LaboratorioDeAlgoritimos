Nota1 = float(input("Insira a primeira nota do aluno:"))
Nota2 = float(input("Insira a segunda nota do aluno:"))
Media = (Nota1 + Nota2) / 2

if Media >= 9 and Media <= 10:
    print("O aluno teve as notas:", Nota1, Nota2, "Media:",Media, "E conceito: A, Portando APROVADO.")
elif Media >= 7.5 and Media <= 9:
    print("O aluno teve as notas:", Nota1, Nota2, "Media:",Media, "E conceito: B, Portando APROVADO.")
elif Media >= 6 and Media <= 7.5:
    print("O aluno teve as notas:", Nota1, Nota2, "Media:",Media, "E conceito: C, Portando APROVADO.")
elif Media >= 4 and Media <= 6:
    print("O aluno teve as notas:", Nota1, Nota2, "Media:",Media, "E conceito: D, Portando REPROVADO.")
else: 
    print("O aluno teve as notas:", Nota1, Nota2, "Media:",Media, "E conceito: E, Portando REPROVADO.")
