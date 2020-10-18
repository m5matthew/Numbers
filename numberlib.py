def is_prime(x):
    # negative numbers and {0,1} are not prime numbers
    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return x % 2 == 1
