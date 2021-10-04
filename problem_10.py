#Finds sum of prime numbers bellow n
#Sieve Of Eratosthenes Method

#Create boolean array[n] and initialize as true.
#A value in array[i] will be false if not a prime.

n = 2000000

prime = [True for i in range(n+1)]
p = 2
while (p*p <= n):
	#If prime[p] is true, it's a prime
	if prime[p] == True:
		for i in range(p*p, n + 1, p):
			prime[i] = False
	p += 1

sum = 0

for p in range(2, n+1):
	if prime[p]: 
		sum += p

print(sum)