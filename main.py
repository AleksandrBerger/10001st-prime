def is_prime(num):
    """
    This function is used to check if each candidate is a prime.

    :param num:
    Takes an integer num

    :return:
    True if num is prime, and False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def nth_prime(n):
    """
    The function uses a while loop to find the nth prime number by counting the number of prime numbers found so far
    and incrementing the candidate number until the nth prime is found.

    The is_prime function is called on each candidate number to check if it is prime.

    :param n: int

    :return: int
    the nth prime number
    """
    prime_counter = 0
    candidate = 2
    while prime_counter < n:
        if is_prime(candidate):
            prime_counter += 1
        candidate += 1
    return candidate - 1


print(nth_prime(10001))
