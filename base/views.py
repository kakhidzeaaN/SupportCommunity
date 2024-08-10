from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Topic, Category, User, Meeting, Conversation, Comment
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, MeetingForm, UserForm
from .seeder import seeder_func
from django.contrib import messages

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(Q(name__icontains=q) | Q(category__heading__icontains=q) | Q(description__icontains=q))
    topics = list(dict.fromkeys(topics))
    seeder_func()

    # topics = Topic.objects.all()
    # print(topics[2].users.all())
    heading = "Supporting community"
    categories = Category.objects.all()
    meetings = Meeting.objects.all()
    conversation = Conversation.objects.all()
    context = {"topics": topics, "categories": categories, 'heading': heading, 'meetings': meetings, 'conversation': conversation}
    return render(request, 'base/home.html', context)


def about(request):
    categories = Category.objects.all()
    meetings = Meeting.objects.all()
    context = {"categories": categories, 'meetings': meetings}
    return render(request, 'base/about.html', context)


login_required(login_url='login')
def profile(request, pk):
    user = User.objects.get(id=pk)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = user.topics.filter(Q(name__icontains=q) | Q(category__heading__icontains=q) | Q(description__icontains=q))
    heading = "My community"
    # topics = user.topics.all()
    categories = Category.objects.all()
    context = {"topics": topics, 'heading': heading, "categories": categories}
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
            messages.error(request, 'User does not exist!')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', request.user.id)
        else:
            messages.error(request, 'User or Password is not correct!')

    return render(request, 'base/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('profile', user.id)

        else:
            messages.error(request, 'Follow The Instructions and create proper user and password...')

    context = {'form': form}
    return render(request, 'base/register.html', context)


def create_meeting(request, meeting_category=None):
    category = Category.objects.all()
    conversation = Conversation.objects.all()
    form = MeetingForm

    if request.method == 'POST':
        meeting_category = request.POST.get('category')
        meeting_conversation = request.POST.get('conversation')

        category, created = Category.objects.get_or_create(heading=meeting_category)
        conversation, created = Conversation.objects.get_or_create(type=meeting_conversation)

        form = MeetingForm(request.POST)

        new_meeting = Meeting(description=form.data['description'], conversation=conversation, file=request.FILES['file'], creator=request.user)

        if not Meeting.objects.filter(file=request.FILES['file']):
            new_meeting.save()
            new_meeting.category.add(category)
        else:
            messages.error(request, 'File with same name already exists...')
        return redirect('home')

    context = {'form': form, 'category': category, 'conversation': conversation}
    return render(request, 'base/create_meeting.html', context)


def reading(request, id):
    meeting = Meeting.objects.get(id=id)
    meeting_comments = meeting.comment_set.all()  # .order_by('-created')
    if request.method == "POST":
        Comment.objects.create(
            user=request.user,
            meeting=meeting,
            body=request.POST.get('body')
        )

    return render(request, 'base/reading.html', {'meeting': meeting, 'comments': meeting_comments})


def delete_meeting(request, id):
    obj = Meeting.objects.get(id=id)

    if request.method == "POST":
        obj.file.delete()
        obj.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': obj})

@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user.id)

    context = {'form': form}
    return render(request, 'base/update_user.html', context)


def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    meeting = comment.meeting
    if request.method == 'POST':
        comment.delete()
        return redirect('reading', meeting.id)

    return render(request, 'base/delete.html', {'obj': comment})