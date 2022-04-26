import numpy as np
 
def calcula_pi(n): 
    sum = 0 
    for i in range(0, n): 
        sum += 1 / ((i + 1)**2) 
 
    pi = np.sqrt(6 * sum) 
    erro_relativo = (abs(pi - np.pi) / (np.pi)) * 100 
 
    print('N:', n)    
    print('pi:', pi) 
    print('Erro relativo:', erro_relativo, '%') 

calcula_pi(10)
calcula_pi(100)
calcula_pi(1000)

'''
Resultado:
N: 10
pi: 3.04936163598207
Erro relativo: 2.9358044717329577 % 
N: 100
pi: 3.1320765318091053
Erro relativo: 0.30290756409218367 %
N: 1000
pi: 3.1406380562059946
Erro relativo: 0.030385778458826077 %
'''