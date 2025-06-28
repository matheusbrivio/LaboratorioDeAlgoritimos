#Crie uma função que receba dois arrays de inteiros como parâmetros. A função deve retornar um novo array contendo os elementos que:
#Estão presentes em ambos os arrays;
#Mas não podem aparecer mais de uma vez em cada array (ou seja, remova duplicatas #internas antes de comparar);
#E devem ser maiores que 10.


def elementoscomuns(array1, array2):
    unicos1 = []
    for i in range(len(array1)):
        if array1[i] not in unicos1:
            unicos1.append(array1[i])
    unicos2 = []
    for i in range(len(array2)):
        if array2[i] not in unicos2:
            unicos2.append(array2[i])
    array3 = []
    for i in range(len(unicos1)):
        for j in range(len(unicos2)):
            if unicos1[i] == unicos2[j] and unicos1[i] > 10:
                array3.append(unicos1[i])

    return array3
