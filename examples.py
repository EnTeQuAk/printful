import json
from pprint import pprint

from printful import Client, PrintfulApiException

key = '3evn1618-ibti-0te8:w8vx-t1y9v38so35e'

client = Client(key)

try:
    #Get information about the store
    # pprint(client.get('store').json())

    # # #Get product list
    # pprint(client.get('products').json())

    # # #Get variants for product 10
    # pprint(client.get('products/10').json())

    # #Get information about Variant 1007
    # pprint(client.get('products/variant/1007'))

    # #Select 10 latest orders and get the total number of orders
    # pprint(client.get('orders',{'limit': 10}))
    # print('Total orders available: %i' % client.item_count())

    # #Select order with ID 12345 (Replace with your order's ID)
    # #pprint(client.get('orders/12345'))

    # #Select order with External ID 9900999 (Replace with your order's External ID)
    # #pprint(client.get('orders/@9900999'))

    # #Confirm order with ID 12345 (Replace with your order's ID)
    # #pprint(client.post('orders/12345/confirm'))

    # #Cancel order with ID 12345 (Replace with your order's ID)
    # #pprint(client.delete('orders/12345'))

    # #Create an order
    # pprint(client.post('orders', data=json.dumps({
    #     'recipient': {
    #         'name': 'John Doe',
    #         'address1': '172 W Providencia Ave #105',
    #         'city': 'Berlin',
    #         'country_code': 'DE',
    #         'zip': '10437'
    #     },
    #     'items': [{
    #         'variant_id': 1,
    #         'quantity': 1,
    #         'name': 'Niagara Falls poster',
    #         'retail_price': '19.99',
    #         'files': [{
    #             'url': 'http://example.com/files/posters/poster_1.jpg'
    #         }]
    #     }]
    # })).json())

    #Create an order and confirm immediately
#     pprint(client.post('orders',
#         {
#             'recipient':  {
#                 'name': 'John Doe',
#                 'address1': '172 W Providencia Ave #105',
#                 'city': 'Burbank',
#                 'state_code': 'CA',
#                 'country_code': 'US',
#                 'zip': '91502'
#             },
#             'items': [
#                 {
#                     'variant_id': 1, #Small poster
#                     'name': 'Niagara Falls poster', #Display name
#                     'retail_price': '19.99', #Retail price for packing slip
#                     'quantity': 1,
#                     'files': [
#                         {'url': 'http://example.com/files/posters/poster_1.jpg'}
#                     ]
#                 }
#             ]
#         },
#         {'confirm': 1}
#     ))


    # #Calculate shipping rates for an order
    # pprint(client.post('shipping/rates', data=json.dumps({
    #     'recipient': {
    #         'country_code': 'DE',
    #     },
    #     'items': [
    #        {'variant_id': 1, 'quantity': 1}, #Small poster
    #        {'variant_id': 1118, 'quantity': 2} #Alternative T-Shirt
    #     ]
    # })).json())


except PrintfulApiException as e:
    #Error code from the API
    print('API exception: %i %s' % (e.code, e.message))
except PrintfulApiException as e:
    #Error while doing the request
    print('Printful exception: %s' % e.message)

