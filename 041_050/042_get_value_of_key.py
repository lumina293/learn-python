# create a dictionary
dict = {
    'name': 'Alace',
    'age': 24,
    'city': "New York"
}
print("Dictionary da tao:", dict)

# Enter key from user
key = input("nhap tu khoa can truy cap: ")

# Check key in dictionary
if key in dict:
    value = dict[key]
    print(f"gia tri cua '{key}' la: {value}")
else:
    print(f"'{key}' khong ton  tai trong dictionary")
