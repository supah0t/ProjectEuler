#Finds sum of multiples of 3 or 5 bellow input number

maxnumber = int(input('Number bellow which to find the sum of multiples of 3 or 5: '))

totalsum = 0

for i in range(maxnumber):
    if i%3 == 0:
        totalsum += i
    elif i%5 ==0:
        totalsum += i

print(totalsum)
