from django.contrib.auth import authenticate

from .models import Goods, Comment, Question
from django.forms import ModelForm
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        }),
    )

    email = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.EmailInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        }),
    )

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
        }),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "ReInputPassword",
        }),
    )

    def clean(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError("passwords dont match")

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password1'],
        )
        user.save()
        return user


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
        }),
    )


class CommentForm(ModelForm):
    assess = forms.IntegerField(
        required=True,
    )

    comment = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
        }),
    )

    class Meta:
        model = Comment
        fields = ('assess', 'comment')


class QuestionForm(ModelForm):
    text = forms.CharField(
        required=True,
        widget= forms.Textarea(attrs={
            'class': "form-control",
            'rows': '7'
        }))

    class Meta:
        model = Question
        fields=('text',)
