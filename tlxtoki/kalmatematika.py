xoy = input().split()
xoy = [i for i in xoy]

x = xoy[0]
o = xoy[1]
y = xoy[2]


if o == "+":
    print(int(x)+int(y))
elif o == "-":
    print(int(x)-int(y))
elif o == "*":
    print(int(x)*int(y))
elif o == "=":
    a = (int(x)==int(y))
    if a == True:
        print("benar")
    else:
        print("salah")
elif o == ">":
    a = (int(x)>int(y))
    if a == True:
        print("benar")
    else:
        print("salah")
elif o == "<":
    a = (int(x)<int(y))
    if a == True:
        print("benar")
    else:
        print("salah")
