from django import forms


class PasswordResetForm(forms.Form):
    new_password= forms.CharField(max_length=100,required=True)
    new_password_again= forms.CharField(max_length=100,required=True)