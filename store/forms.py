from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'contact_number', 'subject', 'reason']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'you@example.com'}),
            'contact_number': forms.TextInput(attrs={'placeholder': '+91 98765 43210'}),
            'subject': forms.TextInput(attrs={'placeholder': 'What is this about?'}),
            'reason': forms.Textarea(attrs={'placeholder': 'Tell us more (optional)', 'rows': 5}),
        }
