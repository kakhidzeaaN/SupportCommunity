from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic, Category, User
from django.db.models import Q


# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(Q(name__icontains=q) | Q(category__heading__icontains=q) | Q(description__icontains=q))
    topics = list(set(topics))
    # topics = Topic.objects.all()
    # print(topics[2].users.all())
    heading = "Supporting community"
    categories = Category.objects.all()
    context = {"topics": topics, "categories": categories, 'heading': heading}
    return render(request, 'base/home.html', context)


def about(request):
    return render(request, 'base/about.html')


def profile(request, pk):
    user = User.objects.get(id=pk)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = user.topics.filter(Q(name__icontains=q) | Q(category__heading__icontains=q) | Q(description__icontains=q))
    heading = "My community"
    # topics = user.topics.all()
    context = {"topics": topics, 'heading': heading}
    return render(request, 'base/profile.html', context)