from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    # path('database/', views.database, name='datebase'),
    # path('api/database', views.database, name='datebase'),
    path('api', APIRootView.as_view()),

    #login
    path('api/token', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login', Login.as_view(), name='login'),
    path('api/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Adverts
    path('api/adverts', AdvertListAPI.as_view(), name='adverts-list'),
    path('api/adverts/<int:pk>/', AdvertRetrieveAPI.as_view(), name='adverts-retrieve'),
    path('api/adverts/create', AdvertCreateAPI.as_view(), name='adverts-create'),
    path('api/adverts/update/<int:pk>', AdvertUpdateAPI.as_view(), name='adverts-update'),
    path('api/adverts/delete/<int:pk>', AdvertDestroyAPI.as_view(), name='adverts-delete'),

    # Companies
    path('api/companies', CompanyListAPI.as_view(), name='company-list'),
    path('api/companies/<int:pk>/', CompanyRetrieveAPI.as_view()),
    path('api/companies/create', CompanyCreateAPI.as_view()),
    path('api/companies/update/<int:pk>', CompanyUpdateAPI.as_view()),
    path('api/companies/delete/<int:pk>', CompanyDestroyAPI.as_view()),

    # Users
    path('api/users', UserListAPI.as_view(), name='users-list'),
    path('api/users/<int:pk>/', UserRetrieveAPI.as_view()),
    path('api/users/create', CreateUser.as_view()),
    path('api/users/update/<int:pk>', UserUpdateAPI.as_view()),
    path('api/users/delete/<int:pk>', UserDestroyAPI.as_view()), 

    # Application
    path('api/application', ApplicationListAPI.as_view(), name='application-list'),
    path('api/application/<int:pk>/', ApplicationRetrieveAPI.as_view()),
    path('api/application/create', ApplicationCreateAPI.as_view()),
    path('api/application/update/<int:pk>', ApplicationUpdateAPI.as_view()),
    path('api/application/delete/<int:pk>', ApplicationDestroyAPI.as_view()),
]