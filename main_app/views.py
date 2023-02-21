from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Follow
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return redirect('post_index')

def about(request):
    return render(request, 'main_app/about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('create_profile')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def logout_index(request):
  return render(request, 'registration/logout_index.html')

class CreateProfile(LoginRequiredMixin, CreateView):
  model = Profile
  fields = ['username', 'name', 'avatar', 'age', 'bio']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


def user_profile(request):
  user = request.user
  posts = Post.objects.filter(user=user)
  return render(request, 'profile/user_index.html', {'posts':posts})

def profile(request, user_id):
  user = request.user
  profile = Profile.objects.get(id=user_id)
  posts = Post.objects.filter(user=profile.user)
  if Follow.objects.filter(follower = user, following = profile.user).exists():
    button_text = 'Unfollow'
  else:
    button_text = 'Follow'

  return render(request, 'profile/index.html', {'profile': profile, 'button_text':button_text, 'posts':posts})

class PostCreate(LoginRequiredMixin, CreateView):
  model = Post
  fields = ['caption', 'url']
  success_url = '/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

def post_index(request):
  posts = Post.objects.all()
  return render(request, 'post/index.html', { 'posts' : posts })