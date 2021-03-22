from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('all-master/', AllMasters.as_view(), name='all_master'),
    path('master/<int:pk>/', GetMaster.as_view(), name='view_master'),
    path('blog/', GetPosts.as_view(), name='blog'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('about/', GetAbout.as_view(), name='about'),
    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
]
