#Finds the difference between the sum of the squares of the first n natural numbers and the square of the sum

def main():
    x = int(input("Insert Number: "))
    print(SquareOfSums(x) - SumOfSquares(x))
    
    
def SumOfSquares(x):
    sumSquare = 0
    for i in range(x + 1):
        sumSquare = sumSquare + pow(i, 2)
    return sumSquare

def SquareOfSums(x):
    squareSum = 0
    for i in range(x + 1):
        squareSum = squareSum + i
    return pow(squareSum, 2)

if __name__ == '__main__':
    main()