import algorithms
from dataclasses import dataclass

@dataclass
class PublicKey:
    e: int
    n: int

@dataclass
class PrivateKey:
    d: int
    n: int


class RSA:
    __public: PublicKey
    __private: PrivateKey

    def __init__(self) -> None:
        self.generate_keys()

    def generate_keys(self, p=None, q=None):
        if p is None:
            p = algorithms.get_random_prime()
        if q is None:
            q = algorithms.get_random_prime()
        n = p * q
        phi = algorithms.euler(p, q)
        e = algorithms.get_coprime(phi)
        d = algorithms.mod_mul_inverse(e, phi)
        self.__public = PublicKey(e, n)
        self.__private = PrivateKey(d, n)

    def encrypt(self, m: int) -> int:
        assert 0 <= m <= (self.__public.n - 1)
        c = algorithms.pow_mod(m, self.__public.e, self.__public.n)
        return c

    
    def decrypt(self, c: int):
        m = algorithms.pow_mod(c, self.__private.d, self.__private.n)
        return m