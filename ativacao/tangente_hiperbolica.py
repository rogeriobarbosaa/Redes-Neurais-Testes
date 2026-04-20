import math

def tangente_hiperbolica(somatorio):
    return (math.e**somatorio - math.e**(-somatorio))/(math.e**somatorio + math.e**(-somatorio))