from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['pid',
                'pname',
                'pcost',
                'pcolor',
                'pmfd',
                'pexfd']

class uppdateForm(forms.Form):
    pid=forms.CharField(label='enter pid',max_length=20)
    pcost=forms.CharField(label='enter pcost',max_length=10)

class DeleteForm(forms.Form):
    pid=forms.IntegerField()