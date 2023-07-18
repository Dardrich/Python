def fibonacci(n):
    if n not in fibo_dict:
        fibo_dict[n] = fibonacci(n-1) + fibonacci(n-2)
    return fibo_dict[n]

fibo_dict = {}
fibo_dict[0] = 1
fibo_dict[1] = 1

fibo_val = int(input("Masukkan angka yang ingin di-Fibonacci-kan: "))
print("Hasil pem-Fibonacci-an angka", fibo_val, "adalah", int(fibonacci(fibo_val)))
