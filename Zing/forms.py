from django import forms
from .models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'bio', 'avatar', 'display_name']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
            'display_name': forms.TextInput(attrs={'placeholder': 'Enter your display name'}),
        }
