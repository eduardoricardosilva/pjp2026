# Criando uma lista
frutas = ["Maçã", "Banana", "Cereja"]
 
# Adicionando itens
frutas.append("Laranja")      # Adiciona ao final
frutas.insert(1, "Morango")   # Adiciona no índice 1
 
# Acessando e Modificando
print(frutas[0])              # Saída: Maçã
frutas[2] = "Amora"           # Altera 'Banana' para 'Amora'
 
# Removendo itens
frutas.remove("Cereja")       # Remove pelo valor
item_removido = frutas.pop(0) # Remove pelo índice (e retorna o valor)
 
# Tamanho da lista
tamanho = len(frutas)
 
frutas = ["Maçã", "Banana", "Cereja"]
 
for fruta in frutas:
    print(f"Eu gosto de {fruta}")