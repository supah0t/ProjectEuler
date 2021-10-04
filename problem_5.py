#Finds smallest positive number that is evenly divisible by all of the numbers from 1 to 20

from sys import exit


def main():
    print(Divisible(4))
    ##while True:
    ##    if Divisible(10):
    ##        print(f"The smallest number divisible by each of the numbers from 1 to 10 is: {i}")
    ##        exit(1)
    ##    else:
    ##        i = i + 1


#Finds smallest number divisible by all numbers up to divisibleBy
def Divisible(divisibleBy):
    j = divisibleBy + 1
    while True:
        for i in range(1, divisibleBy + 1):
            if j%i == 0:
                if i == divisibleBy:
                    return j
                continue
                
            else:
                j = j + 1
                break
            


if __name__ == '__main__':
    main()