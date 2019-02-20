from django.urls import path
from . import views

#Add URL patterns

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
