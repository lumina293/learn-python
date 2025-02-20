str1 = "BYebye MIna"
lower_str = str1.lower()
print(lower_str)

# c2 using for

str1 = "BYebye mina"
lower_str = ""
for char in str1:
    if 'A' <= char <= 'Z':
        lower_str += chr(ord(char) + 32)
    else:
        lower_str += char
print(lower_str)

str1 = "BYebye minAZ"
lower_str = ""
for char in str1:
    if 'A' <= char <= 'Z':
        lower_str += chr(ord(char) * 32)
    else:
        lower_str += char
print(lower_str)
