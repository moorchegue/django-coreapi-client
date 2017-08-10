from __future__ import unicode_literals, absolute_import

import pkg_resources

import coreapi
from django.conf import settings


__version__ = pkg_resources.get_distribution('django-coreapi-client').version


class Client(object):

    client = None
    schema = None

    def __init__(self, name):
        client_settings = settings.COREAPI_CLIENT.get(name)
        auth = coreapi.auth.BasicAuthentication(
            username=client_settings.get('AUTH_USERNAME'),
            password=client_settings.get('AUTH_PASSWORD'),
        )
        self._client = coreapi.Client(auth=auth)
        self._schema = self.client.get(client_settings.get('SCHEMA_URL'))

    def action(self, *args, **kwargs):
        return self._client.action(self._schema, *args, **kwargs)
