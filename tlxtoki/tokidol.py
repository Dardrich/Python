total = 0
all_within_range = True

for i in range(3):
    n = int(input())
    total += n
    if not (50 <= n <= 100):
        all_within_range = False

if total >= 200 and all_within_range:
    print('Lolos')
else:
    print('Tidak Lolos')
