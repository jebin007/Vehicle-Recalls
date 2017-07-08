from django import forms
from vrecalls.models import Register

class UserForm(forms.ModelForm):
    class Meta: #information about the corresponding outer class
        model = Register
        fields = ['name', 'email', 'phone_number']


