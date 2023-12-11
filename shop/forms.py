from django.forms import ModelForm
from .models import productmodel

class productform(ModelForm):
    class Meta:
        model=productmodel
        fields="__all__"