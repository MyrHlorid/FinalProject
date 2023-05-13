from django.urls import path
from . import views
from .views import profile_view, profile_create, profile_update
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path('jobs/', views.job_list, name='job_list'),
    path('job_list/', views.job_list, name="joblist"),
    path('job_add/', views.create_job, name='add_job_to_user'),
    path('clear_user_jobs/', views.clear_user_jobs, name='clear_user_jobs'),
    path('profile/', views.profile_view, name="profile"),
    path('profile/int:pk/', views.profile_view, name='profile_view'),
    path('profile/create/', views.profile_create, name='profile_create'),
    path('profile_update/', views.profile_update, name='profile_update'),
    path('add_job_to_user/<int:job_id>/', views.add_job_to_user, name='add_job_to_user'),
    path('profile/int:pk/update/', views.profile_update, name='profile_update_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)