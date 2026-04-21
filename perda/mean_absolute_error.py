def mae(y_vet, y_hat_vet):
    # calculando somatório da função
    sum = 0
    for y, y_hat in zip(y_vet, y_hat_vet):
        sum = sum + abs((y - y_hat)) # valor absoluto da diferença

    # função mean absolute error
    return (1/len(y_hat_vet)) * sum