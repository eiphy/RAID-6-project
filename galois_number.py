from math import log2

class GaloisNum():
    '''Table for multiplation and divation.'''
    power, log = [0] * 256, [0] *256
    n = 1
    for i in range(0, 256):
        power[i] = n
        log[n] = i
        n *= 2
        if n >= 256:
            n = n ^ 0x11d
    log[1] = 0
    power_table = power
    log_table = log
    del n
    del power
    del log

    '''Definition for object methods.'''
    def __init__(self, value):
        self.value = value

    def get_bin(self):
        return bin(self.value)

    def get_dec(self):
        return str(self.value)

    def __add__(self, other):
        return GaloisNum(self.value ^ other.value)
    
    def __sub__(self, other):
        return GaloisNum(self.value ^ other.value)

    def __mul__(self, other):
        if self.value == 0 or other.value == 0:
            return GaloisNum(0)
        else:
            return GaloisNum(self.power_table[
                (self.log_table[self.value] + self.log_table[other.value]) % 255
            ])

    def __truediv__(self, other):
        if self.value == 0:
            return GaloisNum(0)
        elif other.value == 0:
            raise RuntimeError("Deviede by 0!")
        else:
            return GaloisNum(self.power_table[
                (self.log_table[self.value] - self.log_table[other.value]) % 255
            ])

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
        