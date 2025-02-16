dict2 = {
    'animal': 'cat',
    'place': 'forest'
}
print(dict2)

key_to_check = input("Nhap khoa muon kiem tra: ")
# check key-value using in
if key_to_check in dict2:
    print(f"khoa '{key_to_check}' ton tai trong dictionary")
else:
    print(f" khoa '{key_to_check}' khong ton tai trong dictionary")
