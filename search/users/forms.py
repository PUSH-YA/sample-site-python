from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 
                  'username', 'password1','password2']
        labels = {
            'first_name': 'Enter your name',
            'email': 'Enter your email',
            'username': 'Enter your username',
            'password1': 'Enter password',
            'password2': 'Confirm password',
                  }