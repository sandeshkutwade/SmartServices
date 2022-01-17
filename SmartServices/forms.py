from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name' ,'email', 'username','password1', 'password2']

class AddPartner(ModelForm):
    class Meta:
        model = Partners
        fields = '__all__'
        # exclude = ['user']


class PlaceOrder(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        # exclude = ['user']
        