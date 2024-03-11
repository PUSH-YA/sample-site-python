from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill



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
        

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location',
                  'bio', 'short_intro', 'profile_image',
                  'social_github', 'social_linkedin', 'social_website' ]
        

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['owner']
