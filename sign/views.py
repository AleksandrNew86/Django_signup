from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegistrationForm
    template_name = 'sign/signup.html'
    success_url = '/'


@login_required
def make_me_rival(request):
    user = request.user
    rivals_group = Group.objects.get(name="Rivals")
    if not request.user.groups.filter(name="Rivals").exists():
        rivals_group.user_set.add(user)
    return redirect('/')



