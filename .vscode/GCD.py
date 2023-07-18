def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
num1 = 36
num2 = 48

result = gcd(num1, num2)
print("The GCD of", num1, "and", num2, "is:", result)
