from django import forms
from .models import TropikoModel

class TropikoConfig(forms.ModelForm):
    class Meta:
        model =TropikoModel
        fields =['NAME', 'P_NUM', 'EMAIL', 'MESSAGE']

        widgets = {
            'NAME': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
            'P_NUM': forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}),
            'EMAIL': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'MESSAGE': forms.Textarea(attrs={'placeholder': 'Message', 'class': 'form-control'})
        }