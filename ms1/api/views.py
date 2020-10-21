from rest_framework.decorators import api_view
from rest_framework.response import Response
from nameko.standalone.rpc import ClusterRpcProxy

from api.serializers import PersonSerializer
from api.models import Person
import json
import os

CONFIG = {'AMQP_URI': f"amqp://{os.environ.get('RABBIT_USER')}:{os.environ.get('RABBIT_PASSWORD')}@{os.environ.get('RABBIT_HOST')}"}
print(CONFIG)

@api_view(["GET"])
def birds(request):
    with ClusterRpcProxy(CONFIG) as rpc:
        result = rpc.birds.get()
    return Response({"message": "Invoked", "data": result})

def persons():
    queryset = Person.objects.all()
    persons = PersonSerializer(queryset, many=True)
    return persons.data
