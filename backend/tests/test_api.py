import sys, os
curdir = os.path.dirname(__file__)
sys.path.insert(0, curdir + os.sep + '..')
import pytest
from app import app
from data import productos

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_query_products(client):
    query = '{ products { id nombre precio stock disponible } }'
    resp = client.post('/graphql', json={'query': query})
    assert resp.status_code == 200
    data = resp.get_json()['data']['products']
    assert isinstance(data, list)
    assert len(data) >= 1
    for p in data:
        assert 'id' in p
        assert 'nombre' in p
        assert 'precio' in p
        assert 'stock' in p
        assert 'disponible' in p


def test_update_stock_and_disponible(client):
    # borrar todos los productos
    clear = 'mutation { clearProducts { ok } }'
    resp = client.post('/graphql', json={'query': clear})
    assert resp.status_code == 200
    ok = resp.get_json()['data']['clearProducts']['ok']
    assert ok is True

    # añadir producto de prueba
    productos.clear()
    productos.append({'id': 99, 'nombre': 'test', 'precio': 1.0, 'stock': 1, 'disponible': True})

    # decrementar a 0
    dec = 'mutation { updateStock(id: 99, delta: -1) { product { stock disponible } } }'
    resp = client.post('/graphql', json={'query': dec})
    prod = resp.get_json()['data']['updateStock']['product']
    assert prod['stock'] == 0
    assert prod['disponible'] is False

    # incrementar a 1
    inc = 'mutation { updateStock(id: 99, delta: 1) { product { stock disponible } } }'
    resp = client.post('/graphql', json={'query': inc})
    prod = resp.get_json()['data']['updateStock']['product']
    assert prod['stock'] == 1
    assert prod['disponible'] is True
