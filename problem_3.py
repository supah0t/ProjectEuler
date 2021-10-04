#Finds largest prime factor of given number

x = int(input("Number for which to find largest prime factor: "))
primeFactors = []

for i in range(1, x):
    if x % i == 0:
        x = x / i
        primeFactors.append(i)
        if i > x:
            break
        
print(f"The prime factors of your number are: {primeFactors}")