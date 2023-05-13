from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import NewUserForm, JobForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile
from .models import Job
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from .forms import ApplyJobForm
from .models import Job, Candidates, Profile, UserJob
from django.http import HttpResponse


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


def add_job_to_user(request, job_id):
    user = request.user
    job = Job.objects.get(id=job_id)
    user_job = UserJob(user=user, job=job)
    user_job.save()
    return redirect('job_list')
def job_name(request, job_id, user_id):
    user_job = get_object_or_404(UserJob, job_id=job_id, user_id=user_id)
    job_name = user_job.job.job_name
    return HttpResponse(job_name)
def clear_user_jobs(request):
    if request.user.is_authenticated:
        user_jobs = UserJob.objects.filter(user=request.user)
        user_jobs.delete()
    return redirect('profile')
@login_required
def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        form = ApplyJobForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            if not user.is_authenticated:
                return redirect('login')
            applicant_name = form.cleaned_data.get('name')
            applicant_email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            cv = form.cleaned_data.get('cv')
            cover_letter = form.cleaned_data.get('cover_letter')
            job_apply = JobApply.objects.create(
                job=job,
                user=user,
                applicant_name=applicant_name,
                applicant_email=applicant_email,
                phone=phone,
                cv=cv,
                cover_letter=cover_letter
            )
            job_apply.save()
            return redirect('profile')
    else:
        form = ApplyJobForm()
    context = {'job': job, 'form': form}
    return render(request, 'job/apply_job.html', context)

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

@login_required(login_url='login')
def profile_view(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = Profile(user=user)
        profile.save()
    return render(request, 'job_portal/profile.html', {'profile': profile})

def profile_create(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile_view')
    else:
        form = ProfileForm()
    return render(request, 'job_portal/profile_create.html', {'form': form})

def profile_update(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'job_portal/profile_update.html', {'form': form})

