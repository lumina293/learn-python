dict4 = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# count amount of pairs key-value

# c1 su dung ham len() truc tiep tren dictionary
count1 = len(dict4)
print("so luong cap key-value la: ", count1)

# c2 su dung items() va ham len()
count2 = len(dict4.items())
print("so luong cap key-value la: ", count2)

# c3 su dung vong lap for
count3 = 0
for _ in dict4:
    count3 += 1
#count3 = count3 + 1
print("so luong cap key-value la: ", count3)
