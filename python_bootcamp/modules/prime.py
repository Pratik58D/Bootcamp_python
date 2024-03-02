def isprime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n >1:
        for i in range(2,n):
            if n % i ==0:
                return False

           # else: 
            #    if(n-1==i):
        return True
                
                
def rangeprime(start, end):
    primeNumbers=[]
    for i in range(start,end+1):
        if (isprime(i)):
            primeNumbers.append(i)
    return primeNumbers