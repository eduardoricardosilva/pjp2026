entrada = str(input("Qual o codigo [CAFÉ10]-[PROMO5]?  "))
def validar_cupom(codigo):

    if codigo == "CAFÉ10":
        return "0.10(10%)"
    
    elif codigo == "PROMO5":
        return "0.05(5%)" 
    
    else:
        return "0"

resultado = validar_cupom(entrada)
print(resultado)