from rest_framework import serializers
from .models import Experience, ExperienceType


# class ExperienceTypeSerializer(serializers.ModelSerializer):
#     group_a = serializers.SerializerMethodField()
#     group_b = serializers.SerializerMethodField()

#     def get_group_a(self, instance):
#         return ExperienceSerializer(instance.experience_type.filter(name='Internship'), many=True).data

#     def get_group_b(self, instance):
#         return ExperienceSerializer(instance.experience_type.filter(name='Personal Project'), many=True).data

#     class Meta:
#         model = Experience
#         fields = ('group_a', 'group_b')


class ExperienceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceType
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)

        response['experience_type'] = ExperienceTypeSerializer(
            instance.experience_type).data['name']

        return response
