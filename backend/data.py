# data en memoria
productos = [
    {"id": 1, "nombre": "manzana", "precio": 0.8, "stock": 50, "disponible": True},
    {"id": 2, "nombre": "pan integral", "precio": 1.5, "stock": 30, "disponible": True},
    {"id": 3, "nombre": "leche entera", "precio": 1.2, "stock": 20, "disponible": True},
    {"id": 4, "nombre": "huevos (docena)", "precio": 2.5, "stock": 0,  "disponible": False},
    {"id": 5, "nombre": "queso", "precio": 3.0, "stock": 15, "disponible": True},
    {"id": 6, "nombre": "filetes de ternera", "precio": 10.0,"stock": 10, "disponible": True},
    {"id": 7, "nombre": "arroz (kg)", "precio": 0.9, "stock": 40, "disponible": True},
    {"id": 8, "nombre": "alubias (kg)", "precio": 1.0, "stock": 25, "disponible": True},
]

def get_all_products():
    return productos


def update_stock(id, delta):
    for p in productos:
        if p["id"] == id:
            p["stock"] = max(p["stock"] + delta, 0)
            p["disponible"] = p["stock"] > 0
            return p
    return None