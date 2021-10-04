import functools 

def main():
    print(functools.reduce(lcm,range(2,21)))
    
    
#Greatest common divisor
def gcd(a,b):
    return gcd(b,a%b) if b else a

#Least common multiple
def lcm(a,b):
    return a/gcd(a,b)*b


if __name__ == '__main__':
    main()