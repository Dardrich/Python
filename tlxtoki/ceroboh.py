nmxy = input().split()
nmxy = [int(i) for i in nmxy]

n = nmxy[0]
m = nmxy[1]
x = nmxy[2]
y = nmxy[3]

if (0 <= x <= n <= 20) and (0 <= y <= m <= 15):
    if (n-x) + (2*(m-y)) > 25:
        print("LOLOS")
    else:
        print('TIDAK LOLOS')