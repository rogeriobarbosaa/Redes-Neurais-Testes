import random
from ativacao.threshold import threshold

class PerceptronCompleto:
    def __init__(self, x_vet):
        self.w_vet = [random.random() for _ in range(len(x_vet))]     # Pesos (vetor)
        self.b = random.random()                                      # Bias
        self.line = self.produto_vetorial(x_vet, self.w_vet) + self.b # Eq. Reta ou Somatório
        self.activation = threshold(self.line)                        # Função de ativação de exemplo: Threshold

    def produto_vetorial(self, x_vet, w_vet):
        line = 0
        for x, w in zip(x_vet, w_vet):
            line = line + x*w
        return line
    
    def print_stats(self):
        pesos = [round(w, 3) for w in self.w_vet]

        print(f"Pesos (w) = {pesos}")
        print(f"Bias (b) = {self.b:.3f}")
        print(f"Eq. Reta (y = w1*x1 + w2*x2 + ... + b) = {self.line:.3f}")
        print(f"Resultado da função de ativação (Threshold) = {self.activation}")

# Inicializando perceptron
x_vet = input("Insira os valores de entrada: ").split(", ")
x_vet = [float(x) for x in x_vet]

p = PerceptronCompleto(x_vet)
p.print_stats()