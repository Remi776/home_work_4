# Ряд Мадхавы

import math

n = int(input('Enter the number of components: '))

def piMadhava(n, s = 1, z = 1):
    for i in range(1, n):
        s -= z / ((2*i + 1) * math.exp((i) * math.log(3)))
        z = -z
    return s * math.sqrt(12)
print(piMadhava(n))
