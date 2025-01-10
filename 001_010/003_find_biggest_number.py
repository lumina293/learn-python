# no return, only print

def print_biggest_number(x, y, z):
    if x >= y and x >= z:
        print("the biggest number is", x)
    elif y >= x and y >= z:
        print("the biggest number is", y)
    else:
        print("the biggest number is", z)


print_biggest_number(2, 9, 7)


# return and print

def find_biggest_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


result = find_biggest_number(1, 4, 3)
print("the biggest number is", result)
