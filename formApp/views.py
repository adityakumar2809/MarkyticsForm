from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from . import forms

# Create your views here.

@login_required
def initial_report_view(request):
    if request.method == 'POST':
        form = forms.IncidentReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.reported_by = request.user.username
            report.save()
    form = forms.IncidentReportForm()
    return render(request, 'formApp/initial_report_form.html', {'form':form})