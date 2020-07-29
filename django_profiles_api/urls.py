from django.urls import path

from django_profiles_api import views

# webserveraddress/api/hello-view/
# MAp url to apiView
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]