word = input()
n = int(input())

datas = []

for _ in range(n):
    words = input()
    datas.append(words)

for data in datas:
    if word.startswith("*") and word.endswith("*"):
        if word[1:-1] in data:
            print(data)
    if word.startswith("*") and not word.endswith("*"):
        if data.endswith(word[1:]):
            print(data)
    if word.endswith("*") and not word.startswith("*"):
        if data.startswith(word[:-1]):
            print(data)
