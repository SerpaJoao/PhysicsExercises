import matplotlib.pyplot as plt
import numpy as np

def f(t):
    
    return (2 / (np.sqrt(np.pi))) * (np.exp(-t**2))

def integral_trapz(f, a, b, N):
    h = (b - a) / N
    sum = 0
    for i in range(1, N):
        ti = a + h * i
        sum += f(ti)
    sum += (f(a) + f(b)) / 2
    return  h * sum

print(f'E(1) = {integral_trapz(f, 0, 1, 10):.4f}')

#Resultado: E(1) = 0.8420

lista_x = []
lista_integ_trapz = []

for x in (x * 0.1 for x in range(-30, 30)):
    lista_x.append(x)
    I = integral_trapz(f, 0, x, 10)
    lista_integ_trapz.append(I)

fig, axes = plt.subplots()
axes.plot(lista_x, lista_integ_trapz, 'r')
axes.set_xlabel('x')
axes.set_ylabel('E(x)')
plt.show()