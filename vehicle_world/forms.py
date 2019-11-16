from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from rest_framework import serializers

class SignUpForm(UserCreationForm):
    firstName = forms.CharField(max_length=30, required=True)
    lastName = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    mobile = forms.CharField(max_length=10, required=True)
    password = forms.CharField(max_length=10, required=True)

    class Meta:
        model = User
        fields = ('firstName', 'lastName', 'email', 'mobile', 'password')


class SignUpValidateFormSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True, max_length=30)
    last_name = serializers.CharField(required=True, max_length=30)
    email = serializers.EmailField(required=True, max_length=128)
    mobile_number = serializers.CharField(required=True, max_length=20)
    password = serializers.CharField(required=True, max_length=128)
    confirm_password = serializers.CharField(required=True, max_length=128)