word = input()

if len(word) <= 100:
    for i in range(len(word)):
        if word[i:(i+8)] == "ideafuse":
            print(i+1)
            break
    else:
        print("-1")
