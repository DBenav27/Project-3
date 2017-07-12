from django.shortcuts import render, redirect, get_object_or_404
from .models import Treasure
from .forms import TreasureForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import TreasureForm, LoginForm


def dates(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    return render(request, 'dates.html', {'treasures':treasures,'form':form})

def index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def show(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    return render(request, 'show.html', {'treasure': treasure})

def delete(request,pk):
    treasure = get_object_or_404(Treasure, pk=pk)
    treasure.delete()
    return redirect('/profiles')

def post_treasure(request):
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        treasure = form.save(commit = False)
        treasure.user = request.user
        treasure.save()
    return HttpResponseRedirect('/profiles')


def profile(request, username):
    user = User.objects.get(username=username)
    treasures = Treasure.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'treasures': treasures})

def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user. is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def like_treasure(request):
    treasure_id = request.GET.get('treasure_id', None)
    likes = 0
    if (treasure_id):
        treasure = Treasure.objects.get(id=int(treasure_id))
        if treasure is not None:
            likes = treasure.likes + 1
            treasure.likes = likes
            treasure.save()
    return HttpResponse(likes)
