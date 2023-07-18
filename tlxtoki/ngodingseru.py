sentence = input().split()

amount = []

if sentence[-1][-1] == "." and len(sentence) > 1:
    for word in sentence:
        num = sum(char.isdigit() for char in word)
        lower = sum(char.islower() for char in word)

        if num >= 1 and lower >= 3:
            amount.append(len(word))
        else:
            amount.append(0)

    max_amount = max(amount)

    if max_amount != 0:
        index = amount.index(max_amount)
        if sentence[index] == sentence[-1]:
            print(sentence[index][:-1])
            print(max_amount - 1)
        else:
            print(sentence[index])
            print(max_amount)
    else:
        print("NO")
else:
    print("NO")
