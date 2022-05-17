from rest_framework import serializers

from apps.bookmaster.models import Bookmaster

class BookmasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bookmaster
        fields='__all__'
        depth=0 