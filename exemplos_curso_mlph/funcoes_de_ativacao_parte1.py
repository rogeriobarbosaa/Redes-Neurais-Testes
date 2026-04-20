# Definindo raíz do projeto
import sys
import os

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root)

# Exemplo
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

    def print_stats(self):
        print(f"Peso (w) = {self.w}")
        print(f"Bias (b) = {self.b}")

# Inicializando perceptron
p = PerceptronFA1()
p.print_stats()

for x in range(-10, 11):
    p.calculate(x)