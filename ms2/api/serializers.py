from rest_framework import serializers

from api.models import Bird

class BirdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bird
        fields = "__all__"
