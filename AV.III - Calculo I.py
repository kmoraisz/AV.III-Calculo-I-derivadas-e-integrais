import sympy as sp

def calcular_derivada():
    x, h = sp.symbols('x h')
    entrada = input("\nDigite a função f(x) para derivar: ")
    
    try:
        f = sp.sympify(entrada, locals={"pi": sp.pi})
        f_xh = f.subs(x, x + h)
        derivada_simbolica = (f_xh - f) / h
        derivada = sp.limit(derivada_simbolica, h, 0)
        print(f"\nA derivada de f(x) é:")
        sp.pprint(derivada)
    except Exception as e:
        print("Erro ao processar a função para derivada:", e)

def soma_riemann_meio(expr, var, a, b, n):
    dx = (b - a) / n
    i = sp.Symbol('i', integer=True)
    x_i = a + (i + 0.5) * dx
    f_xi = expr.subs(var, x_i)
    soma = sp.summation(f_xi * dx, (i, 0, n - 1))
    return soma

def calcular_integral():
    x = sp.Symbol('x')
    
    entrada = input("\nDigite a função f(x) para integrar: ")
    a_str = input("Digite o limite inferior a: ")
    b_str = input("Digite o limite superior b: ")
    n = int(input("Digite o número de subintervalos n: "))
    
    try:
        funcao = sp.sympify(entrada, locals={"pi": sp.pi})
        a = float(sp.sympify(a_str, locals={"pi": sp.pi}))
        b = float(sp.sympify(b_str, locals={"pi": sp.pi}))

        # Garante que a < b
        if a > b:
            a, b = b, a

        soma_simbolica = soma_riemann_meio(funcao, x, a, b, n)
        soma_numerica = soma_simbolica.evalf()

        print("\nSoma de Riemann (Ponto do meio):")
        sp.pprint(soma_simbolica)
        print(f"\nValor numérico aproximado da integral: {soma_numerica:.6f}")

    except Exception as e:
        print("Erro ao processar a função para integral:", e)

def menu():
    while True:
        print("Vamos calcular a derivada e/ou integral de uma função?")
        print("\nEscolha a operação desejada:")
        print("1 - Calcular derivada (Diferenças Finitas)")
        print("2 - Calcular integral (Soma de Riemann)")
        escolha = input("Digite 1 ou 2: ")

        if escolha == '1':
            calcular_derivada()
            resposta = input("\nDeseja calcular a integral agora? (s/n): ")
            if resposta.lower() == 's':
                calcular_integral()
        elif escolha == '2':
            calcular_integral()
            resposta = input("\nDeseja calcular a derivada agora? (s/n): ")
            if resposta.lower() == 's':
                calcular_derivada()
        else:
            print("Escolha inválida. Tente novamente.")

        repetir = input("\nDeseja fazer outra operação? (s/n): ")
        if repetir.lower() != 's':
            print("Encerrando o programa.")
            break

if __name__ == "__main__":
    menu()
