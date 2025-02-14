import random

list = [10, 1, 45, 6, 890, 40]

# shuffle()
random.shuffle(list)
print("my list:", list)

# sort_reverse
list.sort(reverse=True)
print("my list after sorting reverse:", list)

list.sort(reverse=False)
print("my list after sorting reverse:", list)


list = [10, 1, 45, 6, 890, 40, 45]
random.shuffle(list)
print("my list:", list)
list.sort(reverse=True)
print("my list after sorting reverse:", list)

