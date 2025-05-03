maioridade = 0
feminino1835 = 0
cabeloloiros = 0
cabelocastanhos = 0
cabelopretos = 0
olhoazul = 0
olhoverde = 0
olhocastanho = 0
masculino = 0
feminino = 0

for i in range(15):
    sexo = input("digite seu sexo:").upper()
    if sexo == "M":
        masculino += 1
    elif sexo == "F":
        feminino += 1
    corolho = input("digite a cor do seu olho:").upper()
    if corolho == "A":
        olhoazul += 1
    elif corolho == "V":
        olhoverde += 1
    elif corolho == "C":
        olhocastanho += 1
    corcabelo = input("Digite a cor do seu cabelo:").upper()
    if corcabelo == "L":
        cabeloloiros += 1
    elif corcabelo == "C":
        cabelocastanhos += 1
    elif corcabelo == "P":
        cabelopretos += 1
    idade = int(input("Digite a idade:"))
    if i == 0:
        maioridade = idade
    elif maioridade < idade:
        maioridade = idade
    if sexo == "F" and idade >= 18 and idade <= 35 and corolho == "V" and corcabelo == "L":
        feminino1835 += 1
porcentagemcabelopreto = cabelopretos / 15 * 100
porcentagemcabeloloiro = cabeloloiros / 15 * 100
porcentagemcabelocastanho = cabelocastanhos / 15 * 100
porcentagemolhoazul = olhoazul / 15 * 100
porcentagemolhoverde = olhoverde / 15 * 100
porcentagemolhocastanho = olhocastanho / 15 * 100
porcentagemmasculino = masculino / 15 * 100
porcentagemfeminino = feminino / 15 * 100
print("Maior idade registrada é:", maioridade)
print("Quantidade de mulheres entre 18 e 35 anos com olhos verdes e cabelos loiros é:", feminino1835)
print("Porcentagem de cabelos pretos é:", porcentagemcabelopreto)
print("Porcentagem de cabelos loiros é:", porcentagemcabeloloiro)
print("Porcentagem de cabelos castanhos é:", porcentagemcabelocastanho)
print("Porcentagem de olhos azuis é:", porcentagemolhoazul)
print("Porcentagem de olhos verdes é:", porcentagemolhoverde)
print("Porcentagem de olhos castanhos é:", porcentagemolhocastanho)
print("Porcentagem de pessoas do sexo masculino é:", porcentagemmasculino)
print("Porcentagem de pessoas do sexo feminino é:", porcentagemfeminino)
