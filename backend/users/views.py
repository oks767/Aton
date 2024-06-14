from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, DetailView

from client.models import Client
from users.models import User

from users.forms import UserLoginForm, UserRegistrationForm


class IndexView(TemplateView):
    template_name = 'users/index.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.select_related('responsible').filter(responsible=self.request.user)
        return context


def update_client_status(request, client_id):
    if request.method == 'POST':
        client = Client.objects.get(pk=client_id)
        new_status = request.POST.get('status')
        client.update_status(new_status)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return HttpResponseRedirect(reverse('profile'))
