from django.contrib.auth.views import LogoutView
from django.urls import path

from app import views

urlpatterns = [
    path("place/", views.PlaceCreateView.as_view(), name='place_page'),
    path("place/<int:pk>/update", views.PlaceUpdateView.as_view(), name='place_update_page'),
    path("place/my", views.AllPlacesView.as_view(), name='my_places_page'),
    path("login", views.PlaceLoginView.as_view(), name='login_page'),
    path("logout", LogoutView.as_view(), name='logout_page'),
    path("registration", views.RegistrationView.as_view(), name='registration_page'),
    path('', views.StartPageTemplateView.as_view(), name='hello_page'),
]
