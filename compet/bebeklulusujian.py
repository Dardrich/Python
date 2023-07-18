def input_numbers():
    n = int(input("Banyak bebek yang ikut ujian: "))
    numbers = []
    daftar = []
    for _ in range(n):
        number = int(input())
        numbers.append(number)
    avg = sum(numbers)/n
    for num in numbers:
        if avg < num:
            daftar.append(num)
    print(len(daftar))

input_numbers()