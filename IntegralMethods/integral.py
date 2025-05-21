from abc import ABC, abstractmethod

class Integral(ABC):
    def __init__(self, limite_inf: int = None, limite_sup: int = None, h: float = None, quant_pontos: int = None, x: list[float] = None, func_integral=None, func_derivada_integral=None):
        self.func_integral = func_integral
        self.func_derivada_integral = func_derivada_integral
        self.y = []

        if x is not None:
            self.x = x
            self.limite_inf = x[0]
            self.limite_sup = x[-1]
            self.quant_pontos = len(x) - 1
            self.h = (self.limite_sup - self.limite_inf) / self.quant_pontos
        else:
            self.limite_inf = limite_inf
            self.limite_sup = limite_sup
            self.h = h
            self.quant_pontos = quant_pontos
            self.x = [self.limite_inf + i * self.h for i in range(self.quant_pontos + 1)]


    def saber_maior(self, x, y):
        if x is None:
            return y
        if y is None:
            return x
        return x if abs(x) > abs(y) else y


    def criar_vetor_x(self):
        i = self.limite_inf
        while round(i, 10) <= round(self.limite_sup, 10):
            self.x.append(round(i, 10))
            i += self.h

    @abstractmethod
    def erro_simples(self):
        pass

    @abstractmethod
    def erro_generalizado(self):
        pass

    @abstractmethod
    def integral(self):
        pass