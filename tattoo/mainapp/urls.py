from django.contrib.auth.views import (
    LogoutView,
    PasswordResetDoneView,
    PasswordResetCompleteView
)
from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('all-master/', AllMasters.as_view(), name='all_master'),
    path('master/<int:pk>/', GetMaster.as_view(), name='view_master'),
    path('blog/', GetPosts.as_view(), name='blog'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('works/', WorksListView.as_view(), name='works'),
    path('master/<int:pk>/works/', WorksMaster.as_view(), name='works_master'),
    path('about/', GetAbout.as_view(), name='about'),


    path('login/', LoginView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
    path('password-reset/', CustomPasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name='mainapp/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(
             template_name='mainapp/password_reset_complete.html')
         ,
         name='password_reset_complete'),
]
