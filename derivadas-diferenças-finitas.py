
from sympy import symbols, sympify, limit

x, h = symbols('x h')

entrada = input("Digite a função f(x): ")

f = sympify(entrada)

# Calcula a derivada: [f(x+h) - f(x)] / h
f_xh = f.subs(x, x + h)
d_f = (f_xh - f) / h

# Calcula o limite quando h → 0
derivada = limit(d_f, h, 0)

print(f"\nA derivada de f(x) é: {derivada}")