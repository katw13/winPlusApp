from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    #path('systemAdmin/', include('systemAdmin.urls')),
    path('', views.usersInformation.as_view()),

]

urlpatterns= format_suffix_patterns(urlpatterns)