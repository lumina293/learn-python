# create a dictionary
my_dict = {
    'name': 'Alace',
    'age': 24,
    'city': "New York"
}
print("Dictionary da tao:", my_dict)

# # Enter key from user
key = input("nhap tu khoa can truy cap: ")
#
# # Check key in dictionary
# if key in my_dict:
#     value = my_dict[key]
#     print(f"gia tri cua '{key}' la: {value}")
# else:
#     print(f"'{key}' khong ton  tai trong dictionary")

value = my_dict.get(key)
print(f"gia tri cua {key} la: {value} ")
