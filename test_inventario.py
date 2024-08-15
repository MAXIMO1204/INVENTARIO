import pytest
from inventario import Producto, agregar_producto, actualizar_stock, eliminar_producto, buscar_producto

def test_agregar_producto():
    inventario = {}
    # Agregar un producto al inventario
    agregar_producto(inventario, "Producto1", 100, 10.99)
    assert "Producto1" in inventario
    assert inventario["Producto1"].cantidad == 100
    assert inventario["Producto1"].precio == 10.99

    # Intentar agregar un producto que ya existe
    with pytest.raises(ValueError):
        agregar_producto(inventario, "Producto1", 50, 9.99)

def test_actualizar_stock():
    inventario = {}
    # Agregar un producto para actualizar
    agregar_producto(inventario, "Producto2", 50, 5.49)
    
    # Actualizar el stock de un producto existente
    actualizar_stock(inventario, "Producto2", 150)
    assert inventario["Producto2"].cantidad == 150

    # Intentar actualizar un producto que no existe
    with pytest.raises(KeyError):
        actualizar_stock(inventario, "ProductoNoExistente", 30)

def test_eliminar_producto():
    inventario = {}
    # Agregar un producto para eliminar
    agregar_producto(inventario, "Producto3", 70, 15.99)
    
    # Eliminar el producto del inventario
    eliminar_producto(inventario, "Producto3")
    assert "Producto3" not in inventario

    # Intentar eliminar un producto que no existe
    with pytest.raises(KeyError):
        eliminar_producto(inventario, "ProductoNoExistente")

def test_buscar_producto():
    inventario = {}
    # Agregar un producto para buscar
    agregar_producto(inventario, "Producto4", 200, 20.49)
    
    # Buscar un producto existente
    producto = buscar_producto(inventario, "Producto4")
    assert producto is not None
    assert producto.nombre == "Producto4"
    assert producto.cantidad == 200
    assert producto.precio == 20.49

    # Buscar un producto que no existe
    producto = buscar_producto(inventario, "ProductoNoExistente")
    assert producto is None
