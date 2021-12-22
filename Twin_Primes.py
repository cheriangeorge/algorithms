### PPA 1 Week 1
### Twin primes are pairs of prime numbers that differ by 2. For example (3, 5), (5, 7), and (11,13) are twin primes.
### Write a function Twin_Primes(n, m) where n and m are positive integers and n < m , that returns all unique twin primes between m and n (both inclusive). The function returns a list of tuples and each tuple (a,b) represents one unique twin prime where n <= a < b <= m.

def Twin_Primes(n,m):
    primes=[]
    for i in range(n,m+1):
        if isPrime(i):
            primes.append(i)
    twin_primes=[]
    for i in range(len(primes)-1):
        if primes[i+1]-primes[i]==2:
            twin_primes.append((primes[i],primes[i+1]))
    return twin_primes
        
def isPrime(n):
    if len([i for i in range(1,n+1) if n%i==0])==2:
        return True
    return False
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))
