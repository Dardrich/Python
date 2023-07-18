nab = input().split()
nab = [int(i) for i in nab]
n = nab[0]
a = nab[1]
b = nab[2]

datas = []

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

lcm = a*b//gcd(a,b)
red = lcm//a
green = lcm//b
print(red+green)