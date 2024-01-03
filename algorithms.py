import primes
import math
import random

def euler(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def get_coprime(num: int) -> int:
    while True:
        new_num = random.randrange(2, num)
        if math.gcd(num, new_num) == 1:
            return new_num


def get_random_prime() -> int:
    return primes.generateLargePrime()


def mod_mul_inverse(num: int, mod: int) -> int:
    return pow(num, -1, mod)