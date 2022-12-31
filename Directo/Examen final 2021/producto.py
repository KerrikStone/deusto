#!/usr/bin/env python3


class Producto:
    def __init__(self,
                 id: str,
                 nombre: str,
                 precio: float,
                 descuento: int):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.descuento = descuento
