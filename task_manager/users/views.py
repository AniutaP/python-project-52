from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.contrib.messages.views import SuccessMessageMixin


class UsersView(SuccessMessageMixin, ListView):
    model = get_user_model()
    context_object_name = 'users'
    template_name = 'users/users_list.html'


class UserCreateView(TemplateView):
    template_name = 'users/user_create.html'
