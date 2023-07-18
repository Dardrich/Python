nm = input().split()
nm = [int(i) for i in nm]

if (nm[0]%2==0)& (nm[1]%2==0):
    print(nm[0]*nm[1])
