from rest_framework import serializers
from .models import Accordion


class AccordionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accordion
        fields = '__all__'
