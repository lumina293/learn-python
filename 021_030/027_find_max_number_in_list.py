import random

list = [10, 78, 40 * 9, 100, 52, 9]
max_number = max(list)
print("The max number in list is:", max_number)

list = [10, 78, 40 * 9, 100, 52, 9, 360.3]
max_number = max(list)
print("The max number in list is:", max_number)

list = [10, 78, 40 * 9, 100, 52, 9, 360.3]
random.shuffle(list)
print("my list after random:", list)
max_number = max(list)
print("The max number in list is:", max_number)
