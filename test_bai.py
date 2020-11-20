from galois_number import GaloisNum as GN

def GF_test():
    a = GN(0x7d)
    b = GN(0x8f)
    print(a, a.get_bin(), a.get_dec())
    print(b, b.get_bin(), b.get_dec())

    print('add:')
    c = a + b
    print(c, c.get_bin(), c.get_dec())
    print('sub:')
    c = a - b
    print(c, c.get_bin(), c.get_dec())
    print('mul:')
    c = a * b
    print(c, c.get_bin(), c.get_dec())
    print('div:')
    c = a / b
    print(c, c.get_bin(), c.get_dec())
    print('-------------------------------------------')
    a = GN(10)
    b = GN(2)
    print(a, a.get_bin(), a.get_dec())
    print(b, b.get_bin(), b.get_dec())

    print('add:')
    c = a + b
    print(c, c.get_bin(), c.get_dec())
    print('sub:')
    c = a - b
    print(c, c.get_bin(), c.get_dec())
    print('mul:')
    c = a * b
    print(c, c.get_bin(), c.get_dec())
    print('div:')
    c = a / b
    print(c, c.get_bin(), c.get_dec())
    print('-------------------------------------------')
    a = GN(200)
    b = GN(2)
    print(a, a.get_bin(), a.get_dec())
    print(b, b.get_bin(), b.get_dec())

    print('add:')
    c = a + b
    print(c, c.get_bin(), c.get_dec())
    print('sub:')
    c = a - b
    print(c, c.get_bin(), c.get_dec())
    print('mul:')
    c = a * b
    print(c, c.get_bin(), c.get_dec())
    print('div:')
    c = a / b
    print(c, c.get_bin(), c.get_dec())
    print('-------------------------------------------')
    a = GN(0)
    b = GN(2)
    print(a, a.get_bin(), a.get_dec())
    print(b, b.get_bin(), b.get_dec())

    print('add:')
    c = a + b
    print(c, c.get_bin(), c.get_dec())
    print('sub:')
    c = a - b
    print(c, c.get_bin(), c.get_dec())
    print('mul:')
    c = a * b
    print(c, c.get_bin(), c.get_dec())
    print('div:')
    c = a / b
    print(c, c.get_bin(), c.get_dec())
    print('-------------------------------------------')


if __name__ == '__main__':
    GF_test()