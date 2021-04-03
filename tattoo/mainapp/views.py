from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import RegistrationForm, LoginForm
from .models import (
    Post, Master, TattooCategory,
    Tag, AboutStudio, Client, WorkMaster
)


class Home(ListView):
    """Вывод главной страницы"""
    model = TattooCategory
    context_object_name = 'categories'
    template_name = 'mainapp/index.html'
    allow_empty = True


class GetPosts(ListView):
    """Вывод всех постов"""
    model = Post
    context_object_name = 'posts'
    template_name = 'mainapp/blog.html'
    paginate_by = 4
    allow_empty = True


class GetAbout(ListView):
    """Выводит страницу 'О нас'"""
    model = AboutStudio
    template_name = 'mainapp/about.html'
    context_object_name = 'about'
    allow_empty = True


class GetPost(DetailView):
    """Показывает каждый пост отдельно"""
    model = Post
    template_name = 'mainapp/blog_post.html'
    context_object_name = 'post'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class PostsByTag(ListView):
    """Выводит записи по тегу"""
    template_name = 'mainapp/blog.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = True

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записи по тегу: ' + str(
            Tag.objects.get(slug=self.kwargs['slug']))
        return context


class AllMasters(ListView):
    """Вывод всех мастеров"""
    model = Master
    context_object_name = 'masters'
    template_name = 'mainapp/all_masters.html'
    allow_empty = True


class GetMaster(DetailView):
    """Показывает каждого мастера отдельно"""
    model = Master
    template_name = 'mainapp/master.html'
    context_object_name = 'master'
    allow_empty = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Тату-студия Якорь :: Портфолио'
        master = context['master']
        # показывает 10 последних работ мастера
        context['last_works'] = master.work_master.order_by('-id')[:10]
        return context


class WorksMaster(ListView):
    """Показывает все работы каждого мастера"""
    model = WorkMaster
    template_name = 'mainapp/works_master.html'
    context_object_name = 'works'

    def get_queryset(self):
        master_id = self.kwargs.get("pk")
        work = Master.objects.get(id=master_id).work_master.all()
        return work


class WorksListView(ListView):
    """Все работы всех мастеров"""
    model = WorkMaster
    template_name = 'mainapp/all_works.html'
    context_object_name = 'works'


class LoginView(View):
    """Авторизация"""
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'mainapp/login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(
                username=username, password=password
            )
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        context = {
            'form': form,
        }
        return render(request, 'mainapp/login.html', context)


class RegistrationView(View):
    """Регистрация"""
    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {
            'form': form,
        }
        return render(request, 'mainapp/registration.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Client.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
            )
            user = authenticate(
                username=new_user.username,
                password=form.cleaned_data['password']
            )
            login(request, user)
            return HttpResponseRedirect('/')
        context = {
            'form': form,
        }
        return render(request, 'mainapp/registration.html', context)
