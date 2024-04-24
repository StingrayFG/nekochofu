from rest_framework import serializers

from .models import Record


class RecordPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

class RecordGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['contents']

