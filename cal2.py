import tkinter as tk
from tkinter import messagebox

def calcular(operacao):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                messagebox.showerror("Erro", "Divisão por zero não é permitida.")
                return
        entry_resultado.config(state=tk.NORMAL)
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, str(resultado))
        entry_resultado.config(state=tk.DISABLED)
        entry_num1.delete(0, tk.END)
        entry_num2.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def sair():
    root.destroy()

root = tk.Tk()
root.title("Calculadora Adaptativa")
root.geometry("400x400")
root.resizable(True, True)
root.eval('tk::PlaceWindow . center')
root.configure(bg='#f2f2f2')
font_style = ("Arial", 14)

frame_input = tk.Frame(root, bg='#f2f2f2')
frame_input.pack(pady=20)

frame_buttons = tk.Frame(root, bg='#f2f2f2')
frame_buttons.pack(pady=10)

frame_result = tk.Frame(root, bg='#f2f2f2')
frame_result.pack(pady=10)

label_num1 = tk.Label(frame_input, text="Primeiro Número:", bg='#f2f2f2', font=font_style)
label_num1.grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(frame_input, font=font_style)
entry_num1.grid(row=0, column=1, padx=5, pady=5, ipadx=10, ipady=5)

label_num2 = tk.Label(frame_input, text="Segundo Número:", bg='#f2f2f2', font=font_style)
label_num2.grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(frame_input, font=font_style)
entry_num2.grid(row=1, column=1, padx=5, pady=5, ipadx=10, ipady=5)

button_add = tk.Button(frame_buttons, text='+', width=8, height=2, command=lambda: calcular('+'), bg='#4CAF50', fg='white', font=font_style)
button_sub = tk.Button(frame_buttons, text='-', width=8, height=2, command=lambda: calcular('-'), bg='#2196F3', fg='white', font=font_style)
button_mul = tk.Button(frame_buttons, text='*', width=8, height=2, command=lambda: calcular('*'), bg='#FF9800', fg='white', font=font_style)
button_div = tk.Button(frame_buttons, text='/', width=8, height=2, command=lambda: calcular('/'), bg='#F44336', fg='white', font=font_style)

button_add.grid(row=0, column=0, padx=10, pady=10)
button_sub.grid(row=0, column=1, padx=10, pady=10)
button_mul.grid(row=1, column=0, padx=10, pady=10)
button_div.grid(row=1, column=1, padx=10, pady=10)

label_result = tk.Label(frame_result, text="Resultado:", bg='#f2f2f2', font=font_style)
label_result.grid(row=0, column=0, padx=5, pady=5)
entry_resultado = tk.Entry(frame_result, font=font_style, state=tk.DISABLED)
entry_resultado.grid(row=0, column=1, padx=5, pady=5, ipadx=10, ipady=5)

button_exit = tk.Button(root, text="Sair", command=sair, bg='red', fg='white', font=font_style)
button_exit.pack(pady=20, ipadx=20, ipady=5)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
frame_input.grid_columnconfigure(0, weight=1)
frame_input.grid_columnconfigure(1, weight=1)
frame_buttons.grid_columnconfigure(0, weight=1)
frame_buttons.grid_columnconfigure(1, weight=1)
frame_result.grid_columnconfigure(0, weight=1)
frame_result.grid_columnconfigure(1, weight=1)

root.mainloop()
