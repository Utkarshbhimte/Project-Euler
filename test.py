print 'started'
num = 600851475143
# num = 500
primes = []
ans = 1
i=0

def findFactor(num):
    #     i = 0
    for i in range(2, 1000000):
        if num % i == 0:
            print num ,'/ ',+ i, '=', num/i
            num = num / i
            primes.append(i)
            findFactor(num)
            break

findFactor(num)

for v in primes:
    ans = ans * v
print 'done', sorted(set(primes)), ans