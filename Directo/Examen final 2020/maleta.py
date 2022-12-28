#!/usr/bin/env python3
from typing import Union


default_codigo = 'VL1131'
default_altura = 40
default_anchura = 30
default_largura = 50
default_peso = 15.5

class Maleta:
    def __init__(self,
                 codigo: str = default_codigo,
                 altura: Union[int, float] = default_altura,
                 anchura: Union[int, float] = default_anchura,
                 largura: Union[int, float] = default_largura,
                 peso: Union[int, float] = default_peso):
        self.codigo = codigo
        self.altura = altura
        self.anchura = anchura
        self.largura = largura
        self.peso = peso

    def __str__(self):
        return f"Maleta {self.codigo}, {self.altura}x{self.anchura}x{self.largura} ({self.peso} kg)."

    def __repr__(self):
        return f"Maleta {self.codigo}, {self.altura}x{self.anchura}x{self.largura} ({self.peso} kg)."

    # Setter y getter (código)
    def _set_codigo(self, value):
        self._codigo = value if isinstance(value, str) else default_codigo

    def _get_codigo(self):
        return self._codigo
    codigo = property(_get_codigo, _set_codigo)

    # Setter y getter (altura)
    def _set_altura(self, value):
        self._altura = value if isinstance(value, (int, float)) and value >= 0 else default_altura

    def _get_altura(self):
        return self._altura
    altura = property(_get_altura, _set_altura)

    # Setter y getter (anchura)
    def _set_anchura(self, value):
        self._anchura = value if isinstance(value, (int, float)) and value >= 0 else default_anchura

    def _get_anchura(self):
        return self._anchura
    anchura = property(_get_anchura, _set_anchura)

    # Setter y getter (largura)
    def _set_largura(self, value):
        self._largura = value if isinstance(value, (int, float)) and value >= 0 else default_largura

    def _get_largura(self):
        return self._largura
    largura = property(_get_largura, _set_largura)

    # Setter y getter (peso)
    def _set_peso(self, value):
        self._peso = value if isinstance(value, (int, float)) and value >= 0 else default_peso

    def _get_peso(self):
        return self._peso
    peso = property(_get_peso, _set_peso)


if __name__ == '__main__':
    print(Maleta('1151', '50', -1, 15, 12.4))
