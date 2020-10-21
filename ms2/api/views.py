from rest_framework.decorators import api_view
from rest_framework.response import Response
from nameko.standalone.rpc import ClusterRpcProxy

from api.serializers import BirdSerializer
from api.models import Bird
import json
import os

CONFIG = {'AMQP_URI': f"amqp://{os.environ.get('RABBIT_USER')}:{os.environ.get('RABBIT_PASSWORD')}@{os.environ.get('RABBIT_HOST')}"}
print(CONFIG)

@api_view(["GET"])
def persons(request):
    with ClusterRpcProxy(CONFIG) as rpc:
        result = rpc.persons.get()
    return Response({"message": "Invoked", "data": result})

def birds():
    queryset = Bird.objects.all()
    birds = BirdSerializer(queryset, many=True)
    return birds.data
