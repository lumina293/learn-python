from xml.dom.minidom import ProcessingInstruction


def is_prime_number(a):
    for b in range(2, int(a ** 0.5) + 1):
        if a % b == 0:
            return False
    return True


for a in range(1, 20):
    if is_prime_number(a):
        print(a, "is prime number")
    else:
        print(a, "is NOT prime number")

# def is_prime_number(n):
#     for d in range(2, n):
#         if n % d == 0:
#             return False
#     return True
#
#
# for n in range(1, 101):
#     if is_prime_number(n):
#         print(n, "is prime number")
#     else:
#         print(n, "is NOT prime number")
