
from random import randint as r
def GetPolynomial(n):
    num_lst = [str(r(0, 100)) for i in range(n + 1)]
    result = ''
    for i in range(0, n + 1):
        if i == n:
            result += num_lst[i] + ' = 0'
        elif i == n-1:
            result += num_lst[i] + 'x + '
        elif i < n-1:
            result += num_lst[i] + 'x^' + str(n - i) + ' + '
    return result

n_1 = int(input('Enter the value of the degree for the first polynomial: '))
n_2 = int(input('Enter the value of the degree for the second polynomial: '))

with open('Polynominal_1.txt', 'w+') as data_1, open('Polynominal_2.txt', 'w+') as data_2:
    data_1.write((GetPolynomial(n_1)))
    data_2.write((GetPolynomial(n_2)))




