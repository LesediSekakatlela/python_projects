import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,10,100)
y = x

plt.plot(x, y, label='linear')
plt.legend()
plt.savefig("Figure_1.png")
plt.show()