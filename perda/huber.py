def huber(y, y_hat, delta):
    if abs(y - y_hat) < delta:
        return 0.5 * (y - y_hat)**2
    elif abs(y - y_hat) >= delta:
        return delta * (abs(y - y_hat) - 0.5*delta)