from django import forms
from django.forms import ModelForm, ModelMultipleChoiceField

from .models import Product, Review


class CSVUploadForm(forms.Form):
    file = forms.FileField()


class ProductSelectForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=True, label="Select a Product")


class ReviewSelectForm(ModelForm):
    reviews = ModelMultipleChoiceField(queryset=Review.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Review
        fields = ['reviews']
