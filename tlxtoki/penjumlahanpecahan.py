import math

a,b = map(int,input().split())
c,d = map(int,input().split())

kpk = math.lcm(b,d)

sum = ((kpk*a)//b) + ((kpk*c)//d)

if math.gcd(sum,kpk) != 1:
    sum1 = sum//math.gcd(sum,kpk)
    kpk1 = kpk//math.gcd(sum,kpk)
    print(sum1,kpk1)
else:
    print(sum,kpk)

