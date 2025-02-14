import random

numbers = list(range(10, 50))
random.shuffle(numbers)
print(numbers)
min_element = min(numbers)
print(min_element)

list = [10, 6, 5, 10 - 7, 99]
min_element = min(list)
print(min_element)

list = [10, 6, 5, 1.7, 99]
min_element = min(list)
print(min_element)
