convidados = ["Ana", "Carlos", "Beatriz", "Daniel", "Eduardo"]

nome = input('Qual é seu nome: ').lower()
minusc = []

for pessoa in convidados:
    minusc.append(pessoa.lower())

if nome in minusc:
    print(f'Bem-vindo! Nome na lista.')
else: 
    print('Desculpe, seu nome não consta na lista.')