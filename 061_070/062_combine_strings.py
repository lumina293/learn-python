str1 = "a"
str2 = "b"
str3 = str1 + str2
print(str3)

str3 = ''.join([str1, str2])
print(str3)
str4 = ''.join([str1, str2, str3])
print(str4)

str3 = f"{str1}{str2}"
print(str3)

str5 = f"{str4}{str3}"
print(str5)

str7 = "{}{}".format(str1, str2)
print(str7)

str7 = "{}{}".format(str1, str3, str4)
print(str7)

str7 = "{}{}{}".format(str1, str3, str4)
print(str7)

str9 = "ft"
str7 = "{}{}".format(str1, str2, str9)
print(str7)

str9 = "ft"
str7 = "{}{}".format(str1, str9, str2)
print(str7)

str9 = "ft"
str7 = "{}{}{}".format(str1, str9, str9)
print(str7)

# str9 = "ft"
# str7 = "{}{}{}".format(str1, str9)
# print(str7)
