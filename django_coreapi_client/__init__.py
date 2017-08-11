from __future__ import unicode_literals, absolute_import

import coreapi
from django.conf import settings


class Client(object):

    client = None
    schema = None
    _name = None
    _keys = []

    def __init__(self, name, keys=[], auth=None, client=None, schema=None):
        client_settings = settings.COREAPI_CLIENT.get(name)

        if not auth:
            auth = coreapi.auth.BasicAuthentication(
                username=client_settings.get('AUTH_USERNAME'),
                password=client_settings.get('AUTH_PASSWORD'),
            )
        if not client:
            client = coreapi.Client(auth=auth)
        if not schema:
            schema = client.get(client_settings.get('SCHEMA_URL'))

        self.client = client
        self.schema = schema
        self._keys = keys
        self._name = name

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]

        keys = self._keys + [key]
        return self.__class__(self._name, keys)

    def __getitem__(self, key):
        return self.__getattr__(key)

    def __call__(self, **kwargs):
        return self.action(self._keys, **kwargs)

    def action(self, keys, **kwargs):
        return self.client.action(self.schema, keys, params=kwargs)
