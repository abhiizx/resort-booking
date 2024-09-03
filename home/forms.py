from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'User ID'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class DateRangeForm(forms.Form):
    checkin_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    checkout_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
