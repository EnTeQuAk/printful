import json

import httpretty

from printful import Client
from printful.tests.helpers import get_fixture


@httpretty.activate
def test_shipping_rates():
    httpretty.register_uri(
        httpretty.POST,
        'https://api.theprintful.com/shipping/rates/',
        body=get_fixture('shipping_de.json'),
        status=200,
        content_type='application/json',
    )

    response = Client('').post('shipping/rates', data=json.dumps({
        'recipient': {
            'country_code': 'DE',
        },
        'items': [
            {'variant_id': 1, 'quantity': 1},
            {'variant_id': 1118, 'quantity': 2}
        ]
    }))

    assert httpretty.last_request().path == '/shipping/rates/'

    assert response.status_code == 200
    assert len(response.json()['result']) == 3
