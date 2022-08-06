from django.contrib.auth.models import Group
from allauth.account.forms import SignupForm
from django.db import models
from datetime import datetime


class BaseSignupForm(SignupForm):

    def save(self, request):
        user = super(BaseSignupForm, self).save(request)
        friend_group = Group.objects.get(name="Friends")
        friend_group.user_set.add(user)
        return user


class Appointment(models.Model):
    date = models.DateField(
        default=datetime.utcnow,
    )
    client_name = models.CharField(
        max_length=200
    )
    message = models.TextField()

    def __str__(self):
        return f'{self.client_name}: {self.message}'