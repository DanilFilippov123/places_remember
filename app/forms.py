from django import forms

from app.models import Place


class PlaceForm(forms.ModelForm):
    name = forms.CharField(label='Название места')
    comment = forms.CharField(label='Комментарий')
    lat = forms.FloatField(widget=forms.HiddenInput())
    lng = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Place
        fields = ['name', 'comment', 'lat', 'lng']
