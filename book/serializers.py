from django.forms import ImageField
from rest_framework import serializers

from django_rest.utils import deleteFile
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    # image = ImageField()
    # image_url = serializers.SerializerMethodField()

    # def validate_image(self, image):
    #     print('IMAGE', image.name)

    class Meta:
        model = Book
        fields = '__all__'

    def update(self, instance, validated_data):
        deleteFile(instance.image.path)
        return super().update(instance, validated_data)
    
    def delete(self, instance):
        deleteFile(instance.image.path)

    # def get_image_url(self, book):
    #     request = self.context.get('request')
    #     image_url = book.image.url
    #     return request.build_absolute_uri(image_url)
