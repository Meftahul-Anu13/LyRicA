from django import forms
from django.contrib.auth.hashers import make_password
from .models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'user_type']  # Include fields from your model

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
