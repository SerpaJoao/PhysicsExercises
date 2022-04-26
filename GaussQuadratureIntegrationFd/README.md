## Integração Númerica (Regra de Quadratura Gaussiana)

No arquivo  encontra-se a função definida para calcular integrais numericamente usando a [Regra de Quadratura Gaussiana](https://en.wikipedia.org/wiki/Gaussian_quadrature): 
```
def integral_qgauss(f, a, b, N): 
    u, _w = roots_legendre(N)
    I = 0
    for k in range(N):
        xk = (b - a) / 2 * u[k] + (b + a) / 2
        wk = (b - a) / 2 * _w[k]
        I += wk * f(xk)
    return I
```
Esta função é usada para calcular e graficar a integral $
T = \sqrt{8m} \int_0^a \frac{\mathrm{d}x}{\sqrt{V(a) - V(x)}}$, que define o período de oscilação anarmônico com potencial $V(x) = - \cos x$, para valores definidos de massa _m_, amplitude _a_ e amostragens _N_.