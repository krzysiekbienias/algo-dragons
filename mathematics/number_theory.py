# find n-thprime number
import math
from typing import List


def is_prime(n: int) -> bool:
    """
    Description
    -----------
    Checks if a number is prime or not.
    Parameters
    ----------
    n

    Returns
    -------

    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# function to return nth prime number

def nth_prime_number(num: int) -> int:
    value = 1
    prime_number_counter = 0
    while prime_number_counter != num:
        value += 1
        if is_prime(value):
            prime_number_counter += 1
    return value


def sieve_of_eratosthenes(n: int) -> List[int]:
    """sieve_of_eratosthenes
    Description
    -----------
    Function returns prime numbers up to given limit.


    Parameters
    ----------
    n : int

    Returns
    -------
    _type_
        _description_
    """
    is_prime_list = [True] * (n + 1)
    is_prime_list[0] = False
    is_prime_list[1] = False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if is_prime_list[i]:
            for j in range(i * i, n + 1, 2 * i if i != 2 else i):
                is_prime_list[j] = False
    return [i for i in range(n + 1) if is_prime_list[i]]


def greatest_common_divisor(n: int, m: int) -> int:
    """
    Description
    -----------
    Function returns greatest common divisor of n and m. It utilizes euclidian algorithm,

    Parameters
    ----------
    n:int
    m:int

    Returns
    -------
    int

    """
    if m == 0:
        return n
    else:
        return greatest_common_divisor(m, n % m)


def power(x: int, y: int) -> int:
    if y == 0: return 1
    if y == 1: return x
    return power(x, y - 1) * y


def sum_of_digits(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

def perfect_number(n: int) -> bool:
    pass

#292 NIm game
def nim_game(n: int) -> bool:
    # orginal game we may take 1 2 or 3 stones from heap
    if n%4 != 0:
        return True
    else:
        return False




if __name__ == '__main__':
    print(greatest_common_divisor(12,2))