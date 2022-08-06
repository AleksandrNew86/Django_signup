from django.urls import path
from .views import IndexView, AppointmentView
urlpatterns = [
    path('', IndexView.as_view()),
    path('appointment/', AppointmentView.as_view(), name='appointments')
]
