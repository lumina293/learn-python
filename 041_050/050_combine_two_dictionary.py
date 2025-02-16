dict1 = {
    'name': 'Alice',
    'age': 25
}

dict2 = {
    'city': 'New York',
    'country': 'USA'
}
# combine dict1 and dict2

# c1 su dung update()
# dict3 = dict1.copy()
# dict3.update(dict2)
dict3 = dict2.copy()
dict3.update(dict1)
print(dict3)

# c2 su dung toan tu **
dict3 = {**dict1, **dict2}
print("the new dictionary after combining dict1 and dict2: ", dict3)
