from django import forms
from .models import ProfileUpdate, CreateBid


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileUpdate
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'size': '40'}),
        }


class CreateBidFroms(forms.ModelForm):
    class Meta:
        model = CreateBid
        fields = '__all__'