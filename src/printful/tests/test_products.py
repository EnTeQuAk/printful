import httpretty

from printful import Client
from printful.tests.helpers import get_fixture


@httpretty.activate
def test_products():
    httpretty.register_uri(
        httpretty.GET,
        'https://api.theprintful.com/products',
        body=get_fixture('products.json'),
        status=200,
        content_type='application/json',
    )

    response = Client('').get('products')

    assert httpretty.last_request().path == '/products'

    assert response.status_code == 200
    assert len(response.json()['result']) == 80


@httpretty.activate
def test_products_variants():
    httpretty.register_uri(
        httpretty.GET,
        'https://api.theprintful.com/products/1',
        body=get_fixture('products_1.json'),
        status=200,
        content_type='application/json',
    )

    response = Client('').get('products/1')

    assert httpretty.last_request().path == '/products/1'

    assert response.status_code == 200
    assert response.json()['result']['product']['id'] == 1
    assert response.json()['result']['product']['type'] == 'POSTER'
    assert len(response.json()['result']['variants']) == 9


@httpretty.activate
def test_products_variant_detail():
    httpretty.register_uri(
        httpretty.GET,
        'https://api.theprintful.com/products/variant/4464',
        body=get_fixture('products_variant_4464.json'),
        status=200,
        content_type='application/json',
    )

    response = Client('').get('products/variant/4464')

    assert httpretty.last_request().path == '/products/variant/4464'

    assert response.status_code == 200
    assert response.json()['result']['variant']['id'] == 4464
    assert response.json()['result']['product']['id'] == 1
