from django import forms
from .models import CreateProject


class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = CreateProject
        fields = '__all__'