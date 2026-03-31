
def calculadora(opcao, valor1, valor2):
    match opcao: 
        case "+":
            return valor1 + valor2
        case "-":
            return valor1 - valor2
        case "*":
            return valor1 * valor2
        case "/":
            return valor1 / valor2
        
valor1 = int(input('Digite um numero: '))
valor2 = int(input('Digite um numero: '))
opcao = input('Escolha a operação (+, -, *, /): ')
        
resultado = calculadora(opcao, valor1, valor2)
print(resultado)