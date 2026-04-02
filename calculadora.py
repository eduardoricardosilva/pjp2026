import tkinter as tk
from tkinter import messagebox
from tkinter import END
import funcoes as f
 
def salvar_dados():
    nome = entry_valor1.get()
    email = entry_valor2.get()
    if nome and email:
        messagebox.showinfo("Sucesso calculo realizado!")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")
    mostradados = f.mostra();
    messagebox.showwarning("Erro", f"Por favor, preencha todos os campos. {mostradados}")


def calcular(operacao):
    valor1 = float(entry_valor1.get())
    valor2 = float(entry_valor2.get())
    if operacao == "+":
        resultado = f.soma(valor1,valor2) 

    if operacao == "-":
        resultado = f.subtracao(valor1,valor2)

    if operacao == "*":
        resultado = f.multiplicacao(valor1,valor2)

    if operacao == "/":
        resultado = f.divisao(valor1,valor2)
    entry_resultado.insert(0,resultado) 

def zerar ():
    entry_valor1.delete(0, END)
    entry_valor2.delete(0, END)
    entry_resultado.delete(0, END)
 
# Criando a janela
root = tk.Tk()
root.title("Calculadora")
root.geometry("350x350")
 
# Configurando o espaçamento interno da janela
root.config(padx=40, pady=40)
 
# --- ELEMENTOS DA TELA ---
 
# Linha 0: Nome
tk.Label(root, text="Valor1:").grid(row=0, column=0, sticky="w", pady=10)
entry_valor1 = tk.Entry(root, width=20, justify="right")
entry_valor1.grid(row=0, column=1, pady=5)

# Linha 1: E-mail
tk.Label(root, text="Valor2:").grid(row=1, column=0, sticky="w", pady=10)
entry_valor2 = tk.Entry(root, width=20, justify="right")
entry_valor2.grid(row=1, column=1, pady=5)

tk.Label(root, text="Resultado").grid(row=2, column=0, sticky="w", pady=20)
entry_resultado = tk.Entry(root, width=20, justify="right")
entry_resultado.grid(row=2, column=1, pady=5)

#Botão: soma
btn_soma = tk.Button(root, text="+", command=lambda:(calcular("+")))
btn_soma.grid(row=5, column=2,padx=5, pady=5)

#Botão: subtração
btn_sub = tk.Button(root, text="-", command=lambda:(calcular("-")))
btn_sub.grid(row=5, column=4, padx=5, pady=5)

#Botão: multiplicação
btn_multi = tk.Button(root, text="x", command=lambda:(calcular("*")))
btn_multi.grid(row=5, column=6,padx=5, pady=5)

#Botão: divisão
btn_divisao = tk.Button(root, text="÷", command=lambda:(calcular("/")))
btn_divisao.grid(row=5, column=8, padx=5, pady=5)

#Botão: zerar
btn_zerar = tk.Button(root, text="Zerar", command=lambda:(zerar()))
btn_zerar.grid(row=5, column=10,padx=5, pady=5)
 
root.mainloop()