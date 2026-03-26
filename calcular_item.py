valor_item = float(input("Qual o valor do item? R$"))
quant = int(input("Qual a quantidade de itens? "))

def calcular_item(preco_unitario,quantidade):
    total = preco_unitario * quantidade
    totimposto = total *1.05
    return totimposto
    
valor_total = calcular_item(valor_item,quant)
print(f"O valor total com iimposto é {valor_total}")