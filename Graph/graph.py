import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def plotar_funcao(f, a=None, b=None, num_pontos=400):
    """
    Plota a função no intervalo especificado e marca as raízes encontradas.

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

    # Encontrando raízes numéricas
    def funcao_aux(x):
        return f(x)
    
    pontos_iniciais = np.linspace(a, b, 10)
    raizes = []
    for p in pontos_iniciais:
        try:
            raiz = fsolve(funcao_aux, p)[0]
            if a - 1 <= raiz <= b + 1 and np.isclose(f(raiz), 0, atol=1e-3):
                raizes.append(raiz)
        except:
            pass
    
    raizes = np.unique(np.round(raizes, decimals=3))
    
    # Limitando o eixo Y entre -10 e 10
    plt.ylim(-5, 5)
    
    # Plotagem
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.plot(x, y, label='f(x)', color='blue')
    
    # Marcando as raízes
    if len(raizes) > 0:
        plt.scatter(raizes, np.zeros_like(raizes), color='red', label='Raízes')
    
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico da função com raízes')
    plt.grid()
    plt.show()
