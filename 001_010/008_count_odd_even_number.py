def count_odd_even_number(numbers):
    count_odd = 0
    count_even = 0
    for number in numbers:
        if number % 2 == 0:
            count_even = count_even + 1
        else:
            count_odd = count_odd + 1
    return count_odd, count_even


a, b = count_odd_even_number([1, 2, 2, 6, 8, 7, 9])
print("There are", a, "odd numbers and", b, "even numbers in the list")
