from nameko.rpc import rpc, RpcProxy
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','app.settings')
django.setup()

from api.views import persons

class Persons:
    name = "persons"

    @rpc
    def get(self):
        print('Called Persons service')
        return persons()
