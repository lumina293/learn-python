def is_prime_number(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d != 0:
            return True


def is_prime_number(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def count_prime_number():
    count = 0
    prime_numbers = []
    for n in range(1, 1001):
        if is_prime_number(n):
            count = count + 1
            prime_numbers.append(n)
    return count, prime_numbers


print(count_prime_number())
