import requests

URL_PRODUCTOS = "https://jsonkeeper.com/b/MX0A"

def obtener_productos():
    respuesta = requests.get(URL_PRODUCTOS)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos.get("products", [])
    return []

def mostrar_productos(productos_disponibles):
    if not productos_disponibles:
        print("No hay productos para mostrar.")
        return False

    for producto in productos_disponibles:
        nombre = producto["name"]
        descripcion = producto["description"]
        precio = producto["price"]
        moneda = producto["currency"]
        stock = "En stock" if producto["in_stock"] else "Sin stock"

        print("#" * 20)
        print(f"Producto:")
        print(f"Nombre: {nombre}")
        print(f"Descripción: {descripcion}")
        print(f"Precio: ${precio} {moneda}")
        print(f"Stock: {stock}")
        print("#" * 20)
    return True