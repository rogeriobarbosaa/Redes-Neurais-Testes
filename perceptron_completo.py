import random

class PerceptronCompleto:
    def __init__(self, x_vet):
        self.w_vet = [random.random() for _ in range(len(x_vet))]     # Pesos (vetor)
        self.b = random.random()                                      # Bias
        self.line = self.produto_vetorial(x_vet, self.w_vet) + self.b # Eq. Reta ou Somatório

    def produto_vetorial(self, x_vet, w_vet):
        line = 0
        for x, w in zip(x_vet, w_vet):
            line = line + x*w
        return line
    
    def print_stats(self):
        print(f"Pesos (w) = {self.w_vet:.3f}")
        print(f"Bias (b) = {self.b:.3f}")
        print(f"Eq. Reta (y = w1*x1 + w2*x2 + ... + b) = {self.line:.3f}")