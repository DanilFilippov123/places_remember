from django.forms import HiddenInput
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from app.forms import PlaceForm
from app.models import Place
from places_remember import settings


# Create your views here.
def hello_page(request):
    return render(request, 'app/index.html')


class PlaceCreateView(CreateView):
    form_class = PlaceForm
    template_name = 'app/place.html'


class PlaceUpdateView(UpdateView):
    model = Place
    form_class = PlaceForm

    template_name = 'app/place.html'
    success_url = reverse_lazy('hello_page')


def place_page(request):
    data = {'yandex_maps_api_key': settings.YANDEX_MAPS_API_KEY}

    return render(request, 'app/place.html', context=data)
