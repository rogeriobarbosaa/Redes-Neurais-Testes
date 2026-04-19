import random

class Perceptron:
    def __init__(self, x):
        self.w = random.random() # Peso
        self.b = random.random() # Bias
        self.line = self.w*x + self.b # Equação da Reta

    def print_stats(self):
        print(f"Peso (w) = {self.w:.2f}")
        print(f"Bias (b) = {self.b:.2f}")
        print(f"Eq. Reta (y = w*x + b) = {self.line:.2f}")

# Inicializando perceptron com exemplo  
p = Perceptron(10)
p.print_stats()