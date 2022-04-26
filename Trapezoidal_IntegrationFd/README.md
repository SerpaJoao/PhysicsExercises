## Integração Númerica (Regra do Trapézio)

No arquivo  encontra-se a função definida para calcular integrais numericamente usando a [Regra do Trapézio](https://en.wikipedia.org/wiki/Trapezoidal_rule): 
```
def integral_trapz(f, a, b, N):
    h = (b - a) / N
    sum = 0
    for i in range(1, N):
        ti = a + h * i
        sum += f(ti)
    sum += (f(a) + f(b)) / 2
    return  h * sum
```

Esta função é usada para calcular e graficar a integral $E(x) = \frac{2}{\sqrt{\pi}} \int_0^x \mathrm{e}^{-t^2}\ \mathrm{d}t$, que não pode ser resolvida analiticamente, para valores selecionados de a, b e N.