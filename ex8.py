soma = 0

contador = 0

while contador < 4:
    notas =  float(input("Digite a nota: "))
    soma = soma + notas
    contador += 1 
    
media = soma/4
print("A média", media)