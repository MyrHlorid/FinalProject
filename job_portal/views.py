from django.contrib.auth import authenticate, login, logout

from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .models import *
from django.http import HttpResponse
from django.db.models import Q


def index(request):
    return render(request, "base.html")


def registration(request):
    form = UserRegistrationForm()
    company_form = CompanyRegistrationForm()

    if request.method == 'POST':
        if request.POST.get('company_registration'):
            form = CompanyRegistrationForm(request.POST)
        else:
            form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return render(request, "base.html")

    return render(request, 'job_portal/registration.html', {'form': form, 'company_form': company_form})





def logout_view(request):
    logout(request)
    return render(request, "base.html")


def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return render(request,
                              "base.html")  # Замените 'dashboard' на имя вашего представления для панели управления
    else:
        form = CustomAuthenticationForm()

    return render(request, 'job_portal/login.html', {'form': form})


def search_job(request):
    search_text = request.GET.get("search", "")
    category = request.GET.get("category")

    jobs = Job.objects.all()

    if search_text and category:
        jobs = jobs.filter(
            Q(job_name__icontains=search_text) & Q(job_type=category)
        )
    elif search_text:
        jobs = jobs.filter(job_name__icontains=search_text)

    context = {
        "jobs": jobs,
    }

    return render(request, "job_portal/search_results.html", context)


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
