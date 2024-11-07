from rest_framework import serializers

from .models import Szkolenie


class SzkolenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Szkolenie
        fields = "__all__"