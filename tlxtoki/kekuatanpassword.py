password = input()
datas = list(password)

has_lowercase = any(c.islower() for c in datas)
has_uppercase = any(c.isupper() for c in datas)
has_digit = any(c.isdigit() for c in datas)
has_special = any(c in "_!?" for c in datas)

if 8 <= len(datas) <= 20 and has_lowercase and has_uppercase and has_digit and has_special:
    print("Kuat")
elif len([c for c in datas if c.isalpha()]) >= 12:
    print("AgakKuat")
else:
    print("Lemah")
