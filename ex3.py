
contador = 1 
resultado = 1
numero = 0

numero = int(input("Qual tabuada?"))

while contador < 11:
    resultado = contador * numero
    print(f"{numero} x {contador} = {resultado}")
    contador += 1