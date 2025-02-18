str1 = "hello, world"
length = len(str1)
print(length)

str1 = "hello,world"
length = len(str1)
print(length)

str1 = "hello, world @#$"
length = len(str1)
print(length)

str1 = "hello, world @#$, a"
length = 0
for char in str1:
    length += 1
print(length)
