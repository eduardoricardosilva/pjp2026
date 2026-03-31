"""
cont = 1
resultado = 1
valor = int(input("Qual tabuada? "))

while cont <= 10:
    resultado = cont * valor
    print(f"{valor} x {cont} = {resultado}")
    cont += 1
    """

frutas = ["Maçã", "Banana", "Cereja", "Kiwi", "Laranja", "Goiaba","Pessêgo","Tangerina"]

frutas.append("Laranja")
frutas.insert(1,"Morango")

ordem = sorted(frutas)
print(ordem)