from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name= 'systemAdmin'

urlpatterns = [
    path('', views.index, name='index'),
    path('testing/', views.testingTemp, name='testingTemp'),
    path('tokenGeneration/', views.tokenGeneration, name='tokenGeneration'),
    path('tokenReturn/', views.tokenReturn.as_view()),
    path('loginUser/', views.loginUser, name='loginUser'),
    path('logoutUser/', views._logout, name='logout')
]

urlpatterns= format_suffix_patterns(urlpatterns)