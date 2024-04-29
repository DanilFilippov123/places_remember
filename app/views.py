from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from app.forms import PlaceForm, RegisterUserForm
from app.models import Place, UserProfile


# Create your views here.
def hello_page(request):
    return render(request, 'app/base.html')


class PlaceCreateView(LoginRequiredMixin, CreateView):
    form_class = PlaceForm
    template_name = 'app/place.html'

    def form_valid(self, form):
        place = form.save(commit=False)
        place.user = self.request.user
        place.save()
        return super().form_valid(form)


class PlaceUpdateView(LoginRequiredMixin, UpdateView):
    model = Place
    form_class = PlaceForm

    template_name = 'app/place.html'
    success_url = reverse_lazy('hello_page')


class AllPlacesView(LoginRequiredMixin, ListView):
    model = Place
    template_name = 'app/user_places.html'
    context_object_name = 'places'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        if user is not None and not user.is_anonymous:
            return user.places.all()
        return Place.objects.none()


class PlaceLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'app/login.html'

    def get_success_url(self):
        return reverse_lazy('my_places_page')


class RegistrationView(CreateView):
    form_class = RegisterUserForm
    template_name = 'app/registration.html'
    success_url = reverse_lazy('login_page')

    def post(self, request, *args, **kwargs):
        # user cant register new users if he authorized
        if request.user.is_authenticated:
            raise PermissionDenied('You are already authenticated')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        redirect = super().form_valid(form)
        user = self.object
        profile = UserProfile(user=user)
        photo = form.cleaned_data['photo']
        if photo is not None:
            profile.photo.save(name=photo.name, content=photo.file)
        profile.save()
        return redirect
