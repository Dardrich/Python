def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

def input_numbers():
    n = int(input())

    numbers = []
    for _ in range(n):
        number = int(input())
        numbers.append(number)

    for number in numbers:
        if is_prime(number):
            print("YA")
        else:
            print("BUKAN")

input_numbers()



