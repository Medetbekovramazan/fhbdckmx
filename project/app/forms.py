from django import forms
class UserForm(forms.Form):
    name = forms.CharField(required=True)
    age = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)

class UserForm2(forms.Form):
    name = forms.CharField(required=True)
    age = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)