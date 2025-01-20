from django import forms
from .models import Poll, Choice

from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=35, min_length=5,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password',
                                max_length=50, min_length=5,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class PollAddForm(forms.ModelForm):

    choice1 = forms.CharField(label='Choice 1', max_length=100, min_length=1,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice2 = forms.CharField(label='Choice 2', max_length=100, min_length=1,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Poll
        fields = ['text', 'choice1', 'choice2']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }


class EditPollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['text', ]
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }


class ChoiceAddForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text', ]
        widgets = {
            'choice_text': forms.TextInput(attrs={'class': 'form-control', })
        }
