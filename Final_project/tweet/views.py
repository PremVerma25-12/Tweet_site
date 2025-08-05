from django.shortcuts import render
from .models import Tweet , Profile
from .forms import TweetForm , UserRegistrationFrom
from django.shortcuts import get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.db import IntegrityError



def tweet_list(request):
   tweets = Tweet.objects.all().order_by('-created_at')
   return render(request , 'tweet_list.html' , {'tweets' : tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST , request.FILES)
        if form.is_valid():
           tweet = form.save(commit=False)
           tweet.user = request.user
           tweet.save()
           return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request , 'tweet_form.html' , {'form' : form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet , pk = tweet_id , user = request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST , request.FILES , instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request , 'tweet_form.html' , {'form' : form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet , pk = tweet_id , user = request.user)
    if request.method == 'POST':
      tweet.delete()
      return redirect('tweet_list')
    return render(request , 'tweet_confirm_delete.html' , {'tweet' : tweet})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationFrom(request.POST)
        if form.is_valid():
            try:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()
                login(request, user)
                messages.success(request, "Registration successful! You are now logged in.")
                return redirect('tweet_list')  # Fixed: removed the context dict from redirect
            except IntegrityError:
                messages.error(request, "Username already exists. Please choose a different one.")
        else:
            # Form is invalid - collect all error messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegistrationFrom()  # Proper instantiation
    
    return render(request, 'registration/register.html', {'form': form})


from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required
def update_avatar(request):
    if request.method == 'POST':
        avatar = request.FILES.get('avatar')
        if avatar:
            if avatar.size > 2*1024*1024:  # 2MB limit
                messages.error(request, "Image size should be less than 2MB")
            else:
                profile, created = Profile.objects.get_or_create(user=request.user)  # Fixed
                profile.avatar = avatar
                profile.save()
                messages.success(request, "Avatar updated successfully")
        else:
            messages.error(request, "No image selected")
    return redirect('tweet_list')