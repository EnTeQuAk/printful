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
