def is_semiprime(n):
    if n<2:
        if n == 1:
            return True
        else:
            return False
    else:
        daftar = []
        for i in range(1,n+1):
            if n%i==0:
                daftar.append(i)
        if 2 <= len(daftar) <= 4:         
            return True
        else:        
            return False
                          
def input_numbers():
    n = int(input())
    numbers = []
    for _ in range(n):
        number = int(input())
        numbers.append(number)

    for number in numbers:
        if is_semiprime(number):
            print("YA")
        else:
            print("BUKAN")

input_numbers()
