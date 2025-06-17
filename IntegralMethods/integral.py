import numpy as np
from scipy.interpolate import KroghInterpolator


class Integral:
    def __init__(self):
        self.limite_inf = None
        self.limite_sup = None
        self.h = None
        self.x = None
        self.y = None
        self.quant_pontos = None

    def saber_maior(self, a, b):
        return a if abs(a) > abs(b) else b

    def integral(self):
        raise NotImplementedError("Método integral() deve ser implementado na subclasse")

    def erro_simples(self):
        raise NotImplementedError("Método erro_simples() deve ser implementado na subclasse")

    def erro_generalizado(self):
        raise NotImplementedError("Método erro_generalizado() deve ser implementado na subclasse")

    def derivada_quarta_ordem(self, ponto):
        # Estima derivada 4a pela interpolação Krogh
        return self.interpolador.derivative(ponto, 4)

    def _setup(self, x=None, y=None, limite_inf=None, limite_sup=None, func_integral=None, h=None):
        if x is not None and y is not None:
            self.x = np.array(x)
            self.y = np.array(y)
            self.limite_inf = self.x[0]
            self.limite_sup = self.x[-1]
            self.h = self.x[1] - self.x[0]
            self.quant_pontos = len(self.x) - 1
        elif limite_inf is not None and limite_sup is not None and func_integral is not None and h is not None:
            self.limite_inf = limite_inf
            self.limite_sup = limite_sup
            self.h = h
            self.x = np.arange(limite_inf, limite_sup + h/10, h)
            self.y = np.array([func_integral(xi) for xi in self.x])
            self.quant_pontos = len(self.x) - 1
        else:
            raise ValueError("Parâmetros inválidos: deve passar x e y ou limite_inf, limite_sup, func_integral e h")

        self.interpolador = KroghInterpolator(self.x, self.y)