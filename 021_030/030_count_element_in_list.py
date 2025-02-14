list = [10, 6, 9, 3 * 3, 70]
element_to_count = list.count(9)
print("9 appears", element_to_count, "times in list")

element_to_count = list.count(1)
print("1 appears", element_to_count, "times in list")

list = [10, 20, 6, 4 * 5, 27, 4, 20]
list.sort()
print("my list after sort:", list)

element_to_count = list.count(20)
print("20 appears", element_to_count, "times in list")
list.remove(20)
list.remove(20)
list.remove(20)
print(list)
sum = sum(list)
print("sum of my list:", sum)
