from rest_framework import serializers
from .models import Jop


class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jop
        fields = '__all__'