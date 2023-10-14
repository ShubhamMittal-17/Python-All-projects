def seive(n):
    prime = [True for _ in range(n+1)]
    prime[0] = prime[1] = False
    p = 2
    while p*p<=n:
        if prime[p]:
            for i in range(p*p,n+1,p):
                prime[i] = False
        p+=1
    primes = [i for i, is_prime in enumerate(prime) if is_prime]
    return primes
def pf(n):
    primes = seive(n)
    for i in range(2,n+1):
        factors = []
        num = i
        for p in primes:
            while num%p ==0:
                factors.append(p)
                num//= p
            if num == 1:
                break
        if num>1:
            factors.append(num)
        res = " ".join(map(str,factors))
        print(res)
n = int(input())
pf(n)