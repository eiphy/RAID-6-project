import numpy as np
import matplotlib.pyplot as plt

def add(a, b):
    return a + b

class Role():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def kiss(self, role):
        print(f'{self.name} kissed {role.name}')

for i in range(10):
    print(i)
    if i == 3:
        print(i)
    elif i == 5:
        print(i)
        break
    else:
        print(i)

print(i)

i = 0
while i < 10:
    i = i + 1
    print(i)