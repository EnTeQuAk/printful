from __future__ import unicode_literals

from base64 import b64encode

import requests

from printful._compat import urllib, force_text, force_bytes


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
        if (self.data and u'paging' in self.data):
            return self.data['paging']['total']
        else:
            return None


class HTTPBasicKeyAuth(requests.auth.AuthBase):
    def __init__(self, key):
        self.key = force_bytes(key, 'utf-8')

    def __call__(self, request):
        auth = 'Basic ' + force_text(b64encode(self.key))
        request.headers['Authorization'] = auth

        return request


class Client(requests.Session):
    API_URL = 'https://api.theprintful.com/'
    USER_AGENT = 'Printful API Python Library 1.0'

    def __init__(self, api_key):
        super(Client, self).__init__()
        self.api_key = api_key

    def request(self, method, url, *args, **kwargs):
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

        full_url = urllib.parse.urljoin(Client.API_URL, url).rstrip('/')

        # TODO: Error handling
        return super(Client, self).request(method, full_url, *args, **kwargs)
