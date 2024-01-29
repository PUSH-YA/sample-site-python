from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    # Helps understand which data model to store / validate / fill
    class Meta:
        model = Project
        fields = ['title', 'description','demo_link','source_link','tags']