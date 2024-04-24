from django import forms 
# from django.forms import ModelForm
from .models import FirstTry,SecondTry,DetailsFeed


class FirstTryForm(forms.ModelForm):
    class Meta:
        model = FirstTry
        fields = '__all__'


class SecondTryForm(forms.ModelForm):
    class Meta:
        model = SecondTry
        fields = '__all__'


class DetailsFeedForm(forms.ModelForm):
    class Meta:
        model = DetailsFeed
        fields = '__all__'