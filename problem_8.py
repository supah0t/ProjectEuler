#Program to find the 13 adjacent digits in a n-digit number that have the greatest product and it's value

#Insert text file with the desired number
f = open('problem_8_number.txt', 'r')
number = f.read()

digits = int(input("How many adjacent digits: "))

tempBig = 0
topBig = 0

for i in range(len(number) - (digits-1)):
    tempBig = 1
    for j in range(int(digits)):
        tempBig = tempBig * int(number[i+j])
        if tempBig > topBig:
            topBig = tempBig

print(topBig)
f.close()
