numero = int(input("Digite um numero: "))
fatorial = 1 
contador = numero

while contador > 1:
    fatorial = fatorial * contador
    contador -=1
    
print("Fatorial de",numero, "é",fatorial)
