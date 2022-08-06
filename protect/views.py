from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.views import View
from django.core.mail import send_mail
from .models import Appointment
from django.shortcuts import redirect, render


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_rival'] = not (self.request.user.groups.filter(name="Rival").exists())
        return context


class AppointmentView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'protect/make_appointment.html', {})

    def post(self, request, *args, **kwargs):
        appointment = Appointment(
            date=datetime.strptime(request.Post['date'], '%Y-%m-%d'),
            client_name=request.Post['client_name'],
            message=request.Post['message'],
        )
        appointment.save()

        send_mail(
            subject=f'{appointment.client_name} {appointment.date.strptime("%Y-%m-%d")}',
            message=appointment.message,
            from_email='seleznevaiu86@yandex.ru',
            recipient_list=['caha150886@gmail.com'],
        )

        return redirect('/')