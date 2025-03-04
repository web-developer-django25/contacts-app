from django import forms
from .models import Contact, Category

# Create your forms here.
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'address', 'notes', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input'}),
            'address': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'notes': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
        } 