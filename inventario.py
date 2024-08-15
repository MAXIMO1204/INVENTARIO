#SE COLOCO UN ERROR, EN LA LINEA 29 EL CUAL NO ACTUALIZA EL STOCK DEL PRODUCTO
# inventario[nombre].cantidad_en_stock = nueva_cantidad  # Debería ser `cantidad` y no 'cantidad_en_stock'
#EL USUARIO AGREGA UN PRODUCTO PERO AL ACTUALIZAR EL STOCK ESTO NO SUCEDE Y QUEDA CON
#EL STOCK ORIGINAL... 
#PARA EL QUE PROGRAMA FUNCIONE CORRECTAMENTE POR FAVOR COLOQUE EL VALOR CORRECTO 

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad en stock del producto
        self.precio = precio  # Precio del producto

def agregar_producto(inventario, nombre, cantidad, precio):
    """Agrega un nuevo producto al inventario."""
    # Verifica si el producto ya existe en el inventario
    if nombre in inventario:
        # Lanza una excepción si el producto ya está presente
        raise ValueError(f"El producto '{nombre}' ya existe en el inventario.")
    # Agrega el nuevo producto al inventario
    inventario[nombre] = Producto(nombre, cantidad, precio)

def actualizar_stock(inventario, nombre, nueva_cantidad):
    """Actualiza la cantidad en stock de un producto existente."""
    # Verifica si el producto existe en el inventario
    if nombre not in inventario:
        # Lanza una excepción si el producto no se encuentra
        raise KeyError(f"El producto '{nombre}' no existe en el inventario.")
    # Actualiza la cantidad en stock del producto
    inventario[nombre].cantidad_en_stock = nueva_cantidad  # Debería ser `cantidad` y no 'cantidad_en_stock'

def eliminar_producto(inventario, nombre):
    """Elimina un producto del inventario."""
    # Verifica si el producto existe en el inventario
    if nombre not in inventario:
        # Lanza una excepción si el producto no se encuentra
        raise KeyError(f"El producto '{nombre}' no existe en el inventario.")
    # Elimina el producto del inventario
    del inventario[nombre]

def buscar_producto(inventario, nombre):
    """Devuelve los detalles de un producto específico."""
    # Busca el producto en el inventario y devuelve sus detalles
    return inventario.get(nombre, None)  # Devuelve None si el producto no existe

def mostrar_inventario(inventario):
    """Muestra todos los productos en el inventario."""
    # Itera sobre todos los productos en el inventario
    for producto in inventario.values():
        # Muestra el nombre, cantidad y precio de cada producto
        print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")

def main():
    inventario = {}  # Diccionario para almacenar los productos del inventario

    while True:
        print("\n1. AGREGAR PRODUCTO")
        print("2. ACTUALIZAR STOCK")
        print("3. ELIMINAR PRODUCTO")
        print("4. BUSCAR PRODUCTO")
        print("5. MOSTRAR INVENTARIO")
        print("6. SALIR")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad en stock: "))
            precio = float(input("Ingrese el precio del producto: "))
            try:
                # Intenta agregar un nuevo producto al inventario
                agregar_producto(inventario, nombre, cantidad, precio)
                print("Producto agregado correctamente.")
            except ValueError as e:
                # Muestra un mensaje de error si el producto ya existe
                print(e)

        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            nueva_cantidad = int(input("Ingrese la nueva cantidad en stock: "))
            try:
                # Intenta actualizar la cantidad en stock del producto
                actualizar_stock(inventario, nombre, nueva_cantidad)
                print("Stock actualizado correctamente.")
            except KeyError as e:
                # Muestra un mensaje de error si el producto no existe
                print(e)

        elif opcion == '3':
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            try:
                # Intenta eliminar el producto del inventario
                eliminar_producto(inventario, nombre)
                print("Producto eliminado correctamente.")
            except KeyError as e:
                # Muestra un mensaje de error si el producto no existe
                print(e)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            # Busca el producto en el inventario
            producto = buscar_producto(inventario, nombre)
            if producto:
                # Muestra los detalles del producto si se encuentra
                print(f"Nombre: {producto.nombre}, Cantidad: {producto.cantidad}, Precio: {producto.precio}")
            else:
                # Muestra un mensaje si el producto no está en el inventario
                print(f"El producto '{nombre}' no se encuentra en el inventario.")

        elif opcion == '5':
            print("\nInventario:")
            # Muestra todos los productos del inventario
            mostrar_inventario(inventario)

        elif opcion == '6':
            # Sale del programa
            print("Usted salió del programa.")
            break

        else:
            # Muestra un mensaje de error si la opción es inválida
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()

