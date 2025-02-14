import numpy as np
import matplotlib.pyplot as plt

def plotar_funcao(f, a, b):
    """
    Plota a função no intervalo especificado.
    
    Parâmetros:
    f -- Função a ser plotada
    a -- Extremidade esquerda do intervalo
    b -- Extremidade direita do intervalo
    """
    x = np.linspace(a - 1, b + 1, 400)
    y = np.vectorize(f)(x)
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.plot(x, y, label='f(x)')
    plt.scatter([a, b], [f(a), f(b)], color='red', label='Intervalo [a, b]')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico da função')
    plt.grid()
    plt.show()
