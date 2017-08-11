#####################
Django CoreAPI client
#####################

Wrapper around ``coreapi.Client`` for convenient usage in Django projects.


#####
Usage
#####

Define settings:

.. code-block:: python

    COREAPI_CLIENT = {
        'example_server': {
            'SCHEMA_URL': 'https://example.com/api/schema/',
            'AUTH_USERNAME': 'client-example',
            'AUTH_PASSWORD': 'password-example',
        },
    }

Initialize client:

.. code-block:: python

   from django_coreapi_client import Client

   client = Client('example_server')


Access API endpoints according to the schema, e.g.

.. code-block:: python

   users = client.api.users.list()
   project = client.api.users.projects.read(id=7)
   new_project = client.api.users.projects.create(name='xxx', user_id=3)

Et cetera.

Hope it's useful. 73!
