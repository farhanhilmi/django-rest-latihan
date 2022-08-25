from rest_framework import serializers
from .models import MataKuliah


class MataKuliahSerializer(serializers.ModelSerializer):
    class Meta:
        model = MataKuliah
        fields = '__all__'
