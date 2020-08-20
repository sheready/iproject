from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Account created for {username}!')
                return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render (request,'register.html',{'form':form})

@login_required
def profile(request,username):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    try:
        user = User.objects.get(pk=username)
        profile = Profile.objects.get(user=user)
        posts = Post.get_author_post(profile.id)
    
    except Post.DoesNotExist:
        post = None

    
    context = {
        'u_form':u_form,
        'p_form':p_form,
        'posts':posts,
    }
    
    return render(request, 'profile.html', context)


