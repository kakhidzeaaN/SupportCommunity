from django.shortcuts import render
from django.http import HttpResponse
from .models import Topics


# Create your views here.
def home(request):
    # context = {"word": "Hello World!!!"}
    topic = Topics.objects.all()
    context = {"topics": topic}
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')