# serializers.py

from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['ID'] = user.id
        token['name'] = user.username
        token['is_superuser'] = user.is_superuser
        return token

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','is_superuser']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'address', 'description', 'url']
    
class AdvertSerializerList(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:  
        model = Advert
        fields = ['id','title','description','experience','salary','company']

class AdvertSerializer(serializers.ModelSerializer):
    class Meta:  
        model = Advert
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

class ApplicationSerializer(serializers.ModelSerializer):
    advert = AdvertSerializerList()
    class Meta:
        model = Application
        fields = ['id', 'user', 'status', 'advert']

class ApplicationSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class ApplicationSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'