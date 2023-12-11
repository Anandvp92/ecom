from django import forms
from .models import productmodel

class productform(forms.ModelForm):
    class Meta:
        model=productmodel
        fields=['TITLE','DESCRIPTION','PRICE','IMAGE', 'PRODUCT_CATEGORY']
        CATEGORY_CHOICES = [
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
        ('category3', 'Category 3'),
        ]

        favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=CATEGORY_CHOICES))