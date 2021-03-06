from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views
from article import views as article_views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',article_views.dashboard, name = 'dashobard'),
    path('profile/',user_views.profile, name='profile'),
    path('register/',user_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
]
