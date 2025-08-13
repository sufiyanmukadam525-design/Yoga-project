from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import UserRegistrationForm, UserLoginForm
from .models import RegisteredUser

class Register(View):
    def get(self, request):
        form = UserRegistrationForm()
        return render(request, "yogaapp/signup.html", {"form": form})

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            admin_code = form.cleaned_data.get("admin_code", "").strip()

            if User.objects.filter(username=username).exists():
                form.add_error("username", "This username is already taken.")
                return render(request, "yogaapp/signup.html", {"form": form})

            # create real Django user (hashed password)
            user = User.objects.create_user(username=username, email=email, password=password)

            # If admin_code matches, make them staff (DO NOT let plain form set admin)
            user_type = "U"
            if admin_code and admin_code == getattr(settings, "ADMIN_INVITE_CODE", ""):
                user.is_staff = True
                user.save()
                user_type = "A"

            # create profile
            RegisteredUser.objects.create(user=user, username=username, email=email, user_type=user_type)

            messages.success(request, "Registration successful. Please login.")
            return redirect("login")
        else:
            return render(request, "yogaapp/signup.html", {"form": form})


class Login(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "yogaapp/login.html", {"form": form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff or user.is_superuser:
                    return redirect("admin_dashboard")
                return redirect("home")
            else:
                form.add_error(None, "Invalid username or password.")
        return render(request, "yogaapp/login.html", {"form": form})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("login")


@method_decorator(login_required, name="dispatch")
class HomeView(View):
    def get(self, request):
        return render(request, "yogaapp/home.html")
