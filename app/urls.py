from django.urls import path

from app import views

urlpatterns = [
    path('index', views.hello_page, name='hello_page'),
    path("place", views.PlaceCreateView.as_view(), name='place_page'),
]
