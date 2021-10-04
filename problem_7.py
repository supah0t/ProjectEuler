#Program to provide a list of n prime numbers

from itertools import count


def ListOfPrimes(x):
    primeList = [2]
    for i in count(2):
        if len(primeList) == x:
            return primeList[len(primeList) - 1]
        for j in range(2, i):
            if i%j == 0:
                break
            elif j == i - 1:
                primeList.append(i)

x = int(input("Number of primes: "))
print(ListOfPrimes(x))