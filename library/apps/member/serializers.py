from rest_framework import serializers

from apps.member.models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields='__all__'
        depth=0 