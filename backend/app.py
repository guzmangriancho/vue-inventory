# app.py
import collections
import collections.abc
# Hacemos que collections.MutableMapping apunte a la clase correcta
collections.MutableMapping = collections.abc.MutableMapping

from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from database import init_db, SessionLocal
from models import Product
from schema import schema

app = Flask(__name__)
CORS(app)

# Inicializa la BBDD y datos de ejemplo
init_db()
db = SessionLocal()
if db.query(Product).count() == 0:
    ejemplos = [
        Product(id=1, nombre="Manzana", precio=0.8,  stock=50, disponible=True),
        Product(id=2, nombre="Pan Integral", precio=1.5, stock=30, disponible=True),
        Product(id=3, nombre="Leche Entera", precio=1.2, stock=20, disponible=True),
        Product(id=4, nombre="Huevos (docena)", precio=2.5, stock=0, disponible=False),
        Product(id=5, nombre="Queso", precio=3.0, stock=15, disponible=True),
        Product(id=6, nombre="Filetes de Ternera", precio=10.0, stock=10, disponible=True),
        Product(id=7, nombre="Arroz (kg)", precio=0.9, stock=40, disponible=True),
        Product(id=8, nombre="Alubias (kg)", precio=1.0, stock=25, disponible=True),
    ]
    db.add_all(ejemplos)
    db.commit()
db.close()

# Configura el endpoint /graphql
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=schema,
        graphiql=True,  # Interfaz web para probar
    ),
)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
