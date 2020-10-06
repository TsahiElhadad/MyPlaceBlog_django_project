from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# inherit form the standard FORM of Django, plus Email field
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
 # The fields that will shown in the FORM
        fields = ['username', 'email', 'password1', 'password2']

# update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # The fields that will shown in the FORM
        fields = ['username', 'email']

# change profile image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']