import matplotlib.pyplot as plt
import numpy as np

kB = 1.380649e-23 # J /K
h = 6.62607015e-34 # J s
c = 299792458.0 # m / s

def planck(l, T):
    A = 2 * h * c**2 / l**5
    B = A / (np.exp(h * c / (kB * T * l)) - 1.0)
    return B

l = np.linspace(0.3e-6, 5e-6, 100) # comprimento de onda em metros
l_um = l / 1e-6 # comprimento de onda em micrômetros

fig, axes = plt.subplots()
for T in(3000, 4000, 6000, 10000):
    axes.plot(l_um, planck(l, T),  label="T={0}K".format(T))
    
leg = axes.legend(loc='upper right', ncol=2, title='Legenda')
axes.set_yscale('log')
axes.set_xlabel(r'Comprimento de onda ($\mu m$)')
axes.set_ylabel(r'Radiância espectral ($W \cdot sr^{-1} \cdot m^{-3}$)')
axes.set_title('Radiação emitida por um corpo negro em equilíbrio térmico')
    
plt.show()