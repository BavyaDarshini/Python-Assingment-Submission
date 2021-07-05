X = set([x*2 for x in range (1,11)])
primes = set()
for i in range (2,20):
    j = 2
    f = 0
    while j<=i/2:
        if i%j==0:
            f = 1
        j+=1
    if f==0:
        primes.add(i)
print("Prime Number : ",primes)
