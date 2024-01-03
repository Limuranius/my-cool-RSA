import primes

def euler(p: int, q: int) -> int:
    return (p - 1) * (q - 1)


def get_coprime(num: int) -> int:
    return 17


def gcdExtended(a, b): 
    if a == 0 : 
        return b,0,1  
    gcd,x1,y1 = gcdExtended(b%a, a) 
    x = y1 - (b//a) * x1 
    y = x1 
    return gcd,x,y 


def get_random_prime() -> int:
    return primes.generateLargePrime()


def mod_mul_inverse(num: int, mod: int) -> int:
    gcd, x, y = gcdExtended(num, mod)
    return mod - abs(min(x, y))


def pow_mod(num: int, power: int, mod: int) -> int:
    """
    Находит выражение num ** power % mod
    """
    res = 1
    while power:
        if (power & 1):
            res = (res * num) % mod
            power -= 1
        else:
            num = (num * num) % mod
            power >>= 1
    return res