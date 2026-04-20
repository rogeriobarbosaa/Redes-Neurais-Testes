# Definindo raíz do projeto
import sys
import os

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root)

# Exemplo
import matplotlib.pyplot as plt
from ativacao.sigmoide import sigmoide

class PerceptronFA1:
    def __init__(self):
        self.w = 3.0 # Definindo Peso
        self.b = 0.5 # Definindo Bias

    def calculate(self, x):
        self.line = self.w*x + self.b
        self.activation = sigmoide(self.line)

        print(f"\nValor de x: {x}")
        print(f"Resultado da Eq. Reta (y = {self.w}*{x} + {self.b}): {self.line}")
        print(f"Resultado da Função de Ativação (Sigmoide): {self.activation:.3f}")

        return self.line, self.activation

    def print_stats(self):
        print(f"Peso (w) = {self.w}")
        print(f"Bias (b) = {self.b}")

# Inicializando perceptron
p = PerceptronFA1()
p.print_stats()

# Calculando resultados a partir de valores de x
sum_results = [x for x in range(-10, 11)]
line_results = [] 
activation_results = []

for x in range(-10, 11):
    y, f = p.calculate(x)

    line_results.append(y)
    activation_results.append(f)

# Plotando gráficos da funções - reta e ativação (sigmoide)
plt.scatter(sum_results, line_results)
plt.title("Equação da Reta")
plt.xlabel("Valores de X")
plt.ylabel("Somatório")
plt.show()

plt.scatter(line_results, activation_results)
plt.title("Função Sigmoide")
plt.xlabel("Somatório")
plt.ylabel("Sigmoide")
plt.show()