'''Kalkulator Sederhana'''

def calc(a,b,operator):
    res = 1
    if operator == "+" :
      return a+b
    if operator == "-":
      return a-b
    if operator == "x":
      return a*b
    if operator == "/":
      return a/b
    if operator == "^":
      for i in range(abs(b)):
        res *= a
      if b >= 0:
         return res
      else:
         return 1 / res

a = int(input("Masukkan bilangan bulat pertama: "))
operator = input("Masukkan operator aritmatika (+,-,x,/,^): ")
b = int(input("Masukkan bilangan bulat kedua: "))

print(f"Hasil {a} {operator} {b} adalah {calc(a,b,operator)}")


