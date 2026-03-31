notas = [4.5, 7.0, 8.5, 5.0, 10, 6.5, 9.0, 3.0, 7.5, 6.0]
aprovados = []
reprovados = []
for nota in notas:
    if (nota >= 7.0):
        aprovados.append(nota)

    else:
        reprovados.append(nota)
print("Aprovados: ", aprovados)
print("Reprovados: ", reprovados)