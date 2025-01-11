def print_numbers():
    for number in range(1, 101):
        print(number, number * number, number * number * number)


def print_multiplication_table():
    for a in range(1, 11):
        for b in range(1, 11):
            print(a, "*", b, "=", a * b)
        print()


print_multiplication_table()
