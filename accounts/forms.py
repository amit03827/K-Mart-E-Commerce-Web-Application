from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UseAuthenticationForm(AuthenticationForm):
    class Meta:
        widgets = {
            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Username...'
             }),
            'password' : forms.PasswordInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Password...'
            })
        }