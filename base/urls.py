from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('add/<str:id>/', views.add, name='add'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
