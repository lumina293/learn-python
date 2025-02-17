set3 = {'chicken', 'pig', 'dog'}
print(set3)

# delete element
# c1 using remove
set3.remove('pig')
print(set3)

# set3.remove(chicken)
# print(set3)

# c2 using discard()
set3.discard('dog')
print(set3)

set3.discard('bird')
print(set3)

set3.remove('bird')
print(set3)
