from django.contrib.auth.forms import UserCreationForm
from .models import User, Topic, Category, Meeting
from django.forms import ModelForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'