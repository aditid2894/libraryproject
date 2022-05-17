from rest_framework import serializers

from apps.entity.models import Entity

class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Entity
        fields='__all__'
        depth=0 