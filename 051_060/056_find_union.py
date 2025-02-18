set1 = {'red', 'green', 'yellow'}
set2 = {'pig', 'chicken', 'bird', 'fish', 'dog'}
set_union = set1 | set2
print(set_union)

set3 = {'a', 'b'}
set_union = set3 | set_union
print(set_union)

set4 = {1, 2, 3}
set_union = set1 | set2 | set3 | set4
print(set_union)

set5 = {1, 4, 1}
set_union = set1 | set2 | set3 | set4 | set5
print(set_union)
length = len(set_union)
print(length)

set_union = set.union(set1, set5)
print(set_union)
