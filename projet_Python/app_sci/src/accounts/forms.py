from django import forms
from .models import Data


class PersonneForm(forms.Form):
    class Meta:
        model = Data
        fields = '__all__'
