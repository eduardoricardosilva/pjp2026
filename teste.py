cont = 1
resultado = 1
valor = int(input("Qual tabuada? "))

while cont <= 10:
    resultado = cont * valor
    print(f"{valor} x {cont} = {resultado}")
    cont += 1
    