def numberLength(n):
    if n == 0:
        return 1
    length = int(math.log10(abs(n)))+1
    return length
    


def rotateNumber(x):
    digit = x % 10
    length= numberLength(x)-1
    x //= 10
    return x + digit * 10**length


def isprime(x):
    if x<2:
        return False
    if x == 2:
        return True
    
    for factor in range(2,x):
        if x % factor == 0:
            return False
    return True
        
    

def isCircularPrime(x):
    
    if not isprime(x):
        return False
    
    currentnumber = x
    length = numberLength(x)
    for i in range(length - 1):
        currentnumber = rotateNumber(currentnumber)
        if not isprime(currentnumber):
            return False
    return True
    

def nthCircularPrime(n):
    count = 0
    prime = 2
    
    if n == 0:
        return 2
    
    while count < n:
        prime += 1
        if isCircularPrime(prime):
            count +=1
    return prime