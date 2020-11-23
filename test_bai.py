import galois_filed as GF
from galois_filed import GaloisNum as GN


def GF_test():
    print("Power Table")
    temp = []
    for i in range(1, 257):
        if i % 17 == 0:
            print(" ".join(temp))
            temp = []
        else:
            temp.append("{:02x}".format(GN.power_table[i - 1]))
    print("Logarithm Table")
    temp = []
    for i in range(1, 257):
        if i % 17 == 0:
            print(" ".join(temp))
            temp = []
        else:
            temp.append("{:02x}".format(GN.log_table[i - 1]))
    a = GN(0x7D)
    b = GN(0x8F)
    print(a, a.get_bin(), a.get_dec())
    print(b, b.get_bin(), b.get_dec())

    print("add:")
    c = a + b
    print(c, c.get_bin(), c.get_dec())
    print("sub:")
    c = a - b
    print(c, c.get_bin(), c.get_dec())
    print("mul:")
    c = a * b
    print(c, c.get_bin(), c.get_dec())
    print("div:")
    c = a / b
    print(c, c.get_bin(), c.get_dec())
    print("-------------------------------------------")
    a = GN(10)
    b = GN(2)
    print(a, a.get_bin(), a.get_dec())
    print(b, b.get_bin(), b.get_dec())

    print("add:")
    c = a + b
    print(c, c.get_bin(), c.get_dec())
    print("sub:")
    c = a - b
    print(c, c.get_bin(), c.get_dec())
    print("mul:")
    c = a * b
    print(c, c.get_bin(), c.get_dec())
    print("div:")
    c = a / b
    print(c, c.get_bin(), c.get_dec())
    print("-------------------------------------------")
    a = GN(200)
    b = GN(2)
    print(a, a.get_bin(), a.get_dec())
    print(b, b.get_bin(), b.get_dec())

    print("add:")
    c = a + b
    print(c, c.get_bin(), c.get_dec())
    print("sub:")
    c = a - b
    print(c, c.get_bin(), c.get_dec())
    print("mul:")
    c = a * b
    print(c, c.get_bin(), c.get_dec())
    print("div:")
    c = a / b
    print(c, c.get_bin(), c.get_dec())
    print("-------------------------------------------")
    a = GN(0)
    b = GN(2)
    print(a, a.get_bin(), a.get_dec())
    print(b, b.get_bin(), b.get_dec())

    print("add:")
    c = a + b
    print(c, c.get_bin(), c.get_dec())
    print("sub:")
    c = a - b
    print(c, c.get_bin(), c.get_dec())
    print("mul:")
    c = a * b
    print(c, c.get_bin(), c.get_dec())
    print("div:")
    c = a / b
    print(c, c.get_bin(), c.get_dec())
    print("-------------------------------------------")

    # a = GN(2)
    # b = GN(0)
    # print(a, a.get_bin(), a.get_dec())
    # print(b, b.get_bin(), b.get_dec())

    # print("add:")
    # c = a + b
    # print(c, c.get_bin(), c.get_dec())
    # print("sub:")
    # c = a - b
    # print(c, c.get_bin(), c.get_dec())
    # print("mul:")
    # c = a * b
    # print(c, c.get_bin(), c.get_dec())
    # print("div:")
    # c = a / b
    # print(c, c.get_bin(), c.get_dec())
    # print("-------------------------------------------")

    a = GF.pow2(-2)
    b = GF.pow2(253)
    c = GF.pow2(257)
    print(f"2^{-2}", hex(a.value), a.get_bin(), a.get_dec())
    print(f"2^{253}", hex(b.value), b.get_bin(), b.get_dec())
    print(f"2^{257}", hex(c.value), c.get_bin(), c.get_dec())


if __name__ == "__main__":
    GF_test()
