from django import forms 
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationFrom(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('phone_number', 'email', 'full_name')
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('password must match')
        return cd['password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
    
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='You can change password via <a href=\'../password\'>this form</a>')

    class Meta:
        model = User
        fields = ('phone_number', 'email', 'full_name', 'password', 'last_login')
        
        
class UsreRegistrationForm(forms.Form):
    full_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=11)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)
    
    