from .models import Adjudication
from django import forms

class adjudicationForm(forms.ModelForm):
    class Meta:
        model = Adjudication
        fields = '__all__'