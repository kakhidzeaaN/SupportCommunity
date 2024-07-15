from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Topic, Category, User
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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

login_required(login_url='login')
def profile(request, pk):
    user = User.objects.get(id=pk)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = user.topics.filter(Q(name__icontains=q) | Q(category__heading__icontains=q) | Q(description__icontains=q))
    heading = "My community"
    # topics = user.topics.all()
    context = {"topics": topics, 'heading': heading}
    return render(request, 'base/profile.html', context)


login_required(login_url='login')
def add(request, id):
    user = request.user
    topic = Topic.objects.get(id=id)
    user.topics.add(topic)
    return redirect('profile', user.id)


login_required(login_url='login')
def delete(request, id):
    obj = Topic.objects.get(id=id)

    if request.method == "POST":
        request.user.topics.remove(obj)
        return redirect('profile', request.user.id)

    return render(request, 'base/delete.html', {'obj': obj})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profile', request.user.id)

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            pass

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            pass

    return render(request, 'base/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')