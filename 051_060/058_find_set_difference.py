set1 = {'apple', 'banana', 'cherry'}
set2 = {'banana', 'cherry', 'durian'}

set_difference = set1 - set2
print(set_difference)

set_difference = set2 - set1
print(set_difference)

set3 = {'bluecherry', 1}
set_difference = set1 - set3
print(set_difference)

set_difference = set1 - set3 - set2
print(set_difference)

set_difference = set1 - set2 - set3
print(set_difference)

set_difference = set2 - set1 - set3
print(set_difference)

set_difference = set.difference(set1, set2)
print(set_difference)

set_difference = set.difference(set3, set2)
print(set_difference)
