import math

''' classes 0 e 1.

    vetores y_vet (vetor de valores reais) e y_hat_vet (vetor de valores preditos):
    - y_vet: contém os valores reais das classes, sendo 0 ou 1.
    - y_hat_vet: contém as probabilidades previstas pelo modelo para a classe 1,
        sendo valores contínuos entre 0 e 1 (geralmente obtidos pela função sigmoide).

    como se trata de um problema binário:
    a probabilidade da classe 0 é o complemento da classe 1, ou seja, (1 - y_hat).

    na binary cross entropy, os valores de y_hat devem se aproximar dos valores de y 
    para que o erro seja baixo.
    quando y_hat se afasta de y, o erro aumenta.

    essa função mede o erro entre os valores reais (y) e os valores previstos (y_hat),
    obtidos pela função de ativação anterior (função de ativação final da rede)

    para cada elemento:
    - se y = 1 -> considera log(y_hat)
    - se y = 0 -> considera log(1 - y_hat)'''

def bce(y_vet, y_hat_vet):
    # calculando somatório da função
    sum = 0
    for y, y_hat in zip(y_vet, y_hat_vet):
        sum = sum + (y*math.log(y_hat) + (1 - y)*math.log(1 - y_hat))

    # função binary cross entropy
    return -((1/len(y_hat_vet)) * sum)