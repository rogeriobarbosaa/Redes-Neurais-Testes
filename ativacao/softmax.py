import math

''' essa função será a função de ativação final,
    que ficará depois da última camada.
    é usada para problemas de classificação,
    normalizando e calculando as possibilidades de cada classe'''

def softmax(somatorio_vet):
    softmax_vet = []

    # calculando o denominador da função
    denominador = 0
    for x in somatorio_vet:
        denominador = denominador + math.e**x

    # calculando a softmax para cada termo do vetor de entrada
    for x in somatorio_vet:
        softmax_x = math.e**x/denominador # softmax para x_i
        softmax_vet.append(softmax_x)

    return softmax_vet