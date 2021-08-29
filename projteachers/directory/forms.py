from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Textarea

from .models import Teacher

class select_subjects(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['data-subjects'] = value.instance.subject
        return option


class MyUserForm(UserCreationForm):
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':"ui left icon input", 'type':'password', 'align':'center', 'placeholder':'Password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':"ui left icon input", 'type':'password', 'align':'center', 'placeholder':'Re-type Password'}),
    )
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'class': 'ui left icon input',
                'placeholder': 'Username'
                }),
            'email': EmailInput(attrs={
                'class': 'ui left icon input', 
                'placeholder': 'E-mail'
                })
        }

class TeacherModelForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'phone', 'room_no', 'subject', 'image', 'slug']
        widgets = {
            
            'slug': TextInput(attrs={
                'placeholder': 'Slug should not contain spaces'
                }),
            'first_name': TextInput(attrs={
                'placeholder': 'First Name'
                }),
            'last_name': TextInput(attrs={
                'placeholder': 'Last Name'
                }),
            'email': EmailInput(attrs={
                'placeholder': 'E-mail'
                }),
            'phone': TextInput(attrs={
                'placeholder': 'Phone / Mobile'
                }),
            'room_no': TextInput(attrs={
                'placeholder': 'Room Number'
                }),
            'subject': TextInput(attrs={
                'placeholder': 'Subjects'
                }),
            }
