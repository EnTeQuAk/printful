import json
import urllib
from base64 import b64encode

import requests
from requests.utils import to_native_string


class PrintfulException(Exception):
    pass


class PrintfulApiException(PrintfulException):
    def __init__(self, message, code):
        super(PrintfulApiException, self).__init__(message, code)
        Exception.__init__(self, message)
        self.code = code

    def __str__(self):
        return '%i - %s' % (self.code, self.message)


class Response(object):

    def __init__(self, data):
        self.data = data

    def item_count(self):
        if (self.data and 'paging' in self.data):
            return self.data['paging']['total']
        else:
            return None


class HTTPBasicKeyAuth(requests.auth.AuthBase):
    def __init__(self, key):
        self.key = bytes(key, 'utf-8')

    def __call__(self, request):
        request.headers['Authorization'] = 'Basic ' + to_native_string(
            b64encode(self.key))

        return request


class Client(requests.Session):
    API_URL = 'https://api.theprintful.com/'
    USER_AGENT = 'Printful API Python Library 1.0'

    def __init__(self, api_key):
        super(Client, self).__init__()
        self.api_key = api_key

    def request(self, method, url, *args, **kwargs):
        data = kwargs.pop('data', {})

        headers = {
            'User-Agent': Client.USER_AGENT,
            'Content-Type': 'application/json',
            'Method': method,
        }

        headers.update(kwargs.pop('headers', {}))

        kwargs.update({
            'auth': HTTPBasicKeyAuth(self.api_key),
            'headers': headers,
        })

        full_url = urllib.parse.urljoin(Client.API_URL, url)

        # TODO: Error handling
        return super(Client, self).request(method, full_url, *args, **kwargs)
