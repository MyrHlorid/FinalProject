from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from job_portal.models import Job

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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo', 'name', 'about_me', 'my_skills', 'my_experience')

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


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
