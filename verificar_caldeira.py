temperatura = float(input("Qual a temperatura? "))
def temp_atual(temp):

    if temp < 90:
        return "Aquecendo..."
    
    if temp <= 100:
        return "Pronto para uso."
    
    if temp > 100:
        return "PERIGO: Superaquecimento!"
    
result = temp_atual(temperatura)
print(result)