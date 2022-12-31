#!/usr/bin/env python3
from random import choice, choices


def producto_str(producto: dict) -> str:
    return f"{producto['nombre']}, {producto['precio']}€ ({producto['descuento']}% de descuento)."

def total_pedido(pedido: dict) -> float:
    return round(sum([p['precio'] for p in pedido['productos']]), 2)

def pedido_str(pedido: dict) -> str:
    return f"usuario: {pedido['usuario']}, {len(pedido['productos'])} productos, total: {total_pedido(pedido)}€"

def cargar_productos(productos: list[dict]):
    with open('productos.csv', 'r') as f:
        for line in f:
            id_, nombre, precio, descuento = line.strip().split(';')
            productos.append({'id': id_, 'nombre': nombre, 'precio': float(precio), 'descuento': int(descuento)})

def crear_pedidos(productos: list[dict], pedidos: list[dict]) -> list[dict]:
    usuarios = ['usuario-1', 'usuario-2', 'usuario-3', 'usuario-4', 'usuario-5']
    for p in range(1, 101):
        pedidos.append({'id': p, 'usuario': choice(usuarios), 'productos': choices(productos, k=5)})
    return pedidos

def guardar_pedidos(pedidos: list[dict]):
    with open('pedidos.csv', 'w') as f:
        for p in pedidos:
            f.write(f"{p['id']};{p['usuario']};{total_pedido(p)}\n")

def total_deustomarket(pedidos: list[dict]) -> float:
    return round(sum([total_pedido(p) for p in pedidos]), 2)

def usuario_vip(pedidos: list[dict]) -> str:
    precio_pedidos = [total_pedido(p) for p in pedidos]
    vip_idx = precio_pedidos.index(max(precio_pedidos))
    return pedidos[vip_idx]['usuario']

def stock_necesario(pedidos: list[dict]) -> dict:
    stock = {}
    for pedido in pedidos:
        for producto in pedido['productos']:
            if producto['id'] in stock:
                stock[producto['id']] += 1
            else:
                stock[producto['id']] = 1
    return stock


if __name__ == '__main__':
    producto1 = {'id': 'ABC123',
                'nombre': 'Tomate frito',
                'precio': 2.3,
                'descuento': 0}
    producto2 = {'id': 'ABC124',
                 'nombre': 'Pizza',
                 'precio': 5.4,
                 'descuento': 0}
    pedido = {'id': 1,
              'usuario': 'Erik',
              'productos': [producto1, producto2]}
    print(producto_str(producto1))
    print(total_pedido(pedido))
    print(pedido_str(pedido))
    productos = []
    cargar_productos(productos)
    print(productos)
    pedidos = []
    print(crear_pedidos(productos, pedidos))
    guardar_pedidos(pedidos)
    print(total_deustomarket(pedidos))
    print(usuario_vip(pedidos))
    print(stock_necesario(pedidos))
