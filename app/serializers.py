from rest_framework import serializers
from .models import Location
from django.contrib.auth.models import User

class LocationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Location
        fields = ('id', 'owner', 'latitude', 'longitude', 'address', 'created', 'updated', 'retrieved')

class UserSerializer(serializers.ModelSerializer):
    locations = serializers.PrimaryKeyRelatedField(many=True, queryset=Location.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'locations')