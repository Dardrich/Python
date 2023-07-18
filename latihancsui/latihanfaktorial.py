def faktorial(n):
    if n < 0:
        print("Masukkan angka nonnegatif, Bung!")
        return faktorial(int(input("Masukkan angka yang ingin difaktorialkan: ")))
    elif n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

input_number = int(input("Masukkan angka yang ingin difaktorialkan: "))
print(faktorial(input_number))