contador = 0
valores = []
while contador < 5:
    valor = int(input('Digite um número: '))
    valores.append(valor)
    contador +=1

maior = max(valores)
menor = min(valores)
soma = sum(valores)
media = sum(valores) / len(valores)

print(f'O maior numero digitado foi {maior}')
print(f'O menor numero digitado foi {menor}')
print(f'A soma de todos os numeros é {soma}')
print(f'A media é {media}')
