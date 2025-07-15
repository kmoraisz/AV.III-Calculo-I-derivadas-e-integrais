
import sympy as sp

def soma_riemann_meio(expr, var, a, b, n):

    dx = (b - a) / n
    i = sp.Symbol('i', integer=True)

    # Ponto médio de cada subintervalo
    x_i = a + (i + 0.5) * dx

    # Substitui o ponto na função
    f_xi = expr.subs(var, x_i)

    # Soma de Riemann
    soma = sp.summation(f_xi * dx, (i, 0, n - 1))
    return soma

if __name__ == "__main__":
    x = sp.Symbol('x')

    entrada = input("Digite a função f(x): ")
    a_str = input("Digite o limite inferior a: ")
    b_str = input("Digite o limite superior b: ")
    n = int(input("Digite o número de subintervalos n: "))

    try:
        funcao = sp.sympify(entrada, locals={"pi": sp.pi})
        a = abs(float(sp.sympify(a_str, locals={"pi": sp.pi})))
        b = abs(float(sp.sympify(b_str, locals={"pi": sp.pi})))
        soma_simbolica = soma_riemann_meio(funcao, x, a, b, n)
        soma_numerica = soma_simbolica.evalf()
        if a > b:
            a, b = b, a

        print("\nSoma de Riemann (Teorema do Valor Médio):")
        sp.pprint(soma_simbolica)
        print(f"\nValor numérico aproximado da integral: {soma_numerica:.6f}")

    except Exception as e:
        print("Erro ao processar a função:", e)
