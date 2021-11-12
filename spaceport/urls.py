from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('accounts/', include('allauth.urls')),
    path('models_temp.html', views.models_temp, name='models_temp')
]