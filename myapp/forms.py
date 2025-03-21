from django import forms
from .models import CustomUser

# In forms.py
from django import forms
from django.contrib.auth.models import User

# forms.py
from django import forms
from django.contrib.auth.models import User  # Use CustomUser if you're using a custom model

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    fullname = forms.CharField(max_length=255)

    class Meta:
        model = User  # Use CustomUser if you're using a custom model
        fields = ['fullname', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user



class LoginForm(forms.Form):
    email = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
