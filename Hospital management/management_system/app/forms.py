
from django import forms
from .models import Admin

class AdminCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Admin
        fields = ('name', 'email', 'password')

