tuple = (2, 1, 6, 7, 9, 30)
min_element = min(tuple)
print(min_element)

# using for
min_element = tuple[0]
for element in tuple:
    if element < min_element:
        min_element = element
print(min_element)
