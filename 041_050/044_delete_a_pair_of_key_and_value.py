dict1 = {
    'color': 'green',
    'shape': 'square',
}

print("Original dictionary: ", dict1)

key_to_delete = input("Nhap khoa muon xoa: ")

# check key in dictionary or not?

if key_to_delete in dict1:
    dict1.pop(key_to_delete)
    print(f"Da xoa cap key-value co khoa: '{key_to_delete}'")
else:
    print(f"khoa '{key_to_delete}' khong ton tai trong dictionary")

print("Dictionary sau khi xoa cap key_value: ", dict1)

# using del
del dict1['color']
print(dict1)
