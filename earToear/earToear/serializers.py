from dataclasses import field, fields
from rest_framework import serializers

from earToear.models import JFLaughs
from .models import JFLaughs

class JFLaughSerializer(serializers.ModelSerializer):
    class Meta:
        model = JFLaughs
        fields = ['id', 'Joke', 'Answer']