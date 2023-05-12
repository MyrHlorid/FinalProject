from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import NewUserForm, JobForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from .models import Job


def index(request):
    return render(request, "base.html")


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return render(request, "job_portal/login.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="job_portal/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, "base.html")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="job_portal/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request, "base.html")


def create_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "base.html")  # Redirect to the job list view after successful form submission
    else:
        form = JobForm()
    return render(request, 'job_portal/job_add.html', {'form': form})


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_portal/job_list.html', {'jobs': jobs})

def profile(request):
    return render(request=request, template_name="job_portal/Profile.html")