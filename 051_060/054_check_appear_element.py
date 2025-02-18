set4 = {'blue', 'green', 'red', 'pink'}
print(set4)
element = input("Nhap phan tu muon kiem tra: ")
# element = 'puple'
if element in set4:
    print(f"Phan tu '{element}' ton tai trong set")
else:
    print(f"Phan tu '{element}' khong ton tai trong set")
