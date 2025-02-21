import numpy as np
import matplotlib.pyplot as plt

def plotar_funcao(f, a=None, b=None, num_pontos=400):
    """
    Plota a função no intervalo especificado e limita o eixo Y entre -10 e 10.

    Parâmetros:
    f -- Função a ser plotada
    a -- Extremidade esquerda do intervalo (opcional)
    b -- Extremidade direita do intervalo (opcional)
    num_pontos -- Número de pontos para o gráfico (padrão: 400)
    """
    if a is None or b is None:
        a, b = -5, 5  # Intervalo padrão se não for fornecido
    
    x = np.linspace(a - 1, b + 1, num_pontos)
    y = np.vectorize(f)(x)

    # Limitando o eixo Y entre -10 e 10
    plt.ylim(-5, 5)

    # Plotagem
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.plot(x, y, label='f(x)', color='blue')
    plt.scatter([a, b], [f(a), f(b)], color='red', label=f'Intervalo [{a}, {b}]')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico da função')
    plt.grid()
    plt.show()