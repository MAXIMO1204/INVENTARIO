# Sistema de Gestión de Inventarios

## Descripción

El **Sistema de Gestión de Inventarios** es una aplicación sencilla diseñada para gestionar los productos en el inventario de una tienda.
Este sistema permite a los usuarios realizar operaciones básicas de inventario, como agregar nuevos productos, actualizar la cantidad en stock, 
eliminar productos y buscar detalles de productos específicos. Está implementado en Python y utiliza una estructura basada en clases para representar productos.

## Funcionalidades

- **Agregar Producto:** Permite añadir un nuevo producto al inventario con un nombre único, cantidad inicial en stock y precio. Si el producto ya existe, se lanza un error.
  
- **Actualizar Stock:** Actualiza la cantidad en stock de un producto existente. Lanza un error si el producto no se encuentra en el inventario.

- **Eliminar Producto:** Elimina un producto del inventario. Si el producto no existe, se lanza un error.

- **Buscar Producto:** Busca un producto en el inventario por su nombre y devuelve sus detalles, incluyendo cantidad en stock y precio. Devuelve `None` si el producto no está en el inventario.

- **Mostrar Inventario:** Lista todos los productos actuales en el inventario junto con sus detalles.

## Manejo de Errores

- Intentar agregar un producto que ya existe lanza una excepción `ValueError`.
- Intentar actualizar o eliminar un producto que no existe lanza una excepción `KeyError`.
- Intentar buscar un producto que no existe devuelve `None`.

## Pruebas Unitarias

El sistema está acompañado de un conjunto de pruebas unitarias escritas con `pytest`, cubriendo los siguientes casos:

- Agregar productos nuevos.
- Actualizar la cantidad en stock de productos.
- Eliminar productos del inventario.
- Buscar productos en el inventario.
- Verificar el manejo de errores, como intentos de agregar productos duplicados o actualizar productos inexistentes.

## Requisitos del Sistema

- Python 3.x
- `pytest` para ejecutar pruebas unitarias

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/inventario.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd inventario
   ```
3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para ejecutar el sistema de gestión de inventarios, ejecuta el script principal:

```bash
python inventario.py
```

## Ejecución de Pruebas

Para ejecutar las pruebas unitarias, utiliza el siguiente comando:

```bash
pytest test_inventario.py
```

## Contribución

Si deseas contribuir a este proyecto, por favor, abre un issue o envía un pull request en GitHub. Todas las contribuciones son bienvenidas.
