from django.urls import path

from . import views

app_name = 'formApp'

urlpatterns = [
    path('', views.initial_report_view, name='initial_report'),
]