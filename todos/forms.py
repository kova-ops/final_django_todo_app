from django import forms
from .models import todo

class todoForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'What needs to be done?'}),
            'description': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Add detail(optional)', 'rows': 3})
        }