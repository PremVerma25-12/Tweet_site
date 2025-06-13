from django  import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']  # Adjust these fields according to your model

    def __init__(self, *args, **kwargs):
        super(TweetForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-input'})
        self.fields['photo'].widget.attrs.update({'class': 'form-input'})

class UserRegistrationFrom(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username' , 'email', 'password1' , 'password2')