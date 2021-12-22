### Goldbach's conjecture is one of the oldest and best-known unsolved problems in number theory. It states that every even number greater than 2 is the sum of two prime numbers. For example [ 12 = 5 + 7 ] [ 26=3+23 or 7+19 or 13+13]. Write a function Goldbach(n) where n is a positive even number (n>2) that returns a list of tuples. In each tuple (a,b) where a<=b, a and b should be prime numbers and the sum of a and b should equal to n. Sample Input : 12 - Output: [(5,7)]. 
def Goldbach(n):
    primes=[]
    for i in range(3,n+1):
        if isPrime(i):
            primes.append(i)
    goldbach=[]
    for i in primes:
        for j in primes[primes.index(i):]:
            if i+j==n:
                goldbach.append((i,j))
    return goldbach        
def isPrime(n):
    if len([i for i in range(1,n+1) if n%i==0])==2:
        return True
    return False
n=int(input())
print(sorted(Goldbach(n)))
