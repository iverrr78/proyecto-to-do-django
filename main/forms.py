from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label = "username", max_length = 50)
    email = forms.EmailField(label = "email", max_length = 50)
    password = forms.CharField(label = "password", max_length= 50)