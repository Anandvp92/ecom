from django import forms
from .models import productmodel

class productform(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('RING', 'RINGS'),  
        ('CHAIN', 'CHAINS'),
        ('BANGLE', 'BANGLES'),
    ]

    PRODUCT_CATEGORY = forms.ChoiceField(label='Select Product Category', choices=CATEGORY_CHOICES)
    DESCRIPTION = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'DESCRIPTION',"class":'input-box','style':'position: relative; width: 500px; height: 100px; color:white; background-color: rgba(255, 255, 255, 0.2);border-radius: 10px;; resize: none;'}))
    TITLE = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'TITLE'}))
    PRICE = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'PRICE'}))
    class Meta:
        model=productmodel
        fields=['TITLE','DESCRIPTION','PRICE','IMAGE', 'PRODUCT_CATEGORY']
        
        