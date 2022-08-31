from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(UserTokenPairSerializer, cls).get_token(user)

        # payload
        token['username'] = user.username
        return token

    # def validate(self, attrs):
    #     data = super().validate(attrs)
    #     refresh = self.get_token(self.user)

    #     data['lifetime'] = int(refresh.access_token.lifetime.total_seconds())
    #     return data

    # def validate(self, attrs):
    #     data = super().validate
    #     print('self', self)
    #     refresh = self.get_token(self.user)
    #     data['refresh'] = str(refresh)
    #     data['access'] = str(refresh.access_token)

    #     # Add extra responses
    #     data['username'] = self.user.username
    #     data['groups'] = self.user.groups.values_list('name', flat=True)
    #     return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'],
                                        first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        return user
