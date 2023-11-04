from django import forms

class URLForm(forms.Form):
    url = forms.URLField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your long URL here...'
        }),
        error_messages={
            'invalid': 'Invalid URL. Please enter a valid URL.'
        }
    )
