from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('meetings/', views.get_meetings),
    path('meetings/<str:id>', views.get_meetings)
]