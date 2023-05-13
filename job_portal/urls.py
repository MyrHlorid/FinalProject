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
    path('job_list/', views.job_list, name="joblist"),
    path('job_add/', views.create_job, name="create a new job"),
    path('profile/', views.profile_view, name="profile"),
    path('profile/<int:pk>/', profile_view, name='profile_view'),
    path('profile/create/', profile_create, name='profile_create'),
    path('profile_update/', profile_update, name='profile_update')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
