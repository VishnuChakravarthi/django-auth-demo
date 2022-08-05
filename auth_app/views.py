from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from auth_app.forms import UserLoginForm, UserForm, UserProfileForm

# Create your views here.


def index(request):
    return render(request, 'auth_app/index.html')


def registration(request):
    user_form = UserForm()
    profile_form = UserProfileForm()

    is_registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            is_registered = True

        else:
            print(user_form.errors, profile_form.errors)

    return render(request, 'auth_app/registration.html', {'user_form': user_form, 'user_profile_form': profile_form, 'is_registered': is_registered})


def user_login(request):
    login_form = UserLoginForm()

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("username", username, password)
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('success')
            else:
                return HttpResponse("Account not active")
        else:
            return HttpResponse("Invalid user")

    return render(request, 'auth_app/login.html', {'form': login_form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def login_success(request):
    return render(request, 'auth_app/success.html')


def register_success(request):
    return render(request, 'auth_app/registration_success.html')
