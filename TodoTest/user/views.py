from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as login_, logout as logout_, get_user_model

from django.views import View

from user.forms import LoginForm, CustomUserCreationForm, UpdateUserProfile
from user.models import Profile

User = get_user_model()


def logout(request):
    logout_(request)
    return redirect("/")


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'user/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        print(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, password=password, username=username)
            print('salam')
            if user:
                print(user)
                login_(request, user)
                return redirect('/')
            else:
                return redirect('login')


class SignUp(View):

    def get(self, request):
        form = CustomUserCreationForm()
        print(request.GET)
        context = {
            'form': form
        }
        return render(request, 'user/signup.html', context)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        context = {
            'form': form
        }
        return render(request, 'user/signup.html', context)


class UpdateProfile(LoginRequiredMixin, View):

    def get(self, request):
        user = Profile.objects.get(username=request.user)
        form = UpdateUserProfile(instance=user)
        context = {'form': form,
                   'avatar': user.image}
        return render(request, 'user/edit_profile.html', context)

    def post(self, request):
        user = Profile.objects.get(username=request.user)
        form = UpdateUserProfile(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
        context = {'form': form,
                   }
        return render(request, 'user/edit_profile.html', context)


class ViewProfile(LoginRequiredMixin, View):

    def get(self, request):
        user = Profile.objects.get(username=request.user)

        avatar = user.image
        return render(request, 'user/profile.html', {'profile': user, 'avatar': avatar})

