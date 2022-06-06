
def multiplier(n):
   i = 2
   multiplier = []
   while not n == 1:
       while n % i == 0:
           multiplier.append(i)
           n //= i
       i += 1
   return multiplier
print(*multiplier(4))