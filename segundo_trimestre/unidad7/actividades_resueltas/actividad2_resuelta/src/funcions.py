import math

def es_primo(num):
    if num < 2:
        return False
    for n in range(2, math.floor(math.sqrt(num) + 1)):
        if num % n == 0:
            return False
    return True