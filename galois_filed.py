import math

A = []
B = []


def generate_recover_table():
    global A, B
    A = [[None for _ in range(256)] for _ in range(256)]
    B = [[None for _ in range(256)] for _ in range(256)]
    for x in range(255):
        for y in range(255):
            if x == y:
                continue
            A[x][y] = pow2(y - x) / (pow2(y - x) + 1)
            B[x][y] = pow2(-x) / (pow2(y - x) + 1)


class GaloisNum:
    """Table for multiplation and divation."""

    power, log = [0] * 256, [0] * 256
    n = 1
    for i in range(256):
        power[i] = n
        log[n] = i
        n *= 2
        if n >= 256:
            n = n ^ 0x11D
    log[1] = 0
    power_table = power
    log_table = log
    del n
    del power
    del log

    """Definition for object methods."""

    def __init__(self, value):
        assert type(value) is int, "Wront type!"
        self.value = value

    def get_bin(self):
        return bin(self.value)

    def get_dec(self):
        return str(self.value)

    def __add__(self, other):
        if type(other) is int:
            return GaloisNum(self.value ^ other)
        else:
            return GaloisNum(self.value ^ other.value)

    def __sub__(self, other):
        return self + other

    def __mul__(self, other):
        if self.value == 0 or other.value == 0:
            return GaloisNum(0)
        else:
            return pow2((log2(self).value + log2(other).value) % 255)

    def __truediv__(self, other):
        if self.value == 0:
            return GaloisNum(0)
        elif other.value == 0:
            raise RuntimeError("Deviede by 0!")
        else:
            return pow2((log2(self).value - log2(other).value) % 255)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __repr__(self):
        return f"{hex(self.value)}: {chr(self.value)}"

    def __str__(self):
        return f"{hex(self.value)}: {chr(self.value)}"


def compute_pq_row(m_row):
    p = GaloisNum(0)
    q = GaloisNum(0)
    for i, x in enumerate(m_row):
        p = p + x
        q = q + GaloisNum(GaloisNum.power_table[i]) * x

    return p, q


def compute_pq(m):
    N = len(m[0])
    R = len(m)
    P = []
    Q = []
    for r in range(R):
        temp_p, temp_q = compute_pq_row([m[r][i] for i in range(N)])
        P.append(temp_p)
        Q.append(temp_q)

    return P, Q


def log2(x):
    x = x if type(x) is int else x.value
    return GaloisNum(GaloisNum.log_table[x])


def pow2(x):
    x = x if type(x) is int else x.value
    return _pow2(x)


def _pow2(x):
    x = 255 + x if x < 0 else x
    x = x % 255 if x > 255 else x
    return GaloisNum(GaloisNum.power_table[x])


def recover_data_from_p(px, p):
    assert type(p) is GaloisNum, "Wrong type of p"
    assert type(px) is GaloisNum, "Wrong type of px"
    return p - px


def recover_data_from_q(qx, q, x):
    assert type(q) is GaloisNum, "Wrong type of p"
    assert type(qx) is GaloisNum, "Wrong type of px"
    return (q + qx) * pow(255 - x)


def recover_2data(p, q, pxy, qxy, x, y):
    assert len(A) > 0, "A, B are not initialized!"
    assert x != y, "Same matrix id for x and y!"
    a, b = A[x][y], B[x][y]
    dx = a * (p + pxy) + b * (q + qxy)
    dy = (p + pxy) + dx

    return (dx, dy)
