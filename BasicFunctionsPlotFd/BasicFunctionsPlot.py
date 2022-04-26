import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 5.0, 100)

f = np.cos(2 * np.pi * x) * np.exp(-x)
g = np.cos(2 * np.pi * x)

fig, axes = plt.subplots(nrows = 2, ncols = 1)
axes[0].plot(x, f, 'g')
axes[1].plot(x, g, 'r')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')

plt.subplots_adjust(top = 0.98, bottom = 0.08, hspace = 0.5)

plt.show()