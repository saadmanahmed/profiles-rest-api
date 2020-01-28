from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Namefield for testing out API View"""
    name=serializers.CharField(max_length=10)
    email=serializers.EmailField(max_length=None, min_length=None, allow_blank=False)
