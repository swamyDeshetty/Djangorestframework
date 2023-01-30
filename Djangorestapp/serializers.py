from rest_framework import serializers
from .models import *

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model =Member
        fields= '__all__'
class CricketerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cricketer
        fields ='__all__'