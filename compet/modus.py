# n = int(input())

# data = []
# m = input().split()

# for num in m:
#     data.append(int(num))

# if len(data) == n:
#     max_length = max(len(str(num)) for num in data)
# print(max_length)

from collections import Counter

# Membaca input N
N = int(input())

# Membaca N bilangan bulat
data = list(map(int, input().split()))

# Menghitung kemunculan setiap bilangan
counter = Counter(data)

# Mencari bilangan dengan kemunculan terbanyak
max_count = max(counter.values())

# Mengumpulkan semua bilangan dengan kemunculan terbanyak
modes = [num for num, count in counter.items() if count == max_count]

# Menampilkan modus terbesar
print(max(modes))

