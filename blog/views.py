from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import logout, login

# Create your views here.


def pageNotFound(request, exception):
    return HttpResponseNotFound(render(request, 'blog/not_found_page.html'))

def home(request):
    return render(request, 'blog/index.html')


def links(request):
    cats = LinksCategory.objects.all()
    context = {'title': 'Ссылки', 'cats': cats}
    return render(request, 'blog/links.html', context=context)


class Contacts(CreateView):
    # initial = {'name': 'xxx'}
    form_class = ContactMessageForm
    template_name = 'blog/contacts.html'
    success_url = reverse_lazy('sent')  # after add
    # login_url = reverse_lazy('home')  # '/admin/'
    raise_exception = True  # 403 Forbidden

    def get_initial(self):
        if self.request.user.is_authenticated:
            return {
                'name': self.request.user,
                'email': User.objects.get(username=self.request.user).email
            }
        else:
            return {}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Контакты'
        return context



def api(request):
    context = {'title': 'API'}
    return render(request, 'blog/api.html', context=context)


class RegisterUser(CreateView):  # from mixins .utils.py = DataMixin
    form_class = RegisterUserForm  # UserCreationForm standart #
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):  # from mixins .utils.py
        context = super().get_context_data(**kwargs)
        context['title'] = "Регистрация"
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'blog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Авторизация"
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def sent(request):
    return render(request, 'blog/sent.html', context={'title': 'Отправлено'})