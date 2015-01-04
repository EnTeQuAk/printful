import httpretty

from printful import Client
from printful.tests.helpers import get_fixture


@httpretty.activate
def test_orders():
    httpretty.register_uri(
        httpretty.GET,
        'https://api.theprintful.com/orders',
        body=get_fixture('orders.json'),
        status=200,
        content_type='application/json',
    )

    response = Client('').get('orders')

    assert httpretty.last_request().path == '/orders'

    assert response.status_code == 200
    assert len(response.json()['result']) == 7


@httpretty.activate
def test_orders_paginated_offset():
    httpretty.register_uri(
        httpretty.GET,
        'https://api.theprintful.com/orders?offset=5',
        body=get_fixture('orders_offset_5.json'),
        status=200,
        content_type='application/json',
    )

    response = Client('').get('orders', params={'offset': 5})

    assert httpretty.last_request().path == '/orders?offset=5'

    assert response.status_code == 200
    assert response.json()['paging'] == {
        'total': 7,
        'offset': 5,
        'limit': 20
    }


@httpretty.activate
def test_orders_paginated_limit():
    httpretty.register_uri(
        httpretty.GET,
        'https://api.theprintful.com/orders?limit=1',
        body=get_fixture('orders_limit_1.json'),
        status=200,
        content_type='application/json',
    )

    response = Client('').get('orders', params={'limit': 1})

    assert httpretty.last_request().path == '/orders?limit=1'

    assert response.status_code == 200
    assert response.json()['paging'] == {
        'total': 7,
        'offset': 0,
        'limit': 1
    }
