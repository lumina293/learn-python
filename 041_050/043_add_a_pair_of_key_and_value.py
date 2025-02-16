dict1 = {
    'name': 'Su',
    'age': 30,
    'city': 'Viet Nam'
}
print("Original Dictionary: ", dict1)

new_key = input("Nhap khoa can them: ")
new_value = input("Nhap gia tri can them: ")

dict1[new_key] = new_value
print("New Dictionary: ", dict1)
