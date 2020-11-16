import numpy as np
import matplotlib.pyplot as plt

a = np.random.rand(10, 3)
plt.figure()
plt.plot(a[:, 0])
plt.plot(a[:, 1])
plt.show()