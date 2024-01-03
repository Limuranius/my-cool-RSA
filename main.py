from RSA import RSA

if __name__ == "__main__":
    rsa = RSA()
    m = 1001
    c = rsa.encrypt(m)
    print(c)
    print(rsa.decrypt(c))