inputs = []
try:
    while True:
        ask = input()
        inputs.append(ask)
except EOFError:
    pass

for input in inputs[::-1]:
    print(input)