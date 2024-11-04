from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UsernamePasswordForm(forms.Form):
    username = forms.CharField(
        max_length=128,
        required=True,
        label="Username"
    )