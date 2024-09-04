def calculadora():
    while True:
        print("\n=============================")
        print("     *** CALCULADORA ***")
        print("=============================")
        print("|  Escolha a operação:       |")
        print("|  1. Adição       (+)       |")
        print("|  2. Subtração    (-)       |")
        print("|  3. Multiplicação(*)       |")
        print("|  4. Divisão      (/)       |")
        print("|----------------------------|")
        print("|  Digite 'q' para sair      |")
        print("=============================\n")

        escolha = input("Digite a operação desejada: ")

        if escolha == 'q':
            print("\nEncerrando a calculadora. Até mais!")
            break

        if escolha in ['+', '-', '*', '/']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '+':
                resultado = num1 + num2
                print(f"\nResultado: {num1} + {num2} = {resultado}")
            elif escolha == '-':
                resultado = num1 - num2
                print(f"\nResultado: {num1} - {num2} = {resultado}")
            elif escolha == '*':
                resultado = num1 * num2
                print(f"\nResultado: {num1} * {num2} = {resultado}")
            elif escolha == '/':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"\nResultado: {num1} / {num2} = {resultado}")
                else:
                    print("\n[🚫 - Erro]: Divisão por zero não é permitida.")
        else:
            print("\n[🚫 - Escolha inválida] Tente novamente.")

calculadora()
