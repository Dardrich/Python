def gcdOfStrings(str1: str, str2: str) -> str:
    datas_min = []
    datas_max = []
    minimum = min(str1,str2)
    maximum = max(str1,str2)
    for i in range(1,len(minimum)):
        if minimum[0:i]==minimum[i:i+i]:
            datas_min.append(minimum[0:i])
    else:
        datas_min.append(minimum)
    for i in range(1,len(maximum)):
        if maximum[0:i]==maximum[i:i+i]:
            datas_max.append(maximum[0:i])
    print(datas_min,datas_max)
    
    if len(set(datas_min).intersection(datas_max))!=0:
        if len(datas_min) == len(datas_max):
            return "".join(max(set(datas_min).intersection(datas_max)))
        else:
            return "".join(min(set(datas_min).intersection(datas_max)))
    else:
        return ""


str1="AAAAAAAAA"
str2="AAACCC"

print(gcdOfStrings(str1,str2))

