from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import SignupForm, UserForm, ProfileForm
from .models import Profile

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('/accounts/profile')

    else:
        form = SignupForm()

    return render(request, 'registration/signup.html', {'form':form})



def profile(request):
    profile = Profile.objects.get(user = request.user)
    return render(request, 'accounts/profile.html', {'profile':profile})



def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile)
        user_form = UserForm(request.POST,instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            new_profile = profile_form.save(commit=False)
            new_profile.user = request.user
            new_profile.save() 
            return redirect( reverse('accounts:profile')   )


            pass

    else:
        profile_form = ProfileForm(instance=profile)
        user_form = UserForm(instance=request.user)

    context = {
        'profile_form':profile_form,
        'user_form':user_form
    }
    return render(request, 'accounts/profile_edit.html',context)