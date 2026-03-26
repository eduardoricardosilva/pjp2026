#função:
def saudar():
    print("Bem vindo à TechCoffee!" )
    print("O que deseja pedir hoje? ")

#função:
def saudar_personalizado(nome):
    print(f"Olá, {nome}! Seu café favorito já está sendo preparado.")

#chamando a função:
saudar()

#chamando a função:
saudar_personalizado("Seu Arnaldo")

#chamando a função:
saudar_personalizado("Eduardo")

#soma
def soma(n1, n2):
    print(n1 + n2)

#chamando soma
soma(5,7)

#subtrair
def subtrair(n1,n2):
    print(n1-n2)

#chamando subtrair
subtrair(5,7)

#multiplicação
def multi(n1,n2):
    print (n1*n2)

#chamando subtrair
multi(5,7)

#divisão
def divisao(n1,n2):
    print(f"{n1/n2:.2f}")

#chamando divisão
divisao(5,7)

#calcular total
def calcular_total(quantidade,preco_unitario):
    total = quantidade *  preco_unitario
    return total

#guardando o resultado em uma variavel
valor_da_venda = calcular_total(3,5.50)
print(f"O valor a pagar é: R${valor_da_venda}")