# Buatlah fungsi subsetSum(), yang menerima input list bilangan
# bulat positif dan sebuah angka target. Fungsi mengembalikan
# nilai True jika ada tiga bilangan pada list yang jika dijumlahkan
# sama dengan angka target. Mengembalikan nilai False jika
# sebaliknya.

# >>> subsetSum([5, 4, 10, 20, 15, 19], 38)
# True
# >>> subsetSum([5, 4, 10, 20, 15, 19], 10)
# False

def subsetSum():
    numbers = input("Masukkan bilangan bulat positif, pisahkan dengan spasi: ").split()
    numbers = [int(num) for num in numbers]
    print(numbers)
    target = int(input("Masukkan angka target: "))

    for i in range(len(numbers) - 2):
        for j in range(i + 1, len(numbers) - 1):
            for k in range(j + 1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == target:
                    print("True")
                    return
    print("False")

subsetSum()
