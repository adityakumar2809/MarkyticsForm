from django import forms
# from django.forms.extras.widgets import SelectDateWidget, SelectTimeWidget

from . import models

class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'



class IncidentReportForm(forms.ModelForm):
    
    class Meta():
        model = models.IncidentReport
        exclude = ['reported_by']
        widgets = {
            'date_of_incident': DateInput(),
            'time_of_incident': TimeInput()
        }