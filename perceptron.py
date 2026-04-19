import random

class Perceptron:
    def __init__(self, x):
        self.w = random.random() # Peso
        self.b = random.random() # Bias
        self.line = self.w*x + self.b # Equação da Reta

    def print_stats(self):
        print(f"Peso (w) = {self.w:.3f}")
        print(f"Bias (b) = {self.b:.3f}")
        print(f"Eq. Reta (y = w*x + b) = {self.line:.3f}")

# Inicializando perceptron
x = int(input("Insira o valor de entrada: "))
p = Perceptron(x)
p.print_stats()