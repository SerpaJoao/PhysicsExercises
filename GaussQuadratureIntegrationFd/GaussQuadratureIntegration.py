from scipy.special import roots_legendre
import matplotlib.pyplot as plt
import numpy as np

def v(x):
    return -np.cos(x)

def f_v(x):
    return 1 / (np.sqrt(v(a) - v(x)))

def integral_qgauss(f, a, b, N): 
    u, _w = roots_legendre(N)
    I = 0
    for k in range(N):
        xk = (b - a) / 2 * u[k] + (b + a) / 2
        wk = (b - a) / 2 * _w[k]
        I += wk * f(xk)
    return I

def T(m, a, N):
    var_massa = np.sqrt(8 * m)
    I = integral_qgauss(f_v, 0, a, N)
    return var_massa * I

m = 1
a = 0.01
N = 20
periodo = T(m, a, N)
erro_rel = (abs(periodo - 2 * np.pi)) / (2 * np.pi) * 100.0
print(f'Período = {periodo:.3f} (erro relativo = {erro_rel:.2f} %)')

a_range = np.arange(0.01, np.pi, 0.1)
lista_T = []

for a in a_range:
    var_massa = np.sqrt(8 * m)
    I = integral_qgauss(f_v, 0, a, N)
    T = var_massa * I
    lista_T.append(T)

fig, axes = plt.subplots()
axes.plot(a_range, lista_T, 'r')
axes.set_xlabel('a')
axes.set_ylabel('T')
plt.show()