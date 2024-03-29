from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    # Helps understand which data model to store / validate / fill
    class Meta:
        model = Project
        fields = ['title', 'owner', 'feature_image', 'description','demo_link','source_link','tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add title'})
        # self.fields['description'].widget.attrs.update({'class':'input', 'placeholder':'Add description'})

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})