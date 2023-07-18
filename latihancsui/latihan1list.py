# Buatlah fungsi count_neg ( ), yang menerima input
# list integer dua dimensi, dan mengembalikan list 1
# dimensi berisi banyaknya elemen negatif dari setiap
# anggotanya.

# misal:
# >>> count_neg ([[2,-1,0], [4,3,4]])
# [1,0]
# >>> count_neg ([[0, -1], [-2,-4],[5,5],[4,-4]])
# [1,2,0,1]

def count_neg():
    matrix = []
    rows = int(input("Masukkan jumlah baris: "))

    for _ in range(rows):
        row = [int(num) for num in input("Masukkan angka-angka pada baris (pisahkan dengan spasi): ").split()]
        matrix.append(row)

    neg_counts = []

    for row in matrix:
        neg_count = sum(1 for value in row if value < 0)
        neg_counts.append(neg_count)

    return neg_counts

print(count_neg())