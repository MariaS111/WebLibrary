from django.urls import path, include
from . import views
from .views import CustomLogoutView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]