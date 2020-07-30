from django.urls import path, include

# for viewsets
from rest_framework.routers import DefaultRouter

from django_profiles_api import views

# register viewset with router in Django and include path
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')


# webserveraddress/api/hello-view/
# MAp url to apiView
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]