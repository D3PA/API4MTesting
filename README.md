# 📱 Actividad 4 - Mobile Testing

## 📌 Descripción

Este proyecto corresponde a la **Actividad 4** de Mobile Testing para Teclab. En él se simula el desarrollo de una funcionalidad para una aplicación de e-commerce, donde se obtiene un listado de productos desde una API externa y se muestran por consola en una interfaz simple. Además, se implementan dos tests unitarios para validar el comportamiento esperado de la funcionalidad.

---

## Objetivos de la actividad

- Crear **tests unitarios** que validen:
  - ✅ Se muestran los productos si hay datos.
  - ✅ No se muestra nada si la lista está vacía.
- Mostrar un listado de productos con:
  - Nombre
  - Descripción
  - Precio
  - Estado de stock

---

## API utilizada

La información de los productos es obtenida desde la siguiente URL:

```
https://www.jsonkeeper.com/b/MX0A
```

---

## Tecnologías usadas

- Python 3
- `requests`
- `pytest` (para los tests unitarios)

---

## Ejecutar

### 1. Instalación de dependencias

Si todavia no tenés las dependencias instaladas, ejecutá:

```bash
pip install -r requirements.txt
```

### 2. Ejecutar los tests

Para correr los tests, usá el siguiente comando en la raíz del proyecto:

```bash
pytest productos_tests.py
```

**Esto ejecutará todos los casos de prueba definidos en el archivo `productos_tests.py`**
---
