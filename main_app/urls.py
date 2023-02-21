from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('accounts/logout_index', views.logout_index, name='logout_index'),
  path('accounts/signup/createprofile', views.CreateProfile.as_view(), name='create_profile'),
  # path('accounts/signup/<int:pk>/updateprofile', views.ProfileUpdate.as_view(), name='update_profile'),
]