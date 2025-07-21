from productos import mostrar_productos

def test_mostrar_productos(capsys):
    lista_simulada = [
        {
            "id": 4,
            "name": "MacBook Pro",
            "description": "The latest MacBook Pro from Apple",
            "price": 1999.99,
            "currency": "USD",
            "in_stock": True
        }
    ]

    resultado = mostrar_productos(lista_simulada)
    salida = capsys.readouterr()

    assert resultado is True
    assert "MacBook Pro" in salida.out
    assert "$1999.99" in salida.out

def test_lista_vacia(capsys):
    resultado = mostrar_productos([])
    salida = capsys.readouterr()

    assert resultado is False
    assert "No hay productos para mostrar." in salida.out