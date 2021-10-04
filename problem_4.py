#Finds largest palindrome made from the product of two 3-digit numbers

import math

def main():
    print(f"The largest palindrome from the product of two 3-digit numbers is: {FindLargestPalindrome()}")


#Round down decimals
def round_down(n, decimals = 0):
    multipler = 10 ** decimals
    return math.floor(n * multipler) / multipler

#Checks if number is palindrome
def IsPalindrome(x):
    y = [int(i) for i in str(x)]
    for j in range(int(round_down(len(y)/2))):
        if y[j] != y[-j-1]:
            return False
    return True
   
#Request function
def FindLargestPalindrome():
    largestNumber = 0
    for i in range(999, 1, -1):
        for j in range(i, 1, -1):
            if IsPalindrome(i * j):
                templargest = i * j
                if largestNumber < templargest:
                    largestNumber = templargest
    return largestNumber


if __name__ == '__main__':
    main()