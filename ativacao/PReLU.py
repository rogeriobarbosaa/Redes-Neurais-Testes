def prelu(somatorio, a):
    return max(0, somatorio) + a * min(0, somatorio)