from django import forms
from django.contrib.auth.forms import AuthenticationForm

from job_portal.models import *


class CompanyRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password', 'company_name']


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password']


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', 'name', 'about_me', 'my_skills', 'my_experience')


class SearchJobForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    category = forms.ChoiceField(required=False,
                                 choices=(
                                     ("category1", "Category 1"),
                                     ("category2", "Category 2"),
                                     ("category3", "Category 3"),
                                 ))


class ApplyJobForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    cv = forms.FileField()
    cover_letter = forms.CharField(widget=forms.Textarea)


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = "__all__"
