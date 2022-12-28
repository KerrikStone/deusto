#!/usr/bin/env python3
from maleta import Maleta


default_nombre = 'Erik'
default_apellido = 'Coruña'
default_talla = 3
default_menu = 'normal'
default_vuelo = 'VL1131'
default_cabina = [Maleta(default_vuelo, 30, 30, 25, 6.1)]
default_facturado = [Maleta(default_vuelo, 50, 60, 45, 21.3)]

class Pasajero:
    def __init__(self,
                 nombre: str = default_nombre,
                 apellido: str = default_apellido,
                 talla: int = default_talla,
                 menu: str = default_menu,
                 cabina: list[Maleta] = default_cabina,
                 facturado: list[Maleta] = default_facturado):
        self.nombre = nombre
        self.apellido = apellido
        self.talla = talla
        self.menu = menu
        self.cabina = cabina
        self.facturado = facturado

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.get_peso_total()} kg)."

    def __repr__(self):
        return f"{self.nombre} {self.apellido} ({self.get_peso_total()} kg)."

    # Setter y getter (nombre)
    def _set_nombre(self, value):
        self._nombre = value if isinstance(value, str) else default_nombre

    def _get_nombre(self):
        return self._nombre
    nombre = property(_get_nombre, _set_nombre)


    # Setter y getter (apellido)
    def _set_apellido(self, value):
        self._apellido = value if isinstance(value, str) else default_apellido

    def _get_apellido(self):
        return self._apellido
    apellido = property(_get_apellido, _set_apellido)

    # Setter y getter (talla)
    def _set_talla(self, value):
        self._talla = value if isinstance(value, int) and value >= 0 and value <= 5 else default_talla

    def _get_talla(self):
        return self._talla
    talla = property(_get_talla, _set_talla)

    # Setter y getter (menú)
    def _set_menu(self, value):
        self._menu = value if isinstance(value, str) and (value == 'normal' or value == 'vegetariano' or value == 'celiaco') else default_menu

    def _get_menu(self):
        return self._menu
    menu = property(_get_menu, _set_menu)

    # Setter y getter (cabina)
    def _set_cabina(self, value):
        self._cabina = value if isinstance(value, list) else default_cabina

    def _get_cabina(self):
        return self._cabina
    cabina = property(_get_cabina, _set_cabina)

    # Setter y getter (facturado)
    def _set_facturado(self, value):
        self._facturado = value if isinstance(value, list) else default_facturado

    def _get_facturado(self):
        return self._facturado
    facturado = property(_get_facturado, _set_facturado)

    def get_peso_total(self):
        return sum([maleta.peso for maleta in self.cabina]
                   + [maleta.peso for maleta in self.facturado])

if __name__ == '__main__':
    print(Pasajero())
