from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('add_rel/<str:id>/', views.add, name='add'),
    path('delete_rel/<str:id>/', views.delete, name='drop'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('create/', views.create_meeting, name='create'),
    path('reading/<str:id>', views.reading, name='reading'),
    path('delete_meeting/<str:id>', views.delete_meeting, name='delete'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_comment/<str:id>', views.delete_comment, name='delete_comment')
]
