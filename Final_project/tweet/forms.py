from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# ------------------ Tweet Form ------------------
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']  # Adjust if needed

    def __init__(self, *args, **kwargs):
        super(TweetForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-input'})


# ------------------ User Registration Form ------------------
class UserRegistrationFrom(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationFrom, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.help_text = ''  # Remove default help texts
            field.widget.attrs.update({'class': 'form-input'})  # Add input styling


# ------------------ Custom Login Form ------------------
class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            field.help_text = '' 
