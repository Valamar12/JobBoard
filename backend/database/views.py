from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class Login(APIView):
    permission_classes = []
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            serializer = LoginSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    

class CreateUser(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
     username = request.data.get('username')
     password = request.data.get('password')
     first_name = request.data.get('first_name')
     last_name = request.data.get('last_name')
     email = "ThisIsAnEmai@oui.com"
     is_superuser = False
     is_staff  = False
     is_active = True

     password = make_password(password)
     last_login = User.last_login = timezone.now()
     date_joined = User.date_joined = timezone.now()

     try:
         User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name, is_superuser=is_superuser, last_login=last_login, date_joined = date_joined, is_staff=is_staff, is_active=is_active, email=email)
         # Additional fields can be set here

         return Response({'message': 'User created successfully.'}, status=status.HTTP_201_CREATED)
     except Exception as e:
         return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
     
class UserUpdateAPI(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request, pk):
     username = request.data.get('username')
     password = request.data.get('password')
     first_name = request.data.get('first_name')
     last_name = request.data.get('last_name')
     email = "ThisIsAnEmai@oui.com"
     is_superuser = False
     is_staff  = False
     is_active = True

     password = make_password(password)
     last_login = User.last_login = timezone.now()

     try:
            # Get the user to update
            user = User.objects.get(pk=pk)
            
            # Update the fields
            user.password = password
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.is_superuser = is_superuser
            user.last_login = last_login
            user.is_staff = is_staff
            user.is_active = is_active
            user.save()

            return Response({'message': 'User Updated successfully.'}, status=status.HTTP_200_OK)
     except User.DoesNotExist:
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
     except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# def database(request):
#     return HttpResponse("Hello world!")

class APIRootView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, *args, **kwargs):
        return Response({
            'adverts': reverse('adverts-list', request=request),
            'companies': reverse('company-list', request=request),
            'users': reverse('users-list', request=request),
            'applications': reverse('application-list', request=request)
        })

def adverts_index(request):
    adverts = Advert.objects.all()
    serializer = AdvertSerializer(adverts, many = True)
    return JsonResponse(serializer.data, safe = False)

def adverts_show(request, pk):
    advert = Advert.objects.get(pk=pk)
    serializer = AdvertSerializer(advert)
    return JsonResponse(serializer.data, safe = False)

def users_index(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return JsonResponse(serializer.data, safe=False)

def users_show(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data, safe = False)

def companies_index(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies, many=True)
    return JsonResponse(serializer.data, safe=False)

def companies_show(request, pk):
    company = Company.objects.get(pk=pk)
    serializer = CompanySerializer(company)
    return JsonResponse(serializer.data, safe = False)


#Advert views
class AdvertListAPI(generics.ListAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializerList

class AdvertRetrieveAPI(generics.RetrieveAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializerList

class AdvertCreateAPI(generics.CreateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer    

class AdvertUpdateAPI(generics.UpdateAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

class AdvertDestroyAPI(generics.DestroyAPIView):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer

#Company views
class CompanyListAPI(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyRetrieveAPI(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyCreateAPI(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer    

class CompanyUpdateAPI(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDestroyAPI(generics.DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

#User views
class UserListAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveAPI(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateAPI(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = LoginSerializer    
    
class UserDestroyAPI(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Application views
class ApplicationListAPI(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationRetrieveAPI(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class ApplicationCreateAPI(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializerCreate   

class ApplicationUpdateAPI(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializerUpdate

class ApplicationDestroyAPI(generics.DestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer